#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

class IMUVisualizer(Node):
    def __init__(self):
        super().__init__('imu_visualizer')
        self.subscription = self.create_subscription(
            Imu,
            '/imu/data',
            self.imu_callback,
            10
        )

    def imu_callback(self, msg):
        # Extract the IMU data
        orientation = msg.orientation
        linear_acceleration = msg.linear_acceleration
        angular_velocity = msg.angular_velocity

        # Display the IMU data
        self.get_logger().info('IMU Orientation: x={}, y={}, z={}, w={}'.format(
            orientation.x, orientation.y, orientation.z, orientation.w))
        self.get_logger().info('Linear Acceleration: x={}, y={}, z={}'.format(
            linear_acceleration.x, linear_acceleration.y, linear_acceleration.z))
        self.get_logger().info('Angular Velocity: x={}, y={}, z={}'.format(
            angular_velocity.x, angular_velocity.y, angular_velocity.z))

def main(args=None):
    rclpy.init(args=args)
    imu_visualizer = IMUVisualizer()
    rclpy.spin(imu_visualizer)
    imu_visualizer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
