# setup.py

from setuptools import setup, find_packages

setup(
    name='audio_sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'dashscope',
        'requests',
        'python-docx'  # 如果需要，添加其他依赖
    ],
    author='zhangying',
    author_email='imuzhangying@163.com',
    description='A Python SDK for audio transcription',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/audio_sdk',  # 替换为你的项目主页
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)