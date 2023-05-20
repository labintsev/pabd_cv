""" Module docstring """
from flask import Flask, request
import tensorflow as tf


app = Flask('Image classifier')
resnet = tf.keras.applications.ResNet101()
with open('data/imgnet_cats_ru.txt', encoding='utf-8') as f:
    cats = f.readlines()

categories_ru = [s.rstrip() for s in cats]
model = tf.keras.models.load_model('models\\my_model')

@app.route('/')
def home():
    """ Function docstring """
    return 'Home page'


@app.route('/classify', methods=['POST', 'GET'])
def classify():
    data = request.data
    img = tf.io.decode_jpeg(data)
    img_t = tf.expand_dims(img, axis=0)
    img_t = tf.image.resize(img_t, (224, 224))
    out = resnet(img_t)
    idxs = tf.argsort(out, direction='DESCENDING')[0][:3].numpy()
    out = ', '.join([categories_ru[int(i)] for i in idxs])
    return out

@app.route('/classify/binary', methods=['POST'])
def classify_binary():
    data = request.data
    img = tf.io.decode_jpeg(data)
    img_t = tf.expand_dims(img, axis=0)
    img_t = tf.image.resize(img_t, (180, 180))
    predictions = model.predict(img_t)
    dog_probability = float(predictions[0])
    print(dog_probability)
    idx = dog_probability > 0.5
    return ('Cat', 'Dog')[idx]

# img = keras.utils.load_img(
#     "PetImages/Cat/6779.jpg", target_size=image_size
# )
# img_array = keras.utils.img_to_array(img)
# img_array = tf.expand_dims(img_array, 0)  # Create batch axis
#
# predictions = model.predict(img_array)
# score = float(predictions[0])
# print(f"This image is {100 * (1 - score):.2f}% cat and {100 * score:.2f}% dog.")


if __name__ == '__main__':
    app.run(port=1234)
    input()

# comment
