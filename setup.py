from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(name='trajectorytools',
      version='0.3-alpha.3',
      description='A tool to study 2D trajectories',
      long_description=long_description,
      url='http://github.com/fjhheras/trajectorytools',
      author='Francisco J.H. Heras',
      author_email='fjhheras@gmail.com',
      license='GPL',

      install_requires=['MiniballCpp',
                        'matplotlib',
                        'scikit-learn',
                        'scipy'],

      packages=['trajectorytools'],
      package_data={'trajectorytools': ['data/*.npy']},
      include_package_data=True,
      zip_safe=False,

      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Physics',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities'
      ],

      )
