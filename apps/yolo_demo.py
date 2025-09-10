# python -m apps.yolo_demo


"""Generic YOLO detection demo."""
import argparse
import numpy as np
from modules import Camera, YOLODetector, boxes as draw_boxes


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--src", default=0)
    p.add_argument("--weights", default="yoloW/yolov8n.pt")
    p.add_argument("--conf", type=float, default=0.25)
    p.add_argument("--wait", type=int, default=1)
    p.add_argument("--mirror", type=int, default=1)
    return p.parse_args()


def main():
    args = parse_args()
    cam = Camera(args.src, mirror=bool(args.mirror), wait=args.wait)
    det = YOLODetector(args.weights, conf=args.conf)

    for frame in cam.iterate():
        boxes, scores, names = det.infer(frame)
        ann = [f"{n}:{s:.2f}" for n, s in zip(names, scores.tolist())]
        draw_boxes(frame, boxes, ann)

        cam.show("YOLO Demo", frame)

    cam.release()


if __name__ == "__main__":
    main()
