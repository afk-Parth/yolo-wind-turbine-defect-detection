from ultralytics import YOLO

model = YOLO("runs/detect/train6/weights/best.pt")
model.train(data="D:/dataset/dataset.yaml", epochs=50)
