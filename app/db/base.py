# app/db/base.py

from app.db.base_class import Base  # ✅ Ensure all models use the same Base
from app.models.user import User
from app.models.reading import SubstationReading

# Import all additional models here for Alembic to detect them
# from app.models.some_other_model import SomeOtherModel
