import pytest

from shopping_cart import to_usd

def test_usd():

    assert to_usd(3.25) == "$3.25"

    assert to_usd(2.5) == "$2.50"

    assert to_usd(1234.555) == "$1,234.56"

