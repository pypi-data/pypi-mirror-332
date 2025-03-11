# coding: utf-8
"""
检测指定文件夹，查询图片上所有人脸，裁剪为600x600大小图片，保存目录文件夹中
"""

import os
import cv2
import dlib
# from pkg_resources import resource_filename

def start(
    folder_path: str = 'input_images',
    output_folder: str = 'output_folder',
    face_landmarks: str = ''
    ) -> None:
    """
    初始化图像处理环境并开始面部特征点检测流程

    主要功能：
    1. 验证输入输出目录的有效性
    2. 加载预训练的人脸特征点检测模型
    3. 遍历指定文件夹内的所有图像文件进行人脸检测
    4. 将检测结果保存至输出目录

    参数说明：
    - folder_path (str): 待处理的原始图像存放路径，默认为'input_images'
    - output_folder (str): 处理后图像保存路径，默认为'output_folder'
    - face_landmarks (dlib.face_landmark_detector, optional): 
        可选参数，用于指定具体的人脸特征点检测模型。若未提供，则自动加载默认模型
        dlib已经训练好的人脸特征点检测器，主要用于检测人脸上的68个关键点：shape_predictor_68_face_landmarks.dat

    返回值：
    - None: 无直接返回值，但会在指定输出目录生成处理结果

    注意事项：
    1. 确保输入目录存在且包含有效图像文件
    2. 输出目录如果不存在会自动创建
    3. 支持的图像格式包括：jpg/png/bmp等常见格式
    """

    # 检查输入文件夹是否存在，如果不存在终止
    if not os.path.exists(folder_path):
        print(f"输入文件夹: {folder_path} 不存在")
        exit()

    # 检查输出文件夹是否存在，如果不存在终止
    if not os.path.exists(output_folder):
        print(f"输出文件夹: {output_folder} 不存在")
        exit()
    if not face_landmarks:
        print(f"shape_predictor_68_face_landmarks.dat 未指定")
        print(f"下载地址1：https://github.com/davisking/dlib-models/blob/master/shape_predictor_68_face_landmarks.dat.bz2")
        print(f"将不显示68个人脸检测点")
        # exit()
    if face_landmarks:
        # 检查人脸特征点检测器是否存在，如果不存在终止
        if not os.path.exists(face_landmarks):
            print(f" {face_landmarks} 不存在")
            exit()

    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 初始化dlib的人脸检测器
    detector = dlib.get_frontal_face_detector()

    if face_landmarks:
        # # 加载预训练的人脸特征点检测器模型
        predictor_path = face_landmarks  # 请替换为实际路径
        # 获取数据文件的绝对路径
        # predictor_path = resource_filename(__name__, "model/shape_predictor_68_face_landmarks.dat")
        predictor = dlib.shape_predictor(predictor_path)
    ii = 1
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        print(f"{ii} 处理图片：{filename}")
        # 只处理jpg和png和bmp格式的图片
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.png') or filename.lower().endswith('.bmp'):
            img_path = os.path.join(folder_path, filename)
            img = cv2.imread(img_path)
            if img is None:
                print(f"无法读取图片: {img_path}")
                continue
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # 使用dlib检测人脸
            rects = detector(gray, 0)

            for i, rect in enumerate(rects):
                x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()

                # 计算裁剪区域
                x = max(0, x - w // 4)
                y = max(0, y - h // 4)
                w = min(img.shape[1] - x, w * 3 // 2)
                h = min(img.shape[0] - y, h * 3 // 2)

                # 裁剪图片
                cropped_img = img[y:y + h, x:x + w]

                # 调整图片大小为600x600，使用更好的插值方法
                resized_img = cv2.resize(cropped_img, (600, 600), interpolation=cv2.INTER_CUBIC)

                # 保存处理后的图片(不包含68节点)
                base_name, ext = os.path.splitext(filename)
                output_filename = f"{base_name}_{i}{ext}"
                output_path = os.path.join(output_folder, output_filename)
                if ext.lower() == '.jpg':
                    cv2.imwrite(output_path, resized_img, [cv2.IMWRITE_JPEG_QUALITY, 100])
                else:
                    cv2.imwrite(output_path, resized_img, [cv2.IMWRITE_JPEG_QUALITY, 100])
                    # cv2.imwrite(output_path, resized_img)
                print("\t",f"{ii}-{i}",f"-> {output_path}")

                # 复制一份用于预览，在预览图上绘制节点
                preview_img = resized_img.copy()

                if face_landmarks:
                    # 检测人脸的 68 个特征点
                    shape = predictor(gray, rect)
                    for j in range(68):
                        x_point = shape.part(j).x - x
                        y_point = shape.part(j).y - y
                        # 因为裁剪和缩放，需要调整特征点坐标
                        x_point = int((x_point / cropped_img.shape[1]) * 600)
                        y_point = int((y_point / cropped_img.shape[0]) * 600)
                        cv2.circle(preview_img, (x_point, y_point), 2, (0, 255, 0), -1)
                    
                # 预览处理后的图片
                cv2.imshow(f"Processed Image - {filename}_{i}", preview_img)
                cv2.waitKey(600) # 等待 n 秒后关闭当前窗口
                cv2.destroyAllWindows()  # 关闭预览窗口
        ii += 1
    if ii>1:
        print('处理结束',"\n")
    else:
        print(folder_path,'中没有找到图片',"\n")

