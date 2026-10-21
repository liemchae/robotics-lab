"""Inspect rosbag directory structure and metadata."""
import os
import sys
import yaml


def inspect_bag(bag_dir):
    if not os.path.isdir(bag_dir):
        print(f"Error: {bag_dir} is not a directory")
        sys.exit(1)

    print(f"Rosbag directory: {bag_dir}")
    print()

    metadata_path = os.path.join(bag_dir, "metadata.yaml")
    if os.path.exists(metadata_path):
        with open(metadata_path) as f:
            meta = yaml.safe_load(f)

        info = meta.get("rosbag2_bagfile_information", {})
        print(f"Duration: {info.get('duration', {}).get('nanoseconds', 0) / 1e9:.2f}s")
        print(f"Message count: {info.get('message_count', 'unknown')}")
        print()

        print("Topics:")
        for topic in info.get("topics_with_message_count", []):
            t = topic.get("topic_metadata", {})
            print(f"  {t.get('name', '?'):30s} "
                  f"{t.get('type', '?'):40s} "
                  f"{topic.get('message_count', 0)} msgs")
    else:
        print("No metadata.yaml found")

    print()
    print("Files:")
    for f in sorted(os.listdir(bag_dir)):
        path = os.path.join(bag_dir, f)
        size = os.path.getsize(path)
        if size > 1024 * 1024:
            print(f"  {f:40s} {size / 1024 / 1024:.1f} MB")
        else:
            print(f"  {f:40s} {size / 1024:.1f} KB")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 inspect_rosbag.py <rosbag_directory>")
        sys.exit(1)
    inspect_bag(sys.argv[1])
