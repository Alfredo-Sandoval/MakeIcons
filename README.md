# MakeIcons

## Overview

Generate multi-size PNG icons and bundle them into a single .ico file.

A simple Python utility to downscale a master PNG into standard icon sizes and produce a Windows-compatible `.ico` file.

## Features

- Downscale a master PNG to multiple sizes: `1024`, `512`, `256`, `128`, `64`, `32`, `16` px
- Bundle all sizes into one `.ico` file for Windows applications
- Customizable icon sizes and output filenames via script constants
- Minimal dependency: only requires [Pillow](https://python-pillow.org/)

## Installation

Ensure you have Python 3.8+ installed, then install Pillow:

```text
pip install pillow
```

## Usage

```text
python make_icons.py [MASTER_IMAGE] [OUTPUT_DIRECTORY]
```

- `MASTER_IMAGE`: Path to your master PNG (default: `Generic_Logo.png`)
- `OUTPUT_DIRECTORY`: Directory to save generated icons (default: `icons/`)

**Examples:**

```text
# Use defaults (requires Generic_Logo.png in script folder)
python make_icons.py

# Custom paths
python make_icons.py ./assets/my_logo.png ./build/icons
```

## Output

For each size in `SIZES`, the script creates:

```text
icons/icon_1024.png
icons/icon_512.png
icons/icon_256.png
icons/icon_128.png
icons/icon_64.png
icons/icon_32.png
icons/icon_16.png
```

And bundles them into:

```text
icons/Generic_Logo.ico
```

## Configuration

Open `make_icons.py` and tweak:

- `SIZES`: Tuple of icon dimensions to generate
- `DEFAULT_MASTER`: Default master image filename
- `DEFAULT_OUTDIR`: Default output directory

