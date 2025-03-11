from pydantic import BaseModel, Field

class Quote(BaseModel):
	symbol: str = Field(..., description="The symbol of the quote")
	name: str = Field(..., description="The name of the quote")
	price: float = Field(..., description="The price of the quote")
	changePercentage: float = Field(..., description="The changes percentage of the quote")
	change: float = Field(..., description="The change of the quote")
	volume: int = Field(..., description="The volume of the quote")
	dayLow: float = Field(..., description="The day low of the quote")
	dayHigh: float = Field(..., description="The day high of the quote")
	yearHigh: float = Field(..., description="The year high of the quote")
	yearLow: float = Field(..., description="The year low of the quote")
	marketCap: int = Field(..., description="The market cap of the quote")
	priceAvg50: float = Field(..., description="The price average of the quote")
	priceAvg200: float = Field(..., description="The price average of the quote")
	exchange: str = Field(..., description="The exchange of the quote")
	open: float = Field(..., description="The open of the quote")
	previousClose: float = Field(..., description="The previous close of the quote")
	timestamp: int = Field(..., description="The timestamp of the quote")


class QuoteShort(BaseModel):
	symbol: str = Field(..., description="The symbol of the quote")
	price: float | None = Field(None, description="The price of the quote")
	change: float | None = Field(None, description="The change of the quote")
	volume: int | float | None = Field(None, description="The volume of the quote")


class AfterMarketTrade(BaseModel):
	symbol: str = Field(..., description="The symbol of the quote")
	price: float = Field(..., description="The price of the quote")
	tradeSize: int = Field(..., description="The trade size of the quote")
	timestamp: int = Field(..., description="The timestamp of the quote")

class AfterMarketQuote(BaseModel):
	symbol: str = Field(..., description="The symbol of the quote")
	bidSize: int = Field(..., description="The bid size of the quote")
	bidPrice: float = Field(..., description="The bid price of the quote")
	askSize: int = Field(..., description="The ask size of the quote")
	askPrice: float = Field(..., description="The ask price of the quote")
	volume: int = Field(..., description="The volume of the quote")
	timestamp: int = Field(..., description="The timestamp of the quote")

class PriceChange(BaseModel):
	symbol: str = Field(..., description="The symbol of the quote")
	oneDay: float = Field(..., alias="1D", description="The one day change of the quote")
	fiveDay: float = Field(..., alias="5D", description="The five day change of the quote")
	oneMonth: float = Field(..., alias="1M", description="The one month change of the quote")
	threeMonth: float = Field(..., alias="3M", description="The three month change of the quote")
	ytd: float = Field(..., alias="ytd", description="The year to date change of the quote")
	oneYear: float = Field(..., alias="1Y", description="The one year change of the quote")
	threeYear: float = Field(..., alias="3Y", description="The three year change of the quote")
	fiveYear: float = Field(..., alias="5Y", description="The five year change of the quote")
	tenYear: float = Field(..., alias="10Y", description="The ten year change of the quote")
	max: float = Field(..., alias="max", description="The max change of the quote")