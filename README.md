# YOLO Detection CV

<img width="2048" height="1364" alt="image" src="https://github.com/user-attachments/assets/bec026d7-7648-4b32-83b6-d45b09461e44" />

<p align="center">(Add a screenshot or GIF of your YOLO detection demo in action here. Place your image at <code>assets/images/yolo_demo.jpg</code>.)</p>

[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-ultralytics-orange)](https://github.com/ultralytics/ultralytics)

## 🔍 About the Project

**YOLO Detection CV** is a Python-based, real-time object detection demo built on YOLO (You Only Look Once). Whether you're showcasing deep learning, testing new detection models, or teaching computer vision — this modular tool has you covered.

It processes each video frame using a YOLO model, detects multiple object classes, and visualizes bounding boxes, labels, and confidence scores live on screen.

---

## 🎯 Features

- 🦾 Real-time object detection with YOLO (configurable model/weights)
- 📹 Video file and webcam support
- 🧩 Modular and extendable architecture
- ⚙️ Adjustable confidence threshold and model parameters
- 📦 Includes demo videos and assets
- 📝 Clean, well-documented Python code

---

## 🧠 Use Cases

- Rapid prototyping of detection pipelines
- CV education and classroom demos
- Benchmarking different YOLO models
- Custom object detection integrations

---

## ⚙️ How It Works

1. **Input:** Video source (webcam or file)
2. **Detection:** YOLO model detects objects in each frame
3. **Annotation:** Draws bounding boxes, labels, and confidence values
4. **Visualization:** Live output shows detection overlays in real time

---

## 🗂️ Project Structure

```

cv\_lib/
apps/
yolo\_demo.py             # Entry point script
modules/
...                      # Detector, visualizer, utils
assets/
demo\_video/              # Test videos
images/                  # Screenshots or demos
ml/
...                      # YOLO weights or model configs

````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/yolo-detection-demo-cv.git
cd yolo-detection-demo-cv
````

### 2. Install Dependencies

Ensure Python 3.7+ is installed.

```bash
pip install opencv-python numpy
```

> If you're using YOLOv8 or other models:

```bash
pip install torch ultralytics
```

---

### 3. Run the YOLO Detection Demo

#### With Webcam:

```bash
python -m apps.yolo_demo --mirror 1
```

#### With Video File and Custom YOLO Weights:

```bash
python -m apps.yolo_demo --src assets/demo_video/cars.mp4 --weights yoloW/yolov8l.pt --conf 0.3 --mirror 0
```

> You can also change the confidence threshold using `--conf`.

---

## 💡 Example Usage

```bash
python -m apps.yolo_demo --mirror 1
```

```bash
python -m apps.yolo_demo --src assets/demo_video/road.mp4 --weights yoloW/yolov8n.pt --conf 0.25 --mirror 0
```

---

## 🙏 Acknowledgments

* Built with [YOLOv8 by Ultralytics](https://github.com/ultralytics/ultralytics)
* Powered by [OpenCV](https://opencv.org/) and [Python](https://www.python.org/)
* Demo videos sourced from public datasets

---

*Explore the codebase for modular logic and clear implementation.*
