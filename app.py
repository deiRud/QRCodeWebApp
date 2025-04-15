import streamlit as st
import qrcode
from PIL import Image

st.title("QR Code Generator")

data = st.text_input("Enter text or URL:")

if st.button("Generate QR Code"):
    if data:
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode.png")

        st.image("qrcode.png", caption="Your QR Code", width=250)
    else:
        st.warning("Please enter something to generate a QR code.")
