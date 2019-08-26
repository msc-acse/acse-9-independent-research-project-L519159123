set -ex
python test.py --dataroot ./datasets/seismic/PZ_combination_crop_900 --name seismic_pix2pix --model pix2pix --netG resnet_9blocks --netD pixel --ngf 64 --ndf 16 --direction AtoB --n_layers_D 1 --input_nc 1 --output_nc 1
