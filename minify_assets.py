import os
import re

def minify_content(content):
    # Minify CSS
    def minify_css(match):
        css = match.group(1)
        # Remove comments
        css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
        # Remove unnecessary whitespace
        css = re.sub(r'\s+', ' ', css)
        css = re.sub(r'\s*([{:;])\s*', r'\1', css)
        css = css.replace('; }', '}')
        return f'<style>{css.strip()}</style>'

    # Minify JS
    def minify_js(match):
        js = match.group(1)
        # Simple whitespace reduction (risky for complex JS, but safe for these scripts)
        # Remove single line comments
        js = re.sub(r'//.*', '', js)
        # Remove multi line comments
        js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
        # Basic whitespace cleanup
        js = re.sub(r'\s+', ' ', js)
        return f'<script>{js.strip()}</script>'

    content = re.sub(r'<style>(.*?)</style>', minify_css, content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<script>(?!.*?src=)(.*?)</script>', minify_js, content, flags=re.DOTALL | re.IGNORECASE)
    
    return content

def minify_html_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                new_content = minify_content(content)

                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Minified {filepath}")

if __name__ == "__main__":
    base_dir = "c:\\Users\\kusak\\Documents\\ea_mo"
    minify_html_files(base_dir)
