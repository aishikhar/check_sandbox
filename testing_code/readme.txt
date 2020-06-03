To obtain instance-masks from the trained model on the MoNuSAC test data in the required challenge format:

- Ensure library requirements mentioned in requirements.txt are installed
- Download MoNuSAC test-data & trained model
- Modify data_dir, output-dir, model-path to reflect MoNuSAC test data, desired output path, & downloaded trained model path (.index file) respectively.

Run the below script as:

python test_script.py --data_dir --output_dir --model_path --img_ext --gpu

Getting Started

Install the required libraries before using this code. Please refer to requirements.txt