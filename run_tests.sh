#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the test suite
python -m pytest test_app.py --disable-warnings
RESULT=$?

# Return 0 if tests passed, 1 otherwise
if [ $RESULT -eq 0 ]; then
  exit 0
else
  exit 1
fi
