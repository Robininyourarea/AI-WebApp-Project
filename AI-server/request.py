import base64
import requests
from PIL import Image
from io import BytesIO
import os


IMAGE_DIR = "./data/"
URL = "http://localhost:3000/predict"


def encode_base64(image_path):
    """
    Convert an image file to a base64 encoded string.
    
    Args:
        image_path (str): Path to the image file.

    Returns:
        str: Base64 encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        # Read the image file in binary mode
        image_data = image_file.read()
        
        # Encode the binary image data to base64
        encoded_string = base64.b64encode(image_data).decode("utf-8")
    
    return encoded_string

def send_request(image_path):
    """
    Send a POST request with base64 encoded image to the specified URL.
    """
    image_base64 = encode_base64(image_path)
    server_url = URL

    request_body = {
        "image": image_base64
    }
    response = requests.post(server_url, json=request_body)
    # response = requests.get(server_url, json=request_body)
    # print(f"Base64: {image_base64[:15]}")
    
    return response.json()

if __name__ == "__main__":

    # Convert image to base64
    images_file = os.listdir(IMAGE_DIR)
    for image in images_file:
        image_path = os.path.join(IMAGE_DIR, image)
        print(f"Sending request for: {image_path}")
        response = send_request(image_path)
        print(response)

    

    
