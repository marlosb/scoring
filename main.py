import datetime
import sys

from abt import get_abt
from score import get_score

# Create constants
DATA_PATH = 'data/olist_dsa.db'
QUERY_PATH = 'sql/Script_ABT_olist_dtref_safra_20200818.sql'
model_path = 'models/'

primeira_safra = "2018-07-01"
ultima_safra = "2018-09-01"

if __name__ == '__main__':
    start_time = datetime.datetime.now()

    if '-abtonly' in sys.argv:
        print('Generating ABT')
        get_abt(DATA_PATH, QUERY_PATH, primeira_safra, ultima_safra)
    elif '-scoreonly' in sys.argv:
        print('Predicting results')
        prediction = get_score(DATA_PATH, model_path)
    else:
        print('Generating ABT and predicting results')
        get_abt(DATA_PATH, QUERY_PATH, primeira_safra, ultima_safra)
        prediction = get_score(DATA_PATH, model_path)

    if prediction is not None:
        prediction.to_csv('prediction.csv')


    end_time = datetime.datetime.now()
    print('==========================================================')
    print('\nScript completo')
    if prediction is not None:
        print('Prediction results saved to prediction.csv file')
    print(f'O tempo total foi {end_time - start_time}\n')
    print('==========================================================')