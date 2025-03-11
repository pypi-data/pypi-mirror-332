from pydantic import BaseModel, Field

class ESGDisclosureItem(BaseModel):
    date: str = Field(..., description="The date of the ESG disclosure")
    acceptedDate: str = Field(..., description="The accepted date of the ESG disclosure")
    symbol: str = Field(..., description="The symbol of the ESG disclosure")
    cik: str = Field(..., description="The cik of the ESG disclosure")
    companyName: str = Field(..., description="The company name of the ESG disclosure")
    formType: str = Field(..., description="The form type of the ESG disclosure")
    environmentalScore: float = Field(..., description="The environmental score of the ESG disclosure")
    socialScore: float = Field(..., description="The social score of the ESG disclosure")
    governanceScore: float = Field(..., description="The governance score of the ESG disclosure")
    ESGScore: float = Field(..., description="The ESG score of the ESG disclosure")
    url: str = Field(..., description="The url of the ESG disclosure")

class ESGRatingItem(BaseModel):
    symbol: str = Field(..., description="The symbol of the ESG rating")
    cik: str = Field(..., description="The cik of the ESG rating")
    companyName: str = Field(..., description="The company name of the ESG rating")
    industry: str = Field(..., description="The industry of the ESG rating")
    fiscalYear: int = Field(..., description="The fiscal year of the ESG rating")
    ESGRiskRating: str = Field(..., description="The ESG risk rating of the ESG rating")
    industryRank: str = Field(..., description="The industry rank of the ESG rating")

class ESGBenchmarkItem(BaseModel):
    fiscalYear: int = Field(..., description="The fiscal year of the ESG benchmark")
    sector: str = Field(..., description="The sector of the ESG benchmark")
    environmentalScore: float = Field(..., description="The environmental score of the ESG benchmark")
    socialScore: float = Field(..., description="The social score of the ESG benchmark")
    governanceScore: float = Field(..., description="The governance score of the ESG benchmark")
    ESGScore: float = Field(..., description="The ESG score of the ESG benchmark")