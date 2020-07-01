#!/bin/bash
#SBATCH -n 80
#SBATCH --gres=gpu:v100:8
#SBATCH --time=1:00:00

/home/dm1/miniconda3/envs/opencv1/bin/python -u test_script_with_ambiguous_removal.py --data_dir='/home/dm1/shikhar/check_sandbox/testing_code/MoNuSAC_testing_data/Testing_images' --output_dir='/home/dm1/shikhar/check_sandbox/testing_code/model_output_final' --model_path='/home/dm1/shikhar/check_sandbox/testing_code/model_saved/model-33198.index' --ambi_path='/home/dm1/shikhar/check_sandbox/testing_code/MoNuSAC_testing_data/MoNuSAC_testing_ambiguous_regions' --img_ext='.tif' --gpu='0,1,2,3'
