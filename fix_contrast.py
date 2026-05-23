import os

def replace_in_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

base_dir = 'app/templates/main/'

# favorites.html
replace_in_file(base_dir + 'favorites.html', [
    ('text-white-50', 'text-theme-muted'),
    ('text-white', 'text-theme')
])

# index.html
with open(base_dir + 'index.html', 'r', encoding='utf-8') as f:
    content = f.read()
hero_start = content.find('<div class="hero-section')
hero_end = content.find('</div>', content.find('</div>', content.find('</div>', hero_start) + 1) + 1)
hero_content = content[hero_start:hero_end]
content = content.replace(hero_content, '###HERO###')

content = content.replace('text-white-50', 'text-theme-muted')
content = content.replace('text-white', 'text-theme')

content = content.replace('###HERO###', hero_content)
with open(base_dir + 'index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# products.html
replace_in_file(base_dir + 'products.html', [
    ('background:#1a1d25', 'background:var(--surface-color)'),
    ('border:1px solid #2a2d35', 'border:1px solid var(--border-color)'),
    ('color:#a0a5b1', 'color:var(--text-muted)'),
    ('text-white-50', 'text-theme-muted'),
    ('text-white', 'text-theme'),
    ('bg-dark', 'bg-surface')
])

# garage_add.html
replace_in_file(base_dir + 'garage_add.html', [
    ('text-white-50', 'text-theme-muted'),
    ('text-white', 'text-theme'),
    ('bg-dark', 'bg-surface')
])

# garage_detail.html
replace_in_file(base_dir + 'garage_detail.html', [
    ('text-white-50', 'text-theme-muted'),
    ('text-white', 'text-theme'),
    ('bg-dark', 'bg-surface')
])

# profile.html
replace_in_file(base_dir + 'profile.html', [
    ('text-white-50', 'text-theme-muted'),
    ('text-white', 'text-theme'),
    ('bg-dark', 'bg-surface')
])

# garage.html
with open(base_dir + 'garage.html', 'r', encoding='utf-8') as f:
    content = f.read()
content = content.replace('text-white">Garajınız şu an boş.', 'text-theme">Garajınız şu an boş.')
content = content.replace('text-white">Garajım', 'text-theme">Garajım')
with open(base_dir + 'garage.html', 'w', encoding='utf-8') as f:
    f.write(content)
