import torch

from datasets import VITONDataset
from models.seg_generator import SegGenerator
from models.gmm import GMM
from models.alias_generator import ALIASGenerator


print("Starting Virtual Try-On Project")


def main():

    dataset = VITONDataset()

    print("Dataset size:", len(dataset))

    seg_model = SegGenerator()
    gmm_model = GMM()
    alias_model = ALIASGenerator()

    # dummy inputs
    person = torch.randn(1, 3, 256, 192)
    cloth = torch.randn(1, 3, 256, 192)

    seg_output = seg_model(person)

    warped_cloth = gmm_model(person, cloth)

    final_output = alias_model(person, warped_cloth)

    print("Segmentation output:", seg_output.shape)
    print("Warped cloth:", warped_cloth.shape)
    print("Final try-on image:", final_output.shape)


if __name__ == "__main__":
    main()