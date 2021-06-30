#!/bin/bash



rsync problem.md testing-dir/
rsync Dockerfile testing-dir/
rsync gen-password.py testing-dir/
rsync split-flag.py testing-dir/
rsync instructions-to-2of3.txt testing-dir/
rsync instructions-to-3of3.txt testing-dir/
rsync start.sh testing-dir/
rsync profile testing-dir/

