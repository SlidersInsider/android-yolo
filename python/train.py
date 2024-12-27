from ultralytics import YOLO

model_yolo = YOLO("yolov8s.pt")
model_yolo.train(data="custom.yaml", device="cpu", epochs=6, batch=10, imgsz=640, task="detect", mode="train", project="results")
model_yolo.export(format="torchscript", optimize=True)

#                  3 epoch
#                  Class     Images  Instances      Box(P          R      mAP50  mAP50-95
#                    all         30        237      0.711      0.637      0.711      0.525
#               banknote         30         94      0.808      0.713      0.824      0.617
#                   coin         30        113      0.722      0.965      0.974       0.76
#                   card         30         30      0.601      0.233      0.333      0.197
#
#                  6 epoch
#                  Class     Images  Instances      Box(P          R      mAP50      mAP50-95
#                    all         30        237       0.75      0.811      0.803      0.597
#               banknote         30         94      0.962      0.803      0.896      0.678
#                   coin         30        113      0.869      0.995      0.988      0.768
#                   card         30         30      0.421      0.633      0.524      0.346
#
#                  12 epoch
#                  Class     Images  Instances      Box(P          R      mAP50      mAP50-95
#                    all         30        237      0.859      0.695      0.795      0.581
#               banknote         30         94      0.958      0.713      0.898      0.672
#                   coin         30        113      0.948      0.973      0.993      0.758
#                   card         30         30      0.671        0.4      0.493      0.313
