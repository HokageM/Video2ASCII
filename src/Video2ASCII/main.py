import argparse
import sys

from Video2ASCIIAnimator import __version__

from .Animator import Animator
from .ASCIITransformer import ASCIITransformer
from .VideoProcessor import VideoProcessor

__author__ = "HokageM"
__copyright__ = "HokageM"
__license__ = "MIT"


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
    run()
