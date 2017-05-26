#!/usr/bin/env python

import argparse
from collections import OrderedDict
import copy
from panoptes_aggregation import reducers
from panoptes_aggregation.flatten_data import flatten_data, unflatten_data
import json
import math
import pandas
import progressbar

parser = argparse.ArgumentParser(description="reduce data from panoptes classifications based on the extracted data (see extract_panoptes_csv)")
parser.add_argument("extracted_csv", help="the extracted csv file output from extract_panoptes_csv", type=str)
parser.add_argument("-F", "--filter", help="how to filter a user makeing multiple classifications for one subject", type=str, choices=['first', 'last', 'all'], default='fisrt')
parser.add_argument("-k", "--keywords", help="keywords to be passed into the reducer in the form of a json string, e.g. \'{\"eps\": 5.5, \"min_samples\": 3}\'  (note: double quotes must be used inside the brackets)", type=json.loads)
parser.add_argument("-o", "--output", help="the base name for output csv file to store the reductions", type=str, default="reductions.csv")
args = parser.parse_args()

extracted = pandas.read_csv(args.extracted_csv)
extracted.created_at = pandas.to_datetime(extracted.created_at)
extracted.sort_values(['subject_id', 'created_at'], inplace=True)

subjects = set(extracted.subject_id)
workflow_id = extracted.workflow_id.iloc[0]
extractor_name = extracted.extractor.iloc[0]
reducer_name = extractor_name.replace('extractor', 'reducer')

reduced_data = OrderedDict([
    ('subject_id', []),
    ('workflow_id', []),
    ('reducer', []),
    ('data', [])
])

widgets = [
    'Reducing: ',
    progressbar.Percentage(),
    ' ', progressbar.Bar(),
    ' ', progressbar.ETA()
]

pbar = progressbar.ProgressBar(widgets=widgets, max_value=len(subjects))
pbar.start()
for sdx, subject in enumerate(subjects):
    idx = extracted.subject_id == subject
    classifications = extracted[idx]
    if args.filter in ['frist', 'last']:
        classifications.drop_duplicates(['user_name'], keep=args.filter, inplace=True)
    data = [unflatten_data(c) for cdx, c in classifications.iterrows()]
    reduced_data['subject_id'].append(subject)
    reduced_data['workflow_id'].append(workflow_id)
    reduced_data['reducer'].append(reducer_name)
    reduced_data['data'].append(reducers.reducer_base[reducer_name](data, **args.keywords))
    pbar.update(sdx + 1)
pbar.finish()

flat_reduced_data = flatten_data(reduced_data)
flat_reduced_data.to_csv('{0}_{1}'.format(reducer_name, args.output), index=False)
