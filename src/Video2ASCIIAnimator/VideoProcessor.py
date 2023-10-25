import cv2
import os


class VideoProcessor:
    def __init__(self, video):
        self.video = video
        self.frame_dir = f"{video}_frames"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get_frame_dir(self):
        return self.frame_dir

    def extract_frames_from_video(self):
        if not os.path.exists(self.frame_dir):
            os.makedirs(self.frame_dir)
            print("directory created:", self.frame_dir)

        vidcap = cv2.VideoCapture(self.video)
        success, image = vidcap.read()
        count = 0
        while success:
            cv2.imwrite(f"{self.frame_dir}/frame{count:08d}.jpg", image)  # save frame as JPEG file
            success, image = vidcap.read()
            count = count + 1

    def create_mp4_from_txt(self):
        pass
