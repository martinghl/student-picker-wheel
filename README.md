# student-picker-wheel

## Overview
**Student Picker - Wheel of Fortune** is a fun and interactive tool to randomly select names from a list, visualized as a spinning wheel. This tool is perfect for educators or team leaders who want a fair and engaging way to select participants.

---

## Requirements
- **Python Version**: 3.8 or higher.
- **Operating System**: Windows, macOS, or Linux.

---

## Dependencies
The following Python packages are required:
- `tkinter` (bundled with Python; no separate installation needed).
- `random` (built-in with Python).
- `math` (built-in with Python).

Ensure your Python environment includes these libraries.
---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/martinghl/student-picker-wheel.git
   cd student-picker-wheel
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. No additional packages need installation as all dependencies are built-in.

---

## Usage
1. Prepare a CSV file (e.g., `students.csv`) with names. Each row should include:
   - **First Name**
   - **Last Name**
   
   Example:
   ```
   Smith, John
   Doe, Jane
   Brown, Alice
   ```

2. Update the file path in `main.py`:
   ```python
   file_path = "path_to_your_csv/students.csv"
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Enjoy the spinning wheel! Press the **SPIN** button to randomly select a name.

---

## Project Structure
- `main.py`: Entry point for the application. Reads names and starts the GUI.
- `spinner.py`: Contains logic for spinning the wheel and selecting the winner.
- `gui.py`: Handles the graphical user interface and wheel rendering.

---

## License
This project is open-source and available under the [MIT License](LICENSE).
