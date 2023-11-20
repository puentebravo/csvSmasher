import pandas as pd;
from dotenv import load_dotenv;
import os;
load_dotenv();

mainData = pd.read_csv(os.getenv("MAIN_DOC_PATH"))
subData = pd.read_csv(os.getenv("SUB_DOC_PATH"))
primaryKey = os.getenv("PRIMARY_KEY")


newData = pd.merge(mainData, subData, on=primaryKey, how="left", left_on=None, right_on=None, left_index=False, right_index=False, sort=False, copy=True)



newData.to_csv("./dist/combined.csv")