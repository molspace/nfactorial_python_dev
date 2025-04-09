from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates

from .users import create_users

users = create_users(100)  # Здесь хранятся список пользователей
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# (сюда писать решение)

@app.get("/users", response_class=HTMLResponse)
def get_users(request: Request, page: int = 1, limit: int = 10):
    start = (page - 1) * limit
    end = start + limit
    paginated_users = users[start:end]
    if not paginated_users:
        return Response("No users found for the given page and limit.", status_code=404)
    return templates.TemplateResponse("/users/index.html", {"request": request, "users": paginated_users, "page": page, "limit": limit})

@app.get("/users/{user_id}", response_class=HTMLResponse)
def get_user_by_id(request: Request, user_id: int):
    for user in users:
        if user["id"] == user_id:
            return templates.TemplateResponse("/users/user.html", {"request": request, "user": user})
    return PlainTextResponse("Not found", status_code=404)

# (конец решения)
