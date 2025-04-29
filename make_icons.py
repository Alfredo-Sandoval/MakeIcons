#!/usr/bin/env python3
"""
make_icons.py  –  Down-scale a master PNG into multi-size PNGs + a bundled .ico
Usage:
  • Place this script alongside your PNG master (default name: Generic_Logo.png)
  • Run: python make_icons.py
  • (Optionally) pass custom paths: python make_icons.py /path/to/mylogo.png /path/to/icons_out
Dependencies: Pillow  •  Python ≥3.8
"""

import sys
from pathlib import Path
from PIL import Image

SCRIPT_DIR = Path(__file__).parent
DEFAULT_MASTER = SCRIPT_DIR / "Generic_Logo.png"
DEFAULT_OUTDIR = SCRIPT_DIR / "icons"

SIZES = (1024, 512, 256, 128, 64, 32, 16)


def main():
    args = sys.argv[1:]
    master_path = Path(args[0]) if len(args) >= 1 else DEFAULT_MASTER
    out_dir = Path(args[1]) if len(args) >= 2 else DEFAULT_OUTDIR

    if not master_path.exists():
        print(f"[ERROR] Master file not found: {master_path}")
        sys.exit(1)

    out_dir.mkdir(parents=True, exist_ok=True)
    img = Image.open(master_path).convert("RGBA")

    # Generate per-size PNGs
    for sz in SIZES:
        dest = out_dir / f"icon_{sz}.png"
        img.resize((sz, sz), Image.Resampling.LANCZOS).save(dest, format="PNG")
        print(f"[OK] {dest}")

    # Bundle into a single ICO
    ico_path = out_dir / "Generic_Logo.ico"
    img.save(ico_path, format="ICO", sizes=[(s, s) for s in SIZES])
    print(f"[OK] {ico_path}")


if __name__ == "__main__":
    main()
