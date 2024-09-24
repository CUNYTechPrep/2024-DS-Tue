import pandas as pd


def pipeline(fp):
    df = pd.read_csv(fp, sep='\t')

    # Drop NAs
    df = df.dropna()

    # Compute age.
    df['age'] = 2024 - df['Year_Birth']

    # Remove one super rich person.
    df = df[df['Income'] < 600000]

    df.columns = [x.lower() for x in df.columns]

    # only 200 duplicates, so just drop them. 
    df = df.drop_duplicates()


    # make column of total spent
    product_columns = [
        'mntwines', 'mntfruits', 'mntmeatproducts', 
        'mntfishproducts', 'mntsweetproducts', 'mntgoldprods'
        ]
    
    df['total_spent'] = df[product_columns].sum(axis=1)

    return df

