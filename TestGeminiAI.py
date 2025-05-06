
from MyKey import gemini_api_key
from google import genai
from PIL import Image

def main():
    client = genai.Client(api_key=gemini_api_key)

    # Generate text
    image_url = "/Users/vishwakumarmc/Downloads/xylo.jpeg"
    imaga_data = Image.open(image_url)
    response = client.models.generate_content(model="gemini-2.0-flash", contents=[imaga_data, "Describe the image"])
    print("Image description: " + response.text)

if __name__ == '__main__':
    main()