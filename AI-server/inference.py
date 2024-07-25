import onnxruntime as ort
import subprocess

from pathlib import Path
from PIL import Image
import torch
import torchvision.transforms as transforms
from torchvision.transforms import InterpolationMode

data_path = Path("data/")
image_path = data_path / "cat1.jpg"
img = Image.open(image_path) # PIL


# Define the transformation pipeline using transforms.Compose
transform_pipeline = transforms.Compose([
    transforms.Resize(256, interpolation=InterpolationMode.BICUBIC),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
print(type((transform_pipeline(img).unsqueeze(dim = 0)).numpy()))
inputs_array = (transform_pipeline(img).unsqueeze(dim = 0)).numpy()


model_path = "./model/efficientnet_b0.onnx"

sess_options = ort.SessionOptions()

# Check device available
try:
    subprocess.check_output('nvidia-smi')
    print('Nvidia GPU is available.')
    DEVICE: str = 'GPU'
except:
    print('No Nvidia GPU available.')
    DEVICE: str = 'CPU'


# Run inference
# ort_inputs = ort.OrtValue.ortvalue_from_numpy(inputs, "cuda", 0)
if DEVICE.lower() == "gpu":
    print("GPU")
    ort_session = ort.InferenceSession(model_path, providers=['AzureExecutionProvider'])
    ort_inputs = {ort_session.get_inputs()[0].name: inputs_array}
    ort_outs = ort_session.run(None, ort_inputs) # result of model
    target_image_pred_probs = ort_outs[0]
    target_image_pred_probs = torch.tensor(target_image_pred_probs)

    top4_values, top4_indices = torch.topk(target_image_pred_probs, 4)
    top4_values_list = list(round(float(v), 4) for v in top4_values[0].cpu().numpy())
    top4_indices_list = list(top4_indices[0].cpu().numpy())

    print(top4_indices_list)
elif DEVICE.lower() == "cpu":
    print("CPU")
    ort_session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])
    ort_inputs = {ort_session.get_inputs()[0].name: inputs_array}
    ort_outs = ort_session.run(None, ort_inputs)
    target_image_pred_probs = ort_outs[0]
    target_image_pred_probs = torch.tensor(target_image_pred_probs)

    top4_values, top4_indices = torch.topk(target_image_pred_probs, 4)
    top4_values_list = list(round(float(v), 4) for v in top4_values[0].cpu().numpy())
    top4_indices_list = list(top4_indices[0].cpu().numpy())
    