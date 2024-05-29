# qURLcode the QR Code Generator

This project provides a simple Python script to generate QR codes from a given URL and save them as both SVG and PNG files. The script prompts the user for the URL and output file name and then generates the QR codes.

## Setup

This project uses a virtual environment to manage dependencies. The setup process is automated with a `setup.sh` script.

### Prerequisites

- Python 3.x

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/k3nh/qURLcode.git
    cd qURLcode
    ```

2. **Make the setup script executable:**

    ```sh
    chmod +x setup.sh
    ```

3. **Run the setup script:**

    ```sh
    ./setup.sh
    ```

This will create a virtual environment, activate it, and install the required dependencies.

## Usage

1. **Activate the virtual environment:**

    ```sh
    source .venv/bin/activate
    ```

2. **Run the QR code generation script:**

    ```sh
    python qURLcode.py
    ```

3. **Follow the prompts:**

    - Enter the URL you want to encode.
    - Enter the desired output file name (without extension).

The script will generate two files with the given name: one in PNG format and one in SVG format.

4. **Deactivate the virtual environment (optional):**

    ```sh
    deactivate
    ```

## Files

- `qURLcode.py`: The main script that generates QR codes.
- `setup.sh`: The setup script to create a virtual environment and install dependencies.
- `README.md`: This file, providing an overview and usage instructions.

## Dependencies

The script requires the following Python packages:

- `qrcode[pil]`: For generating QR codes and saving them as PNG images.
- `qrcode[svg]`: For generating QR codes and saving them as SVG images.

These dependencies are automatically installed by the `setup.sh` script.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

