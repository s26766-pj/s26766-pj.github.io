# Simple Python Web Calculator

This is a minimal **Flask** web application that exposes a small calculator UI in the browser and performs calculations on the server in Python.

## Features

- **Basic operations**: addition, subtraction, multiplication and division
- **Server-side logic** in Python (Flask)
- **Friendly UI** with responsive layout
- Accepts both `.` and `,` as decimal separators

## Running locally

1. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the development server:

   ```bash
   python app.py
   ```

4. Open your browser at `http://127.0.0.1:5000/`.

## Notes

- This app is meant as a **simple example project**; feel free to extend it with more operations or history, styling, etc.
