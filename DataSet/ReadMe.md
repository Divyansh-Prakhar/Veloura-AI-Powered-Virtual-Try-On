## Dataset

This project uses the **VITON-HD dataset**, a high-resolution virtual try-on dataset containing images of people and corresponding clothing items.

The dataset includes:
- Person images
- Clothing images
- Clothing masks
- Parsing and pose annotations used for training and testing the virtual try-on pipeline.

Due to GitHub file size limitations, the dataset is **not included** in this repository.

You can download the dataset from the link below:

**Dataset Download:**  
https://drive.google.com/file/d/1fVSLY91uP7kfTeN1Ubb0kD3wIcTnI9fl/view?usp=drive_link

After downloading, extract the dataset into the `datasets/` directory so the structure looks like this:

```
datasets/
│
├── train/
│   ├── image/
│   ├── cloth/
│   └── cloth-mask/
│
└── test/
    ├── image/
    ├── cloth/
    └── cloth-mask/
```

This directory structure is used by the dataset loader to supply person images and clothing items to the virtual try-on pipeline.
