import csv
import os
import random
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Union, Any


# determine if application is a script file or frozen exe
if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    path = Path(sys._MEIPASS)  # type: ignore # pylint: disable=no-member
path = Path(os.path.dirname(os.path.realpath(__file__)))
cwd = Path.cwd()


@dataclass
class QuoteGenerator:
    """Generator class to return random controls engineering related quotes or facts

    Database should be a CSV file with ';' used as a separator, defaults to quotes.csv
    """

    database: Union[str, Path] = os.path.join(path, "quotes.csv")
    _storage: Any = None
    _count: int = 0

    def __post_init__(self):
        with open(self.database, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=";", quotechar="|")
            # Will need to change when/if the database gets bigger
            self._storage = [
                [row[0], row[1]] for idx, row in enumerate(reader) if idx != 0
            ]  # Don't include the header
            self._count = len(self._storage)

    def quote(self):
        """Returns a random quote from the database"""
        if self._count <= 0:
            return "As a control engineer you should do better"

        index = random.randint(0, self._count - 1)
        quote = self._storage[index][0]
        return quote

    def quote_from_category(self, category: str):
        """Future method to return quote from a particular category. currently just returns a random quote

        The second field of the record contains the category

        return: quote from particular category
        """
        return self.quote()
