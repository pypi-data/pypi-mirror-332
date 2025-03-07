#
# Copyright (c) 2025 NOMANA-IT and/or its affiliates.
# All rights reserved. Use is subject to license terms.
#
#
import json
from typing import Any, Dict, Optional
from fastapi import APIRouter, Body, Depends, HTTPException, Query, Request, Path
from pydantic import Field
from app.utils.jwt import JWT
from app.controllers.api_controller import ApiController
from app.models.auth import TOKEN_ERROR_MESSAGE, TOKEN_RESPONSE_DESCRIPTION, TOKEN_RESPONSE_EXAMPLE, USER_ERROR_MESSAGE, USER_RESPONSE_DESCRIPTION, USER_RESPONSE_EXAMPLE, LoginRequest, TokenResponse, UserResponse
from app.models.base import ErrorResponse, ValidationErrorResponse, response_200, response_422, response_500
from app.services.api_services import LoginType, SessionMode
from app.models.apidb import ENCRYPT_ERROR_MESSAGE, ENCRYPT_RESPONSE_DESCRIPTION, ENCRYPT_RESPONSE_EXAMPLE, EncryptResponse
from app.models.modules import MODULES_ERROR_MESSAGE, MODULES_RESPONSE_DESCRIPTION, MODULES_RESPONSE_EXAMPLE, ModulesResponse
from app.models.applications import APPLICATIONS_ERROR_MESSAGE, APPLICATIONS_RESPONSE_DESCRIPTION, APPLICATIONS_RESPONSE_EXAMPLE, ApplicationsResponse

def setup_api_routes(app, controller: ApiController, jwt: JWT):
    router = APIRouter()

    @router.post(
        "/auth/token",
        summary="AUTH - Token",
        description="Generate a JWT token for the user.",
        tags=["Authentication"], 
        response_model=TokenResponse,
        responses={
            200: response_200(TokenResponse, TOKEN_RESPONSE_DESCRIPTION, TOKEN_RESPONSE_EXAMPLE),
            422: response_422(),  
            500: response_500(ErrorResponse, TOKEN_ERROR_MESSAGE),
        },
    )
    async def token(
        req: Request,
        body: LoginRequest,
        pool: str = Query(None, description="The database pool alias to retrieve the user. (e.g., `default`, `libnsx1`)"),
        mode: SessionMode = Query(None, description="The session mode, retrieve data from framework table or pool. Valid values: `framework`, `session`"),
        type: LoginType = Query(None, description="Authentication type, from database or using OIDC. Valid values: `database`, `oidc`"),
    ):
        return await controller.token(req)


    @router.get("/auth/user",
        summary="AUTH - User",
        description="Retrieve user information.",
        tags=["Authentication"], 
        response_model=UserResponse,
        responses={
            200: response_200(UserResponse, USER_RESPONSE_DESCRIPTION, USER_RESPONSE_EXAMPLE),
            422: {"model": ValidationErrorResponse},  
            500: response_500(ErrorResponse, USER_ERROR_MESSAGE),
        },
    )
    async def user(
        req: Request,
        jwt: str = Depends(jwt.is_valid_jwt),
        user: str = Query(None, description="User ID."),
    ):
        return await controller.user(req)
    

    @router.post(
        "/fmw/encrypt",
        summary="FMW - Encrypt",
        description="Encrypt the input received",
        tags=["Framework"],
        response_model=EncryptResponse,
        responses={
            200: response_200(EncryptResponse, ENCRYPT_RESPONSE_DESCRIPTION, ENCRYPT_RESPONSE_EXAMPLE),
            422: response_422(),  
            500: response_500(ErrorResponse, ENCRYPT_ERROR_MESSAGE),
        },
    )
    async def encrypt(
        req: Request,
        plain_text: str = Query(None, description="Text to be encrypted"),
        ):
        return await controller.encrypt(req)    


    @router.get("/fmw/modules",
        summary="FMW - Modules",
        description="Retrieve Modules.",
        tags=["Framework"], 
        response_model=ModulesResponse,
        responses={
            200: response_200(ModulesResponse, MODULES_RESPONSE_DESCRIPTION, MODULES_RESPONSE_EXAMPLE),
            422: response_422(),  
            500: response_500(ErrorResponse, MODULES_ERROR_MESSAGE),
        },
    )
    async def modules(
        req: Request,
    ):
        return await controller.modules(req)
    
    @router.get("/fmw/applications",
        summary="FMW - Applications",
        description="Retrieve Applications.",
        tags=["Framework"],
        response_model=ApplicationsResponse,
        responses={
            200: response_200(ApplicationsResponse, APPLICATIONS_RESPONSE_DESCRIPTION, APPLICATIONS_RESPONSE_EXAMPLE),
            422: response_422(),  
            500: response_500(ErrorResponse, APPLICATIONS_ERROR_MESSAGE),
        },
    )
    async def applications(
        req: Request,
    ):
        return await controller.applications(req)  

    @router.get("/logs",
        summary="FMW - Get logs",
        description="Get all current logs and upload to cache",
        tags=["Framework"],
    )
    async def get_logs(req: Request):
        return await controller.get_log(req)
    
    @router.get("/logs/details",
        summary="FMW - Get log details",
        description="Get details for a log id from the cache",
        tags=["Framework"],
    )
    async def get_logs(req: Request):
        return await controller.get_log_details(req)
    
    @router.post("/logs",
        summary="FMW - Push logs",
        description="Push logs to files in json and plain text format",
        tags=["Framework"],
    )
    async def post_logs(req: Request):
        return await controller.push_log(req)
    
    @router.get("/airflow/dags",
        summary="DAGS - List",
        description="List DAGs in the database.",
        tags=["Airflow"], 
    )
    async def dags(
        req: Request,
        jwt: str = Depends(jwt.is_valid_jwt),
    ):
        headers = {"Authorization": jwt["authorization"]}


        return await controller.dags(req, headers)
    
    app.include_router(router, prefix="/api")    