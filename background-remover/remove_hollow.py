from PIL import Image

def remove_all_white(image_path, output_path, threshold=240):
    # Open image and convert to RGBA
    img = Image.open(image_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # Check if the pixel is close to white based on threshold
        if item[0] >= threshold and item[1] >= threshold and item[2] >= threshold:
            # Make it fully transparent
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG")

# Usage
remove_all_white("output.png", "hollow_logo_clean.png")
