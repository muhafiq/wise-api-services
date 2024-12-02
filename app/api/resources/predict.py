from flask_restful import Resource
from flask import request
from app.extentions import model
from app.api.error import ResponseError
from app.utils import preprocess_image, after_prediction

class PredictResource(Resource):
    def post(self):
        if 'image' not in request.files: 
            raise ResponseError(code=400, description="No image provided!")
        
        file = request.files['image']
        if file.filename == '':
            raise ResponseError(code=400, description="No file selected!")

        prepared_image = preprocess_image(file)

        print("ukuran : ", prepared_image.shape)

        prediction = model.predict(prepared_image)

        prediction = after_prediction(prediction)

        return {
            'status_code': 200,
            'message': "Prediction successful",
            'data': {
                'prediction': prediction
            }
        }, 200