import { App, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as cnf_service from './cnf-service';

export class CheckNutritionFactsCdKv2Stack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    new cnf_service.CNFService(new App, 'CheckNutritionFactsServiceCdkStack', props);
  }
}
