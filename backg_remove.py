import streamlit as st
from rembg import remove
from io import BytesIO
from PIL import Image
import base64




st.set_page_config(
    page_title="Background remover",
    page_icon="🖼",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.write("Easy Peasy Background remover")
st.write(
    ":dog: Try Uploading your image from your computer:"
)



st.sidebar.write("Upload and Download :gear:" )

MAX_FILESIZE= 10 * 1024 * 1024
# download image

def convert_image(img):
    buF= BytesIO()
    img.save(buF, format="PNG")
    bytesim= buF.getvalue()
    return bytesim

def fix_image(upload):
    image= Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("---")
    st.sidebar.download_button(
        "Download Fixed Image", convert_image(fixed), "fixed.png", "image/png"
    )

col1, col2= st.columns(2)
my_upload= st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size>MAX_FILESIZE:
        st.sidebar.error("File is too big, shouls be less than 5MB")
    else:
        fix_image(my_upload)
else:
    fix_image("./wall.jpg")