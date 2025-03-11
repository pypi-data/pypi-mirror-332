from pydantic import BaseModel, Field

class IndexItem(BaseModel):
    symbol: str = Field(..., description="The symbol of the index")
    name: str = Field(..., description="The name of the index")
    exchange: str = Field(..., description="The exchange of the index")
    currency: str = Field(..., description="The currency of the index")

class IndexConstituent(BaseModel):
    symbol: str = Field(..., description="The symbol of the index")
    name: str = Field(..., description="The name of the index")
    sector: str = Field(..., description="The sector of the index")
    subSector: str = Field(..., description="The sub sector of the index")
    headQuarter: str = Field(..., description="The head quarter of the index")
    dateFirstAdded: str | None = Field(None, description="The date first added of the index")
    cik: str = Field(..., description="The cik of the index")
    founded: str = Field(..., description="The founded of the index")