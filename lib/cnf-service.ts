import * as core from "@aws-cdk/core";
import * as apigateway from "@aws-cdk/aws-apigateway";
import * as lambda from "@aws-cdk/aws-lambda";
import * as s3 from "@aws-cdk/aws-s3";
import * as cdk from '@aws-cdk/core';

export class CNFService extends core.Construct {
  constructor(scope: core.Construct, id: string) {
    super(scope, id);

    const bucket = new s3.Bucket(this, "WidgetStore");

    const handler = new lambda.Function(this, "WidgetHandler", {
      runtime: lambda.Runtime.PYTHON_3_8,
      code: lambda.Code.fromAsset("resources"),
      handler: "cnfAsset.mainHandler",
      environment: {
        BUCKET: bucket.bucketName
      }
    });

    //The code that defines your stack goes here
    const discountS3Bucket = new s3.Bucket(this, "discount-coupons", {
      bucketName: 'cnf-discount-coupons-bucket',
      publicReadAccess: false,
      removalPolicy: cdk.RemovalPolicy.DESTROY

    });

    bucket.grantReadWrite(handler); // was: handler.role);
    discountS3Bucket.grantReadWrite(handler);

    const api = new apigateway.RestApi(this, "cnf-api", {
      restApiName: "CNF Service",
      description: "This service serves content for CNF service.."
    });

    const pathIntegrationWithLambda = new apigateway.LambdaIntegration(handler);


    const api1 = api.root.addResource("{test-path}");
    const api2 = api.root.addResource("test-path2");

    const discountCouponsApi = api.root.addResource("discount-coupons");
    const discountCouponsDeleteApi = discountCouponsApi.addResource("{promo_code}")

    
    api1.addMethod("GET", pathIntegrationWithLambda);
    api2.addMethod("GET", pathIntegrationWithLambda);

    discountCouponsApi.addMethod("GET", pathIntegrationWithLambda);
    discountCouponsApi.addMethod("POST", pathIntegrationWithLambda);
    discountCouponsDeleteApi.addMethod("DELETE", pathIntegrationWithLambda);


    




  }
}

