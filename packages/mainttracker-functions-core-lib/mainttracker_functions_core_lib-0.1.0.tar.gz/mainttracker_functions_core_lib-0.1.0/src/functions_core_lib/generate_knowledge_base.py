#!/usr/bin/env python3
import pathlib
import os

# Handle environments where __file__ may not exist
try:
    current_dir = pathlib.Path(__file__).parent.absolute()
except NameError:
    current_dir = pathlib.Path(os.getcwd()).absolute()

print(f"Current directory: {current_dir}")

# Set up output directory in the parent folder
output_dir = current_dir.parents[2] / "z_knowledge_base" / "functions_core_lib"
print(f"Output directory: {output_dir}")

# Use current directory as input
input_dir = current_dir
print(f"Input directory: {input_dir}")

# Directories to ignore
IGNORED_DIRS = {".venv", ".git", "__pycache__"}

# Make sure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Walk the directory tree
for root, dirs, files in os.walk(input_dir):
    # Modify dirs in-place to skip ignored directories
    dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]

    for file in files:
        # Skip hidden files
        if file.startswith("."):
            continue

        file_path = os.path.join(root, file)

        try:
            # Skip this script itself to avoid infinite copies
            if os.path.samefile(file_path, __file__):
                continue
        except (NameError, OSError):
            # If __file__ isn't defined or file doesn't exist
            pass

        try:
            with open(file_path, "r") as f:
                # Get the relative path from input_dir
                rel_path = os.path.relpath(file_path, input_dir)

                # Create flattened filename by replacing path separators with underscores
                path_parts = rel_path.split(os.sep)
                flattened_name = "_".join(path_parts)

                # Ensure the extension is .txt
                base_name = os.path.splitext(flattened_name)[0]
                if not base_name:  # Skip if empty filename
                    continue

                flattened_name = f"{base_name}.txt"

                # Prepare output path (flat structure in output directory)
                output_file_path = os.path.join(output_dir, flattened_name)

                print(f"Copying {file_path} -> {output_file_path}")

                # Read content and write to the flattened file
                file_contents = f.read()
                with open(output_file_path, "w") as out_f:
                    out_f.write(file_contents)
        except (UnicodeDecodeError, IOError) as e:
            print(f"Skipping {file_path}: {e}")

print("Done!")
