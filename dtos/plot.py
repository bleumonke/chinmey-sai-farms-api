from .base import Base
from sqlalchemy import func, Column, String, JSON, Boolean, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Plot(Base):
    __tablename__ = "plots"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    layout_id = Column(UUID(as_uuid=True), ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"), nullable=True)
    area_in_acres = Column(Float, nullable=False)
    number = Column(String(20), nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    perimeter_coordinates = Column(JSON, nullable=True)
    center_coordinates = Column(JSON, nullable=True)