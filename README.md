# NDR API

Python tools for querying the UK National Data Repository (NDR), generating CSV exports, and downloading well data through the NDR APIs.

## Features

- Generate CSVs by CTAG
- Generate Metadata API access tokens


## Requirements

- Python 3.x
- Jupyter Notebook
- Download this repository as .zip, and unzip it. (the green button <code> should have this option)
- Copy paste this folder from where you can run this in jupyter.

**Install dependencies:**
In Jupyter open a new notebook and rename it as per convenience. Open this same as directory in folder as well.

## **RUN THE FOLLOWING one after another**
pip install -r requirements.txt
import shutil
shutil.copy(".env.example", ".env")

This should create a file called ".env" in your folder. Open this file in Notebook

## Configuration
1. Populate the values in .env using the credentials supplied during NDR registration. To do this use . USE THE DOUBLE INVERTED COMMAS. then save the file.
  eg. TENANT ID= "a5er3t-xyzo-098753-trmo" (this is just a fabricated value, please use one from your email
2. This should get you setup for future

## Running the Tools
Create a new notebook (if needed) and run the following
%run CSVmaker_CTAG.py
This will run the code and get everything running. If you have Setup the .env file correctly with values you got from email. This should work without any issues


