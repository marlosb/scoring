import os

import feature_engine.missing_data_imputers as mdi
from feature_engine import categorical_encoders as ce
from feature_engine import variable_transformers as vt
import pandas
import sqlalchemy
import xgboost as xgb  

def get_score(DATA_PATH, MODEL_PATH):
    ''' Function to generate prediction
        Returns a pandas DataFrame with month, seller ID and prediction.
    '''

    champion_model = os.listdir(MODEL_PATH)[-1]
    model_package = pandas.read_pickle(MODEL_PATH + champion_model)

    model = model_package.model
    columns = model_package.fit_vars

    con = sqlalchemy.create_engine( "sqlite:///" + DATA_PATH )  
    df = pandas.read_sql_table( "TB_ABT", con )

    results = model.predict(df[columns])
    df['fl_venda_predict'] = results

    return df[['dt_ref', 'seller_id', 'fl_venda_predict']]