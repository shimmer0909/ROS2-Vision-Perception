import rclpy
from rclpy.node import Node
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class CameraViewer(Node):
    def __init__(self):
        super().__init__('camera_viewer')

        self.bridge = CvBridge()
        self.subcriber = self.create_subscription(Image, '/camera/image_raw', self.image_callback, 10)

        self.get_logger().info('Camera viewer node started')

    def image_callback(self,msg):
        try:
            frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            cv2.imshow('TurtleBot3 Camera', frame)
            cv2.waitKey(1)

        except Exception as e:
            self.get_logger().error(f'Image conversion failed" {e}')

def main():
    rclpy.init()

    node = CameraViewer()
    rclpy.spin(node)

    cv2.destroyAllWindows()
    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()