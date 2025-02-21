# app/api/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core import security
from app.core.config import settings
from app.db.session import get_db
from datetime import timedelta

router = APIRouter()


@router.post("/login")
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    # Mock user authentication - replace with actual DB check later
    if form_data.username != "test@example.com" or form_data.password != "test123":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# app/api/users.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db

router = APIRouter()


@router.get("/")
def read_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    # Mock user list - replace with actual DB query later
    return [
        {
            "id": 1,
            "email": "user1@example.com",
            "is_active": True
        },
        {
            "id": 2,
            "email": "user2@example.com",
            "is_active": True
        }
    ]


@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    # Mock single user - replace with actual DB query later
    return {
        "id": user_id,
        "email": f"user{user_id}@example.com",
        "is_active": True
    }


# app/api/readings.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from datetime import datetime, timedelta
import random

router = APIRouter()


@router.get("/")
def get_readings(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100
):
    # Mock readings data - replace with actual DB query later
    mock_readings = []
    base_time = datetime.utcnow()

    for i in range(limit):
        reading_time = base_time - timedelta(minutes=15 * i)
        mock_readings.append({
            "id": i + 1,
            "timestamp": reading_time,
            "substation_id": "SUB_001",
            "energy_supply_mw": round(random.uniform(80, 90), 2),
            "energy_demand_mw": round(random.uniform(70, 85), 2),
            "voltage_v": round(random.uniform(229, 231), 1),
            "frequency_hz": round(random.uniform(49.9, 50.1), 2),
            "faults_detected": random.randint(0, 2)
        })

    return mock_readings


@router.get("/{substation_id}")
def get_substation_readings(
        substation_id: str,
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100
):
    # Mock readings for specific substation - replace with actual DB query later
    mock_readings = []
    base_time = datetime.utcnow()

    for i in range(limit):
        reading_time = base_time - timedelta(minutes=15 * i)
        mock_readings.append({
            "id": i + 1,
            "timestamp": reading_time,
            "substation_id": substation_id,
            "energy_supply_mw": round(random.uniform(80, 90), 2),
            "energy_demand_mw": round(random.uniform(70, 85), 2),
            "voltage_v": round(random.uniform(229, 231), 1),
            "frequency_hz": round(random.uniform(49.9, 50.1), 2),
            "faults_detected": random.randint(0, 2)
        })

    return mock_readings


@router.post("/")
def create_reading(
        substation_id: str,
        energy_supply_mw: float,
        energy_demand_mw: float,
        db: Session = Depends(get_db)
):
    # Mock creating a new reading - replace with actual DB operation later
    return {
        "id": random.randint(1000, 9999),
        "timestamp": datetime.utcnow(),
        "substation_id": substation_id,
        "energy_supply_mw": energy_supply_mw,
        "energy_demand_mw": energy_demand_mw,
        "voltage_v": round(random.uniform(229, 231), 1),
        "frequency_hz": round(random.uniform(49.9, 50.1), 2),
        "faults_detected": 0
    }