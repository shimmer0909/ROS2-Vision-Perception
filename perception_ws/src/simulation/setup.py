from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'simulation'

setup(
    name=package_name,
    version='0.0.0',
    # packages=find_packages(exclude=['test']),
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        (os.path.join('share', package_name, 'launch'),
         glob('launch/*.launch.py')),
         
        (os.path.join('share', package_name, 'worlds'),
         glob('worlds/*.world')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='second-code',
    maintainer_email='contact.ashi.gupta@gmail.com',
    description='Simulation package for AWS Small House World',
    license='Apache License 2.0',
    tests_require=['pytest'],
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [],
    },
)
