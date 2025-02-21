# app/models/reading.py

from sqlalchemy import Column, Integer, String, Float, DateTime
from app.db.base_class import Base
from datetime import datetime

class SubstationReading(Base):
    __tablename__ = "substation_readings"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    substation_id = Column(String, index=True)
    energy_supply_mw = Column(Float)
    energy_demand_mw = Column(Float)
    voltage_v = Column(Float)
    frequency_hz = Column(Float)
    faults_detected = Column(Integer, default=0)