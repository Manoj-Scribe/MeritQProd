"""
Develoed by zforce on 03-07-2019

main module to process teh data

"""
import json
import datetime

import os
import io
import csv
from connectsage import sagee

runtime = boto3.Session().client(service_name='sagemaker-runtime',region_name='us-east-2')


def lambda_handler(event, context):
    #parm varibales

    Creditamt ="0"
    Duration ="0"

    pCarX = "0"
    pDom  = "0"
    pEduX = "0"
    pFurX = "0"
    pRadX = "0"
    pRepX = "0"
    pVacX = "0"



    Sex = "0"
    ownHouse ="0"
    rentHouse ="0"
    savingModX ="0"
    savingNoInfX ="0"
    savingMiddleX ="0"
    savingsRichX ="0"

    checkModX ="0"
    checkNoInX ="0"
    checkRichX ="0"

    ageCatYoungX ="0"
    ageCatAdult ="0"
    ageCatSenX ="0"
    job1 ="0"
    job2 ="0"
    job3 ="0"
   
    jsonData = json.dumps(event)
    
    
    
    inputData = json.loads(jsonData)
    
    #populate all metrics for 
    Creditamt = inputData["cr_amt"]
    Duration = inputData["cr_dur"]
    
    #purchases decision
    if inputData["cr_pur"] ==  "Repairs":
      pRepX = "1"
    elif inputData["cr_pur"] ==  "Education":
      pEduX = "1"
    elif inputData["cr_pur"] ==  "Car":
      pCarX = "1"
    elif inputData["cr_pur"] ==  "Furniture":
      pFurX = "1"
    elif inputData["cr_pur"] ==  "Radio":
      pRadX = "1"
    elif inputData["cr_pur"] ==  "Vacation":
      pVacX = "1"
    elif inputData["cr_pur"] ==  "Domestic Appliances":
      pDom = "1"
    else:
      pDom = "0"
    
    
    #sex decision
    if inputData["gender"] ==  "Female":
     Sex = "1"
    			
    
    
    #rented decision
    if inputData["house_type"] ==  "Own":
     ownHouse = "1"
    elif inputData["house_type"] ==  "Rent":
     rentHouse = "1"
    else:
     ownHouse = "0"
    
    
    #savingsd decision
    if inputData["savings_type"] ==  "Rich":
     savingsRichX = "1"
    elif inputData["savings_type"] ==  "Moderate":
     savingModX = "1"
    elif inputData["savings_type"] ==  "Little":
     savingMiddleX = "1"
    else:
     savingNoInfX = "1"
    
    
    #waLTH decision
    if inputData["checkings_type"] ==  "Rich":
     checkRichX = "1"
    elif inputData["checkings_type"] ==  "Moderate":
     checkModX = "1"
    else:
     checkNoInX = "1"
    
    
    
    #aGE decision
    
    agenum = int(inputData["age"])
    
    if agenum  <  25:
     ageCatYoungX = "1"
    elif agenum > 25  and  agenum <  55:
     ageCatAdult = "1"
    else:
     ageCatSenX = "1"
    
    
    #job_type decision
    if inputData["job_type"] ==  "Government":
     job1 = "1"
    
    elif inputData["job_type"] ==  "Private":
     job2  = "1"
    
    elif inputData["job_type"] ==  "Self-employed (Macro)":
     job3 = "1"
    
    else:
     job1 = "0"    
   
   
   
   
    #result = sagee('0','6','0','0','0','1','0','0','0','1','0','1','0','0','0','0','0','0','0','0','1','0','0','0','1');
    
    
    
    result = sagee(Creditamt,Duration,pCarX,pDom,pEduX,pFurX,pRadX,pRepX,pVacX,Sex,ownHouse,rentHouse,savingModX,savingNoInfX,savingMiddleX,savingsRichX
                    ,checkModX,checkNoInX,checkRichX,ageCatYoungX,ageCatAdult,ageCatSenX,job1,job2,job3)
    
    
    
    result = result * 1000
    
    print(result)
    
    if result > 500:
        result_check = "Accepted"
    else:
        result_check = "Declined"
    
    
    

     
    data = {
        'result' : result_check,
        'score'  : result
     }
    
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

