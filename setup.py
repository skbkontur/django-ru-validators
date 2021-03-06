from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="django_ru_validators",
    version="1.7.0",
    description="Django RU validators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    install_requires=["Django>=2.1"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    url="https://github.com/zhelyabuzhsky/django-ru-validators",
    packages=find_packages(include=["django_ru_validators", "django_ru_validators.*"]),
    author="Ilya Zhelyabuzhsky",
    author_email="zhelyabuzhsky@icloud.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.1",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)
