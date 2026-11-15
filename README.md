# Daily coding practice

This repository contains separate, isolated environments for Python and PySpark practice.

## Set up

Run PowerShell from the repository root:

```powershell
.\setup.ps1
```

The script creates a virtual environment in each practice folder and installs its listed dependencies. Python 3.11 or newer is required. Running PySpark locally also requires Java 17 or newer.

## Run a practice example

```powershell
.\python_practice\.venv\Scripts\python.exe .\python_practice\practice.py
.\pyspark_practice\.venv\Scripts\python.exe .\pyspark_practice\practice.py
```

Add your own dated scripts to either folder and run them with that folder's virtual-environment Python executable.
