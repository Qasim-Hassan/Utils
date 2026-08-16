from rembg import remove
from PIL import Image

input_path = 'TensorCode.jpeg'
output_path = 'output.png'

input_image = Image.open(input_path)

# Remove the background
output_image = remove(
    input_image,
    alpha_matting=True,
    alpha_matting_foreground_threshold=240,
    alpha_matting_background_threshold=10,
    alpha_matting_erode_size=10
)

# Save the result
output_image.save(output_path)