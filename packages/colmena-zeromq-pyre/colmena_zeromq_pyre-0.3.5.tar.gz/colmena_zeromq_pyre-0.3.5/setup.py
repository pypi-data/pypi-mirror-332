try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
        name='colmena-zeromq-pyre',
        version='0.3.5',
        description='Python ZRE implementation',
        author='Philip Cummins',
        author_email='philip.cummins@bsc.es',
        url='http://www.github.com/philrhc/pyre/',
        packages=['pyre'],
        include_package_data=True,
        requires=['pyzmq', 'ipaddress'],
        install_requires=['pyzmq', 'ipaddress'],
        extra_requires={'deploy': ['bump2version', 'build'], 'test': ['nose']}
)
