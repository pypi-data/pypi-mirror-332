from pydantic import BaseModel, Field

class SearchResult(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    name: str = Field(..., description="The name of the stock")
    currency: str = Field(..., description="The currency of the stock")
    exchangeFullName: str = Field(..., description="The full name of the exchange")
    exchange: str = Field(..., description="The exchange of the stock")

class SearchCIKResult(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    companyName: str = Field(..., description="The name of the stock")
    cik: str = Field(..., description="The CIK of the stock")
    exchangeFullName: str = Field(..., description="The full name of the exchange")
    exchange: str = Field(..., description="The exchange of the stock")
    currency: str = Field(..., description="The currency of the stock")

class SearchCusipResult(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    companyName: str = Field(..., description="The name of the stock")
    cusip: str = Field(..., description="The CUSIP of the stock")
    marketCap: int = Field(..., description="The market cap of the stock")

class SearchISINResult(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    name: str = Field(..., description="The name of the stock")
    isin: str = Field(..., description="The ISIN of the stock")
    marketCap: int = Field(..., description="The market cap of the stock")
    
    