import tesserocr
import streamlit as st
from PIL import Image
import numpy as np

st.title("OCR")
st.write()

print("loading image")
uploaded_file = st.file_uploader("Choose an image...")

if uploaded_file is not None:
    img_ = Image.open(uploaded_file).convert('RGB')
    image_ = np.array(img_)  # convert image to numpy array for ocr
    # st.image(image_, caption='Uploaded Image.', use_column_width=True) # Display image on streamlit
    st.write(" Extracting Text from Image.......")
    # result = ocr.ocr(image_, cls=True)
    print(tesserocr.image_to_text(image_))
