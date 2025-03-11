from setuptools import setup, find_packages

# 读取 requirements.txt 中的依赖项
def parse_requirements(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line and not line.startswith('#')]

requirements = parse_requirements('requirements.txt')

setup(
    name='otauto',
    version='0.1.1',
    author='ordtie',
    author_email='283044916@qq.com',
    description='vnc窗口操作工具',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=requirements,  # 引用从 requirements.txt 中读取的依赖
)