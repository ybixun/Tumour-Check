from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io

app = Flask(__name__)
model = load_model('mri_cnn_model/checkpoint')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'image' not in request.files:
            return render_template('upload.html', prediction='No image part')
        image_file = request.files['image']
        # if user does not select file, browser also
        # submit an empty part without filename
        if image_file.filename == '':
            return render_template('upload.html', prediction='No selected image')
        if image_file:
            # open, resize and preprocess image
            image = Image.open(io.BytesIO(image_file.read())).resize((128,128))
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)
            image = image / 255.0
            # predict the class of image
            prediction = model.predict(image)
            prediction_class = np.where(prediction >= 0.5, 1, 0)

            if prediction_class[0] == 1:
                return 'Tumour detected!'
            else:
                return 'No Tumour detected.'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
