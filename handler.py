import json
import configparser
import joblib
import pandas as pd

config = configparser.ConfigParser()
config.read('config.ini')

model = joblib.load(config['S3']['key'])


def predict(event, context):
    body = {
        "message": "ok"
    }

    params= event['queryStringParameters']

    age = int(params['age'])
    sex = int(params['sex'])
    cp = int(params['cp'])
    trestbps = int(params['trestbps'])
    chol = int(params['chol'])
    fbs = int(params['fbs'])
    restecg = int(params['restecg'])
    thalach = int(params['thalach'])
    exang = int(params['exang'])
    oldpeak = float(params['oldpeak'])
    slope = int(params['slope'])
    ca = int(params['ca'])
    thal = int(params['thal'])

    data_input = {
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }
    data = pd.DataFrame(data_input, index=[0])

    # Get prediction
    prediction = model.predict(data)[0]

    body['prediction']=int(prediction)

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Access-Control-Allow-Origin": "*"
        }
    }

    return response

