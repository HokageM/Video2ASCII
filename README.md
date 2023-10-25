# Video2ASCIIAnimator
This tool is created to convert MP4 videos into ASCII animations.

## Installation

```commandline
git clone https://github.com/HokageM/Video2ASCII.git
cd Video2ASCII
pip install .
```

## Usage

```commandline
usage: video2ascii [-h] [--version] [-w WIDTH] FILE

Transforms a video to an ASCII animation inside your console.

positional arguments:
  FILE                  mp4 that should be transformed

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -w WIDTH, --width WIDTH
                        defines the width of the ASCII art

```

TIP: If you use a higher resolution for the ASCII frames, you may need to adjust the font size within your terminal.