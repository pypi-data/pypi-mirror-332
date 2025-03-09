# coding: utf-8
"""
检测指定文件夹，查询图片上所有人脸，裁剪为600x600大小图片，保存目录文件夹中
"""

import os
import cv2
import dlib

def start(folder_path='input_images', output_folder='output_folder'):
    # 初始化dlib的人脸检测器
    detector = dlib.get_frontal_face_detector()

    # 检查输入文件夹是否存在，如果不存在终止
    if not os.path.exists(folder_path):
        print(f"文件夹: {folder_path} 不存在")
        exit()

    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

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

                # 调整图片大小为500x500，使用更好的插值方法
                resized_img = cv2.resize(cropped_img, (600, 600), interpolation=cv2.INTER_CUBIC)

                # 预览处理后的图片
                cv2.imshow(f"Processed Image - {filename}_{i}", resized_img)
                cv2.waitKey(800)
                # key = cv2.waitKey(0)  # 等待按键事件
                # if key == ord('s'):  # 如果按下 's' 键，则保存图片
                # 保存处理后的图片
                base_name, ext = os.path.splitext(filename)
                output_filename = f"{base_name}_{i}{ext}"
                output_path = os.path.join(output_folder, output_filename)
                if ext.lower() == '.jpg':
                    cv2.imwrite(output_path, resized_img, [cv2.IMWRITE_JPEG_QUALITY, 100])
                else:
                    cv2.imwrite(output_path, resized_img)
                print(f"图片已保存: {output_path}")
                cv2.destroyAllWindows()  # 关闭预览窗口

