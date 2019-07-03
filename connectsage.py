"""
Develoed by zforce on 03-07-2019

module to process teh data

"""
import json
import datetime
import boto3
import os
import io
import csv

#import Numpy as np


def sagee(Creditamt,Duration,pCarX,pDom,pEduX,pFurX,pRadX,pRepX,pVacX,Sex,ownHouse,rentHouse,savingModX,savingNoInfX,
          savingMiddleX,savingsRichX,checkModX,checkNoInX,checkRichX,ageCatYoungX,ageCatAdult,ageCatSenX,job1,job2,job3):



    runtime = boto3.Session().client(service_name='sagemaker-runtime',region_name='us-east-2')
    
    listParm = [Creditamt,Duration,pCarX,pDom,pEduX,pFurX,pRadX,pRepX,pVacX,Sex,ownHouse,rentHouse,savingModX,savingNoInfX,
                savingMiddleX,savingsRichX,checkModX,checkNoInX,checkRichX,ageCatYoungX,ageCatAdult,ageCatSenX,job1,job2,job3]
                
    string12 = " ,".join(listParm)
                
    #arr = bytearray(listParm, 'utf-8')
    
    #nparray = np.array(listParm)
    
    #values = bytearray(listParm)
    
    print(string12)
    
    csv_text = string12
    #csv_text = Creditamt,Duration,pCarX,pDom,appliances,pEduX,pFurX,pRadX,pRepX,pVacX,Sex,ownHouse,rentHouse,savingModX,savingNoInfX,savingMiddleX,savingsRichX,checkModX,checkRichX,ageCatYoungX,ageCatAdult,ageCatSenX,job1,job2,job3

    #csv_text = '12,6,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1'

    
    response = runtime.invoke_endpoint(EndpointName='MeritQ', ContentType='text/csv', Body=csv_text,Accept = 'Accept')
    

    merit_percent = json.loads(response['Body'].read().decode())
    
    
    

    return merit_percent

