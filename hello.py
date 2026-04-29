import sys

def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to GitHub."

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "Omprakash"
    print(greet(name))
