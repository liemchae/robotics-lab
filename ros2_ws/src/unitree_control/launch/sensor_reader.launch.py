from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='unitree_control',
            executable='sensor_reader',
            name='sensor_reader',
            output='screen',
            parameters=[
                {'publish_rate': 50},
                {'unitree_port': '/dev/ttyUSB0'},
                {'unitree_baudrate': 115200},
            ],
        ),
    ])
