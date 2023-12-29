from azure.search.documents import SearchClient  
from azure.search.documents.models import *
from azure.core.credentials import AzureKeyCredential
from services.OpenAIService import OpenAIService

class DocumentService:
    def process(self, operation, req):
        match(operation):
            case "Write":
                search_client = SearchClient(endpoint=self.azure_cognitive_search_service_url,
                      index_name=self.azure_cognitive_search_index_name,
                      credential=AzureKeyCredential(self.azure_cognitive_admin_key))
                
                contents = []
                titleVector = OpenAIService.generate_embeddings(req.get('Title'))
                contentVector = OpenAIService.generate_embeddings(req.get('Content'))
                
                contents.append({"DocId": req.get('DocId'), "DocNumber": req.get('DocNumber'), "Title": req.get('Title'), "Content": req.get('Content'), "TitleVector": titleVector, "ContentVector": contentVector})
                
                upload = search_client.upload_documents(documents = contents)
                
                return upload[0].succeeded
            case "Query":
                return 'Success'