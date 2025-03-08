"""Command line interface for Mistral OCR."""

import argparse
import sys
from pathlib import Path
import os
from mistralai import Mistral
from dotenv import load_dotenv
import base64

def process_image(client, image_path):
    """Process an image file with OCR."""
    with open(image_path, "rb") as f:
        file_content = f.read()
        
    document = {
        "type": "image_url",
        "image_url": f"data:image/{image_path.suffix[1:]};base64,{base64.b64encode(file_content).decode('utf-8')}"
    }
    
    return client.ocr.process(
        model="mistral-ocr-latest",
        document=document,
        include_image_base64=False
    )

def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(description='Extract text from images using Mistral OCR')
    parser.add_argument('input', type=str, help='Input image file or directory')
    parser.add_argument('-o', '--output', type=str, help='Output file (default: stdout)', default="mistral_ocr_output.txt")
    parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')
    
    args = parser.parse_args()
    
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY not found in .env file", file=sys.stderr)
        sys.exit(1)
    
    # Initialize Mistral client
    client = Mistral(api_key=api_key)
    
    # Process input path
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input path '{args.input}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    if not input_path.is_file():
        print(f"Error: '{args.input}' is not a file", file=sys.stderr)
        sys.exit(1)
        
    print(f"Processing image: {input_path.absolute()}")
    
    try:
        # Process the image
        ocr_response = process_image(client, input_path)
        
        if ocr_response and ocr_response.pages:
            # Write output
            output_path = Path(args.output)
            with open(output_path, 'w', encoding='utf-8') as f:
                for page in ocr_response.pages:
                    f.write(page.markdown)
            print(f"Successfully saved OCR output to: {output_path.absolute()}")
        else:
            print("Error: OCR processing failed or returned no content", file=sys.stderr)
            sys.exit(1)
            
    except Exception as e:
        print(f"Error during OCR processing: {e}", file=sys.stderr)
        sys.exit(1)
    
if __name__ == '__main__':
    main() 