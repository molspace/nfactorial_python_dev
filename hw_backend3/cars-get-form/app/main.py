from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from .cars import create_cars

cars = create_cars(100)
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# (сюда писать решение)


# (конец решения)
