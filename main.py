import streamlit as st
import numpy as np
import cv2


st.title("Streamlit + OpenCV Sample")


img = np.zeros((500, 500, 3), np.uint8)
cv2.rectangle(img, (100, 100), (400, 400), color=(255, 0, 0), thickness=-1)

st.image(img)
