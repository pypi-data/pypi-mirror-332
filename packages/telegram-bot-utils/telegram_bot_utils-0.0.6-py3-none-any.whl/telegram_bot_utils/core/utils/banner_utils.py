def load_and_print_banner(file_path):
    try:
        with open(file_path, 'r') as file:
            banner = file.read()
            return banner
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")