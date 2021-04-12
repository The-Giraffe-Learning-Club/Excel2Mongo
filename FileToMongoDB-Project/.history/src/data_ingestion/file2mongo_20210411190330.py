#!/usr/bin/env python3

import colorama
import typer
from typer import Argument



def main() -> None:
    """Write your mongoDB Connection and code"""
    colorama.init(autoreset=True, strip=False)

    print("########## Sample Print #########")


# Allow the script to be run standalone (useful during development).
if __name__ == "__main__":
    typer.run(main)
