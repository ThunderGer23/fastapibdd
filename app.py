'''Imports'''
from fastapi import FastAPI
from routes.user import user

'''Init Server'''
app = FastAPI()

'''Add routes user'''
app.include_router(user)
