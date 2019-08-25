# Generative Adversarial Networks applied to multi-component seismic data

[![Build Status](https://travis-ci.com/msc-acse/acse-9-independent-research-project-L519159123.svg?branch=master)](https://travis-ci.com/msc-acse/acse-9-independent-research-project-L519159123)

We provide PyTorch implementations for paired seismic data domain translation problems.

**CycleGAN**
<img src="https://github.com/msc-acse/acse-9-independent-research-project-L519159123/blob/master/imgs/cycle.png" width="800"/>

The software is an extension of source code written by Jun-Yan Zhu and Taesung Park which is available via github repository https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix. 

**Note**: The current software works well with PyTorch 0.41+.

You may find useful information in [Training/Test Tips](docs/tips.md). To implement custom models and datasets, check out our [template](#custom-model-and-dataset). To help users better understand and adapt our codebase, we provide an [overview](docs/overview.md) of the code structure of this repository.

## Prerequisites
- Linux or macOS
- Python 3
- CPU or NVIDIA GPU + CUDA CuDNN

## Getting Started
### Installation

- Clone this repo:
```bash
git clone https://github.com/msc-acse/acse-9-independent-research-project-L519159123
cd acse-9-independent-research-project-L519159123
```

- Install [PyTorch](http://pytorch.org and) 0.4+ and other dependencies (e.g., torchvision, [visdom](https://github.com/facebookresearch/visdom) and [dominate](https://github.com/Knio/dominate)).
  - For pip users, please type the command `pip install -r requirements.txt`.
  - For Conda users, we provide a installation script `./scripts/conda_deps.sh`. Alternatively, you can create a new Conda environment using `conda env create -f environment.yml`.
  - For Docker users, we provide the pre-built Docker image and Dockerfile. Please refer to our [Docker](docs/docker.md) page.
  
### CycleGAN train/test
- Download the dataset:
```bash
sh download_data.sh
```
- To view training results and loss plots, run `python -m visdom.server` and click the URL http://localhost:8097.
- Train a model:
```bash
#!./scripts/train_cyclegan.sh
python train.py --dataroot ./datasets/seismic/PZ_combination_crop_900 --name seismic_cyclegan --model cycle_gan --input_nc 1 --output_nc 1 --dataset_mode aligned
```
To see more intermediate results, check out `./checkpoints/seismic_cyclegan/web/index.html`.
- Test the model:
```bash
#!./scripts/test_cyclegan.sh
python test.py --dataroot ./datasets/seismic/PZ_combination_crop_900 --name seismic_cyclegan --model cycle_gan --input_nc 1 --output_nc 1 --dataset_mode aligned
```
- The test results will be saved to a html file here: `./results/seismic_cyclegan/latest_test/index.html`.

### pix2pix train/test
- Download the dataset:
```bash
sh download_data.sh
```
- Train a model:
```bash
#!./scripts/train_pix2pix.sh
python train.py --dataroot ./datasets/seismic/PZ_combination_crop_900 --name seismic_pix2pix --model pix2pix --direction AtoB --input_nc 1 --output_nc 1
```
- To view training results and loss plots, run `python -m visdom.server` and click the URL http://localhost:8097. To see more intermediate results, check out  `./checkpoints/seismic_pix2pix/web/index.html`.

- Test the model (`bash ./scripts/test_pix2pix.sh`):
```bash
#!./scripts/test_pix2pix.sh
python test.py --dataroot ./datasets/seismic/PZ_combination_crop_900 --name seismic_pix2pix --model pix2pix --direction AtoB --input_nc 1 --output_nc 1
```
- The test results will be saved to a html file here: `./results/seismic_pix2pix/test_latest/index.html`. You can find more scripts at `scripts` directory.
- See our training [tips](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/docs/tips.md) for more details.

## [Docker](docs/docker.md)
We provide the pre-built Docker image and Dockerfile that can run this code repo. See [docker](docs/docker.md).

## [Datasets](docs/datasets.md)
Download pix2pix/CycleGAN datasets and create your own datasets.

**NOTE**: Since the whole dataset is too big to be uploaded on AWS, so we only uploaded a small subset which can be trained by both pix2pix and CycleGAN. The corresponding training checkpoints and test results will also be downloaded if you download the dataset via script `sh download_data.sh`. The full data can be provided on request.

## [Training/Test Tips](docs/tips.md)
Best practice for training and testing your models.

## Custom Model and Dataset
If you plan to implement custom models and dataset for your new applications, we provide a dataset [template](data/template_dataset.py) and a model [template](models/template_model.py) as a starting point.

## [Code structure](docs/overview.md)
To help users better understand and use our code, we briefly overview the functionality and implementation of each package and each module.

## Author and Course Information
**Author**: Yuxuan Liu **Github**: L519159123 **CID**: 01550892

This project is completed for Imperial College's MSc in Applied Computational Science and Engineering program, as part of the final course module ACSE9. This project was completed under the supervision of Prof. Mike Warner and Dr.Jiashun Yao.

## Acknowledgments
- Our code is inherited from [pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) and [CycleGAN](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix).
- Thanks to the support from my supervisor Prof. Mike Warner and Dr. Jiashun Yao.
- Thanks to the moral support from my family and friends.

## License
This project is licensed under the MIT [license](LICENSE).
