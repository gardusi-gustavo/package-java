#!/usr/bin/env python3
from __future__ import annotations
import argparse, sys, xml.etree.ElementTree as ET
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--root", default=".")
    root = Path(ap.parse_args().root)
    pom = root / "pom.xml"
    if not pom.is_file():
        print("missing pom.xml", file=sys.stderr); return 1
    try:
        ET.parse(pom)
    except ET.ParseError as exc:
        print(f"pom.xml: {exc}", file=sys.stderr); return 1
    java = sorted((root / "src").rglob("*.java"))
    if not java:
        print("no Java sources", file=sys.stderr); return 1
    for p in java:
        text = p.read_text(encoding="utf-8")
        if "package " not in text:
            print(f"{p}: missing package", file=sys.stderr); return 1
        if text.count("{") != text.count("}"):
            print(f"{p}: unbalanced braces", file=sys.stderr); return 1
    print(f"java validation ok ({len(java)} files)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
