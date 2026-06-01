import os

with open('app/main/routes.py', 'r', encoding='utf-8') as f:
    c = f.read()

target = "filepath = os.path.join(current_app.root_path, 'static/avatars', filename)\n        file.save(filepath)"
replacement = "filepath = os.path.join(current_app.root_path, 'static/avatars', filename)\n        os.makedirs(os.path.dirname(filepath), exist_ok=True)\n        file.save(filepath)"

c = c.replace(target, replacement)

with open('app/main/routes.py', 'w', encoding='utf-8') as f:
    f.write(c)
