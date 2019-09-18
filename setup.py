import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    "opencv-python",
    "matplotlib",
    "numpy",
    "torch",
    "chumpy @ git+ssh://git@github.com/hassony2/chumpy"]

setuptools.setup(
    name="hrnet",
    version="0.0.1",
    author="Forked by Rawal Khirodkar",
    author_email="rawalkhirodkar@gmail.com",
    python_requires=">=3.5.0",
    install_requires=REQUIREMENTS,
    description="The fork makes the hrnet pose estimation repository installable",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rawalkhirodkar/deep-high-resolution-net.pytorch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)

import pdb; pdb.set_trace()
