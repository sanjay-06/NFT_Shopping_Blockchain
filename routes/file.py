
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from flask import redirect
from module import create_nft
import os

filerouter=APIRouter()
templates=Jinja2Templates(directory="html")

@filerouter.get("/")
def get_home(request : Request):
    arr=[]
    if os.path.isdir('./html/images'):
        arr=os.listdir('./html/images')
    return templates.TemplateResponse("index.html",{"request":request,"images":arr})

@filerouter.get("/photo/{id}")
async def get_photo(id:str,request : Request):
    return templates.TemplateResponse("photo-detail.html",{"request":request,"image":id})

@filerouter.get("/createnft")
def get_nft(request : Request):
    create_nft()
    arr=[]
    if os.path.isdir('./html/images'):
        arr=os.listdir('./html/images')
    return templates.TemplateResponse("index.html",{"request":request,"images":arr})
