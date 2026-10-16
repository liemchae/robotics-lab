"""
Unitree Sensor Reader Node

Reads IMU, joint encoders, foot pressure, and battery data from Unitree humanoid.
Publishes sensor data to ROS2 topics for monitoring and control.

Topics published:
  - /unitree/imu: sensor_msgs/Imu
  - /unitree/joint_state: sensor_msgs/JointState
  - /unitree/foot_force: std_msgs/Float32MultiArray
  - /unitree/battery: std_msgs/Float32
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu, JointState
from std_msgs.msg import Float32, Float32MultiArray, Header
import numpy as np
import time
from typing import Dict, List


class UnitreeSensorReader(Node):
    """
    Reads sensor data from Unitree humanoid and publishes to ROS2.
    
    Week 1-2 milestone: Establish real-time sensor acquisition.
    """
    
    def __init__(self):
        super().__init__('unitree_sensor_reader')
        
        # Publishers
        self.imu_pub = self.create_publisher(Imu, '/unitree/imu', 10)
        self.joint_state_pub = self.create_publisher(JointState, '/unitree/joint_state', 10)
        self.foot_force_pub = self.create_publisher(Float32MultiArray, '/unitree/foot_force', 10)
        self.battery_pub = self.create_publisher(Float32, '/unitree/battery', 10)
        
        # Parameters
        self.declare_parameter('publish_rate', 50)  # Hz
        self.declare_parameter('unitree_port', '/dev/ttyUSB0')
        self.declare_parameter('unitree_baudrate', 115200)
        
        publish_rate = self.get_parameter('publish_rate').value
        
        # Create timer
        self.timer = self.create_timer(1.0 / publish_rate, self.sensor_callback)
        
        # Unitree connection (placeholder - implement actual SDK integration)
        self.unitree = None
        self.joint_names = [
            'FL_hip', 'FL_thigh', 'FL_calf',
            'FR_hip', 'FR_thigh', 'FR_calf',
            'RL_hip', 'RL_thigh', 'RL_calf',
            'RR_hip', 'RR_thigh', 'RR_calf',
        ]
        
        self.get_logger().info('UnitreeSensorReader initialized')
        self.get_logger().info(f'Publishing at {publish_rate} Hz')
        
    def sensor_callback(self):
        """
        Periodic callback to read and publish sensor data.
        """
        timestamp = self.get_clock().now()
        
        # TODO: Replace with actual Unitree SDK calls
        # For now, publish synthetic data for testing
        
        # IMU data
        imu_msg = self._create_imu_message(timestamp)
        self.imu_pub.publish(imu_msg)
        
        # Joint state
        joint_msg = self._create_joint_state_message(timestamp)
        self.joint_state_pub.publish(joint_msg)
        
        # Foot forces
        foot_msg = self._create_foot_force_message()
        self.foot_force_pub.publish(foot_msg)
        
        # Battery
        battery_msg = Float32(data=85.0)  # Placeholder
        self.battery_pub.publish(battery_msg)
        
    def _create_imu_message(self, timestamp) -> Imu:
        """Create Imu message with accel, gyro, orientation."""
        msg = Imu()
        msg.header = Header(stamp=timestamp, frame_id='base_link')
        
        # Synthetic data for testing
        msg.linear_acceleration.x = 0.0
        msg.linear_acceleration.y = 0.0
        msg.linear_acceleration.z = 9.81
        
        msg.angular_velocity.x = 0.0
        msg.angular_velocity.y = 0.0
        msg.angular_velocity.z = 0.0
        
        msg.orientation.x = 0.0
        msg.orientation.y = 0.0
        msg.orientation.z = 0.0
        msg.orientation.w = 1.0
        
        return msg
    
    def _create_joint_state_message(self, timestamp) -> JointState:
        """Create JointState message for all joints."""
        msg = JointState()
        msg.header = Header(stamp=timestamp, frame_id='base_link')
        msg.name = self.joint_names
        
        # Synthetic data for testing
        num_joints = len(self.joint_names)
        msg.position = [0.0] * num_joints
        msg.velocity = [0.0] * num_joints
        msg.effort = [0.0] * num_joints
        
        return msg
    
    def _create_foot_force_message(self) -> Float32MultiArray:
        """Create foot force message (4 feet)."""
        msg = Float32MultiArray()
        msg.data = [0.0, 0.0, 0.0, 0.0]  # FL, FR, RL, RR
        return msg
    
    def connect_unitree(self):
        """
        Connect to Unitree robot via SDK.
        TODO: Implement actual Unitree SDK integration (Go2/H1).
        """
        port = self.get_parameter('unitree_port').value
        baudrate = self.get_parameter('unitree_baudrate').value
        
        self.get_logger().info(f'Connecting to Unitree on {port} @ {baudrate} baud...')
        # TODO: self.unitree = unitree_sdk2.connect(port, baudrate)


def main(args=None):
    rclpy.init(args=args)
    node = UnitreeSensorReader()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
