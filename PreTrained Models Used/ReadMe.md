## Pretrained Models

This project uses pretrained weights from the **VITON-HD framework** for the main network components.  
These models were trained on the VITON-HD dataset and are used during inference to generate the final virtual try-on results.

The following pretrained models are required:

- **Segmentation Generator (`seg_final.pth`)**  
- **Geometric Matching Module (`gmm_final.pth`)**  
- **Try-On Generator / ALIAS Generator (`alias_final.pth`)**

Due to GitHub file size limitations, the pretrained weights are **not included in this repository**.

You can download the pretrained models from the link below:

**Pretrained Models Download:**  
[ADD YOUR PRETRAINED MODELS LINK HERE]

After downloading, place the files inside the `checkpoints/` directory so the structure looks like this:

```
checkpoints/
│
├── seg_final.pth
├── gmm_final.pth
└── alias_final.pth
```

These models are automatically loaded during inference by the virtual try-on pipeline.
