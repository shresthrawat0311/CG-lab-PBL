from PIL import Image, ImageOps
import os

class ImageRotator:
    
    def __init__(self):
        self.image = None
        self.original_width = 0
        self.original_height = 0

    def load_image(self, input_path: str):
        try:
            self.image = Image.open(input_path)
            self.original_width, self.original_height = self.image.size
            
            print(f"Loaded image: {input_path} (Size: {self.original_width}x{self.original_height})")
            return True
        
        except FileNotFoundError:
            print(f"Error: File not found at {input_path}")
            return False
        
        except Exception as e:
            print(f"Error loading image: {e}")
            return False

    def rotate_image(self, angle: float, expand: bool = True):
        if not self.image:
            print("Error: No image loaded. Call load_image() first.")
            return None

        print(f"Rotating image by {angle} degrees...")
        
        rotated_image = self.image.rotate(
            angle, 
            resample=Image.Resampling.BICUBIC, 
            expand=expand,
            fillcolor=(0,0,0,0) 
        )
        return rotated_image

    def save_image(self, image_to_save: Image.Image, output_path: str):
        try:
            output_dir = os.path.dirname(output_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
                
            image_to_save.save(output_path, format="PNG")
            print(f"Successfully saved rotated image to {output_path}")
        except Exception as e:
            print(f"Error saving image: {e}")

if __name__ == "__main__":
    rotator = ImageRotator()

    if rotator.load_image("sample.jpg"):
        
        angle_to_rotate = 45
        
        rotated_img = rotator.rotate_image(angle_to_rotate, expand=True)
        
        if rotated_img:
            rotator.save_image(rotated_img, "output/rotated_sample.png")
