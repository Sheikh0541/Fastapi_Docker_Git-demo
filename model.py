
from keras.models import load_model 
from io import BytesIO
from PIL import Image
import numpy as np 
import cv2

model = load_model('cats_dogs_classifier.h5')

def read_image(image_encoded):
    pil_image = Image.open(BytesIO(image_encoded))
    return np.array(pil_image) 


def model_prediction(image):
    image = cv2.resize(image, (224, 224)) 
    image = image.reshape(1, 224, 224, 3)
    pred = model.predict(image)[0]
    if pred[0] > pred[1]: 
        result = 'cat'
    else:
        result = 'dog'
    return result # Return as string 
