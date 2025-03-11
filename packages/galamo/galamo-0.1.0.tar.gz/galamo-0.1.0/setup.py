from setuptools import setup, find_packages  # ✅ This must be at the top!

setup(
    name="galamo",
    version="0.1.0",
    author="Jashanpreet Singh Dingra",
    description="Galaxy Morphology Classification",
    long_description="Galamo is a Python package that utilizes deep learning to classify galaxy morphologies based on input images. It is designed for astronomers, researchers, and space enthusiasts who want an easy-to-use tool for automatic galaxy classification.",
    long_description_content_type="text/markdown",
    url="https://github.com/jdingra11/galamo",
    project_urls={
        "Model Download (Zenodo)": "https://doi.org/10.5281/zenodo.15002609"
    },
    packages=find_packages(),
    install_requires=["tensorflow", "numpy", "opencv-python", "joblib", "requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Astronomy"
    ],
    python_requires=">=3.6",
)
