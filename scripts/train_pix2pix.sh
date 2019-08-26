set -ex
python train.py --dataroot ./datasets/seismic/PZ_combination_crop_900 --name seismic_pix2pix --model pix2pix --direction AtoB --input_nc 1 --output_nc 1 --lambda_L1 200 --n_layers_D 1 --ngf 64 --ndf 16 --netD pixel --netG resnet_9blocks
