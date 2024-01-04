import os

label_folder_path = '/shared/home/sw_innov03/junhan_new2/aug_data_real/train/labels'
# label_folder_path = '/shared/home/sw_innov03/junhan_new2/awl/valid/labels'
# label_folder_path = '/shared/home/sw_innov03/junhan_new2/awl/test/labels'
# 0->16 1->14 2->10 3->8 4->7 5->6 6->13

old_class_index = 6
new_class_index = 13

for filename in os.listdir(label_folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(label_folder_path, filename)
        
        with open(file_path, 'r') as file:
            lines = file.readlines()

        modified_lines = []
        for line in lines:
            parts = line.strip().split()
            class_index = int(parts[0])
            if class_index == old_class_index:
                parts[0] = str(new_class_index)
            modified_lines.append(' '.join(parts))

        with open(file_path, 'w') as file:
            for line in modified_lines:
                file.write(line + '\n')

                
label_folder_path = '/shared/home/sw_innov03/junhan_new2/aug_data_real/valid/labels'

for filename in os.listdir(label_folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(label_folder_path, filename)
        
        with open(file_path, 'r') as file:
            lines = file.readlines()

        modified_lines = []
        for line in lines:
            parts = line.strip().split()
            class_index = int(parts[0])
            if class_index == old_class_index:
                parts[0] = str(new_class_index)
            modified_lines.append(' '.join(parts))

        with open(file_path, 'w') as file:
            for line in modified_lines:
                file.write(line + '\n')
                
# label_folder_path = '/shared/home/sw_innov03/junhan_new2/thermometer_new/test/labels'
# for filename in os.listdir(label_folder_path):
#     if filename.endswith('.txt'):
#         file_path = os.path.join(label_folder_path, filename)
        
#         with open(file_path, 'r') as file:
#             lines = file.readlines()

#         modified_lines = []
#         for line in lines:
#             parts = line.strip().split()
#             class_index = int(parts[0])
#             if class_index == old_class_index:
#                 parts[0] = str(new_class_index)
#             modified_lines.append(' '.join(parts))

#         with open(file_path, 'w') as file:
#             for line in modified_lines:
#                 file.write(line + '\n')