"""
Pyex main entry
"""
import parse
import build


def main():
    """
    Run main code
    """
    build.run(args=parse.args())


if __name__ == "__main__":
    main()
