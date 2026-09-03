# NDR API

Python tools for querying the UK National Data Repository (NDR), generating CSV exports, and downloading well data through the NDR APIs.

## Features

- Generate CSVs by CTAG
- Generate Metadata API access tokens


## Requirements

- Python 3.x
- Jupyter Notebook

**Install dependencies:**
In Jupyter open a new notebook and rename it as per convenience.
## **RUN THE FOLLOWING**
pip install -r requirements.txt
import shutil
shutil.copy(".env.example", ".env")

## Configuration
1. Populate the values in .env using the credentials supplied during NDR registration. USE THE SEMICOLON
2. eg. TENANT ID= "a5er3t-xyzo-098753-trmo" (this is just a fabricated value, please use one from your email

## Running the Tools
Create a new notebook (if needed) and run the following
%run Runner.py
When prompted, enter the name of the script you wish to run.

Examples:

CSVmaker_CTAG.py
