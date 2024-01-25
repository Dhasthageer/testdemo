import pytest
import sys

@pytest.mark.regression
@pytest.mark.skipif(5 < 2, reason="it's not supported")
def test_fristprogram():
    print("hello")


def test_greet():
    print("good morning")