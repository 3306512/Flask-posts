from flask import (
    abort,
    flash,
    Flask,
    redirect,
    render_template,
    url_for, request,
)

from utils import (
    delete_post,
    get_post,
    create_post,
    edit_post,
)

from uuid import uuid4

from models import (
    Post, db
)

app = Flask(__name__)
app.secret_key = str(uuid4())
app.config['SECRET_KEY'] = str(uuid4())
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app=app)
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    content = Post.query.all()
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
    flash(f"post {post.title} was successfully deleted")
    is_deleted = delete_post(post_id)
    if not is_deleted:
        abort(404)
    return redirect(url_for('index'))

@app.route(rule="/create", methods=["POST", "GET"])
def create():
    if request.method == "GET":
        return render_template(template_name_or_list="create_post.html")
    title = request.form["title"]
    content = request.form["content"]
    if not content:
        flash(message="Введіть всі параметри!!!")
        return redirect(url_for("create"))
    is_created = create_post(title=title, content=content)
    if is_created:
        return redirect(url_for("index"))
    return render_template(template_name_or_list="create_post.html"), 400

@app.route("/edit/<int:post_id>", methods=["POST", "GET"])
def edit(post_id):
    post = get_post(post_id)
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if not title or not content:
            flash(message="Введіть всі параметри!!!")
            return redirect(url_for("edit"))
        edit_post(post_id=post_id, title=title, content=content)
        return redirect(url_for("index"))
    if post:
        return render_template(template_name_or_list="edit_post.html", post=post)
    flash(message="Введіть існуючий \"post_id\"!!!")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
