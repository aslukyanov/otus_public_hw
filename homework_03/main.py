from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import asyncio

from fastapi.templating import Jinja2Templates
from shed import get_my_shed

app = FastAPI()
templates = Jinja2Templates(directory="./template")

@app.get("/")
async def home():
    data = {
        "name": "My 2021 schedule",
        "ex": "Go to /my_sched/gay_month page"
    }
    return {"data": data}


@app.get("/my_sched/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):

    
    month = int(page_name.split("_")[1])
    day = int(page_name.split("_")[0])

    data = {
        "page": get_my_shed(day, month)
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})











