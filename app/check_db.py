import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from app import create_app, db
from sqlalchemy import inspect

app = create_app()
with app.app_context():
    inspector = inspect(db.engine)
    print("Tables:", inspector.get_table_names())
    print("Products columns:", [c['name'] for c in inspector.get_columns('products')])
    print("Users columns:", [c['name'] for c in inspector.get_columns('users')])
