def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("I am number 1\n")
            file.write("23-04-2023\n")
            file.write("Another line here\n")
        print("File 'my_file.txt' created and initial content written successfully.")
    except IOError as e:
        print("Error occurred while creating the file:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("File creation process completed.\n")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of 'my_file.txt':")
            for line in file:
                print(line.strip())
        print("\nFile reading completed successfully.")
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to read the file.")
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("File reading process completed.\n")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("98765\n")
            file.write("One more line appended\n")
        print("Content appended to 'my_file.txt' successfully.")
    except IOError as e:
        print("Error occurred while appending to the file:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
    finally:
        print("File appending process completed.\n")

def main():
    create_file()
    read_file()
    append_to_file()

if __name__ == "__main__":
    main()
