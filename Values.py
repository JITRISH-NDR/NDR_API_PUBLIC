from dotenv import load_dotenv
import os

load_dotenv()
required = [
    "TENANT_ID",
    "CLIENT_ID",
    "CLIENT_SECRET"
]

for var in required:
    if not os.getenv(var):
        raise ValueError(f"Missing environment variable: {var}")

Tenant_ID = os.getenv("TENANT_ID")
Client_ID = os.getenv("CLIENT_ID")
Site_ID = os.getenv("SITE_ID")
Comp_ID = os.getenv("COMP_ID")
Client_Secret = os.getenv("CLIENT_SECRET")

Projec_ID_Metadata = os.getenv("PROJECT_ID_METADATA")
Project_ID_Metadata = os.getenv("PROJECT_ID_METADATA")
File_ID_Metadata = os.getenv("FILE_ID_METADATA")

Completeness_mhaz = os.getenv("COMPLETENESS_MHAZ")
Completeness_seis = os.getenv("COMPLETENESS_SEIS")
Completeness_well = os.getenv("COMPLETENESS_WELL")

Company_Name = os.getenv("COMPANY_NAME")
Completeness_Comments = os.getenv("COMPLETENESS_COMMENTS")

Scope_Metadata = "https://graph.microsoft.com/.default"
Scope_Welldata = f"api://{Client_ID}/.default"

Data_Meta = {
    "client_id": Client_ID,
    "scope": Scope_Metadata,
    "grant_type": "client_credentials",
    "client_secret": Client_Secret
}

Data_Well = {
    "client_id": Client_ID,
    "scope": Scope_Welldata,
    "grant_type": "client_credentials",
    "client_secret": Client_Secret
}
