#!/bin/bash

# Define an associative array where the key is the zip file name and the value is the download link
declare -A files
files["ax.zip"]="https://universe.roboflow.com/ds/6QplytrnGq?key=rgasaWx8XC"
files["drill.zip"]="https://universe.roboflow.com/ds/r3uU2PoFUv?key=GvoSfiy2gE"
files["electric_cigarette.zip"]="https://universe.roboflow.com/ds/aQ2hDkvHaP?key=RHpJF29TxO"
files["fire_extinguisher.zip"]="https://universe.roboflow.com/ds/nYUkoFe0D0?key=pAZmv5dWSs"
files["hammer.zip"]="https://universe.roboflow.com/ds/bFm7hZ6EQV?key=aZ9pHuuLjt"
files["knife.zip"]="https://universe.roboflow.com/ds/DbHbaA0ckD?key=64vTF7JgxE"
files["toothpaste.zip"]="https://universe.roboflow.com/ds/a9mFavizHU?key=hpBnNNV7CK"
files["spray.zip"]="https://universe.roboflow.com/ds/1EIcOwoihR?key=cpMwVRTcD7"
files["scissor.zip"]="https://universe.roboflow.com/ds/X77oZHiLls?key=e4zBdUh295"
files["thermometer.zip"]="https://universe.roboflow.com/ds/QlXpkfs7KC?key=WJIKElpFqC"
files["portable_charger.zip"]="https://universe.roboflow.com/ds/ouIt3Knox0?key=4qKrlfiJq0"
files["butane.zip"]="https://universe.roboflow.com/ds/XsDUYnH76t?key=14BQfTAJ2S"
files["driver.zip"]="https://universe.roboflow.com/ds/WeCgDSydwA?key=NKiTg2FgqG"
files["water.zip"]="https://universe.roboflow.com/ds/q4EZn2tRMO?key=UbWMKRKexL"
files["lighter.zip"]="https://universe.roboflow.com/ds/Gzseh5yMoq?key=RWA2GsMKnd"
files["liquid_soap.zip"]="https://universe.roboflow.com/ds/VfBn7fyhlR?key=gi4PxIS1kF"
files["cutter.zip"]="https://universe.roboflow.com/ds/5Gs6wWSp3B?key=uEaJmPufx4"

# Download and unzip each file
for file in "${!files[@]}"; do
    if [[ -n "${files[$file]}" ]]; then
        wget -O "$file" "${files[$file]}"
        folder_name="${file%.*}"
        mkdir -p "$folder_name"
        unzip -o "$file" -d "$folder_name"
    else
        echo "Skipping download for $file as the URL is empty."
    fi
done