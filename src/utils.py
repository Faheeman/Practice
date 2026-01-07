import os
import sys 
import pandas as pd
from src.logger import logging  
from src.exception import CustomException
import numpy as np 
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        import dill
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        logging.info("Exception occurred in save_object function")
        raise CustomException(e,sys)