set -ex
python test.py --dataroot ./datasets/seismic/PZ_combination_crop_900 --name seismic_pix2pix --model pix2pix --netG unet_256 --direction AtoB --dataset_mode aligned --norm batch
