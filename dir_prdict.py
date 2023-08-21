from PIL import Image
import os
from classification import Classification

classfication = Classification()

file_pathname = r"Dataset/train/cat"

for filename in os.listdir(file_pathname):
    image = Image.open(file_pathname + '/' + filename)
    class_name = classfication.detect_image(image)
    print(class_name)
