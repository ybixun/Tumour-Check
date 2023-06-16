    from flask import Flask, request
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing.image import img_to_array
    from PTL import Image
    import numpy as np
    import io
    
    app = Flask(__name__)
    model = load_model('mri_cnn_model/checkpoint')
    
    @app.route('/predict', methods = ['POST'])
    
    def predict():
        
        # check if image is posted up
        if 'image' not in request.files:
            return {'error': 'no image'}, 400
        
        image_file = request.files['image']
        
        # check if no image file was uploaded, it will return error
        if image_file.filename == '':
            return {'error': 'no image'}, 400
        
        # open, resize and preprocess image
        image = Image.open(io.BytesIO(image_file.read())).resize((128,128))
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image = image / 255.0
        
        # predict the class of image
        prediction = model.predict(image)
        prediction_class = np.argmax(prediction, axis=1)
        return {'prediction': int(prediction_class[0])}
    
    if __name__ == '__main__':
        app.run(host = '0.0.0.0', port = 5000)