# main.py
import csv
from gui import WheelOfFortuneGUI

def read_names_from_csv(file_path):

    names = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        # If your CSV has a header row, you can skip it with:
        # next(reader, None)
        
        for row in reader:
            if len(row) >= 2:
                last_name = row[0].strip()
                first_name = row[1].strip()
                full_name = f"{first_name} {last_name}"
                names.append(full_name)

    return names

def main():
    # Update Your Path!!!!
    file_path = "path_to_your_csv/students.csv"  
    names = read_names_from_csv(file_path)
    
    # Create and run the GUI
    app = WheelOfFortuneGUI(names)
    app.run()

if __name__ == "__main__":
    main()
