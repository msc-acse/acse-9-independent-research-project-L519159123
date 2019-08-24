

### CycleGAN Datasets
Download the datasets using the following script.
```bash
sh download_data.sh
```
- `PZ_combination_crop_900`: 1928 training gathers and 408 test gathers. Each of seismic gather is 900 x 240 pixels.


To train a model on your own datasets, you need to create a data folder with two subdirectories `trainA` and `trainB` that contain images from domain A and B. You can test your model on your training set by setting `--phase train` in `test.py`. You can also create subdirectories `testA` and `testB` if you have test data.


### pix2pix datasets
Download the pix2pix datasets using the following script. Some of the datasets are collected by other researchers. Please cite their papers if you use the data.
```bash
sh download_data.sh
```
- `PZ_combination_crop_900`: 1928 training gathers and 408 test gathers. Each of seismic gather is 900 x 240 pixels.
- `PZ_combination_crop_1200`: 1928 training gathers and 408 test gathers. Each of seismic gather is 1200 x 240 pixels.
- `PZ_combination_in_lines_nocrop`: 1168 training gathers and 1168 test gathers. Each of seismic gather is 3800 x 240 pixels.
- `PZ_combination_nocrop`: 1928 training gathers and 408 test gathers. Each of seismic gather is 3800 x 240 pixels.

**NOTE**: Only the `PZ_combination_crop_900` dataset will be downloaded via `sh download_data.sh`. Other datasets can be provided on request.

We provide a python script to generate pix2pix training data in the form of pairs of images {A,B}, where A and B are two different depictions of the same underlying scene. For example, these might be pairs {P_data, Z_data}. Then we can learn to translate A to B or B to A:

Create folder `/path/to/data` with subfolders `A` and `B`. `A` and `B` should each have their own subfolders `train`, `val`, `test`, etc. In `/path/to/data/A/train`, put training images in style A. In `/path/to/data/B/train`, put the corresponding images in style B. Repeat same for other data splits (`val`, `test`, etc).

Corresponding images in a pair {A,B} must be the same size and have the same filename, e.g., `/path/to/data/A/train/1.jpg` is considered to correspond to `/path/to/data/B/train/1.jpg`.

Once the data is formatted this way, call:
```bash
python datasets/combine_A_and_B.py --fold_A /path/to/data/A --fold_B /path/to/data/B --fold_AB /path/to/data
```

This will combine each pair of images (A,B) into a single image file, ready for training.
