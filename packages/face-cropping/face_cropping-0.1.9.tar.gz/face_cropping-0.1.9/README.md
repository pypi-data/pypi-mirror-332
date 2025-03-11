# 从源文件夹中获取所有图片，截取人脸后存入目标文件夹

## 一、安装：

pip install face-cropping

## 二、使用

### 方式1：

import face-cropping as f

folder_path='input_images'  #必填

output_folder='output_folder' #必填

face_landmarks='[./model/shape_predictor_68_face_landmarks.dat](https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2 "下载dat文件")' #选填

f.start(folder_path, output_folder, face_landmarks)

### 方式2：

import face-cropping as f

folder_path='input_images'

output_folder='output_folder'

f.start_simple(folder_path, output_folder)



下载地址1： [https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2](https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2)

下载地址2： [http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

dlib下载： [https://dlib.net/files/](https://dlib.net/files/)

shape_predictor_68_face_landmarks.dat‌是一个已经训练好的人脸特征点检测器，主要用于检测人脸上的68个关键点。这个模型是由dlib库提供的，广泛用于面部特征标记和面部表情分析等领域。
