import pandas as pd
import xarray as xr
import os

def convert_to_csv(file):
    ds = xr.open_dataset(file)
    df = ds.to_dataframe()
    df = df[:366*20]

    num_traj = int(len(df)/366)

    table = []
    for i in range(num_traj):
        for y in range(366):
            row = []
            row.append(i)
            row.append(y)
            lon = df['lon'][i][y]
            lat = df['lat'][i][y]
            row.append(lon)
            row.append(lat)
            table.append(row)

    df = pd.DataFrame(table, columns=['id', 'day', 'lon', 'lat'])
    df.to_csv(file[:-3] + '.csv', index=True)
    print('Final!')

if __name__ == "__main__":
    for file in os.listdir("../datasets/"):
        print(os.path.join("../datasets/", file))
        if os.path.isfile(os.path.join("../datasets/", file)) and file[-2:] == '.nc':
            convert_to_csv(os.path.join("../datasets/", file))
