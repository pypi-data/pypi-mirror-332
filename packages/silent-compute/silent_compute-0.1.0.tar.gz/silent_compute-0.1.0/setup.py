from setuptools import setup, find_packages

setup(
    name="silent-compute",                      
    version="0.1.0",                            
    author="Your Name",
    author_email="your.email@example.com",
    description="A dynamic multi-protocol FFI interface for Rust-based libraries",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aboggm/python-silent-compute",  
    packages=find_packages(include=["silent_compute", "silent_compute.sil_compute"]),
    include_package_data=True, 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",  # Custom license
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Security",
    ],
    python_requires=">=3.6",
    install_requires=[],
    license="Silence Laboratories’ Non-Commercial Use License Agreement (SLL)",  # Custom license
)
