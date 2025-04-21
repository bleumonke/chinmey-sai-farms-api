from pydantic import BaseModel, computed_field
from typing import Optional
import uuid

class PlotCreate(BaseModel):
    layout_id: uuid.UUID
    number: str
    name: str
    area_in_acres: float
    is_active: bool = True
    customer_id: Optional[uuid.UUID] = None
    description: Optional[str] = None
    center_coordinates: Optional[dict] = None
    perimeter_coordinates: Optional[dict] = None


class PlotUpdate(BaseModel):
    layout_id: Optional[str] = None
    customer_id: Optional[uuid.UUID] = None
    number: Optional[str] = None
    name: Optional[str] = None
    area_in_acres: Optional[float] = None
    is_active: Optional[bool] = None
    description: Optional[str] = None
    center_coordinates: Optional[dict] = None
    perimeter_coordinates: Optional[dict] = None
    
class PlotResponse(PlotUpdate):
    id: uuid.UUID

    @computed_field
    @property
    def is_sold(self) -> bool:
        return self.customer_id is not None

    model_config = {
        "from_attributes": True
    }