from setuptools import setup, find_packages
import os

# ฟังก์ชันโหลดไฟล์ README.md และ CHANGELOG.md อย่างปลอดภัย
def read_file(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    return ""

setup(
    name="cifer",
    version="1.0.1",
    author="Cifer.ai",
    author_email="support@cifer.ai",
    description="Federated Learning Client & Server API for AI Model Training",
    long_description=read_file("README.md") + "\n\n" + read_file("CHANGELOG.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/cifer-ai/cifer",
    packages=find_packages(),
    install_requires=[
        "requests",
        "tensorflow>=2.0",
        "numpy",
        "flask",  # สำหรับ API Server
        "uvicorn",  # สำหรับ API Server
        "pydantic",  # ตรวจสอบข้อมูล API
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],

    python_requires=">=3.6",
)
