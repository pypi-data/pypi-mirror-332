from pydantic import BaseModel, Field, AliasChoices

class StockItem(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    name: str = Field(..., description="The company name of the stock", validation_alias=AliasChoices('companyName', 'name'))

class FinancialStatementSymbolItem(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    companyName: str = Field(..., description="The company name of the stock")
    tradingCurrency: str | None = Field(None, description="The trading currency of the stock")
    reportingCurrency: str | None = Field(None, description="The reporting currency of the stock")

class CIKItem(BaseModel):
    cik: str = Field(..., description="The cik of the stock")
    companyName: str = Field(..., description="The company name of the stock")

class SymbolChangeItem(BaseModel):
    date: str = Field(..., description="The date of the symbol change")
    companyName: str = Field(..., description="The company name of the stock")
    oldSymbol: str = Field(..., description="The old symbol of the stock")
    newSymbol: str = Field(..., description="The new symbol of the stock")

class EarningsTranscriptItem(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    companyName: str = Field(..., description="The company name of the stock")
    noOfTranscripts: int = Field(..., description="The number of transcripts of the stock")

class ExchangeItem(BaseModel):
    exchange: str = Field(..., description="The exchange name")

class SectorItem(BaseModel):
    sector: str = Field(..., description="The sector name")

class IndustryItem(BaseModel):
    industry: str = Field(..., description="The industry name")

class CountryItem(BaseModel):
    country: str = Field(..., description="The country name")