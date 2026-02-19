# ROS 2 Vision-Based Object Detection with YOLOv8 in Gazebo

Real-time object detection for mobile robots using ROS 2 + Gazebo + YOLOv8 in a photorealistic indoor simulation.

This project demonstrates a complete robot perception pipeline — from simulated RGB camera data to AI-based object detection.

## 📌 Project Highlights

- 🤖 TurtleBot3 in custom indoor world
- 🎥 RGB camera → real-time YOLOv8 inference
- 🧠 ROS 2 perception node (Python)
- 🏠 Photorealistic AWS RoboMaker small house world
- 🎮 Keyboard teleoperation for live testing
- 🌗 Lighting optimization for improved detection accuracy

## 🎥 Demo

1. [Final Demo](https://drive.google.com/file/d/1Wd6d5arcSVy20p_EnRnbW0kVb2GHAEV1/view?usp=drive_link)

## 🏗 System Architecture

```mermail
flowchart TD

    A[Gazebo Simulation] -->|RGB Image Stream| B[/camera/image_raw]

    B --> C[YOLOv8 Detection Node<br/>- Subscribes to image<br/>- Runs inference<br/>- Draws bounding boxes]

    C -->|Detection messages| D[/detections Topic]

    C -->|Annotated image| E[/image_annotated Topic]

    D --> F[RViz2 Visualization<br/>Bounding boxes / markers]

    E --> G[OpenCV Display Node<br/>Live camera view with detections]

```

## 📂 Repository Structure

```css
ROS2-Vision-Perception
│── assets/
│   ├── demo.gif
│   ├── gazebo_view.png
│   └── yolo_detection.png
│
└── perception_ws/
    └── src/
        ├── simulation/
        │   ├── launch/
        │   └── worlds/
        │
        └── vision_detector/
            ├── yolo_detector.py
            └── camera_viewer.py
```

## ⚙ Installation and quick checks

### 0️⃣ Quick Checks

```bash
lsb_release -a
echo $ROS_DISTRO
gazebo --version
```
You should see:
- Ubuntu 22.04
- Humble
- Gazebo 11

### 1️⃣ Create workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/shimmer0909/ROS2-Vision-Perception
cd ..
colcon build
source install/setup.bash
```

You can permanently source setup.bash 
```bash
source install/setup.bash
echo "source ~/Ros2-Vision-Perception/perception_ws/install/setup.bash" >> ~/.bashrc
```

### 2️⃣ Install dependencies

Install OpenCV
```bash
pip3 uninstall -y opencv-python
opencv-python==4.8.1.78
```

Install numpy==1.26
```bash
pip3 uninstall -y numpy
pip3 install numpy==1.26.4
```

Load AWS RoboMaker Small House in ROS 2 + Gazebo
```bash
cd ~
git clone https://github.com/aws-robotics/aws-robomaker-small-house-world
```

### 3️⃣ Download YOLOv8 model

```bash
pip3 install ultralytics
```

Validate
```bash
python3 -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

Place it inside: vision_detector/

## 🚀 Run the Simulation

### 1. Launch Gazebo world

```bash
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/aws-robomaker-small-house-world/models

ros2 launch gazebo_ros gazebo.launch.py \
world:=/home/second-code/aws-robomaker-small-house-world/worlds/small_house.world
```

This step might take 3-4 minutes the first time.

### 2. Custom spawn the robot

```bash
ros2 launch turtlebot3_gazebo spawn_turtlebot3.launch.py \
x:=0.0 y:=0.0 z:=0.01
```

### 3. Confirm camera is publishing
```bash
ros2 topic list | grep image
```
You should see:
/camera/image_raw

Check the stream
```bash
ros2 run rqt_image_view rqt_image_view
```

### 4. Run YOLO perception node

```bash
ros2 run vision_detector yolo_detector
```

3. Teleoperate the robot

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Motion Keys

- i ⬆️ Move straight forward
- u ↖️ Forward + turn left
- o ↗️ Forward + turn right

- j ↺ Rotate in place left
- k ⏹️ Stop
- l ↻ Rotate in place right

- , ⬇️ Move straight backward
- m ↙️ Backward + turn left
- . ↘️ Backward + turn right

Speed Control

- q increase both linear & angular speed
- z decrease both
- w increase linear only
- x decrease linear only
- e increase angular only
- c decrease angular only

## 🎯 Detection Output

- Real-time bounding boxes
- Class labels
- Confidence scores

Works on:

- chair
- exercise ball
- refrigerator
- person
- etc. (COCO classes)

## 🌗 Key Experiment: Yolo accuracy issues

The default lighting of aws-robomaker-small-house-world and light coloured furniture results in low detection and classification accuracy. 

Things to fix
- Washed-out textures
- Poor contrast
- Low detection confidence

Solution
Dim the simulation lights by reducing 
1. Diffuse light <diffuse>
2. Specular reflection <specular>

```bash
gedit ~/aws-robomaker-small-house-world/worlds/small_house.world
```

## 🧪 Use Cases

- Indoor service robots
- Semantic navigation
- AI-based perception research
- Sim-to-real vision testing

## 🤝 Connect With Me

If you’re working in:

- Robotics
- ROS 2
- Computer Vision
- Autonomous systems

Let’s connect on [LinkedIn](https://www.linkedin.com/in/ashi-gupta-ml-robotics/) 🚀

## ⭐ Consider starring the repo!
