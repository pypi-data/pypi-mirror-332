import argparse
import json
from playwright.sync_api import sync_playwright
from atai_url_tool.headers import get_headers

CONTENT_TYPE_MAP = [
    {"key": "application/pdf", "type": "pdf"},
    {"key": "audio/mpeg", "type": "mp3"},
    {"key": "audio/", "type": "audio"},  
    {"key": "video/mp4", "type": "mp4"},
    {"key": "video/", "type": "video"}, 
    {"key": "text/html", "type": "html"},
    {"key": "text/plain", "type": "text"},
    {"key": "application/json", "type": "json"},
    {"key": "application/xml", "type": "xml"},
    {"key": "image/png", "type": "image"},
    {"key": "image/jpeg", "type": "image"},
    {"key": "image/gif", "type": "image"}
]

def check_response_type(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()
            # Set extra headers using our external get_headers() function.
            page.set_extra_http_headers(get_headers())
            response = page.goto(url, timeout=15000)
            if response is None:
                browser.close()
                return {"type": False, "path": url}
            
            headers = response.all_headers()
            content_type = headers.get("content-type", "")
            browser.close()

            for mapping in CONTENT_TYPE_MAP:
                if mapping["key"] in content_type:
                    return {"type": mapping["type"], "path": url}
            return {"type": content_type or "unknown", "path": url}
    except Exception as e:
        print(f"Request error: {e}")
        return {"type": False, "path": url}

def main():
    parser = argparse.ArgumentParser(
        description="CLI tool to check a URL's content type and map it to a simplified type."
    )
    parser.add_argument("url", help="The URL to check.")
    args = parser.parse_args()

    result = check_response_type(args.url)
    # Print pure JSON output.
    print(json.dumps(result))

if __name__ == "__main__":
    main()
