#!/usr/bin/env python3

import argparse
import re
import os
import glob
import pandas as pd


def pd_insert_beside(df, column_name, value):
    df.insert(df.columns.get_loc(value.name) + 1, column_name, value)

# https://developers.google.com/youtube/iframe_api_reference#getPlayerState
player_state_enum_map = {
    'N':  'unstarted/cued', # -1 = unstarted; 5 = video cued
    'EN': 'ended',   # 0
    'PL': 'playing', # 1
    'PA': 'paused',  # 2
    'B':  'buffering', # 3
    'S':  'seek',    # guess based on player interactions (reverse engineering)
}

# transform comma separated timestamp/at
def trans_comma_sep_at(transformer):
    def inner(value):
        # each value has entries separated by comma
        # each entry is in the form at:metric
        value = [ e.split(':') for e in value.split(',') ]
        # each metric is transformed based on a custom function
        value = [ { 'at': float(at), **transformer(*v) } for at, *v in value ]
        return value
    return inner

column_transformers = {
    'vps':  trans_comma_sep_at(lambda a: { 'value': player_state_enum_map.get(a, a) }),
    'cmt':  trans_comma_sep_at(lambda a: { 'value': float(a) }),
    'bh':   trans_comma_sep_at(lambda a: { 'value': float(a) }),
    'bwe':  trans_comma_sep_at(lambda a: { 'value':   int(a) }),
    'df':   trans_comma_sep_at(lambda a: { 'value':   int(a) }),
    'bwm':  trans_comma_sep_at(lambda a, b: { 'downloaded_bytes': int(a), 'seconds_to_download': float(b) }),
    'bat':  trans_comma_sep_at(lambda a, b: { 'percentage': float(a) * 100, 'is_charging': b == '1' }),
    'view': trans_comma_sep_at(lambda   *a: { 'width': int(a[0]), 'height': int(a[1]) }), # sometimes has an unknown third value
}

array_columns = list(column_transformers.keys())

def youtube_qoe_column_transform(column, value):
    return column_transformers[column](value) if type(value) == str else value

def explode_columns_and_match_at(df, column_names):
    out = pd.DataFrame({ 'cpn': [], 'seq': [], 'at': [] })

    for c in column_names:
        exploded = df.explode(c)[['cpn', 'seq', c]]

        other_columns = exploded.drop(columns=[c]).reset_index(drop=True)
        c_columns = pd.json_normalize(exploded[c]).add_prefix(f'{c}.').rename(columns={f'{c}.at': 'at'})
        other_columns[list(c_columns)] = c_columns

        out = pd.merge(out, other_columns.dropna(), on=['cpn', 'seq', 'at'], how='outer')

    return out


def process_file(filename):
    df = pd.read_json(filename, lines=True, convert_dates=['time'])

    df[array_columns] = df[array_columns].apply(lambda x: x.apply(lambda y: youtube_qoe_column_transform(x.name, y)))

    pd_insert_beside(df, 'first_packet_time', df.groupby('cpn').time.transform(lambda group: group.min()))
    df.drop('time', axis=1, inplace=True)

    not_array_columns = [ c for c in df.columns if c not in array_columns]
    df = pd.merge(df[not_array_columns], explode_columns_and_match_at(df, array_columns), on=['cpn', 'seq'], how='inner')
    df.insert(0, 'session_time', df.pop('at'))
    df.insert(0, 'time_seconds', df.pop('first_packet_time').astype(int) / 10**9 + df.session_time)
    df.insert(0, 'time', pd.to_datetime(df.time_seconds, unit='s'))

    return df


def main(args):
    if args.glob:
        files = glob.glob(args.glob)
    elif args.directory:
        files = [ os.path.join(args.directory, file) for file in os.listdir(args.directory) ]
    else:
        files = args.files

    files = [ file for file in files if re.search(r'\.json$', file, flags=re.IGNORECASE) and os.path.isfile(file) ]

    if len(files) == 0:
        return print('no files to proccess')

    for file in files:
        print(f'processed input: {file}')

    dfs = [ process_file(file) for file in files ]

    if args.output_file:
        dfs = [pd.concat(dfs, ignore_index=True).copy()]

    for (df, file) in zip(dfs, files):
        output_file = args.output_file if args.output_file else re.sub(r'\.json$', '.pickle', file, flags=re.IGNORECASE)
        print(f'output: {output_file}')

        df.to_pickle(output_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Preprocess YouTube QoE URLs from JSON files. Outputs pandas Dataframe(s) in pickle format')

    # mutually exclusive group for file and directory paths
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', dest='files', action='append', help='Input JSON file(s)')
    group.add_argument('-d', '--dir', dest='directory', help='Input directory with JSON files')
    group.add_argument('-g', '--glob', dest='glob', help='Glob pattern to select input JSON files')

    # optional parameter for output filename
    parser.add_argument('-o', '--output-file', dest='output_file', help='Combines multiple files into one pickle file')

    args = parser.parse_args()
    main(args)
