from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlalchemy import select

from .base import Base
from dtos import Pricing as PricingDTO

import uuid


class Pricing(Base):
    def __init__(self, session: AsyncSession):
        super().__init__(PricingDTO, session)
    
    async def get_pricing_by_crop_id(self, crop_id: uuid.UUID) -> List[PricingDTO]:
        result = await self.session.execute(
            select(self.model).where(self.model.crop_id == crop_id)
        )
        return result.scalars().all()