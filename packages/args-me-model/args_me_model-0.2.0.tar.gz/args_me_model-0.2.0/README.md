# args-me-model
Data model for args.me.

```python
from args_me_model import Claim, Source

# Creating claims
claim1 = Claim.from_source(
        Source(
            name="common-knowledge",
            text="Blue is scattered more than other colors"
        )
    )
claim2 = Claim.from_source(
        Source(
            name="common-knowledge",
            text="The sky is blue"
        ),
        support = [[claim1]] # list of linked support
    )
claim3 = Claim.from_source(
        Source(
            name="uncommon-knowledge",
            text="The sky is not blue"
        )
    )
claim1.counter = claim3.id
claim3.counter = claim1.id

# Writing claims to a file
Claim.write_ndjson([claim1, claim2, claim3], "myclaim.ndjson")

# Iterating over claims from a file
for claim in Claim.read_ndjson("myclaim.ndjson"):
    print(claim.text)
```

