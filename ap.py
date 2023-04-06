from fastapi import FastAPI, Request, Form, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import glob

directory_path = 'Media/Result/'

ap = FastAPI()
ap.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates/")

@ap.get("/")
def home(request: Request):
    return templates.TemplateResponse("index1.html", {"request": request})

from fastapi.responses import FileResponse

@ap.get('/result')
def result_mp4():
    video_path = "plwNT.mp4"
    return FileResponse(video_path, media_type='video/mp4', filename='video.mp4')
