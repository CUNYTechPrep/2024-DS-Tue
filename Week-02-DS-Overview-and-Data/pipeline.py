import pandas as pd
import numpy as np

def pipeline_for_mixed_datatypes(absoulte_file_path, output_path=None):
    df = pd.read_csv(absoulte_file_path, 
                 na_values=['MISSING', 'NULL'])
    
    # Remove whitespace, to get NULL to nan and replace it. 
    string_cols = ['mixed_types', 'just_strings']
    for col in string_cols:
        df[col] = df[col].str.strip()
    df = df.replace('NULL', np.nan)
    #########################################################


    #########################################################
    # Convert mixed_types column to numbers
    df['dang_this_is_easy'] = pd.to_numeric(df['mixed_types'], errors='coerce')
    #########################################################


    #########################################################
    # Fill Nans with mean
    df['numbers_filled_na'] = df['dang_this_is_easy'].fillna( df['dang_this_is_easy'].mean() )
    #########################################################

    #########################################################
    # Save file if given path
    if output_path:
        df.to_csv(output_path, index=False)

    return df


file_path = '/Users/ctp/CTP/2024/2024-Fall-DS-Dev/Week-02-DS-Overview-and-Data/data/mixed_types.csv'
pipeline_for_mixed_datatypes(absoulte_file_path=file_path)


