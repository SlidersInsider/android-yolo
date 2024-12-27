import os
from ultralytics import YOLO

trained_model = YOLO("results/train/weights/best.pt")
results = trained_model.val(project="results")
print(results.box.map50)