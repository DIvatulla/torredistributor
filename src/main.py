import uvicorn
from fastapi import FastAPI
from web import owner
import logging
import sys

app = FastAPI()

app.include_router(owner.router)

if __name__ == "__main__":
	uvicorn.run(
		"main:app", 
		host="localhost", 
		port=8000, 
		reload=True
	)
	
