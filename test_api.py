import requests
import base64
import io
from PIL import Image

# Create a tiny 1x1 image
img = Image.new('RGB', (1, 1), color = 'red')
img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format='PNG')
base64_data = base64.b64encode(img_byte_arr.getvalue()).decode()

url = "http://127.0.0.1:8081/generate"
payload = {
    "image": base64_data,
    "guidance_scale": 5.0,
    "num_inference_steps": 1
}

print(f"Sending request to {url}...")
try:
    response = requests.post(url, json=payload, timeout=10)
    print(f"Status: {response.status_code}")
    print(f"Content-type: {response.headers.get('content-type')}")
except Exception as e:
    print(f"Error: {e}")
