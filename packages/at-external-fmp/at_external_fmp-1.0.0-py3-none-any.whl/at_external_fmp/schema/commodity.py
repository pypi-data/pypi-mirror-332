from pydantic import BaseModel, Field

class CommodityItem(BaseModel):
    symbol: str = Field(..., description="The symbol of the commodity")
    name: str = Field(..., description="The name of the commodity")
    exchange: str | None = Field(None, description="The exchange of the commodity")
    tradeMonth: str = Field(..., description="The trade month of the commodity")