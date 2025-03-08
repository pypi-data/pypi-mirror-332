from setuptools import setup, find_packages

setup(
    name="setup_user",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "setup-user=setup_user.setup_user:setup_user",
        ],
    },
    author="Sweetlolc",
    author_email="your.email@example.com",
    description="一键创建Linux用户并赋予sudo权限",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sweetlolc/setup_user",
    license="MIT",
)