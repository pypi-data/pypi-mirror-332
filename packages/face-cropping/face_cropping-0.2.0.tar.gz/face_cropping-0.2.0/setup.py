# python setup.py sdist bdist_wheel
# twine upload dist/* -u __token__ -p pypi-AgEIch....

from setuptools import find_packages, setup

setup(
    name="face-cropping",
    version='0.2.0',
    author="ren3016",
    author_email="ren3016@qq.com",
    description='face-cropping',
    long_description_content_type="text/markdown",
    long_description = open("README.md", encoding='utf-8').read(),
    url="https://gitee.com/ren3016/face_cropping",
    # package_data={"your_project": ["*.txt", "data/*.json"]},  # 包含非代码文件‌:ml-citation{ref="2,5" data="citationList"}
    # include_package_data=True,  # 自动包含 data 文件夹
    # data_files=[("model", ["model/shape_predictor_68_face_landmarks.dat"])],  # 显式指定要包含的文件
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'dlib'
    ],
    keywords=[
    "face_cropping",
    "photo",
    "识别人脸",
    "裁切人脸"
    ],
    project_urls={
        "Documentation": "https://gitee.com/ren3016/face_cropping",
        "Source Code": "https://gitee.com/ren3016/face_crop_code",
        "Issues": "https://gitee.com/ren3016/face_crop_code/issues"
    },

    python_requires=">=3.8",  # Python版本要求
    classifiers=[  # 分类元数据‌:ml-citation{ref="5,6" data="citationList"}
        "Programming Language :: Python :: 3.8", # 声明这个包是用 ​Python 3 编写的。
        "License :: OSI Approved :: MIT License", # 声明这个包采用 ​MIT 许可证，且该许可证已被 OSI（开放源代码促进会）正式批准。
        "Operating System :: OS Independent" # 声明这个包是 ​跨平台的，可以在任何操作系统（Windows/macOS/Linux）上运行。
    ],
)
