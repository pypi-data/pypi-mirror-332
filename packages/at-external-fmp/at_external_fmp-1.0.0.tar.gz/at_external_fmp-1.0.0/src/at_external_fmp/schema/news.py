from pydantic import BaseModel, Field

class FMPArticle(BaseModel):
	title: str = Field(..., description="The title of the article")
	date: str = Field(..., description="The date of the article")
	content: str = Field(..., description="The content of the article")
	tickers: str = Field(..., description="The tickers of the article")
	image: str = Field(..., description="The image of the article")
	link: str = Field(..., description="The link of the article")
	author: str = Field(..., description="The author of the article")
	site: str = Field(..., description="The site of the article")

class NewsItem(BaseModel):
	symbol: str | None = Field(None, description="The symbol of the news")
	publishedDate: str = Field(..., description="The published date of the news")
	publisher: str = Field(..., description="The publisher of the news")
	title: str = Field(..., description="The title of the news")
	image: str | None = Field(None, description="The image of the news")
	site: str = Field(..., description="The site of the news")
	text: str = Field(..., description="The text of the news")
	url: str = Field(..., description="The url of the news")