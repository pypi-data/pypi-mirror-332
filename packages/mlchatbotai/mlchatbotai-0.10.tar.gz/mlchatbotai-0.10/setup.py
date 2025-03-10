from setuptools import setup, find_packages

setup(
    name="mlchatbotai",
    version="0.10",
    packages=find_packages(),  # Automatically find all sub-packages
    include_package_data=True,  # Ensures non-Python files (models, JSON) are included
    install_requires=[
        "numpy",
        "nltk",
        "keras",
        "tensorflow",
        "pyttsx3"
    ],
    author="Shibam Das",
    author_email="shibomdas121@gmail.com",
    description="A simple AI chatbot package",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ShibamDas007/MLChatbotAI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
