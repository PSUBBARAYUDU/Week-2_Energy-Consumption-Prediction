import numpy as np

def predict_energy(model, input_features):
    prediction = model.predict([input_features])
    return prediction[0]
