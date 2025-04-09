from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from .repository import CarsRepository

app = FastAPI()

templates = Jinja2Templates(directory="templates")
repository = CarsRepository()


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/cars")
def get_cars(request: Request):
    cars = repository.get_all()
    return templates.TemplateResponse(
        "cars/index.html",
        {"request": request, "cars": cars},
    )


# (сюда писать решение)



# (конец решения)
