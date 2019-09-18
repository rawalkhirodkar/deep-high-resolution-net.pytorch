import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# ----------------------------------
from distutils.core import setup
from distutils.extension import Extension

try:
    from Cython.Distutils import build_ext
except ImportError:
    use_cython = False
else:
    use_cython = True

cmdclass = {}
ext_modules = []


if use_cython:
    ext_modules += [
        Extension("mypackage.mycythonmodule", ["cython/mycythonmodule.pyx"]),
    ]
    cmdclass.update({'build_ext': build_ext})
else:
    ext_modules += [
        Extension("mypackage.mycythonmodule", ["cython/mycythonmodule.c"]),
    ]

# ----------------------------------


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
    packages=[package for package in setuptools.find_packages() if package.startswith('hrnet')],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    # package_data={'hrnet': ['nms/cpu_nms.pyx', 'nms/gpu_nms.cu', 'nms/gpu_nms.hpp', 'nms/gpu_nms.pyx', 'nms/nms_kernel.cu']},
    package_data={'hrnet': ['nms/*',]},

)

