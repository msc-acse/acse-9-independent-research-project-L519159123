set -ex
python train.py --dataroot ./datasets/seismic/PZ_combination_crop_900 --name seismic_pix2pix --model pix2pix --netG unet_256 --direction AtoB --lambda_L1 100 --dataset_mode aligned --norm batch --pool_size 0
