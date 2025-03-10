from typing import Dict
from pydantic import BaseModel, Field, JsonValue
from pydantic.networks import HttpUrl


class Source(BaseModel):
    """
    The source of a text or support relationship.
    """
    name: str = Field(
            description="Name of the source (e.g., domain or generation method)"
        )
    text: str | None = Field(
            default=None,
            description="Original text taken from the source"
        )
    url: HttpUrl | None = Field(
            default=None,
            description="URL from which the text or support relationship was taken"
        )
    annotations: Dict[str, JsonValue] = Field(
            default={},
            description="Further data on the source"
        )
