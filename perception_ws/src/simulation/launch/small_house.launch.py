from launch import LaunchDescription
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    world_path = os.path.join(
        os.environ['HOME'],
        'Desktop',
        'Robotics',
        'Ros2-Vision-Perception',
        'perception_ws',
        'src',
        'simulation',
        'worlds',
        'small_house.world'
    )
    return LaunchDescription([
        ExecuteProcess(
            cmd=[
                'gazebo',
                '--verbose',
                '-s', 'libgazebo_ros_factory.so',
                world_path
            ],
            output='screen'
        )
    ])

