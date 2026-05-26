import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import json
from datetime import datetime
from src.const import MODELS_DIR, DATA_DIR

def create_model(data_file_name, target_feature, output_filename):
    data_file_name = DATA_DIR + data_file_name
    df = pd.read_csv(data_file_name)

    df.drop(columns=['ID'], inplace=True)

    y = df[target_feature]           
    X = df.drop(target_feature, axis=1) 

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    print(f'accuracy: {accuracy:.2f}')

    full_name =  "".join([MODELS_DIR, output_filename, '.pkl'])

    with open(full_name, 'wb') as f:
        pickle.dump(model, f)
        print('Модель сохранена в model.pkl')

    model_info = {
        'author':'Obozov Andrey',
        'features_type': {key:str(value) for key, value in X.dtypes.to_dict().items()},
        'features_name':list(X.columns),
        'target_name': target_feature,
        'training_date': datetime.now().isoformat(),
        'accuracy': round(accuracy, 2)
    }

    with open(f'{MODELS_DIR}/{output_filename}_info.json', 'w') as f:
        json.dump(model_info, f, indent=2)



def load_model(model_file_name):
    full_name =  "".join([MODELS_DIR, model_file_name, '.pkl'])
    with open(full_name, 'rb') as f:
        model = pickle.load(f)
    return model