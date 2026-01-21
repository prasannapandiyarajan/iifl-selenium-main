#!/bin/bash
set -e

#This is for Gnerating the report.html file
echo "Running Selenium Tests"
pytest pythonSel/test_e2eTestFramework.py

#This is for Generating the mail html contents
echo "Generating Mail HTML"
python3 pythonSel/generate_mail.py

echo "Test execution + Mail HTML generation completed"