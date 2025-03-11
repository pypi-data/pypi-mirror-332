from pydantic import BaseModel, Field

class AnalystEstimates(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    date: str = Field(..., description="The date of the estimate")
    revenueLow: float = Field(..., description="The low revenue estimate")
    revenueHigh: float = Field(..., description="The high revenue estimate")
    revenueAvg: float = Field(..., description="The average revenue estimate")
    ebitdaLow: float = Field(..., description="The low ebitda estimate")
    ebitdaHigh: float = Field(..., description="The high ebitda estimate")
    ebitdaAvg: float = Field(..., description="The average ebitda estimate")
    ebitLow: float = Field(..., description="The low ebit estimate")
    ebitHigh: float = Field(..., description="The high ebit estimate")
    ebitAvg: float = Field(..., description="The average ebit estimate")
    netIncomeLow: float = Field(..., description="The low net income estimate")
    netIncomeHigh: float = Field(..., description="The high net income estimate")
    netIncomeAvg: float = Field(..., description="The average net income estimate")
    sgaExpenseLow: float = Field(..., description="The low sga expense estimate")
    sgaExpenseHigh: float = Field(..., description="The high sga expense estimate")
    sgaExpenseAvg: float = Field(..., description="The average sga expense estimate")
    epsAvg: float = Field(..., description="The average eps estimate")
    epsHigh: float = Field(..., description="The high eps estimate")
    epsLow: float = Field(..., description="The low eps estimate")
    numAnalystsRevenue: int = Field(..., description="The number of analysts for the revenue estimate")
    numAnalystsEps: int = Field(..., description="The number of analysts for the eps estimate")

class RatingsSnapshot(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    rating: str = Field(..., description="The rating of the stock")
    overallScore: int = Field(..., description="The overall score of the stock")
    discountedCashFlowScore: int = Field(..., description="The discounted cash flow score of the stock")
    returnOnEquityScore: int = Field(..., description="The return on equity score of the stock")
    returnOnAssetsScore: int = Field(..., description="The return on assets score of the stock")
    debtToEquityScore: int = Field(..., description="The debt to equity score of the stock")
    priceToEarningsScore: int = Field(..., description="The price to earnings score of the stock")
    priceToBookScore: int = Field(..., description="The price to book score of the stock")

class RatingsHistorical(RatingsSnapshot):
    date: str = Field(..., description="The date of the rating")

class PriceTargetSummary(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    lastMonthCount: int = Field(..., description="The number of price targets in the last month")
    lastMonthAvgPriceTarget: float = Field(..., description="The average price target in the last month")
    lastQuarterCount: int = Field(..., description="The number of price targets in the last quarter")
    lastQuarterAvgPriceTarget: float = Field(..., description="The average price target in the last quarter")
    lastYearCount: int = Field(..., description="The number of price targets in the last year")
    lastYearAvgPriceTarget: float = Field(..., description="The average price target in the last year")
    allTimeCount: int = Field(..., description="The number of price targets in all time")
    allTimeAvgPriceTarget: float = Field(..., description="The average price target in all time")
    publishers: str = Field(..., description="The publishers of the price targets")

class PriceTargetConsensus(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    targetHigh: float = Field(..., description="The high price target of the stock")
    targetLow: float = Field(..., description="The low price target of the stock")
    targetConsensus: float = Field(..., description="The consensus price target of the stock")
    targetMedian: float = Field(..., description="The median price target of the stock")

class PriceTargetNews(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    publishedDate: str = Field(..., description="The published date of the news")
    newsURL: str = Field(..., description="The url of the news")
    newsTitle: str = Field(..., description="The title of the news")
    analystName: str = Field(..., description="The name of the analyst")
    priceTarget: float = Field(..., description="The price target of the news")
    adjPriceTarget: float = Field(..., description="The adjusted price target of the news")
    priceWhenPosted: float = Field(..., description="The price when the news was posted")
    newsPublisher: str = Field(..., description="The publisher of the news")
    newsBaseURL: str = Field(..., description="The base url of the news")
    analystCompany: str = Field(..., description="The company of the analyst")    

class Grades(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    date: str = Field(..., description="The date of the grade")
    gradingCompany: str = Field(..., description="The company of the grade")
    previousGrade: str = Field(..., description="The previous grade of the stock")
    newGrade: str = Field(..., description="The new grade of the stock")
    action: str = Field(..., description="The action of the grade")

class GradesHistorical(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    date: str = Field(..., description="The date of the grade")
    analystRatingsBuy: int = Field(..., description="The number of analyst ratings buy")
    analystRatingsHold: int = Field(..., description="The number of analyst ratings hold")
    analystRatingsSell: int = Field(..., description="The number of analyst ratings sell")
    analystRatingsStrongSell: int = Field(..., description="The number of analyst ratings strong sell")

class GradesConsensus(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    strongBuy: int = Field(..., description="The number of strong buy")
    buy: int = Field(..., description="The number of buy")
    hold: int = Field(..., description="The number of hold")
    sell: int = Field(..., description="The number of sell")
    strongSell: int = Field(..., description="The number of strong sell")
    consensus: str = Field(..., description="The consensus of the grade")

class GradesNews(BaseModel):
    symbol: str = Field(..., description="The symbol of the stock")
    publishedDate: str = Field(..., description="The published date of the news")
    newsURL: str = Field(..., description="The url of the news")
    newsTitle: str = Field(..., description="The title of the news")
    newsBaseURL: str = Field(..., description="The base url of the news")
    newsPublisher: str = Field(..., description="The publisher of the news")
    newGrade: str = Field(..., description="The new grade of the news")
    previousGrade: str | None = Field(None, description="The previous grade of the news")
    gradingCompany: str = Field(..., description="The company of the grade")
    action: str = Field(..., description="The action of the grade")
    priceWhenPosted: float = Field(..., description="The price when the news was posted")