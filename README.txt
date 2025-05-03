Moon Payload Injector
----------------------

A simple Python tool that injects payloads into a URL parameter and checks for reflection in the response.
This is useful for basic reconnaissance and testing for vulnerabilities like XSS or SQLi.

Usage:
------

1. Install Python (3.x recommended)
2. Run the script:

   python moon_payload_injector.py

3. Enter a target URL like:
   https://example.com/search?q=test

   Replace 'test' with the parameter where payloads should be injected.

Requirements:
-------------
- requests (install via pip if not available)

   pip install requests

Files:
------
- moon_payload_injector.py  --> Main script
- payloads.txt              --> List of payloads used for testing
