from fastapi import FastAPI
from app.api.routes import user as user_routes, activity as activity_routes
from app.db.session import Base, engine
from app.models import user, activity, user_activity

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Streaker")

app.include_router(user_routes.router, prefix="/api/users", tags=["Users"])
app.include_router(activity_routes.router, prefix="/api/activity", tags=["Activity"])
