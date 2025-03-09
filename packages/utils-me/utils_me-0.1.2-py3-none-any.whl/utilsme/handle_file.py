import pandas as pd
import os
import shutil
import requests
# from pyspark.sql import types as T
from .time import timing

@timing
def read_file(path_file: str, *args, **kwargs) -> pd.DataFrame:
    if (path_file.endswith('csv') | path_file.endswith('xlsx')):
        raise(f"Error: {path_file.split('.')[1]} file type is not yet taken into account. Only csv and xlsx are considered")
    
    else:
        try:
            if path_file.endswith('csv'):
                return pd.read_csv(path_file, kwargs)
            else:
                return pd.read_excel(path_file, kwargs)
        except Exception as e:
            raise(f"Error found when trying to read: {path_file}. {e}")
        
@timing
def write_file(data: pd.DataFrame, path_file: str, **kwargs) -> None:
    if (path_file.endswith('csv') | path_file.endswith('xlsx')):
        raise(f"Error: {path_file.split('.')[0]} file type is not yet taken into account. Only csv and xlsx are considered")
    
    else:
        try:
            if path_file.endswith('csv'):
                return data.to_csv(path_file, kwargs)
            else:
                return data.to_excel(path_file, kwargs)
        except Exception as e:
            raise(f"Error found when trying to write: {path_file}. {e}")     
        
@timing
def list_files(dir: str, filter: str = '') -> list:
    try:
        result = []
        for file in os.listdir(dir):
            if filter in file:
                print(file)
                result.append(file)
        return result
    except Exception as e:
        print(e)

@timing
def delete_file(file_path: str) -> None:
    try:
        os.remove(file_path)
        print(f"File {file_path} correctly deleted!")
    except Exception as e:
        print(e)
        

@timing
def move_file(src_file: str, dest_path: str) -> str:
    return shutil.move(src_file, dest_path)

@timing
def copy_file(src_file: str, dest_path: str) -> str:
    return shutil.copy(src_file, dest_path)

@timing
def download_file(link: str, dest_file_name: str) -> None:
    
    response = requests.get(link, stream=True)
    with os.open(dest_file_name, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)


@timing
def convert_data_types(df: pd.DataFrame, column_types: dict) -> pd.DataFrame:
    conv_report = dict()
    for col in column_types.keys():
        try:
            if type(df) == pd.DataFrame:
                df[col]= df[col].astype(column_types[col])
            elif type(df) == None: #T.Dataframe:
                # need to implement for spark
                df[col]= df[col].astype(column_types[col])
            
        except Exception as e:
            print(f"Error while converting {col} to {column_types[col]}")
            conv_report[col] = f"Error while converting to {column_types[col]}: {e}"
    print(conv_report)
    return df


@timing
def validate_data_types(df: pd.DataFrame, schema: dict) -> pd.DataFrame:
    conv_report = dict()
    for col, dtype in zip(df.columns, df.dtypes):
        if type(df) == pd.DataFrame:
            if dtype != schema[col]:
                conv_report[col] = f"{col}: Type in dataframe -> {dtype} and type in schema -> {schema[col]}"
        elif type(df) == None: #T.Dataframe:
            if dtype != schema[col]:
                conv_report[col] = f"{col}: Type in dataframe -> {dtype} and type in schema -> {schema[col]}"
    print(conv_report)
    return df

@timing
def remove_duplicates(df: pd.DataFrame, how: str = 'keep_first') -> pd.DataFrame:
    rm_dup_report = dict()
    for col in df.columns:
        if df[col].duplicated:
            if how == 'keep_first':
                pass
            elif how == 'keep_last':
                pass
            else:
                df = df[~df[col].duplicated]
                rm_dup_report[col] = f"{sum(df[col].duplicated)} duplicates remove base on column {col}"
    print(rm_dup_report)
    return df
def handle_missing_values(df, strategy='drop'):
    pass


def normalize_data(df, columns):
    pass


def standardize_data(df, columns):
    pass


def setup_logger(log_file):
    pass


def log_message(message, level='info'):
    pass


def track_progress(task_name, total_steps):
    pass



def load_config(config_file):
    pass


def get_env_variable(key):
    pass


def set_env_variable(key, value):
    pass

def connect_to_db(connection_string):
    pass

def execute_query(connection, query):
    pass


def read_sql_to_df(connection, query):
    pass



def write_df_to_table(df, connection, table_name):
    pass


def assert_data_shape(df, expected_shape): #Asserts that a DataFrame has the expected shape.
    pass

def assert_data_types(df, schema): #Asserts that a DataFrame matches a given schema.
    pass

def assert_no_missing_values(df): #Asserts that a DataFrame has no missing values.
    pass