from pydantic import BaseModel, Field

class ETFHolding(BaseModel):
    symbol: str = Field(..., description="The symbol of the ETF")
    asset: str = Field(..., description="The asset of the ETF")
    name: str = Field(..., description="The name of the ETF")
    isin: str = Field(..., description="The ISIN of the ETF")
    securityCusip: str = Field(..., description="The security CUSIP of the ETF")
    sharesNumber: int | float = Field(..., description="The number of shares in the ETF")
    weightPercentage: float = Field(..., description="The weight percentage of the ETF")
    marketValue: float = Field(..., description="The market value of the ETF")
    updatedAt: str = Field(..., description="The updated at of the ETF")
    updated: str = Field(..., description="The updated of the ETF")

class ETFInfoSector(BaseModel):
    industry: str = Field(..., description="The industry of the ETF")
    exposure: float = Field(..., description="The exposure of the ETF")

class ETFInfo(BaseModel):
    symbol: str = Field(..., description="The symbol of the ETF")
    name: str = Field(..., description="The name of the ETF")
    description: str = Field(..., description="The description of the ETF")
    isin: str = Field(..., description="The ISIN of the ETF")
    assetClass: str = Field(..., description="The asset class of the ETF")
    securityCusip: str = Field(..., description="The security CUSIP of the ETF")
    domicile: str = Field(..., description="The domicile of the ETF")
    website: str = Field(..., description="The website of the ETF")
    etfCompany: str = Field(..., description="The ETF company of the ETF")
    expenseRatio: float = Field(..., description="The expense ratio of the ETF")
    assetsUnderManagement: float = Field(..., description="The assets under management of the ETF")
    avgVolume: float = Field(..., description="The average volume of the ETF")
    inceptionDate: str = Field(..., description="The inception date of the ETF")
    nav: float = Field(..., description="The NAV of the ETF")
    navCurrency: str = Field(..., description="The NAV currency of the ETF")
    holdingsCount: int = Field(..., description="The holdings count of the ETF")
    updatedAt: str = Field(..., description="The updated at of the ETF")
    sectorsList: list[ETFInfoSector] = Field(..., description="The sectors list of the ETF")

class ETFCountryWeight(BaseModel):
    country: str = Field(..., description="The country of the ETF")
    weightPercentage: str = Field(..., description="The weight of the ETF")

class ETFAssetExposure(BaseModel):
    symbol: str = Field(..., description="The symbol of the ETF")
    asset: str = Field(..., description="The asset of the ETF")
    sharesNumber: int = Field(..., description="The shares number of the ETF")
    weightPercentage: float = Field(..., description="The weight percentage of the ETF")
    marketValue: float = Field(..., description="The market value of the ETF")

class ETFSectorWeight(BaseModel):
    symbol: str = Field(..., description="The symbol of the ETF")
    sector: str = Field(..., description="The sector of the ETF")
    weightPercentage: float = Field(..., description="The weight percentage of the ETF")