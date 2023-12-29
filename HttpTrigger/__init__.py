import logging
import os

import azure.functions as func

from services.DocumentService import DocumentService


def set_config(self):
    os.environ["OPENAI_API_TYPE"] = 'azure'  
    os.environ['OPENAI_API_KEY'] = self.openai_api_key  
    os.environ['OPENAI_API_BASE'] = self.openai_api_base  
    os.environ['OPENAI_API_VERSION'] = self.openai_api_version

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    set_config()

    operation = req.get('operation')
    
    documentService = DocumentService()
    return documentService.process(operation, req)