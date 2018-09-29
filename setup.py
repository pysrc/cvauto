from setuptools import setup, find_packages

setup(
    name="cvauto",
    version="0.0.1",
    keywords=["automation", "GUI", "opencv", "rpa"],
    description="It's a gui automation pkg, and base on opencv, just a simple picture match.",
    license="MIT",
    author="L.Chen",
    author_email="1570184051@qq.com",
    packages=find_packages(),
    install_requires=["pillow>=5.2.0", "pyautogui>=0.9.38",
                      "numpy>=1.15.1", "opencv-python>=3.4.3.18"],
    platforms="any",
    url="https://github.com/pysrc/cvauto",
    zip_safe=False,
    package_data={
        "": ["*.dll", "*.pyd", "*.so"]
    }
)
