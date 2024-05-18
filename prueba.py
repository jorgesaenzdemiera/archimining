import pandas as pd
import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import streamlit as st

def show_images(names):
  for name in names:
    path =  images_path + "/" + name
    st.image(path, caption = name)

files_path = "files/"
images_path = "images/"
images_info = pd.read_csv(files_path + "images_info.csv", index_col = 0)

images_ok = list(images_info.query("is_small == 0 and is_transparent == 0 and has_multiple_images == 0 and is_test == 0").index)

st.write("# Architext")
show_images(images_ok[:5])