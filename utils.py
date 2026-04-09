import pandas as pd

def load_data(path):
    df = pd.read_csv(path, encoding='latin1')
    
    # Convert dates
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    
    # Create additional columns
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    
    return df