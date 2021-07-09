#!/bin/bash

set -e

service ssh start

socat tcp-listen:5555,reuseaddr,fork tcp:localhost:22

