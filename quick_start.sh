#!/bin/bash
# Quick Start Script for Robotics Lab

set -e

echo "=== Robotics Lab Quick Start ==="
echo ""

# Check system
echo "[1/5] Checking system..."
if ! command -v ros2 &> /dev/null; then
    echo "❌ ROS2 not found. Follow docs/ROS2_SETUP.md first."
    exit 1
fi
echo "✓ ROS2 found: $(ros2 --version)"

# Build workspace
echo "[2/5] Building ROS2 workspace..."
cd ros2_ws
colcon build --symlink-install
source install/setup.bash
echo "✓ Workspace built"

# Verify packages
echo "[3/5] Verifying packages..."
if ros2 pkg list | grep -q unitree_control; then
    echo "✓ unitree_control package found"
else
    echo "❌ unitree_control package not found"
    exit 1
fi

# Test sensor reader
echo "[4/5] Testing sensor reader node (5 seconds)..."
timeout 5 ros2 run unitree_control sensor_reader || true
echo "✓ Node executed (check for 'UnitreeSensorReader initialized')"

# Summary
echo "[5/5] Setup complete!"
echo ""
echo "=== Next Steps ==="
echo "1. Update docs/WEEKLY_LOG.md with your progress"
echo "2. Run: ros2 run unitree_control sensor_reader"
echo "3. In another terminal: ros2 topic list"
echo ""
echo "See docs/ for detailed guides."
