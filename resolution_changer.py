from PIL import Image
import os

class ResolutionChanger:
    def __init__(self):
        pass
    
    # Get an image from a local folder
    def __get_image(self, image_path: str) -> Image.Image:
        return Image.open(image_path).copy()
    
    def __crop_image_to_square(self, image: Image.Image) -> Image.Image:
        print("square")
        width, height = image.size
        if width == height: 
            return image

        size = min(width, height)
        left = (width - size) // 2
        top = (height - size) // 2

        return image.crop((left, top, left+size, top+size))
    
    def change_resolution(self, image_path: str, output_path: str, resolutions: list[tuple[int, int]], square_cropping=False):
        '''
        Chanage resolution and save
        '''
        os.makedirs(output_path, exist_ok=True)
        img = self.__get_image(image_path)
        if square_cropping:
            img = self.__crop_image_to_square(img)
        for resolution in resolutions:
            width, height = resolution
            resized_img = img.resize((width, height), Image.LANCZOS)
            resized_img.save(f"{output_path}/{width}x{height}_resolution.png")
            print(f"{resolution}: DONE")
        print("ALL DONE")


