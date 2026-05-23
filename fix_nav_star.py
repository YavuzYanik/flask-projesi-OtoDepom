import os

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = 'app/templates/'

# base.html fixes
replace_in_file(base_dir + 'base.html', [
    # 1. Oto text
    ('class="fa-solid fa-car-side text-white me-2"', 'class="fa-solid fa-car-side text-theme me-2"'),
    ('style="color: white; letter-spacing: -0.5px;">Oto<', 'class="text-theme" style="letter-spacing: -0.5px;">Oto<'),
    # 2. Hamburger menu
    ('class="fa-solid fa-bars text-white"', 'class="fa-solid fa-bars text-theme"'),
    # 3. JS Reset Color
    ("icon.style.color = 'var(--text-color)';", "icon.style.color = '#4b5563';")
])

# index.html and products.html fixes
replace_in_file(base_dir + 'main/index.html', [
    ('color: var(--text-color); font-size: 1rem;', 'color: #4b5563; font-size: 1rem;')
])

replace_in_file(base_dir + 'main/products.html', [
    ('color: var(--text-color); font-size: 1rem;', 'color: #4b5563; font-size: 1rem;')
])

print("Fixes applied successfully!")
