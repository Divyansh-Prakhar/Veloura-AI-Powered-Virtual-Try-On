# Veloura – AI-Powered Virtual Try-On

## Project Description
**Veloura** is a research-oriented project that explores the integration of modern computer vision and deep learning techniques to create an **AI-powered virtual try-on system**. The system allows a user to visualize how a garment would appear on a person using only a **single image of the person and a clothing image**.

The primary objective of this project is to investigate how **2D virtual try-on models and 3D human reconstruction techniques** can be combined into a unified pipeline. Traditional virtual try-on systems focus only on generating 2D images. Veloura extends this concept by also reconstructing a **3D human mesh**, enabling further visualization, rendering, and potential applications in immersive environments.

The project integrates multiple state-of-the-art models and tools, including **VITON-HD for high-resolution garment transfer, ECON for 3D human reconstruction, and SMPL-X for parametric human body modeling**. These components are combined to produce both **realistic 2D try-on images and reconstructed 3D human models**, which can then be visualized using **Blender**.

Through this project, we analyze challenges such as **garment alignment, pose estimation, mesh reconstruction, texture mapping, and multi-model pipeline integration**. The work also highlights practical issues in deploying such systems, including dependency management, computational constraints, and rendering limitations.

Veloura serves as both a **research prototype and a technical exploration** of virtual try-on systems that could eventually be used in **e-commerce platforms, virtual fashion experiences, AR/VR applications, and digital avatar generation**.

---

## Motivation
Online fashion platforms face a significant challenge due to high product return rates caused by uncertainty in fit and appearance. Virtual try-on systems aim to address this problem by allowing users to visualize clothing on a digital representation of themselves before purchasing.

Veloura investigates how modern **Virtual Try-On Networks (VTON)** and **3D reconstruction pipelines** can be integrated to create more immersive and realistic try-on experiences.

---

## Applications
- E-commerce virtual fitting rooms  
- Digital fashion visualization  
- AR/VR avatar customization  
- Gaming and metaverse character styling  
- Reducing return rates in online retail  

---

## System Architecture

### Input
The system requires two inputs:
- A **person image** (frontal view)
- A **target clothing image**

### Stage 1: 2D Virtual Try-On
The first stage generates a realistic try-on image using **VITON-HD**.

Processes involved:
- Human parsing and segmentation  
- Pose estimation  
- Garment warping and alignment  
- Image synthesis for realistic clothing transfer  

### Stage 2: 3D Human Reconstruction
The generated image is used to reconstruct a **3D human mesh** using **ECON**.

Key steps include:
- Surface normal estimation  
- Depth reconstruction  
- Mesh generation using SMPL-X body models  

### Stage 3: Visualization
The reconstructed mesh is imported into **Blender** for visualization and rendering.

Operations performed:
- Mesh import and scene setup  
- Texture projection experiments  
- Rendering of reconstructed 3D avatars  

---

## Technology Stack

### Programming
- Python

### Deep Learning Frameworks
- PyTorch  
- PyTorch3D  

### Computer Vision
- OpenCV  
- MediaPipe (pose estimation)

### Models
- **VITON-HD** – High-resolution virtual try-on generation  
- **ECON** – Single-image 3D human reconstruction  
- **SMPL-X** – Parametric human body model  

### Visualization
- Blender  

---

## Results
The project successfully demonstrates the integration of multiple AI pipelines.

Key outcomes:
- Realistic **2D virtual try-on image generation**
- Successful **3D human mesh reconstruction**
- Experimental **3D visualization using Blender**

Observed limitations:
- Texture mapping and UV alignment challenges  
- High computational cost on CPU-only systems  
- Complexity in integrating multiple models and frameworks  

---

## Challenges
Several technical challenges were encountered:

- Integration of multiple deep learning pipelines  
- Dependency and environment setup issues  
- Texture projection and UV mapping difficulties  
- Slow inference due to lack of GPU acceleration  

---

## Future Work
Potential improvements include:

- Developing a more robust texture mapping pipeline  
- Automating the full end-to-end workflow  
- Enabling GPU acceleration for faster processing  
- Improving mesh realism and garment simulation  
- Deploying the system as a web or mobile application  

---

## Project Status
Research prototype – ongoing development and experimentation.
