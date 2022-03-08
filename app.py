'''Imports'''
from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata
'''Init Server'''
app = FastAPI(
    title="API with FastAPI and MongoDB",
    description="This is API for the class BDD",
    version="1.0",
    openapi_tags=tags_metadata
)

'''Add routes user'''
app.include_router(user)
