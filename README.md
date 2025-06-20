# Wind-Turbine Surface Defect Detection using YOLO 🌬️🔧

This project uses YOLO (You Only Look Once) to detect surface defects on wind turbine blades from drone images. It automates visual inspection to save time, reduce manual labor, and enable real-time defect monitoring in energy infrastructure.

---

## 📦 Dataset

- **Source:** DTU - Drone Inspection Images of Wind Turbines  
- **Annotations:** Created using [LabelImg](https://github.com/tzutalin/labelImg)  
- **Format:** YOLO (`.txt` files with class, x_center, y_center, width, height)  
- **Classes:**
  - `0`: Crack  
  - `1`: Erosion  
  - `2`: Lightning Strike  

> 📁 *A small sample (10 images + labels) is included inside the `data/` folder.*  
> 📥 Full dataset: [⬜ Link to Google Drive / HuggingFace]

---

## 🧠 Model Details

- **Model Used:** YOLOv8s (from [Ultralytics](https://github.com/ultralytics/ultralytics))  
- **Input Image Size:** 640×640  
- **Epochs:** 50  
- **Batch Size:** 16  
- **Optimizer:** SGD  
- **Data Augmentations:** Mosaic, HSV shift, flipping  

---

## 📈 Results & Evaluation Metrics

| Metric         | Value   |
|----------------|---------|
| **mAP@0.5**    |  0.87 |
| **Precision**  |  0.85 |
| **Recall**     |  0.83 |
| **F1-Score**   |  0.84 |
| **Validation Loss** |  0.02 |

> ✨ YOLO’s built-in evaluation during training gives real-time feedback on these metrics.

---

## 🖼️ Result Samples

<p align="center">
  <img src="D:\its python\runs\detect\predict23\sample.jpg" width="400">
</p>

- Left: **Ground Truth** | Right: **Predictions**

---

## 🧪 How to Train

```bash
yolo task=detect mode=train model=yolov8s.pt \
     data=data/windmill.yaml epochs=50 imgsz=640
