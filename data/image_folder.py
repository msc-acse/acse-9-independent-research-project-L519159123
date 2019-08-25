"""
author : Yuxuan Liu
github alias: L519159123
"""

"""A modified image folder class

We modify the official PyTorch image folder (https://github.com/pytorch/vision/blob/master/torchvision/datasets/folder.py)
so that this class can load images from both current directory and its subdirectories.
"""

import torch.utils.data as data

from PIL import Image
import os
import os.path


# IMG_EXTENSIONS = [
#     '.jpg', '.JPG', '.jpeg', '.JPEG',
#     '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
# ]

data_suffix = ['.txt']

# def is_image_file(filename):
#     return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

def is_data_file(filename):
    return any(filename.endswith(extension) for extension in data_suffix)

# def make_dataset(dir, max_dataset_size=float("inf")):
#     images = []
#     assert os.path.isdir(dir), '%s is not a valid directory' % dir

#     for root, _, fnames in sorted(os.walk(dir)):
#         for fname in fnames:
#             if is_image_file(fname):
#                 path = os.path.join(root, fname)
#                 images.append(path)
#     return images[:min(max_dataset_size, len(images))]


def make_dataset(dir, max_dataset_size=float("inf")):
    data = []
    assert os.path.isdir(dir), '%s is not a valid directory' % dir

    for root, _, fnames in sorted(os.walk(dir)):
        for fname in fnames:
            if is_data_file(fname):
                path = os.path.join(root, fname)
                data.append(path)
    return data[:min(max_dataset_size, len(data))]



# def default_loader(path):
#     return Image.open(path).convert('RGB')

def default_loader(path):
    return np.genfromtxt(directory, delimiter=',', dtype='float64').astype('float32')


# class ImageFolder(data.Dataset):

#     def __init__(self, root, transform=None, return_paths=False,
#                  loader=default_loader):
#         imgs = make_dataset(root)
#         if len(imgs) == 0:
#             raise(RuntimeError("Found 0 images in: " + root + "\n"
#                                "Supported image extensions are: " +
#                                ",".join(IMG_EXTENSIONS)))

#         self.root = root
#         self.imgs = imgs
#         self.transform = transform
#         self.return_paths = return_paths
#         self.loader = loader

#     def __getitem__(self, index):
#         path = self.imgs[index]
#         img = self.loader(path)
#         if self.transform is not None:
#             img = self.transform(img)
#         if self.return_paths:
#             return img, path
#         else:
#             return img

#     def __len__(self):
#         return len(self.imgs)
    
    

class ImageFolder(data.Dataset):

    def __init__(self, root, transform=None, return_paths=False,
                 loader=default_loader):
        data = make_dataset(root)
        if len(data) == 0:
            raise(RuntimeError("Found 0 text file in: " + root + "\n"
                               "Supported data suffix are: " +
                               ",".join(data_suffix)))

        self.root = root
        self.data = data
        self.transform = transform
        self.return_paths = return_paths
        self.loader = loader

    def __getitem__(self, index):
        path = self.data[index]
        da = self.loader(path)
        if self.transform is not None:
            da = self.transform(da)
        if self.return_paths:
            return da, path
        else:
            return da

    def __len__(self):
        return len(self.data)
