# 👗 Veloura – AI-Powered Virtual Try-On  
### *AI-Powered Virtual Try-On*

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red?logo=pytorch)
![Computer Vision](https://img.shields.io/badge/Computer%20Vision-VTON-green)
![Blender](https://img.shields.io/badge/Blender-3D%20Rendering-orange?logo=blender)
![Status](https://img.shields.io/badge/Status-Research%20Project-yellow)

---

## 📌 Overview  
**Veloura** is an AI-powered virtual try-on system that enables users to visualize clothing on a person from a single image.  
It integrates 2D try-on generation and 3D human reconstruction into a unified pipeline, focusing on realism, alignment, and system integration challenges.

---

## 🎯 Use Case  

- 🛍️ Try clothes virtually before purchasing  
- 👕 Visualize outfits instantly  
- 🧑‍🎨 Create styled digital avatars  
- 🕶️ Applications in AR/VR and gaming  
- 📦 Reduce return rates in e-commerce  

---

## 🧠 Key Features  

- High-resolution **2D virtual try-on (VITON-HD)**  
- **3D human reconstruction (ECON)** from a single image  
- Pose-aware garment alignment and warping  
- Blender-based 3D visualization  
- End-to-end multi-model pipeline  

---

## 🏗️ Tech Stack  

### 🔹 Languages & Frameworks  
- Python  
- PyTorch  
- OpenCV  

### 🔹 Models Used  
- **VITON-HD** – High-resolution 2D try-on  
- **ECON** – 3D human reconstruction  
- **SMPL-X** – Human body modeling  

### 🔹 Tools  
- Blender (rendering & visualization)  
- PyTorch3D  
- MediaPipe (pose estimation)  

---

## ⚙️ Pipeline  

### 🔄 Workflow  

1. **Input**  
   - Person image (front view)  
   - Target clothing image  

2. **2D Try-On (VITON-HD)**  
   - Segmentation and pose estimation  
   - Garment warping and alignment  
   - Realistic try-on image generation  

3. **3D Reconstruction (ECON)**  
   - Normal map estimation  
   - Depth reconstruction  
   - Mesh generation  

4. **Visualization (Blender)**  
   - Import reconstructed mesh  
   - Attempt texture projection  
   - Render 3D output  

---

## 📊 Results  

- ✅ Realistic 2D try-on outputs  
- ✅ Successful 3D mesh reconstruction  
- ⚠️ Texture projection not fully successful  
- ⚠️ CPU-based execution resulted in slow performance  

---

## ⚠️ Challenges  

- Texture mapping and UV projection issues  
- Integration of multiple pipelines  
- Dependency and environment setup complexity  
- High computation time without GPU  

---

## 🚀 Future Work  

- Improve texture mapping pipeline  
- Automate integration workflow  
- Enable GPU acceleration  
- Enhance realism and rendering quality  
- Deploy as a web/mobile application  

---
