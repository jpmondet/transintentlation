import os
import sys
import pytest

from context import transintentlation

sys.path.append(os.path.abspath("."))
sys.path.insert(0, os.path.abspath(".."))


def test_translate_no_params():
    """ Should fail with no params """

    with pytest.raises(TypeError):
        transintentlation.Translate()
