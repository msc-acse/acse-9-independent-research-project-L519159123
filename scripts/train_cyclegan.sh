set -ex
python train.py --dataroot ./datasets/seismic/PZ_combination_crop_900 --name seismic_cyclegan --model cycle_gan --direction AtoB --input_nc 1 --output_nc 1 --netG resnet_9blocks --ngf 64 --ndf 8 --n_layers_D 1 --dataset_mode aligned --netD pixel --lr 0.0002 --lambda_L1 100
