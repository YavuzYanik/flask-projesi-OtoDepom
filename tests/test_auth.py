from app.models import User
from app import db

def test_register_page_loads(client):
    """Kayıt sayfasının doğru yüklendiğini test eder"""
    response = client.get('/auth/register')
    assert response.status_code == 200
    assert b'Yeni Hesap Olu\xc5\x9ftur' in response.data or b'Kayıt Olun' in response.data.decode('utf-8')

def test_successful_registration(client, app):
    """Yeni bir kullanıcının başarıyla kayıt olabildiğini test eder"""
    response = client.post('/auth/register', data={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123',
        'password_confirm': 'password123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    # Başarılı kayıttan sonra giriş sayfasına yönlendirilmeli
    assert b'Giri\xc5\x9f Yap' in response.data or b'Giriş Yap' in response.data.decode('utf-8')
    
    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        assert user is not None
        assert user.email == 'test@example.com'
        assert user.check_password('password123')

def test_login_page_loads(client):
    """Giriş sayfasının doğru yüklendiğini test eder"""
    response = client.get('/auth/login')
    assert response.status_code == 200
    assert b'Giri\xc5\x9f Yap' in response.data or b'Giriş Yap' in response.data.decode('utf-8')

def test_successful_login(client, app):
    """Geçerli bilgilerle giriş işleminin başarılı olduğunu test eder"""
    # Önce test veritabanına bir kullanıcı ekle
    with app.app_context():
        user = User(username='loginuser', email='login@example.com')
        user.set_password('login123')
        db.session.add(user)
        db.session.commit()
    
    # Ardından bu kullanıcıyla giriş yap
    response = client.post('/auth/login', data={
        'username_or_email': 'loginuser',
        'password': 'login123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    # Giriş yaptıktan sonra ana sayfada/menüde "Çıkış Yap" yazısı olmalı
    assert b'\xc3\x87\xc4\xb1k\xc4\xb1\xc5\x9f' in response.data or b'Çıkış' in response.data.decode('utf-8')
