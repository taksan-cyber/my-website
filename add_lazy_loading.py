import os
import re

def add_lazy_loading(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Find <img> tags and add loading="lazy" if not present
                new_content = re.sub(
                    r'<img\s+([^>]*?)(?<!loading=["\']lazy["\'])(/?>)',
                    r'<img \1loading="lazy"\2',
                    content,
                    flags=re.IGNORECASE
                )

                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")

if __name__ == "__main__":
    base_dir = "c:\\Users\\kusak\\Documents\\ea_mo"
    add_lazy_loading(base_dir)
