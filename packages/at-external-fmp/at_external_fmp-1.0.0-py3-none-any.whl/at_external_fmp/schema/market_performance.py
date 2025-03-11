from pydantic import BaseModel, Field

class SectorPerformanceSnapshot(BaseModel):
    date: str = Field(..., description="The date of the performance snapshot")
    sector: str = Field(..., description="The sector of the performance snapshot")
    exchange: str = Field(..., description="The exchange of the performance snapshot")
    averageChange: float = Field(..., description="The average change of the sector")

class IndustryPerformanceSnapshot(BaseModel):
    date: str = Field(..., description="The date of the performance snapshot")
    industry: str = Field(..., description="The industry of the performance snapshot")
    exchange: str = Field(..., description="The exchange of the performance snapshot")
    averageChange: float = Field(..., description="The average change of the industry")

class SectorPESnapshot(BaseModel):
    date: str = Field(..., description="The date of the PE snapshot")
    sector: str = Field(..., description="The sector of the PE snapshot")
    exchange: str = Field(..., description="The exchange of the PE snapshot")
    pe: float = Field(..., description="The PE of the sector")

class IndustryPESnapshot(BaseModel):
    date: str = Field(..., description="The date of the PE snapshot")
    industry: str = Field(..., description="The industry of the PE snapshot")
    exchange: str = Field(..., description="The exchange of the PE snapshot")
    pe: float = Field(..., description="The PE of the industry")

class Stock(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    price: float = Field(..., description="The price of the stock")
    name: str = Field(..., description="The name of the stock")
    change: float = Field(..., description="The change of the stock")
    changesPercentage: float = Field(..., description="The changes percentage of the stock")
    exchange: str = Field(..., description="The exchange of the stock")