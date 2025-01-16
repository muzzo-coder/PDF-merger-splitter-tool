import os
import PyPDF2
from tkinter import Tk, filedialog, Button, Label
import sqlite3
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def merge_pdfs(output_path, *pdf_paths):
    merger = PyPDF2.PdfMerger()
    try:
        for pdf in pdf_paths:
            merger.append(pdf)
        merger.write(output_path)
        merger.close()
        logging.info(f"Merged PDFs into {output_path}")
    except Exception as e:
        logging.error(f"Error merging PDFs: {e}")
        print(f"Error: {e}")

def split_pdf(input_path, output_dir):
    try:
        with open(input_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for i, page in enumerate(reader.pages):
                writer = PyPDF2.PdfWriter()
                writer.add_page(page)
                output_file = os.path.join(output_dir, f"page_{i + 1}.pdf")
                with open(output_file, "wb") as output:
                    writer.write(output)
                logging.info(f"Saved split page to {output_file}")
    except Exception as e:
        logging.error(f"Error splitting PDF: {e}")
        print(f"Error: {e}")

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class CalculatorHistory:
    def __init__(self, db_name="history.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS history (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   operation TEXT,
                   operands TEXT,
                   result TEXT,
                   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )"""
        self.conn.execute(query)
        self.conn.commit()

    def save_operation(self, operation, operands, result):
        query = "INSERT INTO history (operation, operands, result) VALUES (?, ?, ?)"
        self.conn.execute(query, (operation, operands, result))
        self.conn.commit()

    def fetch_history(self):
        query = "SELECT * FROM history"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    # Console UI
    print("PDF and Calculator Utility")
    print("1. Merge PDFs")
    print("2. Split PDF")
    print("3. Calculator")
    print("4. View Calculator History")
    choice = input("Choose an option: ")

    if choice == "1":
        output_path = input("Enter output PDF path: ")
        pdf_paths = input("Enter paths to PDFs to merge (comma-separated): ").split(",")
        merge_pdfs(output_path, *pdf_paths)

    elif choice == "2":
        input_path = input("Enter input PDF path: ")
        output_dir = input("Enter output directory for split pages: ")
        split_pdf(input_path, output_dir)

    elif choice == "3":
        calc = Calculator()
        history = CalculatorHistory()
        print("Calculator Options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        calc_choice = input("Choose an operation: ")
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        try:
            if calc_choice == "1":
                result = calc.add(a, b)
                operation = "Add"
            elif calc_choice == "2":
                result = calc.subtract(a, b)
                operation = "Subtract"
            elif calc_choice == "3":
                result = calc.multiply(a, b)
                operation = "Multiply"
            elif calc_choice == "4":
                result = calc.divide(a, b)
                operation = "Divide"
            else:
                print("Invalid choice")
                exit()

            print(f"Result: {result}")
            history.save_operation(operation, f"{a}, {b}", str(result))

        except Exception as e:
            logging.error(f"Calculation error: {e}")
            print(f"Error: {e}")

        history.close()

    elif choice == "4":
        history = CalculatorHistory()
        for row in history.fetch_history():
            print(row)
        history.close()

    else:
        print("Invalid option")
