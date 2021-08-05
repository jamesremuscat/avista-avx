from setuptools import setup, find_packages


setup(
    name='avista_avx',
    version='0.0.1',
    description='Avista bridge component for avx',
    author='James Muscat',
    author_email='jamesremuscat@gmail.com',
    url='https://github.com/jamesremuscat/avista-avx',
    packages=find_packages('src', exclude=["*.tests"]),
    package_dir={'': 'src'},
    long_description="""\
    An avx device that bridges to an avista system. Power-on and power-off
    are propagated from avx to avista. Requires an HTTP Caller endpoint
    configured on the avista router.
    """,
    install_requires=["avx", "requests"]
)
