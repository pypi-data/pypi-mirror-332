from setuptools import setup, find_packages

setup(
    name="fourchains_test_unique",  # 고유한 이름으로 변경
    version="0.1.2",  # 버전도 확인
    author="fourchains",
    author_email="fourchains.work@gmail.com",
    description="A sample PyPI package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fourchainswork/fourchains",  # 깃허브 URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10.15",
)
