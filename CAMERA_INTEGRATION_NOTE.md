# Real Camera Integration (Nov 11 Investigation)

## Status: H.264 Decoding Blocked

### What We Found
- Unitree /frontvideostream publishes Go2FrontVideoData (H.264 encoded)
- Frame sizes: 360-720 bytes each
- H.264 start codes confirmed (0x00000001, 0x000001)
- NAL unit stream format

### Why Decoding Failed
- ffmpeg not available on Unitree robot
- No system H.264 codec libraries
- OpenCV H.264 support limited (requires NVDEC on GPU)
- Unitree SDK video decoder library not provided

### Solution Path (Future)
1. Install ffmpeg on Unitree: `apt-get install ffmpeg`
2. OR use Unitree's internal video_hub service API (if documented)
3. OR decode on PC: stream H.264 over network, decode locally
4. OR request raw RGB frames from Unitree (if API supports)

### Workaround: Mock Camera
- Pipeline validated with mock 1280×960 @ 30 FPS
- All preprocessing + YOLO detection working
- Ready for real camera swap once decoder available

### Next Steps
- Complete sorting logic (Days 22-35) with mock camera
- After sorting demo, revisit camera integration
- Document findings for Unitree SDK upgrade

