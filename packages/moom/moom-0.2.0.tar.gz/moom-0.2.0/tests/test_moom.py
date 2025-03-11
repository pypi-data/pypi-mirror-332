import os
import sys
from pathlib import Path

import pytest

from moom.api import QuoteGenerator


# determine if application is a script file or frozen exe
if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    path = Path(sys._MEIPASS)  # type: ignore # pylint: disable=no-member
path = Path(os.path.dirname(os.path.realpath(__file__)))
cwd = Path.cwd()


@pytest.fixture
def generator():
    generator = QuoteGenerator()
    yield generator


class TestQuoteGenerator:

    def test_moom_quote(self, generator):
        quote = generator.quote()
        assert quote == "A logix timer will time out after 24 days"

    def test_moom_quote_with_category(self, generator):
        quote = generator.quote_from_category("ControlLogix")
        assert quote == "A logix timer will time out after 24 days"

    def test_moom_quote_empty_database(self):
        quote = QuoteGenerator(os.path.join(path, "empty.csv")).quote()
        assert quote == "As a control engineer you should do better"
