from setuptools import find_packages, setup

package_name = 'vision_detector'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='second-code',
    maintainer_email='contact.ashi.gupta@gmail.com',
    description='ROS2 YOLOv8 perception node',
    license='Apache License 2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'camera_viewer = vision_detector.camera_viewer:main',
            'yolo_detector = vision_detector.yolo_detector:main',
        ],
    },
)
