# atai-url-tool

atai-url-tool is a command-line interface (CLI) tool that fetches a URL and determines its content type, mapping it to a simplified type. It’s designed to quickly check the MIME type of a URL and categorize it accordingly.

## Features
- **Fetch URL Headers:** Uses an HTTP GET request to retrieve the `Content-Type` header.
- **Simplified Type Mapping:** Maps detailed MIME types (e.g., `application/pdf`, `audio/mpeg`) to simple labels like `pdf`, `mp3`, etc.
- **Easy-to-Use CLI:** Run the tool directly from your terminal with a single command.

## Installation

You can install atai-url-tool via pip (once published on PyPI):

```bash
pip install atai-url-tool
```

Alternatively, clone the repository and install it locally:

```bash
git clone https://github.com/AtomGradient/atai-url-tool.git
cd atai-url-tool
pip install .
```

## Usage

Run atai-url-tool from the command line with the URL you want to check:

```bash
atai-url-tool https://example.com/sample.pdf
```

The tool will output the fetched content type and the simplified result. For example:

```bash
{"type": "pdf", "path": "https://example.com/sample.pdf"}
```

## Development

To contribute or modify atai-url-tool:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AtomGradient/atai-url-tool.git
   cd atai-url-tool
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Make your changes, write tests, and submit a pull request.**

## License

atai-url-tool is released under the MIT License. See the [LICENSE](LICENSE) file for details.
