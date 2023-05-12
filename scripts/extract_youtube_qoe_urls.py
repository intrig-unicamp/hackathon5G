#!/usr/bin/env python3

import argparse
import re
import os
import glob
import json
from urllib.parse import urlparse, parse_qsl
import pyshark

# https://github.com/KimiNewt/pyshark/issues/360#issuecomment-700425352
import nest_asyncio

def open_youtube_qoe_pcap_filtered(filename):
    pcap = pyshark.FileCapture(input_file=filename, display_filter='http2.header.value contains "api/stats/qoe"')
    pcap = [ { 'time': each.sniff_time.isoformat() + 'Z', 'url': each.http2.headers_path } for each in pcap]
    return pcap


def open_youtube_qoe_har_filtered(filename):
    with open(filename, 'r') as fp:
        har = json.load(fp)
        return [ { 'time': each['startedDateTime'], 'url': '/api' + each['request']['url'].split('/api', 1)[1] } for each in har['log']['entries'] if 'youtube.com/api/stats/qoe?' in each['request']['url']]


def process_file(filename):
    if re.search(r'\.pcap(ng)?$', filename, flags=re.IGNORECASE):
        res = open_youtube_qoe_pcap_filtered(filename)

    elif re.search(r'\.har$', filename, flags=re.IGNORECASE):
        res = open_youtube_qoe_har_filtered(filename)

    else:
        raise Exception(f'file extension not recognized: {filename}')

    # extract query params from URLs
    res = [ { k: v for k, v in [('time', i['time'])] + parse_qsl(urlparse(i['url']).query) } for i in res ]

    return res

def main(args):
    if args.glob:
        files = glob.glob(args.glob)
    elif args.directory:
        files = [ os.path.join(args.directory, file) for file in os.listdir(args.directory) ]
    else:
        files = args.files

    files = [ file for file in files if re.search(r'\.(har|pcap(ng)?)$', file, flags=re.IGNORECASE) and os.path.isfile(file) ]

    if len(files) == 0:
        return print('no files to proccess')

    for file in files:
        print(f'processed input: {file}')

    request_list = [ process_file(file) for file in files ]

    if args.output_file:
        request_list = [sum(request_list, [])]

    for (entry, file) in zip(request_list, files):
        output_file = args.output_file if args.output_file else re.sub(r'\.(har|pcap(ng)?)$', '.json', file, flags=re.IGNORECASE)
        print(f'output: {output_file}')

        with open(output_file, 'w') as outfile:
            for line in entry:
                json.dump(line, outfile, separators=(',', ':'))
                outfile.write('\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract URLs from pcap, pcapng and har files. Outputs JSON file(s)')

    # mutually exclusive group for file and directory paths
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', dest='files', action='append', help='Input pcap, pcapng or har file(s)')
    group.add_argument('-d', '--dir', dest='directory', help='Input directory with pcap, pcapng or har files')
    group.add_argument('-g', '--glob', dest='glob', help='Glob pattern to select input pcap, pcapng or har files')

    # optional parameter for output filename
    parser.add_argument('-o', '--output-file', dest='output_file', help='Combines multiple files into one output file')

    args = parser.parse_args()
    nest_asyncio.apply()
    main(args)
