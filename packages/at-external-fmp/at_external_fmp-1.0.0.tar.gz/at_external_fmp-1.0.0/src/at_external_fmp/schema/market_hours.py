from pydantic import BaseModel, Field

class MarketHours(BaseModel):
    exchange: str = Field(..., description="The exchange of the market hours")
    name: str = Field(..., description="The name of the market hours")
    openingHour: str = Field(..., description="The opening hour of the market hours")
    closingHour: str = Field(..., description="The closing hour of the market hours")
    timezone: str = Field(..., description="The timezone of the market hours")
    isMarketOpen: bool = Field(..., description="Whether the market is open")