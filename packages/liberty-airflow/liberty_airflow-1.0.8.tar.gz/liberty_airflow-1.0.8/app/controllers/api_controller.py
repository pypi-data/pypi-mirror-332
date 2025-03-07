from fastapi import HTTPException, Request
from app.utils.jwt import JWT
from app.services.api_services import API
from app.utils.encrypt import Encryption
from app.services.rest_services import Rest

class ApiController:
    def __init__(self, jwt: JWT):
        self.jwt = jwt
        self.api = API(jwt)
        self.rest = Rest(self.api)

    async def token(self, req: Request):
        return await self.api.token(req)
    
    async def user(self, req: Request):
        return await self.api.user(req)
    
    async def check(self, req: Request):
        return await self.api.check(req)
    
    async def get(self, req: Request):
        return await self.api.get(req)

    async def post(self, req: Request):
        return await self.api.post(req)

    async def put(self, req: Request):
        return await self.api.post(req)

    async def delete(self, req: Request):
        return await self.api.post(req)

    async def open(self, req: Request):
        return await self.api.open(req)
    
    def get_pool_info(self, req: Request, pool: str):
        return self.api.get_pool_info(req, pool)

    async def close(self, req: Request):
        return await self.api.close(req)

    async def encrypt(self, req: Request):
        try:
            data = await req.json()
            plain_text = data.get("plain_text")
            encryption = Encryption(self.jwt)
            encrypted_text = encryption.encrypt_text(plain_text)
            return {"encrypted": encrypted_text}
        except Exception as err:
            raise HTTPException(status_code=500, detail=str(err))

    async def audit(self, req: Request, table: str, user: str):
        return await self.api.audit(req, table, user)    
    
    async def modules(self, req: Request):
        return await self.api.modules(req)
    
    async def applications(self, req: Request):
        return await self.api.applications(req)    

    async def themes(self, req: Request):
        return await self.api.themes(req)    
    
    async def push_log(self, req: Request):
        return await self.rest.push_log(req)    

    async def get_log(self, req: Request):
        return await self.rest.get_log(req) 
    
    async def get_log_details(self, req: Request):
        return await self.rest.get_log_details(req) 

    async def ai_prompt(self, req: Request):
        return await self.rest.ai_prompt(req)     
    
    async def ai_welcome(self, req: Request):
        return await self.rest.ai_welcome(req)      
        
    async def call_rest(self, req: Request):
        return await self.rest.call_rest(req)          
    
    async def version(self, req: Request):
        return await self.rest.get_version(req)          

    async def dags(self, req: Request, headers: dict):
        return await self.api.dags(req, headers)  
    
