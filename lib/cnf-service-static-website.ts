import * as cdk from "aws-cdk-lib";
import { Duration } from "aws-cdk-lib";
import { CfnIndex } from "aws-cdk-lib/aws-kendra";

export class CnfServieStaticWebSite extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const CNF_URL_WWW_VERSION = "www.checknutritionfacts.com";
    const CNF_URL_NON_WWW_VERSION = "checknutritionfacts.com";


    /**
     *  S3 bucket where we will put the static website content.
     *  The index page is set to be index.html, setting it also enables the static website hosting property.
     */

    const CnfStaticWebsiteBucket = new cdk.aws_s3.Bucket(this, CNF_URL_WWW_VERSION, {
      bucketName: CNF_URL_WWW_VERSION,
      publicReadAccess: true,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      websiteIndexDocument : "index.html",
      // websiteErrorDocument : "index.html", 
      // Why ? Ans: https://stackoverflow.com/questions/51218979/react-router-doesnt-work-in-aws-s3-bucket (Still it throws 404 response code hence not recognised by Google)
      // https://via.studio/journal/hosting-a-reactjs-app-with-routing-on-aws-s3
    //   websiteRoutingRules :
    //   [
    //     {
    //       condition: { httpErrorCodeReturnedEquals: '403'},
    //       replaceKey: cdk.aws_s3.ReplaceKey.prefixWith('#/'),
    //       hostName: CNF_URL_WWW_VERSION,
    //       httpRedirectCode : "301",
    //     },
    //     {
    //       condition: { httpErrorCodeReturnedEquals: '404'},
    //       replaceKey: cdk.aws_s3.ReplaceKey.('#/'),
    //       hostName: CNF_URL_WWW_VERSION,
    //       httpRedirectCode : "301",
    //     }
    //     ]
    }
    );

    /**
     *  2nd S3 bucket, non www version. We wont put any content here.
     *  but it will redirect to www bucket.
     *  .
     */

    const CnfStaticWebsiteBucket2 = new cdk.aws_s3.Bucket(this, CNF_URL_NON_WWW_VERSION, {
      bucketName: CNF_URL_NON_WWW_VERSION,
      publicReadAccess: true,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      websiteRedirect : {
        hostName: CNF_URL_WWW_VERSION,
        protocol :  cdk.aws_s3.RedirectProtocol.HTTPS
      }
    });

    /**
     *  Route 53, add records to the existing domain name which was created automatically
     *  after the domain name registration.
     */

    // Get the hosted zone using name and id from the console.
    const cnfHostedZone = cdk.aws_route53.HostedZone.fromHostedZoneAttributes(this, "cnfHostedZone", {
      zoneName: CNF_URL_NON_WWW_VERSION,  // It has nothing to do with www or non www,  put non www.
      hostedZoneId: 'Z057919633RJHL9FA8NVW',
    });




    /**
     *  Stuffs for https support
     */
    /**
     * ACM certificate creation.
     * It will add "cNames" to hosted zone.
     */

    const certCfnWWW = new cdk.aws_certificatemanager.DnsValidatedCertificate(this, 'CNFCrossRegionCertificateWWW', {
      domainName: CNF_URL_WWW_VERSION,
      hostedZone: cnfHostedZone,
      region: 'us-east-1', // Why ? https://github.com/cloudposse/terraform-aws-cloudfront-s3-cdn/issues/55
      //https://docs.aws.amazon.com/cdk/api/v1/docs/aws-certificatemanager-readme.html
    });

    const certCfn = new cdk.aws_certificatemanager.DnsValidatedCertificate(this, 'CNFCrossRegionCertificate', {
      domainName: CNF_URL_NON_WWW_VERSION,
      hostedZone: cnfHostedZone,
      region: 'us-east-1',
    });

    /**
     * Cloudfront distribution
     * Use the ACM certificate & map to S3 buckets.
     */

    // WWW version
    const cnfDistributionWWW = new cdk.aws_cloudfront.Distribution(this, 'cnfDistributionWWW', {
      defaultBehavior: {
        origin: new cdk.aws_cloudfront_origins.S3Origin(CnfStaticWebsiteBucket),
        viewerProtocolPolicy : cdk.aws_cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
        allowedMethods : cdk.aws_cloudfront.AllowedMethods.ALLOW_GET_HEAD,
      },
      certificate : certCfnWWW,
      domainNames : [CNF_URL_WWW_VERSION],
      errorResponses : [{
        httpStatus: 403,
        responseHttpStatus : 200,
        responsePagePath : "/index.html",
        ttl : Duration.millis(0)
      },
      {
        httpStatus: 404,
        responseHttpStatus : 200,
        responsePagePath : "/index.html",
        ttl : Duration.millis(0)
      }]
    });

    // Non WWW version
    const cnfDistribution = new cdk.aws_cloudfront.Distribution(this, 'cnfDistribution', {
      defaultBehavior: {
        origin: new cdk.aws_cloudfront_origins.S3Origin(CnfStaticWebsiteBucket2),
        viewerProtocolPolicy : cdk.aws_cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
        allowedMethods : cdk.aws_cloudfront.AllowedMethods.ALLOW_GET_HEAD,
      },
      certificate : certCfn,
      domainNames : [CNF_URL_NON_WWW_VERSION],
      errorResponses : [{
        httpStatus: 403,
        responseHttpStatus : 200,
        responsePagePath : "/index.html",
        ttl : Duration.millis(0)
      },
      {
        httpStatus: 404,
        responseHttpStatus : 200,
        responsePagePath : "/index.html",
        ttl : Duration.millis(0)
      }]
    });

    
    
    
    /**
     * Route 53 configurations.
     * Mapping Route 53 to Cloudfront using aRecord
     */
    // ARecord routes traffic to an IPV4 address & some AWS resources
    // know about other type of records from the Route53 console.

    // For www version
    new cdk.aws_route53.ARecord(this, "cnfARecordWWW", {
      zone : cnfHostedZone,
      recordName: "www",
      ttl : cdk.Duration.minutes(27), // default 30mins
      target : cdk.aws_route53.RecordTarget.fromAlias(
        new cdk.aws_route53_targets.CloudFrontTarget(cnfDistributionWWW))
    })

    // For non www version
    new cdk.aws_route53.ARecord(this, "cnfARecord", {
      zone : cnfHostedZone,
      ttl : cdk.Duration.minutes(27),
      target : cdk.aws_route53.RecordTarget.fromAlias(
        new cdk.aws_route53_targets.CloudFrontTarget(cnfDistribution))
    })
  }
}
