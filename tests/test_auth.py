from app.models import User
from app import db

def test_register_success(client, app):
    """Test valid user registration"""
    response = client.post('/auth/register', data={
        'username': 'testuser',
        'email': 'test@test.com',
        'password': 'password123',
        'password_confirm': 'password123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    
    data = response.data.decode('utf-8')
    assert 'giriş yapabilirsiniz' in data.lower() or 'başarıyla' in data.lower()
    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        assert user is not None
        assert user.email == 'test@test.com'
        assert user.check_password('password123') == True

def test_register_existing_user(client, app):
    """Test registration with already existing email or username"""
    # Create initial user
    with app.app_context():
        user = User(username='testuser', email='test@test.com')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        
    # Try to register with same username
    response = client.post('/auth/register', data={
        'username': 'testuser',
        'email': 'another@test.com',
        'password': 'password123',
        'password_confirm': 'password123'
    }, follow_redirects=True)
    
    data = response.data.decode('utf-8')
    assert 'bu kullanıcı adı alınmış' in data.lower() or 'zaten' in data.lower()

def test_login_success(client, app):
    """Test logging in with correct credentials"""
    with app.app_context():
        user = User(username='loginuser', email='login@test.com')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        
    # Test valid login with username
    response = client.post('/auth/login', data={
        'username_or_email': 'loginuser',
        'password': 'password123'
    }, follow_redirects=True)
    
    data = response.data.decode('utf-8')
    assert 'başarıyla giriş yaptınız' in data.lower() or 'profilim' in data.lower() or 'loginuser' in data.lower()

def test_login_invalid(client, app):
    """Test logging in with incorrect credentials"""
    with app.app_context():
        user = User(username='loginuser', email='login@test.com')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        
    response = client.post('/auth/login', data={
        'username_or_email': 'loginuser',
        'password': 'wrongpassword'
    }, follow_redirects=True)
    
    data = response.data.decode('utf-8')
    assert 'geçersiz' in data.lower() or 'şifre' in data.lower()
    assert 'loginuser' not in data or 'giriş yap' in data.lower()

def test_logout(client, app):
    """Test user logout"""
    with app.app_context():
        user = User(username='logoutuser', email='logout@test.com')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        
    # Login first
    client.post('/auth/login', data={
        'username_or_email': 'logoutuser',
        'password': 'password123'
    })
    
    # Logout
    response = client.get('/auth/logout', follow_redirects=True)
    data = response.data.decode('utf-8')
    assert 'giriş yap' in data.lower() or 'başarıyla çıkış' in data.lower()
