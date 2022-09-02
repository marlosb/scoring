import datetime
import sys

from abt import create_abt
   
DATA_PATH = 'data/olist_dsa.db'
QUERY_PATH = 'sql/Script_ABT_olist_dtref_safra_20200818.sql'
MODEL_PATH = 'models/'

primeira_safra = "2018-07-01"
ultima_safra = "2018-09-01"

if __name__ == "__main__":
    start_time = datetime.datetime.now()

    if '-abtonly' in sys.argv:
        print('Creating ABT....')
        create_abt(QUERY_PATH, DATA_PATH, primeira_safra, ultima_safra)
    elif '-scoreonly' in sys.argv:
        print('Scoring results')
        
    else:
        print('Creating ABT and Scoring results!')
        create_abt(QUERY_PATH, DATA_PATH, primeira_safra, ultima_safra)
    
    end_time = datetime.datetime.now()

    print('==========================================================')
    print(f'\nScript completo em: {end_time - start_time}\n')
    print('==========================================================')

    print('==========================================================')
