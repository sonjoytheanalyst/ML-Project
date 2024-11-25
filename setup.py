import setuptools

__version__ = "0.0.0"

# Metadata variables
REPO_NAME = "ML-Project"
AUTHOR_USER_NAME = "sonjoytheanalyst"
SRC_REPO = "src.winequality"
AUTHOR_EMAIL = "sonjoytheanalyst@gmail.com"

# Read long description from README.md (or provide a string directly)
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A small python package for ML app."

# Setup function
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ML app",
    long_description=long_description,  # Now defined
    long_description_content_type="text/markdown",  # Correct argument
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
