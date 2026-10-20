"""Rosbag analysis template for CP1 real Unitree data."""
import sqlite3
import math


def analyze_bag(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM messages")
    total = cursor.fetchone()[0]
    print(f"Total messages: {total}")

    cursor.execute("""
        SELECT t.name, COUNT(m.id)
        FROM messages m
        JOIN topics t ON m.topic_id = t.id
        GROUP BY t.name
    """)
    for name, count in cursor.fetchall():
        print(f"  {name}: {count} messages")

    cursor.execute("""
        SELECT MIN(timestamp), MAX(timestamp)
        FROM messages
    """)
    t_min, t_max = cursor.fetchone()
    if t_min and t_max:
        duration = (t_max - t_min) / 1e9
        print(f"Duration: {duration:.2f}s")
        print(f"Avg rate: {total / duration:.1f} Hz")

    conn.close()


def compute_latency(timestamps):
    """Compute inter-message latency from timestamp list."""
    if len(timestamps) < 2:
        return []
    deltas = []
    for i in range(1, len(timestamps)):
        dt = (timestamps[i] - timestamps[i-1]) / 1e6
        deltas.append(dt)
    avg = sum(deltas) / len(deltas)
    std = math.sqrt(sum((d - avg)**2 for d in deltas) / len(deltas))
    print(f"Latency: avg={avg:.2f}ms, std={std:.2f}ms, "
          f"min={min(deltas):.2f}ms, max={max(deltas):.2f}ms")
    return deltas


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_rosbag.py <path_to.db3>")
        sys.exit(1)
    analyze_bag(sys.argv[1])
