from database_connection import get_db_connection


def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute("""
    SELECT * FROM posts WHERE id = ?
    """, (post_id, )).fetchone()
    connection.close()
    return post


def delete_post(post_id):
    connection = get_db_connection()
    connection.execute("""
    DELETE FROM posts WHERE id = ?
    """, (post_id, ))
    connection.commit()
    connection.close()
    return True