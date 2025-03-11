from pydantic import BaseModel, Field

class ForexItem(BaseModel):
    symbol: str = Field(..., description="The symbol of the forex")
    fromCurrency: str = Field(..., description="The from currency of the forex")
    toCurrency: str = Field(..., description="The to currency of the forex")
    fromName: str = Field(..., description="The from name of the forex")
    toName: str = Field(..., description="The to name of the forex")