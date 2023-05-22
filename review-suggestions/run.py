import csv
import json
from os import getenv
from pathlib import Path


output_folder = Path(getenv(
    'CROSSCOMPUTE_OUTPUT_FOLDER', 'batches/standard/output'))
datasets_folder = Path('datasets')
runs_folder = datasets_folder / 'runs'
with (output_folder / 'suggestions.csv').open('wt') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow([
        'website_url',
        'subject',
        'start_date',
        'end_date'
        'location',
        'talk_deadline',
        'proposal_url'])
    for run_folder in runs_folder.glob('*'):
        with (run_folder / 'input' / 'variables.dictionary').open('rt') as f:
            d = json.load(f)
        csv_writer.writerow(d.values())
