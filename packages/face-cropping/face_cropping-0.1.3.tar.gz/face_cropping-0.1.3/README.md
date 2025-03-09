# 从源文件夹中获取所有图片，截取人脸后存入目标文件夹

## 一、安装：

pip install face-cropping

## 二、使用

### 方式一：

import face-cropping

folder_path='input_images'

output_folder='output_folder'

start(folder_path, output_folder)

### 方式二：

import face-cropping

folder_path='input_images'

output_folder='output_folder'

face_landmarks='[model/shape_predictor_68_face_landmarks.dat](https://gitee.com/ren3016 "下载dat文件")'

start68(folder_path, output_folder, face_landmarks)
