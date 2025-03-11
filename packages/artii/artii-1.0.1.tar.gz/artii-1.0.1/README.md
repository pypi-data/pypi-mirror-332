# 🎨 ASCII Art CLI
Convert images, videos, and GIFs to **ASCII art** directly in your terminal!
Supports **color**, **background effects**, and **video/GIF playback**.

## 🚀 Features
✔️ **Image to ASCII conversion** (JPG, PNG, etc.)
✔️ **Video to ASCII playback** (MP4, AVI, etc.)
✔️ **GIF to ASCII animation** (Animated GIF support)
✔️ **Color & background options** (`--color`, `--bg`)
✔️ **Interactive mode** (`-i`) for easy use
✔️ **Docker support** (No dependencies needed)

---

## 📦 Installation

### 🔹 1. Install Locally with Python
Requires **Python 3.7+**
```bash
pip install -r requirements.txt
python ascii_art.py -i
```

### 🔹 2. Run with Docker (No Dependencies Needed)
```bash
docker build -t ascii-art-cli .
docker run --rm -it -v "$(pwd):/app" ascii-art-cli -i
```

---

## 🎥 Usage Examples

### 1️⃣ **Convert an Image to ASCII**
```bash
python ascii_art.py my_image.jpg --color
```

### 2️⃣ **Play a Video as ASCII**
```bash
python ascii_art.py my_video.mp4 --color --fps 15
```

### 3️⃣ **Play an Animated GIF as ASCII**
```bash
python ascii_art.py my_animation.gif --color
```

### 4️⃣ **Interactive Mode (Step-by-Step Selection)**
```bash
python ascii_art.py -i
```

---

## 🛠️ Advanced Options
| Option       | Description                        | Default |
|-------------|------------------------------------|---------|
| `--width`   | Output ASCII width                | `100`   |
| `--color`   | Enable color output               | `False` |
| `--bg`      | Enable background color effects   | `False` |
| `--fps`     | Frame rate for videos             | `30`    |
| `--output`  | Save ASCII output to a file       | `None`  |

Example: Save ASCII output to a file
```bash
python ascii_art.py my_image.jpg --output=ascii_output.txt
```

---

## 🐫 Running Inside Docker
**No Python installation needed!** Just use Docker:

1️⃣ **Build the Docker image**
```bash
docker build -t ascii-art-cli .
```

2️⃣ **Run an image through Docker**
```bash
docker run --rm -it -v "$(pwd):/app" ascii-art-cli samples/vegeta.jpeg --color
```

```bash
docker run --rm -it -v "$(pwd):/app" ascii-art-cli samples/sangoku.png --color
```

3️⃣ **Play a video in ASCII through Docker**
```bash
docker run --rm -it -v "$(pwd):/app" ascii-art-cli samples/countdown.mp4 --fps 60 --color
```

4️⃣ **Play an animated GIF in ASCII through Docker**
```bash
docker run --rm -it -v "$(pwd):/app" ascii-art-cli samples/fusion.gif --color
```

---

## 🤖 Contributing
Feel free to **fork**, create a PR, or submit an issue!

---

## 📝 License
MIT License

