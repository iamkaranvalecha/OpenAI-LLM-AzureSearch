from openai import AzureOpenAI
from typing import Optional


class OpenAIService:
    def __init__(self, params: Optional[dict] = None):
        self.params = params or {}
        self.openai = AzureOpenAI(api_key= self.openai_api_key, azure_endpoint=self.openai_api_base, api_version=self.openai_api_version)
      
    def generate_embeddings(self,text):
        return self.openai.embeddings.create(
                input=text, model='text-embedding-ada-002').data[0].embedding
    
    def generate_completion(self,prompt,modelName='gpt-4',max_token=1024):
        return self.openai.chat.completions.create(
            model=modelName, 
            messages=prompt,
            temperature=0,
            max_tokens=max_token,
            top_p=0.2
            ).choices[0].message.content