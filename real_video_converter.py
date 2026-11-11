#!/usr/bin/env python3
"""Decode real Unitree H.264 video to ROS2 Image."""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Header
import cv2
import numpy as np
import subprocess
import tempfile
import os

from unitree_go.msg import Go2FrontVideoData

class RealVideoConverterNode(Node):
    def __init__(self):
        super().__init__('real_video_converter')
        
        self.sub = self.create_subscription(
            Go2FrontVideoData, '/frontvideostream', self.video_callback, 1
        )
        self.pub = self.create_publisher(Image, '/camera/image_raw', 10)
        self.frame_count = 0
        self.h264_buffer = b''
        self.temp_dir = tempfile.mkdtemp()
        self.get_logger().info(f"Real H.264 video converter initialized (temp: {self.temp_dir})")
    
    def video_callback(self, msg):
        """Decode H.264 video data."""
        try:
            # Accumulate H.264 stream
            video_data = bytes(msg.video720p)
            if len(video_data) == 0:
                return
            
            self.h264_buffer += video_data
            
            # Try to decode accumulated frames every 5 frames
            self.frame_count += 1
            if self.frame_count % 5 == 0:
                self.try_decode()
        
        except Exception as e:
            self.get_logger().error(f"Error: {e}")
    
    def try_decode(self):
        """Try to decode H.264 buffer with ffmpeg."""
        if len(self.h264_buffer) < 100:
            return
        
        try:
            # Write H.264 to temp file
            h264_file = os.path.join(self.temp_dir, "temp.h264")
            with open(h264_file, 'wb') as f:
                f.write(self.h264_buffer)
            
            # Decode with ffmpeg
            output_file = os.path.join(self.temp_dir, "temp.raw")
            cmd = [
                'ffmpeg', '-y', '-i', h264_file,
                '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                output_file
            ]
            
            result = subprocess.run(cmd, capture_output=True, timeout=2)
            
            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                # Read decoded image
                with open(output_file, 'rb') as f:
                    raw_data = f.read()
                
                # Estimate dimensions (assume common sizes)
                for h, w in [(960, 1280), (720, 1280), (480, 640)]:
                    if len(raw_data) == h * w * 3:
                        img_rgb = np.frombuffer(raw_data, dtype=np.uint8).reshape((h, w, 3))
                        self.publish_image(img_rgb)
                        self.h264_buffer = b''  # Reset buffer
                        return
                
                self.get_logger().warn(f"Decoded {len(raw_data)} bytes, no matching size")
        
        except subprocess.TimeoutExpired:
            self.get_logger().warn("ffmpeg decode timeout")
        except Exception as e:
            self.get_logger().warn(f"Decode attempt failed: {e}")
    
    def publish_image(self, img_rgb):
        """Publish RGB image."""
        img_msg = Image()
        img_msg.header = Header()
        img_msg.header.stamp = self.get_clock().now().to_msg()
        img_msg.header.frame_id = "camera_link"
        img_msg.height = img_rgb.shape[0]
        img_msg.width = img_rgb.shape[1]
        img_msg.encoding = "rgb8"
        img_msg.step = img_rgb.shape[1] * 3
        img_msg.data = img_rgb.tobytes()
        
        self.pub.publish(img_msg)
        self.frame_count += 1
        self.get_logger().info(f"Published frame: {img_rgb.shape}")

def main(args=None):
    rclpy.init(args=args)
    node = RealVideoConverterNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
