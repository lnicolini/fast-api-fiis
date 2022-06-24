import bcrypt
from datetime import date, timedelta
from aiohttp import ClientSession
from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete
from hashing import Hasher

from database.models import User, Transactions
from database.connection import async_session


class UserService:
    async def create_user(des_login: str, des_password: str):
        async with async_session() as session:
            hashed_password = Hasher.get_hash_password(des_password)
            session.add(User(des_login=des_login, des_password=hashed_password))
            await session.commit()           

    async def list_user():
        async with async_session() as session:
            result = await session.execute(select(User))
            return result.scalars().all()
    
    async def get_by_id(idt_user):
        async with async_session() as session:
            result = await session.execute(select(User).where(User.idt_user==idt_user))
            return result.scalar()

class TransactionsService:
    async def list_transaction():
        async with async_session() as session:
            result = await session.execute(select(Transactions))
            return result.scalars().all()

    async def delete_transaction(cod_transaction: int):
        async with async_session() as session:
            await session.execute(delete(Transactions).where(Transactions.cod_transaction==cod_transaction))
            await session.commit()      

    async def get_by_id(cod_transaction):
        async with async_session() as session:
            result = await session.execute(select(Transactions).where(Transactions.cod_transaction==cod_transaction))
            return result.scalar()

    async def get_by_idt_user(idt_user):
        async with async_session() as session:
            result = await session.execute(select(Transactions).where(Transactions.idt_user==idt_user))
            return result.scalar().all()            
                

    async def create_transaction(
        cod_ticker: str, 
        des_broker: str, 
        type_transaction: str,
        num_amount: int,
        num_price_cost: float,
        num_cost_operation: float,
        idt_user: int,
        dat_transaction: date):
        async with async_session() as session:
            session.add(Transactions(
                cod_ticker=cod_ticker,
                des_broker=des_broker,
                type_transaction=type_transaction,
                num_amount=num_amount,
                num_price_cost=num_price_cost,
                num_cost_operation=num_cost_operation,
                idt_user=idt_user,
                dat_transaction=dat_transaction
                 ))
            await session.commit()