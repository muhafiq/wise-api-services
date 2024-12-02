from flask_restful import Resource
from flask import request
from app.extentions import model, db
from app.api.error import ResponseError
from app.utils import preprocess_image, after_prediction
from app.utils.gcs import allowed_file, upload_image
from app.models.injury_classes import InjuryClass
from app.api.schemas.injury_classes import InjuryClassSchema
from app.models.medical_records import MedicalRecord

class PredictResource(Resource):
    def post(self):
        schema = InjuryClassSchema()

        # validate the data image
        if 'image' not in request.files: 
            raise ResponseError(code=400, description="No image provided!")
        
        file = request.files['image']
        if file.filename == '':
            raise ResponseError(code=400, description="No file selected!")

        if not allowed_file(file.filename):
            raise ResponseError(code=400, description="Format file not supported!")

        # preprocess image
        prepared_image = preprocess_image(file)

        # prediction
        prediction = model.predict(prepared_image)
        prediction_class = after_prediction(prediction)

        # upload image to google cloud storage and query the injury class
        file_url = upload_image(file)
        injury_class = InjuryClass.query.filter_by(class_name=prediction_class).first()

        # add new medical record
        medical_record = MedicalRecord(
            diagnosis_id=injury_class.id,
            photo=file_url,
            treatment=injury_class.treatment
        )
        db.session.add(medical_record)
        db.session.commit()

        return {
            'status_code': 200,
            'message': "Prediction successful",
            'data': {
                'prediction': f'You have a {prediction_class} in your skin',
                'details': schema.dump(injury_class),
            }
        }, 200