from glob import glob 
import os
import cv2
import numpy as np
from scipy import io as sio
import matplotlib.pyplot as plt
from IPython.display import clear_output
import sys
data_dir = None
output_dir = None
model_path = None
img_ext = None
ambi_path = None

data_dir = '/home/dm1/shikhar/check_sandbox/testing_code/test_output_1' # Predicted without Ambigous Removal
output_dir = '/home/dm1/shikhar/check_sandbox/testing_code/overlay_output_withoutremoval' # Staging - Overlay Predicted & Ambiguous
ambi_path = '/home/dm1/shikhar/check_sandbox/testing_code/MoNuSAC_testing_data/MoNuSAC_testing_ambiguous_regions'

#file_list = glob.glob('%s/*%s' % (data_dir, img_ext))
#file_list.sort() # ensure same order
#if(not file_list):
# print('No Images found in data_dir! Check script arg-paths') 
# Create Output Directory
#rm_n_mkdir(output_dir)       
# Expecting MoNuSAC's input data directory tree (Patient Name -> Image Name -> )

if not os.path.isdir(output_dir):
    os.makedirs(output_dir)
os.chdir(output_dir)

patients = glob(data_dir + '/*')
print(len(patients))

for patient_loc in patients:
    patient_name = patient_loc[len(data_dir)+1:]#Patient name
    print('Patient name: ',patient_name)
    
    ## To make patient's name directory in the destination folder
    try:
        os.mkdir(patient_name)
    except OSError:
        print ("\n Creation of the patient's directory %s failed" % patient_name,  flush=True)

    sub_images = glob(str(patient_loc) + '/*')
    for sub_image_loc in sub_images:
        sub_image_name = sub_image_loc[len(data_dir)+len(patient_name)+1:]        
        print('Sub image name: ',sub_image_name)
        
        ## To make sub_image directory under the patient's folder
        sub_image = './'+patient_name + sub_image_name #Destination path
        
        try:
            os.mkdir(sub_image)
            os.mkdir(sub_image + '/Epithelial')
            os.mkdir(sub_image + '/Lymphocyte')
            os.mkdir(sub_image + '/Macrophage')
            os.mkdir(sub_image + '/Neutrophil')
        except OSError:
            print ("\n Creation of the patient's directory %s failed" % sub_image)
        

        image_name = sub_image_loc
        print(sub_image_loc)
        e_image = sio.loadmat(sub_image_loc + '/Epithelial/maskorempty.mat')['n_ary_mask']
        l = sio.loadmat(sub_image_loc + '/Lymphocyte/maskorempty.mat')['n_ary_mask']
        m = sio.loadmat(sub_image_loc + '/Macrophage/maskorempty.mat')['n_ary_mask']
        n = sio.loadmat(sub_image_loc + '/Neutrophil/maskorempty.mat')['n_ary_mask']

    
        # Read Ambiguous Region mask if any
        ambi_mask_final = None
        full_ambi_path = ambi_path + '/' + patient_name + '/' + sub_image_name + '/Ambiguous' 
        print('\tAmbi Path: ',full_ambi_path)
        ambi_masks = glob(full_ambi_path+'/*')
        if(ambi_masks):
            try:
                ambi_mask_final = cv2.imread(ambi_masks[0])
                #print('Ambiguous Mask Found: ',ambi_mask_final.shape)
            
                # START CHANGES 
                gray = cv2.cvtColor(ambi_mask_final, cv2.COLOR_BGR2GRAY)
                count, ambi = cv2.connectedComponents(gray)                
                
                # Show Overlay of Prediction & Ambi
                plt.imshow(e_image, 'gray', interpolation='none')
                plt.imshow(ambi, 'Paired', interpolation='none', alpha=0.7)
                plt.savefig(sub_image + '/Epithelial' + '/fig.png')

                plt.imshow(l, 'gray', interpolation='none')
                plt.imshow(ambi, 'Paired', interpolation='none', alpha=0.7)
                plt.savefig(sub_image + '/Lymphocyte' + '/fig.png')

                plt.imshow(m, 'gray', interpolation='none')
                plt.imshow(ambi, 'Paired', interpolation='none', alpha=0.7)
                plt.savefig(sub_image + '/Macrophage' + '/fig.png')

                plt.imshow(n, 'gray', interpolation='none')
                plt.imshow(ambi, 'Paired', interpolation='none', alpha=0.7)
                plt.savefig(sub_image + '/Neutrophil' + '/fig.png')
        
                '''#print('Prediction: ',np.unique(pred_inst))
                plt.imshow(pred_inst)
                plt.show()
                #print('Prediction Cleaned: ',np.unique(prediction_cleaned))
                plt.imshow(prediction_cleaned)
                plt.show()
                #print('Ambiguous: ',np.unique(ambi))
                plt.imshow(ambi)
                plt.show()'''
                #print('Removed are: ', set(list(np.unique(pred_inst))) - set(list(np.unique(prediction_cleaned))) )
                # ========
            except Exception as e:
                print(e)
        else:
            print('\n\t # No Ambiguous Masks for this image: ', full_ambi_path)
            plt.imshow(e_image, 'gray', interpolation='none')
            plt.savefig(sub_image + '/Epithelial' + '/fig.png')

            plt.imshow(l, 'gray', interpolation='none')
            plt.savefig(sub_image + '/Lymphocyte' + '/fig.png')

            plt.imshow(m, 'gray', interpolation='none')
            plt.savefig(sub_image + '/Macrophage' + '/fig.png')

            plt.imshow(n, 'gray', interpolation='none')
            plt.savefig(sub_image + '/Neutrophil' + '/fig.png')

'''        # Write Instance Maps based on their Classes/Labels to the folders
        for class_id in range(1,self.nr_types):
            separated_inst = pred_inst.copy()
            separated_inst[pred_inst_type[separated_inst-1]!=[class_id]] = 0
            # Create directory for each label
            label = class_id_mapping[class_id]
            sub_path = sub_image+'/'+label
            try:
                os.mkdir(sub_path)
            except OSError:
                print ("Creation of the directory %s failed" % label)
            else:
                print ("Successfully created the directory %s " % label)

            sio.savemat(sub_path +'/maskorempty.mat', 
                {'n_ary_mask'  :  separated_inst})'''