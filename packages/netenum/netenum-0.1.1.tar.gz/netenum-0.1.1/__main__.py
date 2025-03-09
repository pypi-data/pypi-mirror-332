#!/usr/bin/env python3
"""Command-line interface for the netenum package.

This module provides the main entry point for the command-line tool,
allowing users to enumerate IP addresses from CIDR ranges provided via stdin.
"""

import sys
import random
import argparse
from typing import List

from .core import netenum


def get_cidrs_from_stdin() -> List[str]:
    """Read CIDR ranges from stdin, one per line."""
    return [line.strip() for line in sys.stdin if line.strip()]


def main() -> None:
    """Execute the main CLI function.

    Reads CIDR ranges from stdin and outputs enumerated IP addresses,
    optionally in random order if specified.
    """
    parser = argparse.ArgumentParser(description="Enumerate IP addresses from CIDR ranges")
    parser.add_argument(
        "-r",
        "--random",
        action="store_true",
        help="Output addresses in random order",
    )
    args = parser.parse_args()

    try:
        cidrs = get_cidrs_from_stdin()
        if not cidrs:
            print(
                "Error: No CIDR ranges provided.\n" "Pipe CIDR ranges to stdin, one per line.",
                file=sys.stderr,
            )
            sys.exit(1)

        # Get all addresses
        addresses = list(netenum(cidrs))

        # If random flag is set, shuffle the addresses
        if args.random:
            random.shuffle(addresses)

        # Print addresses one per line
        for addr in addresses:
            print(addr)

    except KeyboardInterrupt:
        sys.exit(0)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
