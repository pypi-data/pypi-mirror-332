from typing import List
from datetime import datetime
from pydantic import Field
from at_common_schemas.base import BaseSchema
from at_common_schemas.common.news import ( News )

class NewsLatestBatchRequest(BaseSchema):
    date_from: datetime = Field(..., description="The start date of the news articles to retrieve")
    date_to: datetime = Field(..., description="The end date of the news articles to retrieve")
    limit: int = Field(..., description="Maximum number of news articles to retrieve")

class NewsLatestBatchResponse(BaseSchema):
    items: List[News] = Field(..., description="List of market news articles")

class NewsStockBatchRequest(BaseSchema):
    symbol: str = Field(..., description="The stock ticker symbol to fetch news for")
    date_from: datetime = Field(..., description="The start date of the news articles to retrieve")
    date_to: datetime = Field(..., description="The end date of the news articles to retrieve")
    limit: int = Field(..., description="Maximum number of news articles to retrieve")

class NewsStockBatchResponse(BaseSchema):
    items: List[News] = Field(..., description="List of stock-specific news articles")