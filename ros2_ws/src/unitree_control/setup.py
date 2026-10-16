from setuptools import find_packages, setup

package_name = 'unitree_control'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/sensor_reader.launch.py']),
        ('share/' + package_name + '/config', ['config/unitree_config.yaml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Chaehyuen Liem',
    author_email='chaehyuen@gmail.com',
    maintainer='Chaehyuen Liem',
    maintainer_email='chaehyuen@gmail.com',
    description='Unitree humanoid control package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_reader = unitree_control.sensor_reader:main',
            'walk_controller = unitree_control.walk_controller:main',
        ],
    },
)
