#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import numpy as np

# split without crop
def save_txt(input_directory, output_directory):
    # iterate over all the data binary file
    for filename in sorted(os.listdir(input_directory)):
        if filename.endswith(".bin"):
            print(os.path.join(input_directory, filename))
            # load data
            with open(os.path.join(input_directory, filename), 'rb') as fh:
                loaded_array = np.frombuffer(fh.read(), dtype="float32")
            # data processing
            img = loaded_array.reshape(240, -1)
            img = img.transpose()

            output = os.path.splitext(filename)[0] + '.txt'
            np.savetxt(os.path.join(output_directory, output), img, delimiter=",")

            fh.close()
            continue
        else:
            continue
            
# split data into train and test according to lines (without random crop)
def save_txt_lines(input_directory, output_directory):
    train_suffix = [1, 3, 5, 7]
    test_suffix = [2, 4, 6, 8]
    # iterate over all the data binary file
    for filename in sorted(os.listdir(input_directory)):
        # if filename ends up with 1, 3, 5, 7, it will be classfied into the train data
        if filename.endswith(".bin") and eval(os.path.splitext(filename)[0][-1]) in train_suffix:
            print(os.path.join(input_directory, filename))
            
            # load data
            with open(os.path.join(input_directory, filename), 'rb') as fh:
                loaded_array = np.frombuffer(fh.read(), dtype="float32")
            # data processing
            img = loaded_array.reshape(240, -1)
            img = img.transpose()

            output = os.path.splitext(filename)[0] + '.txt'
            np.savetxt(os.path.join(output_directory, 'train', output), img, delimiter=",")

            fh.close()
        
        # if filename ends up with 2, 4, 6, 8, it will be classfied into the test data
        if filename.endswith(".bin") and eval(os.path.splitext(filename)[0][-1]) in test_suffix:
            print(os.path.join(input_directory, filename))
            
            # load data
            with open(os.path.join(input_directory, filename), 'rb') as fh:
                loaded_array = np.frombuffer(fh.read(), dtype="float32")
            # data processing
            img = loaded_array.reshape(240, -1)
            img = img.transpose()
            # flip left to right
            img = np.fliplr(img)

            output = os.path.splitext(filename)[0] + '.txt'
            np.savetxt(os.path.join(output_directory, 'test', output), img, delimiter=",")

            fh.close()
            
            continue
        else:
            continue
            
# crop the PZ_combination dataset
def save_txt_crop(input_directory, output_directory):
    splits = os.listdir(input_directory)
    for sp in sorted(splits):
        output_folder = os.path.join(output_directory, sp)
        if not os.path.isdir(output_folder):
            os.makedirs(output_folder)
        # iterate over all the txt files
        for filename in sorted(os.listdir(os.path.join(input_directory, sp))):
            if filename.endswith(".txt"):
                print(os.path.join(input_directory, sp, filename))
                # load data
                with open(os.path.join(input_directory, sp, filename), 'rb') as fh:
                    loaded_array = np.genfromtxt(fh, delimiter=',', dtype='float64').astype('float32')
                # crop size can be edited here
                img = loaded_array[1300:2200, :]
                np.savetxt(os.path.join(output_folder, filename), img, delimiter=",")
                fh.close()
                continue
            else:
                continue

