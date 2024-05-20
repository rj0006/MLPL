from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Consignment, Invoice
import json
import requests
from datetime import datetime

def operation(request):
    return render(request, 'operation_nav/navbar.html')

def get_ewaybill(request):
    if request.method == 'POST':
        data = request.POST
        vno = data.get('ewayBill')
        # Url for the post request
        # url = "http://ewaysandbox.webtel.in/Sandbox/EWayBill/v1.3/GetEWB"
        url = 'http://ewayasp.webtel.in/EWayBill/v1.3/GetEWB'
        headers = {
            'Authorization' : '/IalkRmh3z4=:::ZH4TUvIeJ3A=',
            'Content-Type' : 'application/json'
        }
        
        # # Live
        parameters = {
            "GSTIN": "06AADCM8862E1ZD",
            "ewbNo": vno, # 101671124843
            "EWBUserName": "mahalakshm_API_pkg",
            "EWBPassword": "Admin@5303",
            "Year": 2024,
            "Month": 1,
            "EFUserName": "039C10BA-5F49-4C9C-98B7-2B14AAFA38E8",
            "EFPassword": "1D4331EF-1DFB-43D3-A065-4F24DBBEB1CD",
            "CDKey": "1550859"
        }
        
        # parameters = {
        #     "GSTIN": "05AAACD5767E1ZT", 
        #     "ewbNo": vno, # 341000798954
        #     "EWBUserName": "05AAACD5767E1ZT",
        #     "EWBPassword": "abc123@@", 
        #     "Year" : 2024,
        #     "Month" : 1,
        #     "EFUserName": "05AAACD5767E1ZT",
        #     "EFPassword": "abc123@@", 
        #     "CDKey": "1000685"
        # }
        
        # request
        response = requests.post(url, json=parameters, headers = headers)
        # Check if the request was successful status code 200
        if response.status_code == 200:
            response_string = response.json()
            response_list = json.loads(response_string)
            
            for item in response_list:
                EWBDetails_str = item.get("EWBDetails")
                if EWBDetails_str:
                    try:
                        item['EWBDetails'] = json.loads(EWBDetails_str)
                    except json.JSONDecodeError as e:
                        print("Error parsing EWBDetails string:", e)
            
        else:
            print(f"Error: {response.status_code} - {response.text}")

        request.session['response_list'] = response_list

        return redirect('/operations/consignment/')
    return render(request, 'getEwayBill.html')

def consignment(request):
    # Retrieve response_list from session
    response_list = request.session.get('response_list', [])
    # Process the response_list and submit the HTML page with the response to the database
    # ...
    if request.method == 'POST':
        data = request.POST
        consignor = data.get('consignor')
        print(consignor)
        
        return redirect('/operations/consignment/')
    request.session.flush()
    
    # print(type(response_list))
    # Pass response_list to the template
    context = {'data': response_list}
    return render(request, 'consignment.html', context)
    
def consignment_tracking(request):
    if request.method == 'POST':
        data = request.POST
        vno = data.get('consignmentNo')
        # Url for the post request
        url = "https://cntrack.lozics.in/Tracking.Ashx"
        parameters = {
            'interface': 'RestAPI',
            'method': 'GetConsignmentDetail',
            'parameters': {'VNO': vno},
            'token': 'MLPL'
        }
        # POST request body
        data = {
            "method": "post",
            "url": url,
            "json": parameters
        }
        # request
        response = requests.post(url, json=parameters)
        # Check if the request was successful status code 200
        if response.status_code == 200:
            # Parse the JSON response
            result_json = response.json()
            # Extract the 'value' field and parse it JSON  
            value_json = json.loads(result_json['Value'])
            # cnmtDetail
            cnmt_detail = value_json['cnmtDetail']
            # movementDetail
            movementDetail = value_json['movementDetail']
            # DeliveryStatus
            DeliveryStatus = value_json['DeliveryStatus']
            # Table3
            Table3 = value_json['Table3']
            # Table4
            Table4 = value_json['Table4']
            # Table5
            Table5 = value_json['Table5']
    
            for item in value_json:
                print(item)
                
            # print(json.dumps(value_json, indent=2))
            # for detail in value_json['cnmtDetail']:
            #     voucherDate = detail.get('CNNO')
            #     print(voucherDate)
                
        else:
            print(f"Error: {response.status_code} - {response.text}")
        
        context = {
            'cnmt_detail': cnmt_detail,
            'movementDetail': movementDetail,
        }
        return render(request, 'consignment_tracking.html', context)
    
    return render(request, 'consignment_tracking.html')
