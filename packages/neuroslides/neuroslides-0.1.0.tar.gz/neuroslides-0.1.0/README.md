# NeuroSlides

NeuroSlides is a Python client library for generating professional PowerPoint slides using AI. It provides a simple interface to create visually appealing presentation slides with just a few lines of code.

## Features

- Generate PowerPoint slides with AI-powered content formatting
- Support for custom titles, lessons, and key points
- Optional slide numbering
- Integration with Pexels for image content (optional)
- Simple and intuitive API

## Installation

You can install NeuroSlides using pip:

```bash
pip install neuroslides
```

## Quick Start

Here's a simple example to generate a PowerPoint slide:

```python
from neuroslides import NeuroSlidesClient
from dotenv import load_dotenv
import os

# Load environment variables (optional)
load_dotenv()

# Initialize the client
client = NeuroSlidesClient(
    api_key="your_api_key_here"  # Replace with your API key
)

# Generate a slide
pptx_content = client.generate_slide(
    title="Building Employee Wellness Programs",
    lesson="Employee wellness programs are essential for attracting and retaining talent and boosting productivity.",
    points=[
        "Effective wellness initiatives address physical, mental, emotional, and financial well-being",
        "Technology enhances the accessibility and personalization of wellness programs, promoting engagement and community."
    ],
    slide_number=9  # Optional
)

# Save the generated slide
with open("output.pptx", "wb") as f:
    f.write(pptx_content)
```

## Authentication

NeuroSlides requires an API key for authentication. You can obtain your API key by:
1. [Contact the development team for access]
2. Store your API key securely (recommended to use environment variables)

## Configuration

The `NeuroSlidesClient` can be configured with the following parameters:

- `api_key` (required): Your NeuroSlides API key
- `pexels_key` (optional): Pexels API key for enhanced image capabilities
- `base_url` (optional): Custom API endpoint URL

## API Reference

### NeuroSlidesClient

#### `generate_slide(title, lesson, points, slide_number=None)`

Generates a PowerPoint slide with the specified content.

Parameters:
- `title` (str): The title of the slide
- `lesson` (str): The main lesson or content
- `points` (list): A list of key points to include
- `slide_number` (int, optional): The slide number

Returns:
- Binary content of the generated PPTX file

## Error Handling

The library includes comprehensive error handling. API errors will raise exceptions with detailed error messages:

```python
try:
    pptx_content = client.generate_slide(...)
except Exception as e:
    print(f"Error: {e}")
```

## Requirements

- Python 3.6+
- requests
- python-dotenv (optional, for environment variable management)

## License

[Add your chosen license here]

## Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## Support

For support, please email us at muhammadsaboor119@gmail.com

## Version History

- 1.0.0 (Initial Release)
    - Basic slide generation functionality
    - Pexels integration support
    - Error handling
    - Documentation

---

Made with ❤️ by CutHours