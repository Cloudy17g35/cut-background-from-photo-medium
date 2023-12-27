import cv2
import rembg
from datetime import datetime


# to this format file will be written
OUTPUT_FORMAT = 'png'
# to this directory output file will be written
OUTPUT_DIR = 'output'

def remove_background_from_file(filepath:str) -> str:
    input_image = cv2.imread(filepath)
    output_image = rembg.remove(input_image)
    output_file:str = f'{datetime.now()}.{OUTPUT_FORMAT}'
    output_path:str = f'{OUTPUT_DIR}/{output_file}'
    cv2.imwrite(output_path, output_image)
    return output_path

