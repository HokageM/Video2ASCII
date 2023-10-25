"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = test.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import sys

from Video2ASCIIAnimator import __version__

from .Animator import Animator
from .ASCIITransformer import ASCIITransformer
from .VideoProcessor import VideoProcessor

__author__ = "HokageM"
__copyright__ = "HokageM"
__license__ = "MIT"


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Transforms a video to an ASCII animation inside your console.")
    parser.add_argument(
        "--version",
        action="version",
        version=f"Test {__version__}",
    )
    parser.add_argument('video', metavar='FILE', type=str, help='mp4 that should be transformed')
    parser.add_argument('-w', '--width', type=int, default=100, help='defines the width of the ASCII art')
    return parser.parse_args(args)


def main(args):
    """Wrapper allowing :func:`fib` to be called with string arguments in a CLI fashion

    Instead of returning the value from :func:`fib`, it prints the result to the
    ``stdout`` in a nicely formatted message.

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    args = parse_args(args)

    video_processor = VideoProcessor(args.video)
    video_processor.extract_frames_from_video()

    transformer = ASCIITransformer(args.width)
    transformer.convert_directory_to_ascii(video_processor.get_frame_dir())

    with Animator(transformer.get_ascii_dir()) as animator:
        animator.run_ascii_animation()


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m test.skeleton 42
    #
    run()
