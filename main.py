#!/usr/bin/env python3
"""ridiculous-glance-01: ridiculous at first glance, real by the second."""
import os

ENTRY = "A man in Japan makes a living being hired to do absolutely nothing, and he has a five-month waiting list."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote /output/entry.txt ({len(ENTRY)} characters)")

if __name__ == "__main__":
    main()
