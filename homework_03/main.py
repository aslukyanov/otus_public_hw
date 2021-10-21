from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from shed import get_my_shed, get_period_of_sched

app = FastAPI()
templates = Jinja2Templates(directory="./template")

@app.get("/")
def home():
    data = {
        "name": "My 2021 schedule",
        "sched_day": "Go to /my_sched/day_month page",
        "sched_period" : "Go to /my_sched/day1_month1_day2_month2 page"
    }
    return {"data": data}


@app.get("/my_sched/{page_name}", response_class=HTMLResponse)
def page(request: Request, page_name: str):
    if len(page_name.split("_")) == 2 :

        month = int(page_name.split("_")[1])
        day = int(page_name.split("_")[0])
        responce_date = page_name.split("_")[0] + "." + page_name.split("_")[1]
        data = {
            "shift": get_my_shed(day, month)[0],
            "day" : get_my_shed(day, month)[1],
            "responce" : responce_date
        }
        return templates.TemplateResponse("page.html", {"request": request, "data": data})

    if len(page_name.split("_")) == 4 :
        month1 = int(page_name.split("_")[1])
        day1 = int(page_name.split("_")[0])
        month2 = int(page_name.split("_")[3])
        day2 = int(page_name.split("_")[2])

        data = {
            "result": get_period_of_sched(day1, month1, day2, month2)
        }
        #print(data)
        return templates.TemplateResponse("page2.html", {"request": request, "data": data})


@app.get("/ping/", summary="Get test message")
def ping():
    return {"message": "pong"}






