import datetime
import os
import argparse

def tree(directory, exclude=None, output_file="output.txt", indent="", list_type="file"):
    if exclude is None:
        exclude = []
    
    with open(output_file, "w", encoding="utf-8") as f:
        def walk(dir_path, level_indent):
            entries = sorted(os.listdir(dir_path))
            
            for entry in entries:
                full_path = os.path.join(dir_path, entry)
                if entry in exclude or any(os.path.abspath(full_path).startswith(os.path.abspath(e)) for e in exclude):
                    continue
                
                # If 'folder' type, list only directories, if 'file' type, list both
                if list_type == "folder" and not os.path.isdir(full_path):
                    continue
                elif list_type == "file" and os.path.isdir(full_path):
                    # For 'file' type, include directories as well
                    f.write(f"{level_indent}{entry}/\n")
                    walk(full_path, level_indent + "    ")
                    continue
                
                # For 'file' type, write file entries
                f.write(f"{level_indent}{entry}\n")
        
        f.write(f"{directory}\n")
        walk(directory, indent)

def parse_args():
    parser = argparse.ArgumentParser(description="Generate a directory tree listing.")
    parser.add_argument("-i", "--input_folder", type=str, default=".", help="Input folder to start the tree generation.")
    parser.add_argument("-e", "--exclude", type=str, nargs="*", default=["venv", "__pycache__", ".git", ".exclude"], help="List of files/folders to exclude.")
    parser.add_argument("-o", "--output_file", type=str, default=f"{datetime.datetime.now().strftime('%Y-%m-%d')}.txt", help="Output file to write the tree structure.")
    parser.add_argument("-t", "--type", choices=["file", "folder"], default="file", help="Type of entries to list. 'folder' lists only directories, 'file' lists files and directories.")
    return parser.parse_args()

def read_exclude_file():
    exclude_file = ".exclude"
    if os.path.exists(exclude_file):
        with open(exclude_file, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

def main():
    args = parse_args()
    exclude_list = args.exclude + read_exclude_file()
    tree(args.input_folder, exclude=exclude_list, output_file=args.output_file, list_type=args.type)
    print(f"Tree structure generated and saved to {args.output_file}")

if __name__ == "__main__":
    main()