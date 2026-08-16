from rembg import remove
from PIL import Image

input_path = 'input.jpg'
output_path = 'output.png'

input_image = Image.open(input_path)

# Remove the background
output_image = remove(input_image)

# Save the result
output_image.save(output_path)