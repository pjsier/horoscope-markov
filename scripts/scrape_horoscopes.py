import re
import os
import sys

from bs4 import BeautifulSoup

INPUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "input"
)


def parse_horoscope(soup):
    horoscope_str = re.sub(
        r"\s+",
        " ",
        " ".join(el.get_text() for el in soup.select("nav.switcher + p, .subnav + p")),
    ).strip()
    return re.sub(r"^[A-Z][a-z]{1,8} \d{1,2},? \d{4} - ", "", horoscope_str)


if __name__ == "__main__":
    for root, dirs, files in os.walk(INPUT_DIR):
        for filename in files:
            if not filename.endswith(".html"):
                continue
            with open(os.path.join(root, filename), "r") as f:
                soup = BeautifulSoup(f, "html.parser")
            sys.stdout.write(f"{parse_horoscope(soup)}\n")
