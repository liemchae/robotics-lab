# ROS2 Humble Setup Guide

**Target:** Ubuntu 22.04 on lab machine (NVIDIA RTX5090)

---

## 1. Prerequisites

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install build tools
sudo apt install -y \
  build-essential \
  cmake \
  git \
  python3-pip \
  python3-venv

# Install ROS2 dependencies
sudo apt install -y \
  curl \
  gnupg \
  lsb-release
```

---

## 2. Install ROS2 Humble

```bash
# Add ROS2 key
sudo curl -sSL https://repo.ros2.org/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

# Add repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://repo.ros2.org/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Install ROS2
sudo apt update
sudo apt install -y ros-humble-desktop
sudo apt install -y ros-humble-dev-tools
```

---

## 3. Setup Workspace

```bash
# Create & navigate to workspace
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws

# Clone dependencies (Unitree SDK, etc.)
cd src
git clone https://github.com/unitreerobotics/unitree_sdk2.git
git clone https://github.com/unitreerobotics/unitree_ros2.git

# Build workspace
cd ~/ros2_ws
colcon build --symlink-install

# Source setup
source install/setup.bash

# Add to bashrc for auto-source
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

---

## 4. Install Supporting Tools

```bash
# Gazebo (simulation)
sudo apt install -y ros-humble-gazebo-ros-pkgs

# RViz (visualization)
sudo apt install -y ros-humble-rviz2

# Building/testing
sudo apt install -y \
  python3-colcon-common-extensions \
  python3-flake8-docstrings \
  python3-pytest \
  python3-pytest-cov \
  python3-pytest-repeat

# Sensor drivers
sudo apt install -y \
  ros-humble-sensor-msgs \
  ros-humble-geometry-msgs
```

---

## 5. Verify Installation

```bash
# Start talker/listener test
# Terminal 1:
source ~/.bashrc
ros2 run demo_nodes_cpp talker

# Terminal 2:
source ~/.bashrc
ros2 run demo_nodes_cpp listener

# If you see messages flowing, ROS2 is working.

# Check ROS2 version
ros2 --version

# List topics
ros2 topic list
```

---

## 6. Python Development Environment

```bash
# Create venv (optional)
python3 -m venv ~/ros2_py_env
source ~/ros2_py_env/bin/activate

# Install ROS2 Python packages
pip install \
  rclpy \
  rosgraph \
  rosidl-runtime-py

# Install ML/control dependencies
pip install \
  torch \
  numpy \
  scipy \
  opencv-python \
  pyyaml
```

---

## 7. Create First ROS2 Package

```bash
cd ~/ros2_ws/src

# Generate C++ package
ros2 pkg create --build-type ament_cmake unitree_control --dependencies rclcpp sensor_msgs

# Or Python package
ros2 pkg create --build-type ament_python perception_pipeline --dependencies rclpy std_msgs sensor_msgs

# Build
cd ~/ros2_ws
colcon build --symlink-install

# Source
source install/setup.bash
```

---

## 8. Docker Setup (Optional, Recommended)

Create `Dockerfile` for reproducible environment:

```dockerfile
FROM ubuntu:22.04

RUN apt update && apt install -y \
  ros-humble-desktop \
  python3-colcon-common-extensions \
  git

RUN mkdir -p /root/ros2_ws/src

WORKDIR /root/ros2_ws

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

CMD ["/bin/bash"]
```

Build & run:
```bash
docker build -t robotics-lab:ros2-humble .
docker run -it --gpus all -v $(pwd):/root/ros2_ws robotics-lab:ros2-humble
```

---

## 9. Troubleshooting

**Issue:** `colcon build` fails with missing packages
```bash
# Install missing dependencies
rosdep install --from-paths src --ignore-src -r -y
```

**Issue:** ROS2 commands not found
```bash
# Ensure sourcing
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
```

**Issue:** GPU not visible in container
```bash
# Add --gpus all flag
docker run --gpus all -it robotics-lab:ros2-humble
```

---

## Next Steps

1. Complete setup verification (section 5)
2. Clone Unitree SDK → `~/ros2_ws/src/`
3. Build first ROS2 package (section 7)
4. Proceed to **UNITREE_API.md** for sensor integration

---

## Resources

- [ROS2 Humble Installation](https://docs.ros.org/en/humble/Installation.html)
- [Colcon Build System](https://colcon.readthedocs.io/)
- [Unitree Go2 ROS2 Wrapper](https://github.com/unitreerobotics/unitree_ros2)

