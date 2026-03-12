import os

class VITONDataset:

    def __init__(self, root="datasets/test"):
        self.root = root

        self.image_dir = os.path.join(root, "image")
        self.cloth_dir = os.path.join(root, "cloth")

        if not os.path.exists(self.image_dir):
            print("Warning: image directory not found")

        if not os.path.exists(self.cloth_dir):
            print("Warning: cloth directory not found")

        self.images = os.listdir(self.image_dir) if os.path.exists(self.image_dir) else []
        self.cloths = os.listdir(self.cloth_dir) if os.path.exists(self.cloth_dir) else []

        print("Dataset initialized")
        print("Images found:", len(self.images))
        print("Clothes found:", len(self.cloths))


    def __len__(self):
        return len(self.images)


    def __getitem__(self, idx):
        img_name = self.images[idx]

        return {
            "image_name": img_name
        }