from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date, timedelta

from app.schemas import activity as schemas
from app.models.activity import Activity
from app.models.user_activity import UserActivity
from app.db.session import get_db
from app.core.auth import get_current_user

router = APIRouter()

@router.post("/create")
def create_activity(payload: schemas.ActivityCreate, db: Session = Depends(get_db)):
    existing = db.query(Activity).filter_by(name=payload.name).first()
    if existing:
        return {"message": "Activity already exists", "activity": existing}
    
    activity = Activity(name=payload.name)
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity

@router.post("/start")
def start_activity(payload: schemas.UserActivityCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    user_activity = UserActivity(user_id=user.id, activity_id=payload.activity_id, streak=0)
    db.add(user_activity)
    db.commit()
    db.refresh(user_activity)
    return {"message": "Activity started", "activity": user_activity}

@router.post("/record")
def record_activity(payload: schemas.UserActivityUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ua = db.query(UserActivity).filter_by(user_id=user.id, activity_id=payload.activity_id).first()
    if not ua:
        raise HTTPException(status_code=404, detail="User activity not found")
    
    today = date.today()
    yesterday = today - timedelta(days=1)

    if ua.last_practiced == today:
        return {"message": "Already recorded for today", "streak": ua.streak}

    if ua.last_practiced == yesterday:
        ua.streak += 1
    else:
        if ua.streak_frozen:
            ua.streak_frozen = False
        else:
            ua.streak = 1

    ua.last_practiced = today
    db.commit()
    return {"message": "Activity recorded", "streak": ua.streak}
