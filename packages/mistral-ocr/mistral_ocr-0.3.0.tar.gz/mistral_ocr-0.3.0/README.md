# Mistral OCR

A command-line tool for performing OCR (Optical Character Recognition) using Mistral.

## Installation

You can install this package directly from the repository:

```bash
pip install .
```

Or if you want to install in development mode:

```bash
pip install -e .
```

## Prerequisites

This package requires Tesseract OCR to be installed on your system:

### macOS
```bash
brew install tesseract
```

### Ubuntu/Debian
```bash
sudo apt-get install tesseract-ocr
```

### Windows
Download and install from: https://github.com/UB-Mannheim/tesseract/wiki

## Usage

After installation, you can use the `mistral-ocr` command from anywhere:

```bash
mistral-ocr path/to/image.jpg
```

Options:
- `-o, --output`: Specify output file (default: prints to stdout)
- `-v, --verbose`: Increase output verbosity

Example:
```bash
mistral-ocr image.jpg -o extracted_text.txt
```

## License

This project is licensed under the MIT License.
