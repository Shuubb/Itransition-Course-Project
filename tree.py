import os

def print_directory_tree(rootdir, indent=''):
    with os.scandir(rootdir) as entries:
        for entry in entries:
            if entry.name != 'node_modules' and entry.name != '.git':  # Ignore the node_modules directory
                if entry.is_dir():
                    print(f"{indent}├── {entry.name}/")
                    print_directory_tree(entry.path, indent + '│   ')
                else:
                    print(f"{indent}├── {entry.name}")

react_project_directory = "."

print(f"{os.path.basename(react_project_directory)}/")
print_directory_tree(react_project_directory)