from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date, datetime
from uuid import UUID

class UserCreateInput(BaseModel):
    des_login: str = Field(title='login',description='example: test')
    des_password: str = Field(title='password',description='example: 123!@#')

class TransactionCreateInput(BaseModel):
    cod_ticker: str = Field('BTLG11',title='ticker',description='example: BTLG11')
    des_broker: str = Field('RICO', title='broker',description='example: RICO')
    type_transaction: str = Field('COMPRA', title='transaction type',description='example: "COMPRA" OR "VENDA"')
    num_amount: int = Field(1,title='amount',description='example: 1')
    num_price_cost: float = Field(1,title='cost price',description='example: 1')
    num_cost_operation: float = Field(1,title='operation cost',description='example: 1')
    idt_user: int = Field(1,title='user identifier',description='example: 1')
    dat_transaction: date = Field('2022-01-01', title='transaction date',description='example: 2022-01-01')

class TransactionListOutput(BaseModel):    
    cod_transaction: UUID
    cod_ticker: str
    des_broker: str
    type_transaction: str
    num_amount: int
    num_price_cost: float
    num_cost_operation: float
    dat_transaction: date
    dat_created: datetime
    dat_modified: datetime   

    class Config:
        orm_mode = True       

class TransactionAllListOutput(TransactionListOutput):    
    idt_user: int

    class Config:
        orm_mode = True   


class StandardOutput(BaseModel):
    message: str


class ErrorOutput(BaseModel):
    detail: str

class UserListOutput(BaseModel):
    idt_user: int
    des_login: str
    ind_status: bool
   
    class Config:
        orm_mode = True

class TransactionUserListOutput(BaseModel):
    transactions: List[TransactionListOutput]
    
    class Config:
        orm_mode = True