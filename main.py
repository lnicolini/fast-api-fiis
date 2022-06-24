from fastapi import FastAPI, APIRouter

from views import user_router, transaction_router

app = FastAPI()
router = APIRouter()

@router.get('/')
def first():
    return 'Hello world!'

app.include_router(user_router)
app.include_router(transaction_router)