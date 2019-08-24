set -ex
python test.py --dataroot ./datasets/seismic/PZ_combination_crop_900 --name seismic_cyclegan --model cycle_gan --phase test --no_dropout
