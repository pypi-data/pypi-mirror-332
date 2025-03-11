import argparse
import os
import sys
import time

import cv2
from PIL import Image

# ASCII characters from dark to light
ASCII_CHARS = "@%#*+=-:. "

def rgb_to_ansi_fg(r, g, b):
    """Convert RGB to ANSI foreground escape sequence."""
    return f"\033[38;2;{r};{g};{b}m"

def rgb_to_ansi_bg(r, g, b):
    """Convert RGB to ANSI background escape sequence."""
    return f"\033[48;2;{r};{g};{b}m"

def frame_to_ascii(frame, width=100, colored=False, background=False):
    """Convert a video frame to ASCII art."""
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    aspect_ratio = image.height / image.width
    new_height = int(width * aspect_ratio * 0.5)
    image = image.resize((width, new_height))

    ascii_str = ""
    for y in range(new_height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            gray = (r + g + b) // 3
            char = ASCII_CHARS[gray * (len(ASCII_CHARS) - 1) // 255]

            if colored or background:
                ansi_code = ""
                if colored:
                    ansi_code += rgb_to_ansi_fg(r, g, b)
                if background:
                    ansi_code += rgb_to_ansi_bg(r, g, b)
                ascii_str += ansi_code + char
            else:
                ascii_str += char

        ascii_str += "\033[0m\n" if (colored or background) else "\n"

    return ascii_str

def play_video_ascii(video_path, width=100, colored=False, background=False, fps=30):
    """Convert a video to ASCII and play it in the terminal."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("❌ Error: Could not open video.")
        return

    frame_delay = 1 / fps  # Control playback speed

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break  # End of video

            ascii_frame = frame_to_ascii(frame, width, colored, background)
            os.system("clear" if os.name == "posix" else "cls")  # Clear screen
            print(ascii_frame + "\033[0m")  # Print ASCII frame
            time.sleep(frame_delay)  # Control playback speed

    except KeyboardInterrupt:
        print("\n⏹️ Playback stopped.")
    finally:
        cap.release()

def play_gif_ascii(gif_path, width=100, colored=False, background=False):
    """Play an animated GIF as ASCII using OpenCV and stop after the last frame."""
    cap = cv2.VideoCapture(gif_path)
    if not cap.isOpened():
        print("❌ Unable to open GIF file.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break  # Stop after the last frame

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            ascii_frame = frame_to_ascii(frame, width, colored, background)
            os.system("clear" if os.name == "posix" else "cls")  # Clear screen
            print(ascii_frame + "\033[0m")  # Print ASCII frame
            time.sleep(0.1)  # Adjust frame rate
    except KeyboardInterrupt:
        print("\n⏹️ Playback stopped.")
    finally:
        cap.release()

def main():
    parser = argparse.ArgumentParser(description="Convert images/videos to ASCII art.")
    parser.add_argument("file", nargs="?", help="Path to image or video file")
    parser.add_argument("-w", "--width", type=int, default=100, help="Width of output ASCII (default: 100)")
    parser.add_argument("-c", "--color", action="store_true", help="Enable colored ASCII")
    parser.add_argument("-b", "--bg", action="store_true", help="Enable background colors")
    parser.add_argument("-f", "--fps", type=int, default=30, help="Frame rate for video playback (default: 30)")
    parser.add_argument("-i", "--interactive", action="store_true", help="Run interactive mode")

    args = parser.parse_args()

    if args.interactive:
        print("\n🎥 Welcome to ASCII Video Generator! 🎥\n")
        file_path = input("Enter image/video path: ").strip()
        width = input("Enter width (default 100): ").strip()
        width = int(width) if width.isdigit() else 100
        colored = input("Enable color? (y/n): ").strip().lower() == "y"
        background = input("Enable background colors? (y/n): ").strip().lower() == "y"
        fps = input("Enter FPS (default 30): ").strip()
        fps = int(fps) if fps.isdigit() else 30

        if file_path.lower().endswith((".mp4", ".avi", ".mov")):
            play_video_ascii(file_path, width, colored, background, fps)
        elif file_path.lower().endswith(".gif"):
            play_gif_ascii(args.file, args.width, args.color, args.bg)
        else:
            ascii_art = frame_to_ascii(cv2.imread(file_path), width, colored, background)
            print(ascii_art + "\033[0m")

    elif args.file:
        if args.file.lower().endswith((".mp4", ".avi", ".mov")):
            play_video_ascii(args.file, args.width, args.color, args.bg, args.fps)
        elif args.file.lower().endswith(".gif"):
            play_gif_ascii(args.file, args.width, args.color, args.bg)  
        else:
            frame = cv2.imread(args.file)
            ascii_art = frame_to_ascii(frame, args.width, args.color, args.bg)
            print(ascii_art + "\033[0m")

    else:
        print("❌ Error: No file provided. Use -i for interactive mode.")

if __name__ == "__main__":
    main()

