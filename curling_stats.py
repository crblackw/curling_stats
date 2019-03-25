#!/usr/bin/env python3
"""
Module Docstring
"""

from bs4 import BeautifulSoup
from requests import get


def main():
    """ Main entry point of the app """
    url = "http://www.curlingzone.com/statistics.php"
    resp = get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    print(soup.head)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
