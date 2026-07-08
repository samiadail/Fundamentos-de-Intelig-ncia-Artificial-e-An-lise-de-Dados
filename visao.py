from ultralytics import YOLO
modelo = YOLO("yolov8n.pp")
modelo.predict(source=0, show=True)