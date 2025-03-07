from setuptools import setup, find_packages 

setup(
    name='CharNetOCR',
    version='1.0.0',
    packages=find_packages(include=["CharNetOCR", "CharNetOCR.*"]),
    include_package_data=True,
    package_data={
        "CharNetOCR": ["models/*.pt"]  # Include YOLO model weights
    },
    install_requires=[
        'ultralytics',
        'opencv-python',
        'numpy'
    ]
)