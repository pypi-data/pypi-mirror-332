# coding: utf-8
"""
检测指定文件夹，查询图片上所有人脸，裁剪为600x600大小图片，保存目录文件夹中
"""

import os
import cv2
import dlib
from pkg_resources import resource_filename

def start68(folder_path='input_images', output_folder='output_folder', face_landmarks=''):

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
        exit()

    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 初始化dlib的人脸检测器
    detector = dlib.get_frontal_face_detector()

    # # 加载预训练的人脸特征点检测器模型
    predictor_path = face_landmarks  # 请替换为实际路径
    # 获取数据文件的绝对路径
    # predictor_path = resource_filename(__name__, "model/shape_predictor_68_face_landmarks.dat")
    predictor = dlib.shape_predictor(predictor_path)

    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.png'):  # 只处理jpg和png格式的图片
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
                    cv2.imwrite(output_path, resized_img)
                # print(f"图片已保存: {output_path}")

                # 复制一份用于预览，在预览图上绘制节点
                preview_img = resized_img.copy()

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
                cv2.waitKey(800) # 等待 n 秒后关闭当前窗口
                cv2.destroyAllWindows()  # 关闭预览窗口
    print('处理结束')

