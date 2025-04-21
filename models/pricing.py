from pydantic import BaseModel, computed_field
from typing import Optional
from enum import Enum
from datetime import date
import uuid

# Enum for Payment Mode
class PaymentMode(str, Enum):
    OUT_RIGHT = "OUT-RIGHT"
    EMI = "EMI"

# Enum for Pricing Status
class PricingStatus(str, Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    UPCOMING = "upcoming"

# PricingCreate model
class PricingCreate(BaseModel):
    crop_id: uuid.UUID
    name: str
    payment_mode: PaymentMode
    extent_unit: str = "acre"
    extent_min_value: float
    extent_max_value: Optional[float] = None
    cost_per_acre: Optional[float] = None
    cost_per_cent: Optional[float] = None
    cost_per_sqft: Optional[float] = None
    total_cost_per_acre: Optional[float] = None
    emi_per_month: Optional[float] = None
    valid_from: Optional[date] = None
    valid_to: Optional[date] = None
    description: Optional[str] = None

# PricingUpdate model
class PricingUpdate(BaseModel):
    crop_id: Optional[uuid.UUID] = None
    name: Optional[str] = None
    payment_mode: Optional[PaymentMode] = None
    extent_unit: Optional[str] = "acre"
    extent_min_value: Optional[float] = None
    extent_max_value: Optional[float] = None
    cost_per_acre: Optional[float] = None
    cost_per_cent: Optional[float] = None
    cost_per_sqft: Optional[float] = None
    total_cost_per_acre: Optional[float] = None
    emi_per_month: Optional[float] = None
    valid_from: Optional[date] = None
    valid_to: Optional[date] = None
    description: Optional[str] = None

# PricingResponse model
class PricingResponse(PricingUpdate):
    id: uuid.UUID

    @computed_field
    @property
    def status(self) -> PricingStatus:
        today = date.today()
        if self.valid_from and today < self.valid_from:
            return PricingStatus.UPCOMING
        if self.valid_to and today > self.valid_to:
            return PricingStatus.EXPIRED
        return PricingStatus.ACTIVE

    model_config = {
        "from_attributes": True,
        "computed_fields": ["status"]
    }
