
from MyKey import gemini_api_key
import google.generativeai as genai
from PIL import Image

def main():
    genai.configure(api_key=api_key)

    # Generate text
    image_url = "/Users/vishwakumarmc/Downloads/xylo.jpeg"
    imaga_data = Image.open(image_url)
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
    response = model.generate_content(imaga_data)
    print("Image description: " + response.text)

if __name__ == '__main__':
    main()