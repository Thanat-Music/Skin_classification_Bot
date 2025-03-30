import requests
import io
from PIL import Image
import numpy as np


def get_image(meassageID):
    url = f"https://api-data.line.me/v2/bot/message/{meassageID}/content"
    channelAccessToken ="RUYr3K+qxKWm10gaor6rR3kD74zofsWoNzQbhbooG6VA9wEeAzu0xSEszHCvsNf/o5qQsdfumK1svVVcFqPdpLbjFFOeIzA9xdPw2WO1BudbJQNQ8yHK1fFveDJDw9Q5eVkSZYpHAtXqhn/sMoHmtwdB04t89/1O/w1cDnyilFU="
    headers = {
        "Authorization": f"Bearer {channelAccessToken}"
    }

    response = requests.get(url, headers=headers)
    image = Image.open(io.BytesIO(response.content))
    # Get the width and height of the image
    width, height = image.size

    # Find the minimum dimension
    min_dim = min(width, height)

    # Calculate the left, top, right and bottom coordinates for cropping
    left = (width - min_dim) // 2
    top = (height - min_dim) // 2
    right = (width + min_dim) // 2
    bottom = (height + min_dim) // 2

    # Crop the image to a square ratio and keep the center
    cropped_image = image.crop((left, top, right, bottom))

    return np.array(cropped_image)