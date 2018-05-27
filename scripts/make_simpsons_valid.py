import os
import math

import numpy as np
import pandas as pd

data_path = '/path/to/the-simpsons-characters-dataset'

sub_dirs = os.listdir(data_path)
char_dirs = os.listdir(data_path+'/simpsons_dataset')

csv_path = data_path+'/number_pic_char.csv'
df = pd.read_csv(csv_path)
first_20_chars = [char.lower().replace(' ', '_') for char in df['name'][:20]]

os.mkdir(data_path+'/excluded_chars')

for dir in char_dirs:
    if dir not in first_20_chars:
        src = data_path+'/simpsons_dataset/'+dir
        target = data_path+'/excluded_chars/'+dir
        os.rename(src, target)

if 'valid' not in sub_dirs:
    os.mkdir(data_path+'/valid')
    for dir in first_20_chars:
        print('Creating validation data path: '+data_path+'/valid/'+dir)
        os.mkdir(data_path+'/valid/'+dir)

char_paths_train = [data_path+'/simpsons_dataset/'+dir for dir in first_20_chars]

for path in char_paths_train:
    print('Creating training data path: ' + path)
    char = path.split('/')[-1]
    files = os.listdir(path)
    file_paths = [path+'/'+file for file in files]
    np.random.shuffle(file_paths)
    total_files = len(file_paths)
    test_split = math.floor(total_files*0.8)
    test_file_paths = file_paths[test_split:]
    destination_dir = data_path+'/valid/'+char
    for path in test_file_paths:
        file = path.split('/')[-1]
        os.rename(path, destination_dir+'/'+file)

print('Moving training data to '+data_path+'/train')
os.rename(data_path+'/simpsons_dataset', data_path+'/train')