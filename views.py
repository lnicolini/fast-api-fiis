from asyncio import gather
from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException
from starlette import responses

from sqlalchemy.orm import Session
from schemas import (
    UserCreateInput, StandardOutput,  ErrorOutput, TransactionCreateInput, UserListOutput, TransactionListOutput, TransactionUserListOutput, TransactionAllListOutput
)
from services import UserService, TransactionsService

user_router        = APIRouter(prefix='/user')
transaction_router = APIRouter(prefix='/transaction')

@user_router.get('/list', response_model=List[UserListOutput], responses={400: {'model': ErrorOutput}})
async def user_list():
    try:
        return await UserService.list_user()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@user_router.post('/create', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def user_create(user_input: UserCreateInput):
    try:
        await UserService.create_user(
            des_login=user_input.des_login,
            des_password=user_input.des_password)
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))  

@transaction_router.get('/list', response_model=List[TransactionAllListOutput], responses={400: {'model': ErrorOutput}})
async def transaction_list():
    try:
        return await TransactionsService.list_transaction()
    except Exception as error:
        raise HTTPException(400, detail=str(error))     


@transaction_router.get('/list_by_transaction/{cod_transaction}', response_model=TransactionListOutput, responses={400: {'model': ErrorOutput}})
async def list_transaction_id(cod_transaction: UUID):
    try:
        transaction = await TransactionsService.get_by_id(cod_transaction)       
        return transaction

    except Exception as error:
        raise HTTPException(400, detail=str(error))  



@transaction_router.get('/list_by_user/{idt_user}', response_model=TransactionUserListOutput, responses={400: {'model': ErrorOutput}})
async def list_transaction_id(idt_user: int):
    try:
        user = await UserService.get_by_id(idt_user)
        return user
    except Exception as error:
        raise HTTPException(400, detail=str(error))    

@transaction_router.delete('/delete/{cod_transaction}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def delete_transaction(cod_transaction: UUID):
    try:
        await TransactionsService.delete_transaction(cod_transaction)
        return StandardOutput(message='Ok') 
    except Exception as error:
        raise HTTPException(400, detail=str(error))
            

@transaction_router.post('/create', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def transaction_create(transaction_input: TransactionCreateInput):
    try:
        await TransactionsService.create_transaction(
            cod_ticker=transaction_input.cod_ticker,
            des_broker=transaction_input.des_broker,
            type_transaction=transaction_input.type_transaction,
            num_amount=transaction_input.num_amount,
            num_price_cost=transaction_input.num_price_cost,
            num_cost_operation=transaction_input.num_cost_operation,
            idt_user=transaction_input.idt_user,
            dat_transaction=transaction_input.dat_transaction
            )
        return StandardOutput(message='Ok')      
        
    except Exception as error:
        raise HTTPException(400, detail=str(error))        