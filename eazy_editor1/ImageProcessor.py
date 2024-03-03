from PIL import Image, ImageFilter
import os
class ImageProcessor:
    def __innit__ (self, workdir):
        self.current_image: Image = None
        self.filename: str = None
        self.modified_folder = "modified"
        self.workdir = workdir

    def open(self, fn):
       self.filename = fn 
       path = os.path.join(self.workdir, self.filename)
       self.current_image = image.open(path)
    def show(self)
        ...