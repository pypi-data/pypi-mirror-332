import cv2
import numpy as np
import tifffile as tiff
import torch
from torch.utils.data import Dataset

from tests import DATASETS  # Import shared dataset list


class BBBCDataset(Dataset):
    """
    PyTorch-compatible dataset for loading BBBC datasets with full 3D support.

    - Supports both 2D and 3D images.
    - Optionally applies transformations (PyTorch `torchvision.transforms`).
    - Returns (image, label) pairs where available.

    Args:
        dataset_cls: The BBBC dataset class to load.
        transform (callable, optional): Optional transform to apply to images.
        target_transform (callable, optional): Optional transform for labels.
    """

    def __init__(self, dataset_cls, transform=None, target_transform=None):
        self.dataset = dataset_cls()
        self.image_paths = self.dataset.get_image_paths()
        self.label_path = self.dataset.get_label_paths()

        if not self.image_paths:
            raise RuntimeError(f"No images found in {dataset_cls.__name__}")

        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_path = self.image_paths[idx]
        image = self.load_image(image_path)

        label = None
        if self.label_path:
            label = self.load_image(self.label_path)

        # Apply transforms if provided
        if self.transform:
            image = self.transform(image)
        if self.target_transform and label is not None:
            label = self.target_transform(label)

        return image, label

    def load_image(self, image_path):
        """
        Loads an image (2D or full 3D) and converts it to a PyTorch tensor.
        """
        if image_path.endswith((".tif", ".tiff")):
            img = tiff.imread(image_path)  # Load 3D TIFF or 2D image
        else:
            img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)  # Load 2D image

        if img is None:
            raise ValueError(f"Error: Could not read image {image_path}")

        # Normalize grayscale images
        img = (img - np.min(img)) / (np.max(img) - np.min(img) + 1e-8)

        # Convert to tensor
        if len(img.shape) == 2:  # 2D grayscale image
            img = torch.tensor(img, dtype=torch.float32).unsqueeze(0)  # (C, H, W)
        elif len(img.shape) == 3:  # 3D volume (Z, H, W)
            img = torch.tensor(img, dtype=torch.float32).unsqueeze(0)  # (C, Z, H, W)

        return img


class DatasetManager:
    """
    Manages all BBBC datasets and provides utilities.

    - Lists available datasets.
    - Loads datasets dynamically as PyTorch Datasets.
    - Displays dataset information.
    """

    @staticmethod
    def list_available_datasets(filter_3d=None):
        """
        Lists all available BBBC datasets without downloading them.
        :param filter_3d: If True, lists only 3D datasets. If False, lists only 2D datasets. If None, lists all datasets.
        """
        print("📂 Available BBBC Datasets:")
        filtered_datasets = DatasetManager.filter_datasets(filter_3d)
        for dataset_cls in filtered_datasets:
            print(
                f"- {dataset_cls.__name__}: {dataset_cls.__doc__.splitlines()[1].strip()}"
            )

    @staticmethod
    def get_dataset(name, transform=None, target_transform=None):
        """
        Loads a dataset by name.

        Args:
            name (str): The dataset class name (e.g., "BBBC003").
            transform: Optional image transformations.
            target_transform: Optional label transformations.

        Returns:
            BBBCDataset instance.
        """
        for dataset_cls in DATASETS:
            if dataset_cls.__name__ == name:
                return BBBCDataset(dataset_cls, transform, target_transform)

        raise ValueError(
            f"Dataset {name} not found. Use DatasetManager.list_datasets() to see available datasets."
        )

    @staticmethod
    def filter_datasets(filter_3d=None):
        """
        Filters the datasets based on whether they are 2D, 3D, or both.
        :param filter_3d: If True, filters only 3D datasets. If False, filters only 2D datasets. If None, includes all datasets.
        :return: Filtered list of dataset classes.
        """
        if filter_3d is None:
            return DATASETS
        return [
            dataset_cls for dataset_cls in DATASETS if dataset_cls().is_3d == filter_3d
        ]


if __name__ == "__main__":
    # Example Usage
    DatasetManager.list_available_datasets()

    # Load a dataset
    dataset = DatasetManager.get_dataset("BBBC003")
    print(f"\nLoaded {len(dataset)} samples from BBBC003")
