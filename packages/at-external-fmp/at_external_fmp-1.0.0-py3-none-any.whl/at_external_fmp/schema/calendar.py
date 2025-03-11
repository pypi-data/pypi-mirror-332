from pydantic import BaseModel, Field

class Dividends(BaseModel):
	symbol: str = Field(..., description="The symbol of the stock")
	date: str = Field(..., description="The date of the dividend")
	recordDate: str = Field(..., description="The record date of the dividend")
	paymentDate: str = Field(..., description="The payment date of the dividend")
	declarationDate: str = Field(..., description="The declaration date of the dividend")
	adjDividend: float = Field(..., description="The adjusted dividend of the stock")
	dividend: float = Field(..., description="The dividend of the stock")
	theYield: float = Field(..., alias="yield", description="The yield of the stock")
	frequency: str | None = Field(None, description="The frequency of the dividend")

class Earnings(BaseModel):
	symbol: str = Field(..., description="The symbol of the stock")
	date: str = Field(..., description="The date of the earnings")
	epsActual: float | None = Field(None, description="The actual earnings per share")
	epsEstimated: float | None = Field(None, description="The estimated earnings per share")
	revenueActual: float | None = Field(None, description="The actual revenue")
	revenueEstimated: float | None = Field(None, description="The estimated revenue")
	lastUpdated: str = Field(..., description="The last updated date")

class Splits(BaseModel):
	symbol: str = Field(..., description="The symbol of the stock")
	date: str = Field(..., description="The date of the split")
	numerator: int | float = Field(..., description="The numerator of the split")
	denominator: int | float = Field(..., description="The denominator of the split")

class IPOs(BaseModel):
	symbol: str = Field(..., description="The symbol of the stock")
	date: str = Field(..., description="The date of the ipo")
	daa: str = Field(..., description="The date and time of the ipo")
	company: str = Field(..., description="The company of the ipo")
	exchange: str = Field(..., description="The exchange of the ipo")
	actions: str = Field(..., description="The actions of the ipo")
	shares: float | None = Field(None, description="The shares of the ipo")
	priceRange: float | None = Field(None, description="The price range of the ipo")
	marketCap: float | None = Field(None, description="The market cap of the ipo")

class IPOsDisclosure(BaseModel):
	symbol: str = Field(..., description="The symbol of the stock")
	filingDate: str = Field(..., description="The filing date of the ipo")
	acceptedDate: str = Field(..., description="The accepted date of the ipo")
	effectivenessDate: str = Field(..., description="The effectiveness date of the ipo")
	cik: str = Field(..., description="The cik of the ipo")
	form: str = Field(..., description="The form of the ipo")
	url: str = Field(..., description="The url of the ipo")

class IPOsProspectus(BaseModel):
	symbol: str = Field(..., description="The symbol of the stock")
	acceptedDate: str = Field(..., description="The accepted date of the ipo")
	filingDate: str = Field(..., description="The filing date of the ipo")
	ipoDate: str = Field(..., description="The ipo date of the ipo")
	cik: str = Field(..., description="The cik of the ipo")
	pricePublicPerShare: float = Field(..., description="The price public per share of the ipo")
	pricePublicTotal: float = Field(..., description="The price public total of the ipo")
	discountsAndCommissionsPerShare: float = Field(..., description="The discounts and commissions per share of the ipo")
	discountsAndCommissionsTotal: float = Field(..., description="The discounts and commissions total of the ipo")
	proceedsBeforeExpensesPerShare: float = Field(..., description="The proceeds before expenses per share of the ipo")
	proceedsBeforeExpensesTotal: float = Field(..., description="The proceeds before expenses total of the ipo")
	form: str = Field(..., description="The form of the ipo")
	url: str = Field(..., description="The url of the ipo")
