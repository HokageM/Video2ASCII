import PIL.Image
import os


class ASCIITransformer:
    """!
    This class is responsible for the transformation of images to ASCII art.
    """

    def __init__(self, width):
        self.ascii_chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
        self.ascii_dir = None
        self.ascii_width = width
        self.ascii_height = None

    def get_ascii_dir(self) -> str:
        """
        Returns the directory of the ASCII arts.
        :return: 
        """
        return self.ascii_dir

    def convert_image_to_ascii(self, image: str, directory: str):
        """
        Converts the specified image to an ASCII art and saves the ASCII art is saved inside a seperated file.
        :param image:
        :param directory:
        :return:
        """
        try:
            img = PIL.Image.open(f"{directory}/{image}")
        except:
            print("unable to find image")

        width, height = img.size
        aspect_ratio = height / width
        self.ascii_height = aspect_ratio * self.ascii_width * 0.55
        img = img.resize((self.ascii_width, int(self.ascii_height)))

        img = img.convert('L')

        pixels = img.getdata()
        new_pixels = [self.ascii_chars[pixel // 25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)

        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + self.ascii_width] for index in
                       range(0, new_pixels_count, self.ascii_width)]
        ascii_image = "\n".join(ascii_image)

        self.ascii_dir = directory + "_ascii"
        if not os.path.exists(self.ascii_dir):
            os.makedirs(self.ascii_dir)
            print("directory created:", self.ascii_dir)
        with open(f"{self.ascii_dir}/{image}.txt", "w") as f:
            f.write(ascii_image)

    def convert_directory_to_ascii(self, directory: str):
        """
        Converts every image file inside the specified directory to an ASCII art.
        :param directory:
        :return:
        """
        for filename in sorted(os.listdir(directory)):
            self.convert_image_to_ascii(filename, directory)
