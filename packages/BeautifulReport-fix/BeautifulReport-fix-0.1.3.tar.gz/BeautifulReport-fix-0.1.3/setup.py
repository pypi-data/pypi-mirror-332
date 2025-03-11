import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="BeautifulReport-fix",
    version="0.1.3",
    author="xiaomaipian",
    author_email="ice_emp@163.com",
    description="unittest自动化测试的可视化报告模板-修复源版本",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xiaomaipian/BeautifulReport-fix",
    packages=['BeautifulReport'],
    package_data={'BeautifulReport': ['template/*.*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
