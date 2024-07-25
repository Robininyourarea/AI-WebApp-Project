from ultralytics import YOLO



model = YOLO("yolov8s-seg.pt")
model.export(format="onnx")

print('Export Succesfully')