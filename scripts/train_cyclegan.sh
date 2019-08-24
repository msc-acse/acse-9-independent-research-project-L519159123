set -ex
python train.py --dataroot ./datasets//seismic/PZ_combination_crop_900 --name seismic_cyclegan --model cycle_gan --pool_size 50 --no_dropout
