from fastapi import FastAPI
# from routes.user import user
# from routes.navigate import navigator
from routes.file import filerouter
from routes.blockchainroute import block
from fastapi.staticfiles import StaticFiles
import uvicorn

app=FastAPI()

app.mount("/static", StaticFiles(directory="html"), name="static")

app.include_router(block)

# app.include_router(navigator)

app.include_router(filerouter)

uvicorn.run(app,host='0.0.0.0',port=9000) 