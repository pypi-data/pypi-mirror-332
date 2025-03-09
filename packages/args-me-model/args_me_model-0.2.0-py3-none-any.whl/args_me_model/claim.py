from typing import Annotated, Iterator, List
from pydantic import BaseModel, Field, FilePath, model_validator

from .claim_id import claim_id_pattern, hash_claim_id
from .support import Support
from .source import Source


class Claim(BaseModel):
    """
    A statement that something it true.
    """
    id: Annotated[str, Field(pattern=claim_id_pattern)] = Field(
            description="The claim's unique identifier",
        )
    text: str = Field(
            description="The claim's text"
        )
    counter: Annotated[str, Field(pattern=claim_id_pattern)] | None = Field(
            default=None,
            description="ID of the counter claim to this claim",
        )
    support: List[Support] = Field(
            default=[],
            description="Other claims that support this claim as an argument"
        )
    sources: List[Source] = Field(
            description="Sources for this claim",
            min_length=1
        )

    @model_validator(mode="after")
    def _validate_sources(self):
        for source in self.sources:
            if not source.text:
                raise ValueError("Sources for a claim must contain the 'text' attribute")
        return self

    @classmethod
    def from_source(
            cls,
            source: Source,
            support: List[List['Claim']] = []) -> 'Claim':
        """
        Derive a claim object directly from the source, copying its text.

        :param cls: the class object
        :param Source source: the source object from which the claim should be derived
        :param support: a list of linked supports from the same source; each list of
        claims within the list corresponds to one linked support relation
        :type support: list[list[Claim]]
        :return: the claim object directly derived from the source
        :rtype: Claim
        :raises ValueError: if the source contains no 'text'
        """
        return cls(
                id=hash_claim_id(source.name, source.text),
                text=source.text,
                support=[Support(
                        premises=[claim.id for claim in sup],
                        sources=[source]
                    ) for sup in support],
                sources=[source]
            )

    @staticmethod
    def read_ndjson(file_name: FilePath) -> Iterator['Claim']:
        """
        Read claims from a Newline Delimited JSON file.

        :param str file_name: The name of the file to read
        :return: an iterator over the claims in the file
        :rtype: iterator[Claim]
        """
        with open(file_name) as file:
            for line in file:
                trimmed_line = line.strip()
                if trimmed_line != "":
                    yield Claim.model_validate_json(trimmed_line)

    @staticmethod
    def write_ndjson(
            claims: Iterator['Claim'],
            file_name: str,
            mode: Annotated[str, Field(pattern=r"[awx]")]="w"):
        """
        Read claims from a Newline Delimited JSON file.

        :param iterator[Claim] claims: An iterator over the claims to write
        :param str file_name: The name of the file to write to
        :param str mode: The mode for writing to the file ("a" for appending),
        defaults to "w"
        """
        with open(file_name, mode=mode) as file:
            for claim in claims:
                file.write(claim.model_dump_json(exclude_none=True))
                file.write("\n")
