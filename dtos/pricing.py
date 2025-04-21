from .base import Base
from sqlalchemy import Column, ForeignKey, Float, String, Date
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Pricing(Base):
    __tablename__ = "pricing"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    crop_id = Column(UUID(as_uuid=True), ForeignKey("crops.id"), nullable=False)
    name = Column(String(50), nullable=False)
    payment_mode = Column(String, nullable=False)
    extent_unit = Column(String(50), nullable=False)
    extent_min_value = Column(Float, nullable=False)
    extent_max_value = Column(Float, nullable=True)
    cost_per_acre = Column(Float, nullable=True)
    cost_per_cent = Column(Float, nullable=True)
    cost_per_sqft = Column(Float, nullable=True)
    total_cost_per_acre = Column(Float, nullable=True)
    emi_per_month = Column(Float, nullable=True)
    valid_from = Column(Date, nullable=True)
    valid_to = Column(Date, nullable=True)
    description = Column(String(255), nullable=True)