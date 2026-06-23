#!/usr/bin/env python3
import os
import rasterio
import numpy as np
import matplotlib.pyplot as plt


def load_image(path: str):
    with rasterio.open(path) as src:
        return src.read()


def calculate_ndvi(red_band: np.ndarray, nir_band: np.ndarray) -> np.ndarray:
    return (nir_band - red_band) / (nir_band + red_band + 1e-6)


def main():
    # Placeholder example using synthetic data
    red = np.random.rand(100, 100)
    nir = np.random.rand(100, 100)
    ndvi = calculate_ndvi(red, nir)
    plt.imshow(ndvi, cmap='RdYlGn')
    plt.colorbar(label='NDVI')
    plt.title('Sample NDVI Calculation')
    # Ensure results directory exists
    os.makedirs('results', exist_ok=True)
    plt.savefig('results/sample_ndvi.png')


if __name__ == '__main__':
    main()
