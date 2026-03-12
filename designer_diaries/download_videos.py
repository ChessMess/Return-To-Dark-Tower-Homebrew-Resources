"""
Download videos for the 8 Stages of Grief designer diary post.
Run this script from your local machine (same folder as download_images.py).

No external dependencies required (uses Python stdlib only).

Usage:
    python3 download_videos.py

Videos are saved to:
    designer_diaries/videos/post_2735575_8_stages_of_grief_tim_burrell_saward/
"""

import os
import time
import urllib.request
import urllib.error

VIDEOS_DIR = os.path.join(os.path.dirname(__file__), "videos")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Referer": "https://www.kickstarter.com/",
    "Accept": "video/mp4,video/*;q=0.9,*/*;q=0.8",
}

_CF = "https://d15chbti7ht62o.cloudfront.net/assets"

# Video files are at the same Cloudfront CDN paths as their thumbnail images,
# with .mp4 replacing .jpg. These are public (no signature required).
VIDEOS = {
    "post_2735575_8_stages_of_grief_tim_burrell_saward": [
        # (url, label)
        (f"{_CF}/027/819/033/323ff1d1c77ea80fcdaa52f59bff3693_h264_base.mp4",
         "Mark 1/2 — stepper motor mechanism"),
        (f"{_CF}/027/819/069/c94a0cdc42d39488fa07e42274fd90ba_h264_high.mp4",
         "Mark 3/4 — doors and skull ejection"),
        (f"{_CF}/027/819/106/0df10df01daced09681f879f2213cc6f_h264_high.mp4",
         "Mark 4 — electromagnet door test"),
        (f"{_CF}/027/819/117/0a0e6c0b29a0068f5673fabee27ba07a_h264_high.mp4",
         "Mark 4 — skull distribution mechanism"),
        (f"{_CF}/027/819/143/dabd4f5622e9381fcf03fcffef35aa42_h264_base.mp4",
         "Mark 5 — gearbox assembly"),
        (f"{_CF}/027/819/162/27df478570735ffc6f3240f8601771c2_h264_high.mp4",
         "Mark 6 — tower coming to life"),
    ],
}


def download_file(url, dest_path):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp, open(dest_path, "wb") as f:
        # Stream in chunks (videos can be large)
        while True:
            chunk = resp.read(1024 * 64)
            if not chunk:
                break
            f.write(chunk)


def main():
    os.makedirs(VIDEOS_DIR, exist_ok=True)
    total_downloaded = 0
    total_skipped = 0
    total_failed = 0

    for folder, videos in VIDEOS.items():
        folder_path = os.path.join(VIDEOS_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"\n📁 {folder}  ({len(videos)} videos)")

        for url, label in videos:
            filename = url.split("/")[-1]
            dest = os.path.join(folder_path, filename)

            if os.path.exists(dest):
                size = os.path.getsize(dest)
                print(f"  ✓ Already exists: {filename} ({size:,} bytes)")
                total_skipped += 1
                continue

            print(f"  ⬇ Downloading: {filename}  ({label})")
            try:
                download_file(url, dest)
                size = os.path.getsize(dest)
                print(f"    ✅ Done — {size:,} bytes ({size / 1_000_000:.1f} MB)")
                total_downloaded += 1
                time.sleep(0.5)
            except urllib.error.HTTPError as e:
                print(f"    ❌ HTTP {e.code}: {filename}")
                total_failed += 1
            except Exception as e:
                print(f"    ❌ Failed: {filename} — {e}")
                total_failed += 1

    print(f"\n{'='*55}")
    print(f"Done!  Downloaded: {total_downloaded}  |  Skipped: {total_skipped}  |  Failed: {total_failed}")


if __name__ == "__main__":
    main()
