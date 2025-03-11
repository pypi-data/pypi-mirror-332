from pydantic import BaseModel, Field

class PriceEODLight(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    date: str = Field(..., description="The date of the chart")
    price: float = Field(..., description="The price of the stock")
    volume: int = Field(..., description="The volume of the stock")

class PriceEODFull(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    date: str = Field(..., description="The date of the chart")
    open: float = Field(..., description="The open price of the stock")
    high: float = Field(..., description="The high price of the stock")
    low: float = Field(..., description="The low price of the stock")
    close: float = Field(..., description="The close price of the stock")
    volume: int = Field(..., description="The volume of the stock")
    change: float = Field(..., description="The change of the stock")
    changePercent: float = Field(..., description="The change percent of the stock")
    vwap: float = Field(..., description="The vwap of the stock")

class PriceEODAdjusted(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    date: str = Field(..., description="The date of the chart")
    adjOpen: float = Field(..., description="The adj open price of the stock")
    adjHigh: float = Field(..., description="The adj high price of the stock")
    adjLow: float = Field(..., description="The adj low price of the stock")
    adjClose: float = Field(..., description="The adj close price of the stock")
    volume: int = Field(..., description="The volume of the stock")

class PriceIntraday(BaseModel):
    date: str = Field(..., description="The date of the chart")
    open: float = Field(..., description="The open price of the stock")
    low: float = Field(..., description="The low price of the stock")
    high: float = Field(..., description="The high price of the stock")
    close: float = Field(..., description="The close price of the stock")
    volume: int = Field(..., description="The volume of the stock")