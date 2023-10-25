import PIL.Image
import os


class ASCIITransformer:

    def __init__(self, width):
        self.ascii_chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
        self.ascii_dir = None
        self.width = width

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get_ascii_dir(self):
        return self.ascii_dir

    def convert_image_to_ascii(self, image, directory):
        try:
            img = PIL.Image.open(f"{directory}/{image}")
        except:
            print("unable to find image")

        width, height = img.size
        aspect_ratio = height / width
        new_height = aspect_ratio * self.width * 0.55
        img = img.resize((self.width, int(new_height)))

        img = img.convert('L')

        pixels = img.getdata()
        new_pixels = [self.ascii_chars[pixel // 25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)

        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + self.width] for index in range(0, new_pixels_count, self.width)]
        ascii_image = "\n".join(ascii_image)

        self.ascii_dir = directory + "_ascii"
        if not os.path.exists(self.ascii_dir):
            os.makedirs(self.ascii_dir)
            print("directory created:", self.ascii_dir)
        with open(f"{self.ascii_dir}/{image}.txt", "w") as f:
            f.write(ascii_image)

    def convert_directory_to_ascii(self, directory):
        for filename in sorted(os.listdir(directory)):
            self.convert_image_to_ascii(filename, directory)
