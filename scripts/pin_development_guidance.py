"""Collect an additive development guidance snapshot without changing the original review set."""

from __future__ import annotations

import argparse

from scripts import pin_official_sources as pins


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download", action="store_true")
    parser.add_argument("--ca-file")
    args = parser.parse_args()
    # Trusted fixed paths in this standalone CLI; the original reviewed source set stays intact.
    pins.CATALOG = "data/development/2025/c001/catalog.json"
    pins.MANIFEST = "data/development/2025/c001/manifest.json"
    pins.PREFIX = "data/development/2025/c001/sources/"
    count = pins.download(ca_file=args.ca_file) if args.download else pins.verify()
    print(f"Verified {count} supplementary official guidance pages; professional QA pending.")


if __name__ == "__main__":
    main()
