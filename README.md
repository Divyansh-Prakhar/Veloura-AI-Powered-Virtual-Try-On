# Veloura – AI-Powered Virtual Try-On
<img width="2697" height="1517" alt="image" src="https://github.com/user-attachments/assets/3eb67ab1-e133-4219-b8f7-feb4e6df129a" />


Veloura is an experimental **AI-powered virtual try-on system** that allows users to visualize how a garment would look on a person using only a **single image of the person and a clothing image**.  
The project investigates how modern **2D virtual try-on networks and 3D human reconstruction models** can be combined into a unified pipeline. The system produces both a **realistic 2D try-on image** and a **reconstructed 3D human mesh** for visualization.

---

## Features

Veloura integrates multiple computer vision techniques to simulate clothing transfer and human reconstruction.

- **Virtual Clothing Transfer** – Generates a realistic image of a person wearing a target garment using deep learning models.  
- **High-Resolution Try-On Generation** – Uses advanced models capable of producing detailed and visually convincing try-on results.  
- **3D Human Reconstruction** – Reconstructs a 3D mesh of the dressed person from a single generated image.  
- **3D Visualization** – Allows inspection and rendering of the reconstructed mesh using Blender.  
- **Modular Pipeline** – The system is designed as a multi-stage pipeline so that each component can be improved or replaced independently.

---
<img width="867" height="438" alt="image" src="https://github.com/user-attachments/assets/412e6701-d3ea-4e47-97eb-b00c76f7d12e" />


## System Pipeline

The system operates through a three-stage processing pipeline that combines multiple AI models.

### 1. 2D Virtual Try-On
The first stage generates a realistic try-on image using **VITON-HD**.  
This stage performs **human parsing, pose estimation, garment alignment, and image synthesis** to produce a high-quality image of the person wearing the target clothing.

### 2. 3D Human Reconstruction
The generated try-on image is passed to **ECON**, which reconstructs a **3D human mesh** using learned surface and depth information.  
The reconstruction is based on the **SMPL-X parametric human body model**, enabling structured and realistic body geometry.

### 3. Visualization
The reconstructed mesh is imported into **Blender** for rendering and inspection.  
This step enables experiments with **scene setup, lighting, and rendering** to visualize the generated 3D avatar.

---

## Tech Stack

Veloura integrates multiple tools and frameworks from computer vision, deep learning, and 3D graphics.

**Programming**
- Python – Used to implement the pipeline and integrate different models.

**Deep Learning Frameworks**
- PyTorch – Core framework used for running deep learning models.  
- PyTorch3D – Used for 3D operations and mesh-related processing.

**Computer Vision**
- OpenCV – Used for image processing and preprocessing tasks.  
- MediaPipe – Provides pose estimation and body landmark detection.

**Models**
- **VITON-HD** – Generates high-resolution virtual try-on images.  
- **ECON** – Performs single-image 3D human reconstruction.  
- **SMPL-X** – Provides a parametric representation of the human body.

**Visualization**
- Blender – Used for rendering and inspecting reconstructed meshes.

---

## Applications

Virtual try-on systems have multiple potential applications across industries.

- **E-commerce Virtual Fitting Rooms** – Allow users to preview clothing before purchasing online.  
- **Digital Fashion Visualization** – Enable designers to showcase clothing on virtual models.  
- **AR/VR Avatar Creation** – Provide realistic avatars for immersive environments.  
- **Gaming and Metaverse Customization** – Support character styling and outfit previews.

---
