from models import db, Post
from main import app

with app.app_context():
    db.create_all()
    post1 = Post(title="Test post 1", content="content for test post 1")
    post2 = Post(title="Test post 2", content="content for test post 2")
    db.session.add_all([post1, post2])
    db.session.commit()
    print("Все круто")
