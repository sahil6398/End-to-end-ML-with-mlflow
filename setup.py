from setuptools import setup, find_packages

__version__ = "0.1.0"
REPO_NAME  = 'End-to-end-ML-with-mlflow'
AUTHOR_USER_NAME = 'sahil'
SRC_REPO = 'ml_project'
AUTHOR_EMAIL = 'sahilt56yadav@gmail.com'

setup(
    name=SRC_REPO,              # Your package name
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A simple Python package for ml app",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    }
    
)