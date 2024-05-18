import pandas as pd
import os

print(os.listdir("images/file_008678_files"))

images_info = pd.read_csv("files/images_info.csv")
print(images_info.shape)

imgs = 0
for c in os.listdir("images"):
    imgs += len(os.listdir("images/" + c))
print(imgs)