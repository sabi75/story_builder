#!/usr/bin/env python
"""
Quick launcher for Children's Story Generator
Sets up environment and starts the Streamlit app
"""

import os
import sys
import subprocess

# Set API key from environment
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("❌ Error: OPENROUTER_API_KEY not set")
    print("Please set your API key first:")
    print('  $env:OPENROUTER_API_KEY = "your-key-here"')
    sys.exit(1)

print("✅ API Key configured")
print("🚀 Launching Children's Story Generator...\n")

# Set Streamlit config to skip email
config_dir = os.path.expanduser("~/.streamlit")
os.makedirs(config_dir, exist_ok=True)

config_file = os.path.join(config_dir, "credentials.toml")
if not os.path.exists(config_file):
    with open(config_file, "w") as f:
        f.write('[general]\nemails = false\n')

# Launch Streamlit
os.system('python -m streamlit run app.py --logger.level=error')
