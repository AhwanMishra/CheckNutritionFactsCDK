import * as cdk from "aws-cdk-lib";




export class CNFService extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id);

    const bucket = new cdk.aws_s3.Bucket(this, "WidgetStore");

    const handler = new cdk.aws_lambda.Function(this, "WidgetHandler", {
      runtime: cdk.aws_lambda.Runtime.PYTHON_3_9,
      handler: "index.handler",
      code: cdk.aws_lambda.Code.fromAsset("CNFAssets"),
      environment: {
        BUCKET: bucket.bucketName
      },
      // Duration.seconds(3)
    });

    //The code that defines your stack goes here
    const discountS3Bucket = new cdk.aws_s3.Bucket(this, "discount-coupons", {
      bucketName: 'cnf-discount-coupons-bucket',
      publicReadAccess: false,
      removalPolicy: cdk.RemovalPolicy.DESTROY

    });

    const productDetailsS3Bucket = new cdk.aws_s3.Bucket(this, "product-details", {
      bucketName: 'cnf-product-details-bucket',
      publicReadAccess: false,
      removalPolicy: cdk.RemovalPolicy.DESTROY

    });

    const productCategoryMetaDataS3Bucket = new cdk.aws_s3.Bucket(this, "product-category-metadata", {
      bucketName: "cnf-product-category-metadata",
      publicReadAccess: false,
      removalPolicy: cdk.RemovalPolicy.DESTROY

    });


    bucket.grantReadWrite(handler);
    discountS3Bucket.grantReadWrite(handler);
    productDetailsS3Bucket.grantReadWrite(handler);
    productCategoryMetaDataS3Bucket.grantReadWrite(handler);

    const api = new cdk.aws_apigateway.RestApi(this, "cnf-api", {
      restApiName: "CNF Service",
      description: "This service serves content for CNF service.."
    });

    const pathIntegrationWithLambda = new cdk.aws_apigateway.LambdaIntegration(handler);

    const discountCouponsApi = api.root.addResource("discount-coupons");
    const discountCouponsDeleteApi = discountCouponsApi.addResource("{promo_code}");

    const searchApi = api.root.addResource("search");
    
    const productDetailsApi = api.root.addResource("product-details");
    const productDetailsGetApi = productDetailsApi.addResource("{productId}");

    discountCouponsApi.addMethod("GET", pathIntegrationWithLambda);
    discountCouponsApi.addMethod("POST", pathIntegrationWithLambda);
    discountCouponsDeleteApi.addMethod("DELETE", pathIntegrationWithLambda);
    searchApi.addMethod("GET", pathIntegrationWithLambda);
    productDetailsGetApi.addMethod("GET", pathIntegrationWithLambda);
  }
}

