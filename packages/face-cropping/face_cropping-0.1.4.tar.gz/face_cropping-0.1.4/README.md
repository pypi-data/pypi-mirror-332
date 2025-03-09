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

face_landmarks='[./model/shape_predictor_68_face_landmarks.dat](https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2 "下载dat文件")'

下载地址1：[https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2](https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2)

下载地址2：[http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

[
    https://dlib.net/files/](https://dlib.net/files/)

start68(folder_path, output_folder, face_landmarks)
