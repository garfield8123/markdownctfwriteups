import os

def generate_sidebar(root_dir="docs", indent=0):
    sidebar_lines = []
    items = sorted(os.listdir(root_dir))  # sort alphabetically

    for item in items:
        full_path = os.path.join(root_dir, item)
        # Skip hidden files/folders and files with _
        if "_" in item:
            continue

        if os.path.isdir(full_path):
            # Folder: create a parent entry
            folder_name = item.replace("-", " ").replace("_", " ").title()
            sidebar_lines.append("  " * indent + f"* {folder_name}")
            # Recurse into folder
            sidebar_lines.extend(generate_sidebar(full_path, indent + 1))
        elif os.path.isfile(full_path) and item.endswith(".md"):
            # Markdown file: add link
            # Use relative path from root_dir
            relative_path = os.path.relpath(full_path, start="docs")
            file_name = os.path.splitext(item)[0].replace("-", " ").title()
            sidebar_lines.append("  " * indent + f"* [{file_name}]({relative_path})")
    return sidebar_lines

# Generate sidebar
sidebar_content = generate_sidebar("docs")

# Write to _sidebar.md
with open("docs/_sidebar.md", "w", encoding="utf-8") as f:
    f.write("\n".join(sidebar_content))

print("Sidebar generated successfully!")