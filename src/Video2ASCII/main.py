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
    parser.add_argument('video', metavar='FILE', type=str, help='MP4 that should be transformed.')
    parser.add_argument('-w', '--width', type=int, default=250,
                        help='Defines the width of the ASCII art. Default value is set to 250.')
    parser.add_argument('-p', '--play', type=str, default='',  help='Enter name of previously created '
                                                                    'ASCII art frames, then it plays the animation.')
    return parser.parse_args(args)


def main(args):
    args = parse_args(args)
    if not args.play:
        video_processor = VideoProcessor(args.video)
        video_processor.extract_frames_from_video()

        transformer = ASCIITransformer(args.width)
        transformer.convert_directory_to_ascii(video_processor.get_frame_dir())

        play_dir = transformer.get_ascii_dir()
    else:
        play_dir = args.play
    with Animator(play_dir) as animator:
        animator.run_ascii_animation()


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
