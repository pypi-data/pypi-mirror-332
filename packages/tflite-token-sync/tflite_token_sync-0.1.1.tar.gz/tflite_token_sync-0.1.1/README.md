# TFLite Caching Token Synchronizer

[![PyPI version](https://badge.fury.io/py/tflite-token-sync.svg)](https://badge.fury.io/py/tflite-token-sync)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A utility tool to synchronize caching tokens among multiple TensorFlow Lite models, especially useful for EdgeTPU deployment.

## Overview

When deploying multiple TensorFlow Lite models on EdgeTPU devices, inconsistent caching tokens can cause unnecessary recompilation and decreased performance. This tool helps you synchronize the caching tokens across all your models to ensure optimal performance when inferencing models alternately.

## Features

- Extracts and synchronizes caching tokens across multiple TFLite models
- Option to preserve original models by creating synchronized copies
- Simple command-line interface
- Supports all TFLite models for EdgeTPU

## Installation

### Prerequisites

- Python 3.7+
- TensorFlow Lite

### Install from PyPI

The easiest way to install is via pip:

```bash
pip install tflite-token-sync
```

After installation, you can use the command `tflite-token-sync` directly from the terminal.

### Install from Source

Clone the repository and set up the environment:

```bash
git clone https://github.com/HanChangHun/tflite-token-sync.git
cd tflite-token-sync
pip install .
```

## Usage

### Using Command Line Tool

After installation from PyPI, you can use the command directly:

```bash
tflite-token-sync --models MODEL_PATH_1 MODEL_PATH_2 [MODEL_PATH_N...]
```

For preserving originals:

```bash
tflite-token-sync --models MODEL_PATH_1 MODEL_PATH_2 [MODEL_PATH_N...] -o OUTPUT_DIR
```

### Using Python Module

You can also use the Python module directly in your code:

```python
from pathlib import Path
from tflite_token_sync import TfliteTokenSync

# Initialize the synchronizer
token_sync = TfliteTokenSync(output_dir=Path("output_directory"))  # optional output_dir

# Synchronize multiple models
model_paths = [
    Path("model1.tflite"),
    Path("model2.tflite"),
    Path("model3.tflite")
]
processed_paths = token_sync.sync_caching_token(model_paths)

print(f"Models synchronized: {processed_paths}")
```

### Command Line Arguments

- `--models`: List of TFLite model paths to synchronize (required)
- `--output_dir`, `-o`: Output directory for synchronized models (optional)

## Example

Synchronize two EdgeTPU models and save the results to a specific directory:

```bash
tflite-token-sync --models test_data/models/tpu/efficientnet-edgetpu-M_quant_edgetpu.tflite \
test_data/models/tpu/mobilenet_v2_1.0_224_quant_edgetpu.tflite \
-o test_data/models/processed
```

If installed directly from the repository:

```bash
python -m tflite_token_sync --models test_data/models/tpu/efficientnet-edgetpu-M_quant_edgetpu.tflite \
test_data/models/tpu/mobilenet_v2_1.0_224_quant_edgetpu.tflite \
-o test_data/models/processed
```

## Testing Results

After synchronizing the models, you can verify the improved performance by running the models alternately:

```bash
python tests/invoke_alternately.py \
--models test_data/models/processed/efficientnet-edgetpu-M_quant_edgetpu.tflite \
test_data/models/processed/mobilenet_v2_1.0_224_quant_edgetpu.tflite
```

You should observe more consistent and potentially faster inference times when models are executed alternately, as the EdgeTPU won't need to reload compilation caches.

## How It Works

1. The tool extracts the caching token from the first model in the list
2. It then replaces the caching tokens in all other models with this token
3. When used on an EdgeTPU, these models will share the same compilation cache

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
