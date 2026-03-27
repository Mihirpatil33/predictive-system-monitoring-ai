import pickle
import os

MODEL_PATH = "backend/model.pkl"


def save_model(model):
    with open(MODEL_PATH, "wb") as file:
        pickle.dump(model, file)


def load_model():
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as file:
            return pickle.load(file)
    return None