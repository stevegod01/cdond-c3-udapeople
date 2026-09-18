"""Bounded endpoint probes; tests inject responses and never contact the network."""
import argparse
import json
import time
import urllib.error
import urllib.request


def check(url, kind, attempts=12, delay=5, opener=urllib.request.urlopen, sleep=time.sleep):
    """Require a successful HTTP status and the correct service content."""
    if attempts < 1:
        raise ValueError("attempts must be positive")
    last_error = "No response"
    for attempt in range(attempts):
        try:
            with opener(url, timeout=10) as response:
                status = response.status
                body = response.read(1024 * 1024).decode("utf-8")
            if not 200 <= status < 300:
                raise ValueError(f"HTTP {status}")
            if kind == "backend":
                if json.loads(body).get("status") != "ok":
                    raise ValueError("Backend status is not ok")
            elif '<div id="root"' not in body and "<div id='root'" not in body:
                raise ValueError("Frontend application root is missing")
            return
        except (OSError, ValueError, AttributeError, urllib.error.URLError) as error:
            last_error = str(error)
            if attempt + 1 < attempts:
                sleep(delay)
    raise RuntimeError(f"{kind} smoke test failed after {attempts} attempt(s): {last_error}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=["backend", "frontend"])
    parser.add_argument("url")
    args = parser.parse_args()
    check(args.url, args.kind)
    print(f"{args.kind} smoke test passed")
