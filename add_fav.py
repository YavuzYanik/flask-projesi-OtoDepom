with open('app/templates/main/products.html', 'r', encoding='utf-8') as f:
    content = f.read()
repl = '''<div class="product-card position-relative">
                    <!-- Favorite Button -->
                    <button onclick="toggleFavorite({{ p.id }}, event)" class="btn btn-sm btn-light position-absolute top-0 end-0 m-2 rounded-circle shadow-sm" style="width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; z-index: 10;">
                        {% if current_user.is_authenticated and p in current_user.favorites %}
                            <i class="fa-solid fa-star fav-icon-{{ p.id }}" style="color: #f59e0b; font-size: 1rem;"></i>
                        {% else %}
                            <i class="fa-regular fa-star fav-icon-{{ p.id }}" style="color: var(--text-color); font-size: 1rem;"></i>
                        {% endif %}
                    </button>'''
content = content.replace('<div class="product-card">', repl)
with open('app/templates/main/products.html', 'w', encoding='utf-8') as f:
    f.write(content)
