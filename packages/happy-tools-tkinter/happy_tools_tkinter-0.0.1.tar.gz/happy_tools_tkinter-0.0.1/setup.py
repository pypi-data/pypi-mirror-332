from setuptools import setup, find_namespace_packages


def _read(f):
    """
    Reads in the content of the file.
    :param f: the file to read
    :type f: str
    :return: the content
    :rtype: str
    """
    return open(f, 'rb').read()


setup(
    name="happy_tools_tkinter",
    description="tkinter user interface for the happy-tools library.",
    long_description=(
        _read('DESCRIPTION.rst') + b'\n' +
        _read('CHANGES.rst')).decode('utf-8'),
    url="https://github.com/wairas/happy-tools-tkinter",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3',
    ],
    license='MIT License',
    install_requires=[
        "happy_tools_core>0.0.1",
        "pygubu==0.31",
        "redis",
        "ttkSimpleDialog==1.2.1",
        "fast-opex>=0.0.4",
        "orjson",
        "shapely",
        "scikit-learn",
        "matplotlib",
    ],
    package_dir={
        '': 'src'
    },
    package_data={
        "happy.tkinter.envi_viewer": ["*.ui"],
        "happy.tkinter.data_viewer": ["*.ui"],
        "happy.tkinter.raw_checker": ["*.ui"],
    },
    packages=find_namespace_packages(where='src'),
    entry_points={
        "console_scripts": [
            "envi-viewer=happy.tkinter.envi_viewer.viewer:sys_main",  # deprecated
            "happy-envi-viewer=happy.tkinter.envi_viewer.viewer:sys_main",
            "happy-data-viewer=happy.tkinter.data_viewer.viewer:sys_main",
            "happy-raw-checker=happy.tkinter.raw_checker.checker:sys_main",
        ],
    },
    version="0.0.1",
    author='Peter Reutemann',
    author_email='fracpete@waikato.ac.nz',
)
