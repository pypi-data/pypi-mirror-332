from typing import Annotated, List
from pydantic import BaseModel, Field

from .claim_id import claim_id_pattern
from .source import Source


class Support(BaseModel):
    """
    A list of premises (claims) that together support some conclusion (another claim).
    """
    premises: List[Annotated[str, Field(pattern=claim_id_pattern)]] = Field(
            description="IDs of the claims that provide linked support for the conclusion",
            min_length=1
        )
    sources: List[Source] = Field(
            description="Sources for this support relation",
            min_length=1
        )
