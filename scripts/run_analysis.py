#!/usr/bin/env python3
"""Command-line entry point to run analysis."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        default="config/analysis.yaml",
        help="Path to the analysis configuration file.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config_path = Path(args.config)
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    print(
        "Scaffold only. Implement this script before publication. "
        f"Configuration located at: {config_path}"
    )


if __name__ == "__main__":
    main()
