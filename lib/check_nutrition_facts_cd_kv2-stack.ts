import { App, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import {CNFService} from './cnf-service';
import {CnfServieStaticWebSite} from './cnf-service-static-website';


export class CheckNutritionFactsCdKv2Stack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    new CNFService(new App, 'CheckNutritionFactsServiceCdkStack', props);
    new CnfServieStaticWebSite(new App, 'CnfServiceStaticWebsiteCdkStack', props);
  }
}
