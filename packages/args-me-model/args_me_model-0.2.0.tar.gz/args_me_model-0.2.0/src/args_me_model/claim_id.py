import hashlib


"""
IDs consist of `S<source-hash>C<test-hash>`.
"""
claim_id_pattern = r"S[0-9a-z]{4}C[0-9a-f]{16}$"


def _str_hash(string: str, length: int) -> str:
    return hashlib.sha1(string.encode("utf-8")).hexdigest()[0:length]


def hash_claim_id(source_name: str, text: str) -> str:
    """
    Generates an ID from the claim source's name and the claim's text.

    :param str source_name: The name of the claim's source
    :param str text: The text of the claim from the source
    :return: a claim ID based on the hashed name and text
    :rtype: str
    """
    return "S" + _str_hash(source_name, 4) + "C" + _str_hash(text, 16)
