from pydantic import BaseModel, Field

class CryptoCurrency(BaseModel):
    symbol: str = Field(..., description="The symbol of the crypto")
    name: str = Field(..., description="The name of the crypto")
    exchange: str = Field(..., description="The exchange of the crypto")
    icoDate: str | None = Field(None, description="The ico date of the crypto")
    circulatingSupply: int | float | None = Field(None, description="The circulating supply of the crypto")
    totalSupply: int | float | None = Field(None, description="The total supply of the crypto")
