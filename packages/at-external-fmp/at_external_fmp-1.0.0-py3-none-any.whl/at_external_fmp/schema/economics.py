from pydantic import BaseModel, Field

class TreasuryRate(BaseModel):
    date: str = Field(..., description="The date of the treasury rates")
    month1: float = Field(..., description="The rate of the treasury rates")
    month2: float = Field(..., description="The rate of the treasury rates")
    month3: float = Field(..., description="The rate of the treasury rates")
    month6: float = Field(..., description="The rate of the treasury rates")
    year1: float = Field(..., description="The rate of the treasury rates")
    year2: float = Field(..., description="The rate of the treasury rates")
    year3: float = Field(..., description="The rate of the treasury rates")
    year5: float = Field(..., description="The rate of the treasury rates")
    year7: float = Field(..., description="The rate of the treasury rates")
    year10: float = Field(..., description="The rate of the treasury rates")
    year20: float = Field(..., description="The rate of the treasury rates")
    year30: float = Field(..., description="The rate of the treasury rates")

class EconomicIndicator(BaseModel):
    name: str = Field(..., description="The name of the economic indicators")
    date: str = Field(..., description="The date of the economic indicators")
    value: float = Field(..., description="The value of the economic indicators")

class EconomicCalendarItem(BaseModel):
    date: str = Field(..., description="The date of the economic calendar")
    country: str = Field(..., description="The country of the economic calendar")
    event: str = Field(..., description="The event of the economic calendar")
    currency: str = Field(..., description="The currency of the economic calendar")
    previous: float | None = Field(None, description="The previous value of the economic calendar")
    estimate: float | None = Field(None, description="The estimate value of the economic calendar")
    actual: float | None = Field(None, description="The actual value of the economic calendar")
    change: float | None = Field(None, description="The change value of the economic calendar")
    impact: str = Field(..., description="The impact of the economic calendar")
    changePercentage: float | None = Field(None, description="The change percentage of the economic calendar")

class MarketRiskPremiumItem(BaseModel):
    country: str = Field(..., description="The country of the market risk premium")
    continent: str = Field(..., description="The continent of the market risk premium")
    countryRiskPremium: float = Field(..., description="The country risk premium of the market risk premium")
    totalEquityRiskPremium: float = Field(..., description="The total equity risk premium of the market risk premium")