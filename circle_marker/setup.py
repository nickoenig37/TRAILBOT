import os
from glob import glob
from setuptools import setup

package_name = 'circle_marker'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'marker'), glob('marker/*.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='koener',
    maintainer_email='nic.koenig37@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'circle_marker_node = circle_marker.circle_marker_node:main'
        ],
    },
)
