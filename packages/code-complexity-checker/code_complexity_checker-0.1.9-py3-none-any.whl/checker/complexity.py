import argparse
from radon.visitors import ComplexityVisitor

def get_big_o(complexity):
    if complexity == 1:
        return "O(1)"  # Constant Time
    elif 2 <= complexity <= 5:
        return "O(log n)"  # Logarithmic Time
    elif 6 <= complexity <= 10:
        return "O(n)"  # Linear Time
    elif 11 <= complexity <= 15:
        return "O(n log n)"  # Log-Linear Time
    elif 16 <= complexity <= 25:
        return "O(n^2)"  # Quadratic Time
    elif 26 <= complexity <= 35:
        return "O(n^3)"  # Cubic Time
    elif 36 <= complexity <= 50:
        return "O(2^n)"  # Exponential Time
    else:
        return "O(n!)"  # Factorial Time

def analyze_file(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()

        visitor = ComplexityVisitor.from_code(code)
        results = []

        for block in visitor.functions + visitor.classes:
            big_o = get_big_o(block.complexity)
            result = {
                "function": block.name,
                "complexity": block.complexity,
                "big_o": big_o,
                "lineno": block.lineno
            }
            results.append(result)
            print(f"Function/Class: {block.name}, Complexity: {block.complexity}, Approx. Complexity: {big_o}, Line: {block.lineno}")

        return results

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description="Analyze code complexity of a Python file.")
    parser.add_argument("--file", type=str, help="Path to the Python file")
    args = parser.parse_args()

    if args.file:
        analyze_file(args.file)
    else:
        print("Please provide a file path using --file option.")
