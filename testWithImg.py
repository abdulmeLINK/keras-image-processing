import cv2
import tensorflow as tf
CATEGORIES = ["categ1", "categ2","empty"] # categories you have. Should be in same order...
def prepare(file):
    IMG_SIZE = 50
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
model = tf.keras.models.load_model("MODEL_NAME.model")
image = "path-to-sample-image" # image of sample
image = prepare(file=image)
print(image)
prediction = model.predict([image])
print(prediction)
prediction = list(prediction[0])
print(CATEGORIES[prediction.index(max(prediction))])