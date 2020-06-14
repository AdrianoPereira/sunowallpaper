from setuptools import setup, find_packages


setup(
    name="sunowallpaper",
    version="1.0.0",
    url="http://github.com/AdrianoPereira/sunowallpaper",
    author="Adriano Almeida",
    author_email="adriano.almeida@inpe.br",
    license="MIT",
    description="Set wallpaper with image of sun near real time",
    install_requires=["appdirs", "pillow", "python-dateutil"],
    packages=find_packages(),
)
