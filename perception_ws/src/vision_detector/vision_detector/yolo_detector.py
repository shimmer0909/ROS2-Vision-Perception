import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
import cv2
import time
from ultralytics import YOLO

class YoloDetector(Node):
    def __init__(self):
        super().__init__('yolo_detector')
        self.bridge = CvBridge()

        self.model = YOLO('yolov8n.pt')
        self.get_logger().info('YOLOv8 model loaded')

        self.subscription = self.create_subscription(Image, '/camera/image_raw', self.image_callback, 10)

        self.get_logger().info('YOLO detection node started')

    def image_callback(self, msg):
        start_time = time.time()

        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # Resize for speed
        frame_resized = cv2.resize(frame, (640, 480))

        results = self.model(frame_resized, verbose=False)[0]

        for box in results.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = self.model.names[cls_id]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Draw bounding box
            cv2.rectangle(frame_resized, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame_resized,
                f'{label} {conf:.2f}',
                (x1, y1 - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

        fps = 1.0 / (time.time() - start_time)
        cv2.putText(
            frame_resized,
            f'FPS: {fps:.2f}',
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

        cv2.imshow('YOLOv8 Detection', frame_resized)
        cv2.waitKey(1)

def main():
    rclpy.init()
    node = YoloDetector()
    rclpy.spin(node)

    cv2.destroyAllWindows()
    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()

