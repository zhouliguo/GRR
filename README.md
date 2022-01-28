# GRR Face Detection
Image Grid Recognition and Regression Fast and Accurate Face Detection

This repository is under building

C++ Version
https://github.com/zhouliguo/FaceDetection

## Download

Model: https://drive.google.com/drive/folders/1niPITB5tU4aC-NDy4mkAmzePkYeKfXxV?usp=sharing

## Test
### Evaluate WIDER FACE
1. Modify the input path, output path and model path in eval_wider.py
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
