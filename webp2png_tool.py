import os
import sys
from PIL import Image
from tqdm import tqdm

# Platform-specific "press any key" implementation
def press_any_key_to_exit():
    print("\nPress any key to exit...", end='', flush=True)
    try:
        # Windows
        import msvcrt
        msvcrt.getch()
    except ImportError:
        # Unix/Linux/Mac
        import termios
        import tty

        def getch():
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                return sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        getch()

def get_directory_input(prompt):
    while True:
        directory = input(prompt).strip('"')
        if os.path.isdir(directory):
            return directory
        else:
            print("Directory not found. Please try again.\n")

def convert_webp_to_png(source_dir, target_dir):
    webp_files = [f for f in os.listdir(source_dir) if f.lower().endswith('.webp')]
    
    if not webp_files:
        print("No .webp files found in the source directory.")
        return
    
    print(f"\n{len(webp_files)} file(s) are being converted...\n")

    for file in tqdm(webp_files, desc="Converting", unit="file"):
        source_path = os.path.join(source_dir, file)
        target_file_name = os.path.splitext(file)[0] + '.png'
        target_path = os.path.join(target_dir, target_file_name)

        try:
            with Image.open(source_path) as img:
                img.save(target_path, 'PNG')
        except Exception as e:
            print(f"Failed to convert {file}: {e}")
    
    print(f"\n{len(webp_files)} file(s) have been converted successfully!")

if __name__ == "__main__":
    print("=== WEBP to PNG Converter ===")
    source = get_directory_input("Enter the path to the folder containing .webp files: ")
    destination = get_directory_input("Enter the path to the folder to save .png files: ")
    
    convert_webp_to_png(source, destination)
    press_any_key_to_exit()
