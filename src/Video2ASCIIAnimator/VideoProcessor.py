import cv2
import os


class VideoProcessor:
    """!
    This class handles all video related functions.
    """

    def __init__(self, path_to_video):
        self.path_to_video = path_to_video
        self.frame_dir = f"{path_to_video}_frames"

    def get_frame_dir(self):
        """
        Returns the directory of the frames.
        :return:
        """
        return self.frame_dir

    def extract_frames_from_video(self):
        """
        Saves every frame of a video as an JPEG.
        :return:
        """
        if not os.path.exists(self.frame_dir):
            os.makedirs(self.frame_dir)
            print("directory created:", self.frame_dir)

        video = cv2.VideoCapture(self.path_to_video)
        success, image = video.read()
        count = 0
        while success:
            cv2.imwrite(f"{self.frame_dir}/frame{count:08d}.jpg", image)
            success, image = video.read()
            count = count + 1

    def create_mp4_from_txt(self):
        pass
