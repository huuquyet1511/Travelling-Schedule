from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Text, Enum, DateTime
from sqlalchemy.orm import relationship
from app import db, app


class BaseModel(db.Model):
    __abstract__ = True  # lớp thành lớp trừu tượng
    id = Column(Integer, primary_key=True, autoincrement=True)

class Destination(BaseModel):
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)

    def __str__(self):
        return self.name

class TouristAttraction(BaseModel):
    name = Column(String(50), nullable=False)
