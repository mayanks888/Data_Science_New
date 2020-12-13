import os
import cv2
import numpy as np
thres_def=0.8
# input_folder = '/media/mayank_sati/DATA/datasets/one_shot_datasets/Farmington/images/new_farm_imageS_with_correct_box_n_qual/evaluation/Groundtruth'
input_folder = '/home/mayank_s/codebase/cplus_plus/ai/darknet_AlexeyAB/data/val_bdd_list.txt'

# output_folder = '/media/mayank_sati/DATA/datasets/one_shot_datasets/Farmington/images/new_farm_imageS_with_correct_box_n_qual/evaluation/Groundtruth_bet_32_96'
# output_folder = '/media/mayank_sati/DATA/datasets/one_shot_datasets/Farmington/images/new_farm_imageS_with_correct_box_n_qual/evaluation/Groundtruth_less_32'
# output_folder = '/media/mayank_sati/DATA/datasets/one_shot_datasets/Farmington/images/new_farm_imageS_with_correct_box_n_qual/evaluation/Groundtruth_less_32'

output_folder = '/home/mayank_s/codebase/cplus_plus/ai/darknet_AlexeyAB/data/val_bdd_list_modified.txt'
# output_folder = '/media/mayank_sati/DATA/datasets/one_shot_datasets/Farmington/images/new_farm_imageS_with_correct_box_n_qual/tenflow_api_result/result_at_250000_and_farm_added/box_size/prediction_bet_32_96'
# output_folder = '/media/mayank_sati/DATA/datasets/one_shot_datasets/Farmington/images/new_farm_imageS_with_correct_box_n_qual/tenflow_api_result/result_at_250000_and_farm_added/box_size/prediction_more_96'

new_path="/home/mayank_s/datasets/bdd/bdd100k_images/bdd100k/images/100k/val"
# for root, _, filenames in os.walk(input_folder):
#     if (len(filenames) == 0):
#         print("Input folder is empty")
#         # return 1
#     # time_start = time.time()
# #     for filename in filenames:
# #         # print("file : {fn}".format(fn=filename), '\n')
# #         file_path = (os.path.join(root, filename))
# #
# #         ###############################3333
#         labelname = (os.path.join(root, filename))
#         output_labelfilename = (os.path.join(output_folder, filename))

        # labelname = imagename + '.txt'
        # labelfilename = os.path.join(outDir, labelname)
bbox_cnt = 0
# if os.path.exists(labelname):
with open(output_folder, 'w') as k:
    with open(input_folder) as f:
        for (i, line) in enumerate(f):
            yolo_data = line.strip().split()
            # lenth=int(yolo_data[3])-int(yolo_data[1])
            # height=int(yolo_data[4])-int(yolo_data[2])
            linesplit=yolo_data[0].split("/")[-1]
            new_name= (os.path.join(new_path, linesplit))
            # lenth = int(yolo_data[3+1]) - int(yolo_data[1+1])
            # height = int(yolo_data[4+1]) - int(yolo_data[2+1])
            # area=int(lenth)*int(height)
            # # if (area<(9216) and area>(1024)):
            # # if area>=(9216):
            # if  area<=(1024) :
            #     print(labelname, area)
            # # if float(yolo_data[1])>=thres_def:
            # #     1
            #     k.write(" ".join([str(a) for a in yolo_data]) + '\n')
            k.write(new_name + '\n')
