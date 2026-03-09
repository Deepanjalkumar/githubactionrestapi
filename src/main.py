'''
Name: Deepanjal
Date: 03-09-2026
Description: Python fastapi program for showing github action workflow in actions
'''
from fastapi import FastAPI
import logging, uvicorn
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
from dotenv import load_dotenv
load_dotenv()
app=FastAPI()

@app.get("/vendor/{vendor}")
async def greetings(vendor:str):
    '''
    Greetings() -> Simple function to return json response
    Arguments:
        vendor: name of the vendor making request
    '''
    try:
        logging.info("[Info]: Got request from {}".format(vendor))
        return {
            "message":"Greetings {}".format(vendor)
        }
    except Exception as e:
        logging.error("[Error]: Got the error while processing request for vendor : {}".format(vendor))
        return {
            "status":"Not found"
        }
    

