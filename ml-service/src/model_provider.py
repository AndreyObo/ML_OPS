from datetime import datetime
import json
import re
from src.const import MODELS_DIR, DATA_DIR
import pickle
from sklearn.ensemble import RandomForestClassifier
from .utils import ModelData
import pandas as pd


# Класс для загрузки модели
# трансформации запроса к классу типа входных признаков
# выполнения предсказаний модели

class ModelProvider:
    def __init__(self):
        self.model = None
        self.model_info = None
        
    def load_model(self, model_name:str):
        full_name =  "".join([MODELS_DIR, '/', model_name, '.pkl'])
        with open(full_name, 'rb') as f:
            self.model = pickle.load(f)

        metadata_name =  "".join([MODELS_DIR,'/', model_name, '_info' '.json'])
        with open(metadata_name, 'r', encoding='utf-8') as f:
            self.model_info = json.load(f)
        

    def predict(self, params:ModelData):
        if self.model is None:
            raise "Модель не загружена"
        
        model_data = params.model_dump()
        
        try:
            #Для восстановления порядка признаков воспользуемся сохраненным json конфигом
            features_values = [model_data[col] for col in self.model_info['features_name']]

            prediction = self.model.predict([features_values])
            print(prediction)
            return str(prediction[0])
        except BaseException as e:
            raise Exception(f'Возникла ошибка при загрузке праметров в модель: {e}')
        