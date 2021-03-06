import os
import re
import sys

import numpy as np
from scipy.io import loadmat
import pandas as pd

DEFAULT_MAT_FILE = './data/nut_data_reps.mat'
DEFAULT_OUT_DIR = './output'

CSV_FILENAME = 'nes-lter-nutrient.csv'

if len(sys.argv) < 3:
    in_mat_file = DEFAULT_MAT_FILE
    out_dir = DEFAULT_OUT_DIR
else:
    assert len(sys.argv) == 3, 'must specify input file and output directory'
    in_mat_file, out_dir = sys.argv[1], sys.argv[2]

assert os.path.exists(in_mat_file), 'input mat file {} not found'.format(in_mat_file)
assert os.path.exists(out_dir), 'output directory {} does not exist'.format(out_dir)

# load the mat file
mat = loadmat(in_mat_file, squeeze_me=True)

# construct dataframe

# column renaming map
COL_MAP = {
  'Event_Number': 'event_number',
  'Event_Number_Niskin': 'event_number_niskin',
  'Latitude': 'latitude',
  'Longitude': 'longitude',
  'Depth': 'depth',
  'Nut_a_uM NO2- + NO3-': 'ntra_a',
  'Nut_b_uM NO2- + NO3-': 'ntra_b',
  'Nut_c_uM NO2- + NO3-': 'ntra_c',
  'Nut_a_uM NH4+': 'amon_a',
  'Nut_b_uM NH4+': 'amon_b',
  'Nut_c_uM NH4+': 'amon_c',
  'Nut_a_uM SiO2-': 'slca_a',
  'Nut_b_uM SiO2-': 'slca_b',
  'Nut_c_uM SiO2-': 'slca_c',
  'Nut_a_uM PO43-': 'phos_a',
  'Nut_b_uM PO43-': 'phos_b',
  'Nut_c_uM PO43-': 'phos_c',
}

# now parse mat file

cols = mat['header_nut']
d = {}
for i, col in enumerate(cols):
    d[col] = pd.Series(list(mat['MVCO_nut_reps'][:,i]))
df = pd.DataFrame(d, columns=cols)

# compute datetimes from start date and incorrect start time cols

dt = []
for d, t in zip(df['Start_Date'], df['Start_Time_UTC']):
    dt.append(pd.to_datetime('{}T{}Z'.format(d[:10],t[11:])))
dt = pd.Series(dt)

# add to dataframe

df['time (UTC)'] = dt
del df['Start_Date']
del df['Start_Time_UTC']

# rename columns

df = df.rename(columns=COL_MAP)

# just outputting the dataframe using to_csv produces
# extra digits of precision, and applying a single float
# format is not appropriate because the columns have
# varying precision, so do this using string formatting

def convert_series_fixed(series, significant_digits=3):
    fmt = r'{{:.{}f}}'.format(significant_digits)
    for n in series:
        if np.isnan(n):
            yield 'NaN'
        else:
            yield fmt.format(n)

SIGNIFICANT_DIGITS = 3

# apply precision formatting

data_cols = []

for var in ['ntra', 'slca', 'phos', 'amon']:
    for replicate in ['a', 'b', 'c']:
        colname = '{}_{}'.format(var, replicate)
        data_cols.append(colname)

for colname in data_cols:
    df[colname] = list(convert_series_fixed(df[colname], SIGNIFICANT_DIGITS))

cols = ['time (UTC)', 'latitude', 'longitude', 'depth', 'event_number'] + data_cols
df = df[cols]

# chop off everything before april 2006
df = df[df['time (UTC)'] >= '2006-04-01']

df.to_csv(CSV_FILENAME, index=None)