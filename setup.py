from setuptools import setup, find_packages

setup(
    name="lda",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "aqctl_lda = lda.aqctl_lda:main",
        ],
    },
)
