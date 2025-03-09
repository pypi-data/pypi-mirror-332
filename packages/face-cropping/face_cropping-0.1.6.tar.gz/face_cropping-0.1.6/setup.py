# python setup.py sdist bdist_wheel
# twine upload dist/* -u __token__ -p pypi-AgEIch....

from setuptools import find_packages, setup

setup(
    name="face-cropping",
    version='0.1.6',
    author="ren3016",
    author_email="ren3016@qq.com",
    description='face-cropping',
    long_description_content_type="text/markdown",
    long_description = open("README.md", encoding='utf-8').read(),
    url="https://github.com/ren3016/face_cropping",
    # package_data={"your_project": ["*.txt", "data/*.json"]},  # 包含非代码文件‌:ml-citation{ref="2,5" data="citationList"}
    # include_package_data=True,  # 自动包含 data 文件夹
    # data_files=[("model", ["model/shape_predictor_68_face_landmarks.dat"])],  # 显式指定要包含的文件
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'dlib'
    ],
    keywords=['face_cropping', 'photo'],
    python_requires=">=3.8",  # Python版本要求
    classifiers=[  # 分类元数据‌:ml-citation{ref="5,6" data="citationList"}
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
