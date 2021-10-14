import * as cdk from '@aws-cdk/core';
import * as cnf_service from './cnf-service';

export class CheckNutritionFactsCdkStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    new cnf_service.CNFService(this, 'cnf_id');
  }
}
