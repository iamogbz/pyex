"""
Mock app to test building
"""
from seinfeld import Seinfeld  # pylint: disable=import-error

SEINFELD = Seinfeld('mock.db')

if __name__ == "__main__":
    print(SEINFELD.season(1).episodes[1].title)
