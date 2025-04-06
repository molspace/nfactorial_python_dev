from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date, timedelta

from app.schemas.activity import ActivityCreate, UserActivityCreate
from app.schemas.user_activity import ActivityProgress
from app.models.activity import Activity
from app.models.user_activity import UserActivity
from app.db.session import get_db
from app.core.auth import get_current_user

router = APIRouter()

@router.post("/create")
def create_activity(payload: ActivityCreate, db: Session = Depends(get_db)):
    existing = db.query(Activity).filter_by(name=payload.name).first()
    if existing:
        return {"message": "Activity already exists", "activity": existing}
    
    activity = Activity(name=payload.name)
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity

@router.post("/start")
def start_activity(payload: UserActivityCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    user_activity = UserActivity(user_id=user.id, activity_id=payload.activity_id, streak=0)
    db.add(user_activity)
    db.commit()
    db.refresh(user_activity)
    return {"message": "Activity started", "activity": user_activity}

@router.post("/record")
def record_activity(payload: UserActivityCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    user_activity = db.query(UserActivity).filter_by(user_id=user.id, activity_id=payload.activity_id).first()
    if not user_activity:
        raise HTTPException(status_code=404, detail="User activity not found")
    
    today = date.today()
    yesterday = today - timedelta(days=1)

    if user_activity.last_practiced == today:
        return {"message": "Already recorded for today", "streak": user_activity.streak}

    if user_activity.last_practiced == yesterday:
        user_activity.streak += 1
    else:
        if user_activity.streak_frozen:
            user_activity.streak_frozen = False  # Use streak freeze
        else:
            user_activity.streak = 1  # Restart streak

    user_activity.last_practiced = today
    db.commit()
    return {"message": "Activity recorded", "streak": user_activity.streak}

# TODO: decide if relevant or redundant
@router.post("/complete")
def complete_activity(payload: UserActivityCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    user_activity = db.query(UserActivity).filter_by(user_id=user.id, activity_id=payload.activity_id).first()

    if not user_activity:
        raise HTTPException(status_code=404, detail="Activity not started yet")

    today = date.today()

    if user_activity.last_completed_date == today:
        raise HTTPException(status_code=400, detail="Activity already completed today")

    yesterday = today - timedelta(days=1)

    if user_activity.last_completed_date == yesterday:
        user_activity.streak += 1
    elif user_activity.has_freeze:
        user_activity.has_freeze = False  # Use streak freeze
    else:
        user_activity.streak = 1  # Restart streak

    user_activity.last_completed_date = today

    db.commit()
    db.refresh(user_activity)

    return {"message": "Activity completed for today!", "streak": user_activity.streak}

@router.get("/progress", response_model=list[ActivityProgress])
def get_user_progress(db: Session = Depends(get_db), user=Depends(get_current_user)):
    user_activities = db.query(UserActivity).filter(UserActivity.user_id == user.id).join(Activity).all()

    progress = []
    for user_activity in user_activities:
        # TODO: tmp ensured has_freeze is either True or False
        has_freeze = user_activity.has_freeze if user_activity.has_freeze is not None else False
        progress.append(ActivityProgress(
            activity_id=str(user_activity.activity_id),
            activity_name=user_activity.activity.name,
            streak=user_activity.streak,
            streak_frozen=user_activity.streak_frozen,
            has_freeze=has_freeze,
            last_practiced=user_activity.last_practiced,
            last_completed_date=user_activity.last_completed_date,
        ))

    return progress

