import unittest

from args_me_model import Claim, Source


class TestParsing(unittest.TestCase):

    def test_constructor(self):
        claim = Claim(id="S0000C0123456789abcdef", text="Foo", sources=[
          Source(name="Bar", text="Fooooooooo")
        ])
        self.assertEqual(
            claim,
            Claim.model_validate_json(claim.model_dump_json())
          )

    def test_from_source(self):
        source = Source(name="test", text="foo")
        claim = Claim.from_source(source)
        self.assertEqual("foo", claim.text)
        self.assertEqual(1, len(claim.sources))
        self.assertEqual(source, claim.sources[0])
        self.assertEqual(0, len(claim.supports))
        self.assertEqual(
            claim,
            Claim.model_validate_json(claim.model_dump_json())
          )

    def test_from_source_with_support(self):
        source = Source(name="test", text="foo")
        claim = Claim.from_source(
            source,
            [
                [
                    Claim.from_source(Source(name="test", text="one")),
                    Claim.from_source(Source(name="test", text="two"))
                ],
                [
                    Claim.from_source(Source(name="test", text="three"))
                ]
            ]
          )
        self.assertEqual("foo", claim.text)
        self.assertEqual(1, len(claim.sources))
        self.assertEqual(source, claim.sources[0])
        self.assertEqual(2, len(claim.supports))
        self.assertEqual(
            claim,
            Claim.model_validate_json(claim.model_dump_json())
          )

    def test_read_example_minimal(self):
        source = Source(name="imagination", text="Original text as in the source")
        claim = Claim(
            id="S0000C0000000000000000",
            text="Example text of the claim",
            sources=[source]
          )
        with open("tests/example-minimal.json") as f:
            self.assertEqual(claim, Claim.model_validate_json(f.read()))

    def test_read_examples_minimal(self):
        source = Source(name="imagination", text="Original text as in the source")
        claim = Claim(
            id="S0000C0000000000000000",
            text="Example text of the claim",
            sources=[source]
          )
        parsed = list(Claim.read_ndjson("tests/example-minimal.ndjson"))
        self.assertEqual(2, len(parsed))
        self.assertEqual(claim, parsed[0])
        self.assertEqual(claim, parsed[1])


if __name__ == '__main__':
    unittest.main()
