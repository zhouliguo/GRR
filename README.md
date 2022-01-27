# GRR Face Detection
Image Grid Recognition and Regression

This repository is under building

## Download

Model: https://drive.google.com/file/d/1CdAYQFW93naWBTLBsD9vy8oZXJ5SKpr3/view?usp=sharing

Light Model for Non-CUDA device: https://github.com/zhouliguo/GRR/blob/main/weights/torchscript_lightmodel.pt

## Test
### Evaluate WIDER FACE
1. Modify the input path, output path and model path in eval.py
2. cd GRR, run python eval.py

### Detect Demo
1. cd GRR, run python detect.py --image-path='image_path'

### Speed Test on CPU
1. Build a Visul Studio C++ project with OpenCV and LibTorch
2. Complie detect.cpp

## Train

## Comparison of Accuracy

### WIDER FACE
<img src="https://github.com/zhouliguo/GRR/blob/main/figures/wider.png">

### DarkFace, DFD and MAFA
<img src="https://github.com/zhouliguo/GRR/blob/main/figures/ddm.png">

## Comparison of Speed

### Light Model on Intel i7-5930K CPU
<img src="https://github.com/zhouliguo/GRR/blob/main/figures/light.png">

## Detection examples

### WIDER FACE
<img src="https://github.com/zhouliguo/GRR/blob/main/figures/wider_example.png">

### DARK FACE
<img src="https://github.com/zhouliguo/GRR/blob/main/figures/dark_example.png">
