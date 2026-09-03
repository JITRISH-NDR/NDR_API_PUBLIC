import requests
import json
import Values
output_file = "ukndr_Metadata_api_access_token.txt"
session = requests.Session()
data = Values.Data_Meta
response = session.post(
 "https://login.microsoftonline.com/"+Values.Tenant_ID+"/oauth2/v2.0/token", 
 data=data, 
 headers = {"Content-Type": "application/x-www-form-urlencoded"}
) 
if response.status_code == 200:
 access_token = response.json()["access_token"]
 woutfile = open(output_file, "w")
 woutfile.write(access_token)
 woutfile.close()
 print(json.dumps(response.json(), indent=2))
 print("data_access_token also written to file", output_file) 
else:
 print("There was an error getting the access token", response.status_code,response.json())
