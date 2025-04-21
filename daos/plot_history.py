from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlalchemy import select

from .base import Base
from dtos import PlotHistory as PlotHistoryDTO

import uuid

class PlotHistory(Base):
    def __init__(self, session: AsyncSession):
        super().__init__(PlotHistoryDTO, session)

    async def get_tranctions_by_plot_id(self, plot_id: uuid.UUID) -> List[PlotHistoryDTO]:
        result = await self.session.execute(
            select(self.model).where(self.model.plot_id == plot_id)
        )
        return result.scalars().all()
    
    async def get_tranctions_by_customer_id(self, customer_id: uuid.UUID) -> List[PlotHistoryDTO]:
        result = await self.session.execute(
            select(self.model).where(self.model.customer_id == customer_id)
        )
        return result.scalars().all()
    


    
