import os
import sys 
import pandas as pd
from src.logger import logging  
from src.exception import CustomException
import numpy as np 
from sklearn.metrics import r2_score
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
def evaluate_models(X_train,y_train,X_test,y_test,models):
    try:
        report={}
        for i in range(len(models)):
            model=list(models.values())[i]
            model.fit(X_train,y_train)
            y_pred=model.predict(X_test)
            from sklearn.metrics import r2_score
            r2_square=r2_score(y_test,y_pred)
            report[list(models.keys())[i]]=r2_square
        return report
    except Exception as e:
        logging.info("Exception occurred in evaluate_models function")
        raise CustomException(e,sys)