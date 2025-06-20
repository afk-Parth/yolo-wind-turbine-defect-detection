from ultralytics import YOLO

model = YOLO("D:/its python/runs/detect/train7/weights/best.pt")

# Lower confidence to capture low-confidence detections
results = model("D:/dataset/test/images/sample.png", save=True, show=True, conf=0.05)
