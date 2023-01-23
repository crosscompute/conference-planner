import pandas as pd
from os.path import join
from sys import argv

output_folder = argv[1]

url = 'https://raw.githubusercontent.com/python-organizers/conferences/master/2020.csv'
data = pd.read_csv(url)

calendar_frame = pd.DataFrame({
    'Conference': data['Subject'],
    'Location': data['Location'],
    'Website': data['Website URL'],
    'Talk Deadline': data['Talk Deadline'],
})

calendar_frame.to_json(join(output_folder, 'calendar.csv'), orient='split')

# save to json 
# compute logger in examples
#to_json in pandas