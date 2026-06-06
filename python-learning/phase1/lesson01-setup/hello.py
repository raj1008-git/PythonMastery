def greet(name: str) -> str:
    """Return a professional greeting string."""
    return f"Hello, {name}! Welcome to python."


def main() -> None:
    """Entry Point of the Script."""
    message = greet("Raj")
    print(message)
    
if __name__ == "__main__":
    main()
    
