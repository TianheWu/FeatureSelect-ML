import pandas as pd


def func_read():
    CSV_FILE_PATH = 'D:\wutianhe_document\Project_biological\data.csv'
    file = pd.read_csv(CSV_FILE_PATH)
    df = pd.DataFrame(file)
    df['ans'] = 1

    for i in range(53, len(df)):
        df.loc[i, 'ans'] = -1

    x = df.drop(['id', 'ans'], 1)
    y = df['ans']
    return x, y
