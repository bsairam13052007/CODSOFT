import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  

from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
import numpy as np

resnet_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base", use_fast=False)
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

img_path = input("Enter full path of your image: ")

img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

features = resnet_model.predict(img_array, verbose=0)

inputs = processor(images=img, return_tensors="pt")
out = caption_model.generate(**inputs)
caption = processor.decode(out[0], skip_special_tokens=True)

print("\nGenerated Caption:")
print(caption)
