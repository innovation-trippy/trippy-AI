import os

# 사물 이름과 인덱스를 매핑하는 딕셔너리
object_to_index = {
    'ax': 0, 'drill': 1, 'electric_cigarette': 2, 'fire_extinguisher': 3,
    'hammer': 4, 'knife': 5, 'toothpaste': 6, 'spray': 7, 'scissor': 8,
    'thermometer': 9, 'portable_charger': 10, 'butane': 11, 'driver': 12,
    'water': 13, 'lighter': 14, 'liquid_soap': 15, 'cutter': 16
}

base_folder_path = '/shared/home/sw_innov03/junhan_new2/original_data'
old_class_index = 0

# 각 사물에 대한 작업을 반복
for object_name, new_class_index in object_to_index.items():
    for folder_type in ['train', 'valid', 'test']:
        label_folder_path = os.path.join(base_folder_path, object_name, folder_type, 'labels')

        # 폴더가 존재하는지 확인
        if not os.path.exists(label_folder_path):
            continue  # 폴더가 없으면 해당 폴더에 대한 처리를 건너뜁니다.

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