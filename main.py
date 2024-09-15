from flask import (
    abort,
    flash,
    Flask,
    redirect,
    render_template,
    url_for,
)

from database_connection import get_db_connection
from utils import (
    delete_post,
    get_post,
)

app = Flask(__name__)


@app.route("/")
def index():
    connection = get_db_connection()
    content = connection.execute("""
    SELECT * FROM posts 
    """).fetchall()
    connection.close()
    return render_template("index.html", content=content)


@app.route("/post/<int:post_id>")
def post(post_id):
    post = get_post(post_id)
    if post is None:
        abort(404)
    return render_template("post.html", post=post)


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete(post_id):
    post = get_post(post_id)
    is_deleted = delete_post(post_id)
    if not is_deleted:
        abort(404)
    flash(f"post {post['title']} was successfully deleted")
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
