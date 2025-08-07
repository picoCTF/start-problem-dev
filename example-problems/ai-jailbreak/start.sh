#!/bin/bash

set -e

socat tcp-listen:5555,reuseaddr,fork SYSTEM:"python3 /app/ai-interface.py",pty
