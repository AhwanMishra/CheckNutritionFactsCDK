import * as core from "@aws-cdk/core";
import * as apigateway from "@aws-cdk/aws-apigateway";
import * as lambda from "@aws-cdk/aws-lambda";
import * as s3 from "@aws-cdk/aws-s3";

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

    bucket.grantReadWrite(handler); // was: handler.role);

    const api = new apigateway.RestApi(this, "cnf-api", {
      restApiName: "CNF Service",
      description: "This service serves content for CNF service.."
    });


    const api1 = api.root.addResource("{test-path}");
    const api2 = api.root.addResource("test-path2");

    const getTestPathIntegrationWithLambda = new apigateway.LambdaIntegration(handler);
    
    api1.addMethod("GET", getTestPathIntegrationWithLambda);
    api2.addMethod("GET", getTestPathIntegrationWithLambda);

  }
}

