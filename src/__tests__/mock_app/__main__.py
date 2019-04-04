"""
Mock app to test building
"""
from seinfeld import Seinfeld
seinfeld = Seinfeld('mock.db')

if __name__ == "__main__":
    print(seinfeld.season(1).episodes[1].title)
