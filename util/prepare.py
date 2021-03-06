'''

    prepare.py

    Description: This file contains functions used for preparing the kepler 
        exoplanet data for exploration and modeling.

    Variables:

        None

    Functions:

        prepare_kepler_explore(df)
        prepare_kepler_modeling(df)
        drop_missing_values(df, required_percentage_columns = 0, required_percentage_rows = 0)

'''

################################################################################

import pandas as pd

################################################################################

def prepare_kepler_explore(df: pd.DataFrame) -> pd.DataFrame:
    '''
        Prepare the kepler exoplanet data for exploration and modeling. This 
        function will remove columns with more than 75% missing values and all 
        rows with missing values. The columns rowid, kepid, and kepoi_name are 
        dropped. The column koi_disposition is renamed to disposition.
    
        Parameters
        ----------
        df: DataFrame
            A pandas dataframe containing the unprepared kepler exoplanet data.
    
        Returns
        -------
        DataFrame: The prepared kepler exoplanet data.
    '''

    df = drop_missing_values(df, 0.75, 1)

    not_candidate = ~(df.koi_disposition == 'CANDIDATE')
    df = df[not_candidate]
    
    columns_to_drop = [
        'rowid',
        'kepid',
        'kepoi_name'
    ]
    df = df.drop(columns = columns_to_drop)
    
    rename_map = {
        'koi_disposition' : 'disposition'
    }
    df = df.rename(columns = rename_map)

    return df

################################################################################

def prepare_kepler_modeling(df: pd.DataFrame) -> pd.DataFrame:
    '''
        Prepare the kepler exoplanet data for exploration and modeling. This 
        function will remove columns with more than 75% missing values and all 
        rows with missing values. The columns rowid, kepid, and kepoi_name are 
        dropped. The column koi_disposition is renamed to disposition.
    
        Parameters
        ----------
        df: DataFrame
            A pandas dataframe containing the unprepared kepler exoplanet data.
    
        Returns
        -------
        DataFrame: The prepared kepler exoplanet data.
    '''

    df = drop_missing_values(df, 0.75, 1)

    not_candidate = ~(df.koi_disposition == 'CANDIDATE')
    df = df[not_candidate]
    
    columns_to_keep = [
        'koi_disposition',
        'koi_depth',
        'koi_prad',
        'koi_teq',
        'koi_model_snr',
        'koi_period',
        'koi_duration'
    ]
    df = df[columns_to_keep]
    
    rename_map = {
        'koi_disposition' : 'disposition',
        'koi_depth' : 'transit_depth',
        'koi_prad' : 'planetary_radius',
        'koi_teq' : 'temperature',
        'koi_model_snr' : 'normalized_depth',
        'koi_period' : 'orbital_period',
        'koi_duration' : 'transit_duration'
    }
    df = df.rename(columns = rename_map)

    return df

################################################################################

def drop_missing_values(df: pd.DataFrame, required_percentage_columns: float = 0, required_percentage_rows: float = 0) -> pd.DataFrame:
    '''
        Drops columns and rows with a percentage of missing values greater than 
        required_percentage_columns and required_percentage_rows respectively.
    
        Parameters
        ----------
        df: DataFrame
            A pandas dataframe containing data with missing values.

        required_percentage_columns: float, optional
            A number between 0 and 1. The percentage of missing values in a 
            column required to drop the column from the dataframe.

        required_percentage_rows: float, optional
            A number between 0 and 1. The percentage of missing values in a 
            row required to drop the row from the dataframe.
    
        Returns
        -------
        DataFrame: The input with columns and rows dropped according to the 
            percentages given.
    '''

    df = df.dropna(axis = 'columns', thresh = round(df.shape[0] * required_percentage_columns))
    df = df.dropna(axis = 'index', thresh = round(df.shape[1] * required_percentage_rows))
    
    return df