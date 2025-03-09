from setuptools import setup, find_packages

setup(
    name="django-reality-polls",
    version="0.1.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "Django>=5.1",
    ],
    python_requires=">=3.10",
    author="P.Yaswanth Reddy",
    author_email="yaswanthreddypanem@gmail.com",
    description="A Django app to conduct web-based polls.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yaswanth33-ui/django-reality-polls",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 5",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
