from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import PlainTextResponse


from .cars import create_cars

cars = create_cars(100)  # Здесь хранятся список машин
app = FastAPI()


@app.get("/")
def index():
    return Response("<a href='/cars'>Cars</a>")


# (сюда писать решение)

# cars-pagination
@app.get("/cars")
def get_cars(page: int = 1, limit: int = 10):
    start = (page - 1) * limit
    end = start + limit
    return cars[start:end]

# get car id
@app.get("/cars/{id}")
def get_car_by_id(id: int):
    for car in cars:
        if car["id"] == id:
            return car
    # weird way to handle exception to pass the test:
    return PlainTextResponse("Not found", status_code=404)
    # this way is more natural but it fails the test:
    # raise HTTPException(status_code=404, detail="Not found")

# (конец решения)
