import os
import rawpy
import io
from PIL import Image

def convert_arw_to_jpg_using_camera_wb(input_folder, output_folder, max_size_mb=4, quality_step=5):
    """
    Converts all ARW files in the specified folder to JPEG using the camera's white balance settings.
    
    Args:
        input_folder (str): The directory path that contains ARW files.
        output_folder (str): The directory path where JPEG files will be saved.
        max_size_mb (int, optional): Maximum file size in megabytes for the JPEG images. Default is 4 MB.
        quality_step (int, optional): Step decrement for adjusting JPEG quality. Default is 5.
        
    This function reads each ARW file in the specified input folder, processes it using
    the camera's white balance settings, and saves it as a JPEG file in the specified
    output folder. The JPEG's quality is adjusted to ensure the file size is under the max_size_mb limit.
    """
    # Create output directory if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each file in the input directory
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.arw'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")

            with rawpy.imread(input_path) as raw:
                # Use camera white balance
                rgb = raw.postprocess(use_camera_wb=True)
                image = Image.fromarray(rgb)

                # Adjust JPEG quality to stay under size limit
                temp_file = io.BytesIO()
                quality = 95
                while True:
                    image.save(temp_file, 'JPEG', quality=quality)
                    size_mb = temp_file.tell() / (1024 * 1024)
                    if size_mb <= max_size_mb or quality <= 10:
                        break
                    quality -= quality_step
                    temp_file.seek(0)
                    temp_file.truncate()

                # Save the final image
                image.save(output_path, 'JPEG', quality=quality)
                print(f"Image {filename} has been saved as {os.path.basename(output_path)} with quality {quality}% and size {size_mb:.2f} MB")

# Example usage
if __name__ == "__main__":
    input_folder = 'path/to/your/arw/files'
    output_folder = os.path.join(input_folder, 'output_jpg')
    convert_arw_to_jpg_using_camera_wb(input_folder, output_folder)
