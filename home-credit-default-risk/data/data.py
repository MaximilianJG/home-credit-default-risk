import pandas as pd
import os 
from pathlib import Path

class Data: 
    def __init__(self):
        pass
    
    def get_data(self, tables=["application_train", "bureau", "bureau_balance", "POS_CASH_balance", 
                               "credit_card_balance", "previous_application", "installments_payments"]):
        
        root_dir = Path(__file__).parents[2]
        df_dict = {}
        
        for table in tables: 
            data_dir_path = os.path.join(root_dir, f"raw_data/{table}" + ".csv")
            df_dict[table] =  pd.read_csv(data_dir_path)
        
        return df_dict



if __name__ == "__main__": 
    data = Data()
    print(data.get_data())
    
    