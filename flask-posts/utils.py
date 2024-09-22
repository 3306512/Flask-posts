from models import Post, db

def get_post(post_id):
    return Post.query.get(post_id)


def delete_post(post_id):
    result_post = get_post(post_id=post_id)
    if result_post:
        db.session.delete(result_post)
        db.session.commit()
        return True
    return False

def create_post(title: str, content: str):
    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()
    return True

def edit_post(title: str, content: str, post_id: int):
    result_post = get_post(post_id=post_id)
    if result_post:
        result_post.title = title
        result_post.content = content
        db.session.commit()
        return True
    return False
