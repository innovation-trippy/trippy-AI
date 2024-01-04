#!/bin/bash

# 대상 폴더 리스트
folders=("ax" "drill" "electric_cigarette" "fire_extinguisher" "hammer" "knife" "toothpaste" "spray" "scissor" "thermometer"
        "portable_charger" "butane" "driver" "water" "lighter" "liquid_soap" "cutter")

# 각 폴더에 대해 작업 수행
for folder in "${folders[@]}"; do
    # 'train' 및 'valid' 폴더의 'images'와 'labels' 이동
    mv "$folder/train/images/"* data_total/train/images/
    mv "$folder/train/labels/"* data_total/train/labels/
    mv "$folder/valid/images/"* data_total/valid/images/
    mv "$folder/valid/labels/"* data_total/valid/labels/

    # 'test' 폴더가 있는 경우에만 'test' 폴더의 'images'와 'labels' 이동
    if [ -d "$folder/test" ]; then
        mv "$folder/test/images/"* data_total/test/images/
        mv "$folder/test/labels/"* data_total/test/labels/
    fi
done