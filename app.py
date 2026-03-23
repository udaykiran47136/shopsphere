from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


def get_db():
    conn = sqlite3.connect(app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    db = get_db()
    db.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT    UNIQUE NOT NULL,
            email    TEXT    UNIQUE NOT NULL,
            password TEXT    NOT NULL,
            is_admin INTEGER DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS products (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            description TEXT,
            price       REAL    NOT NULL,
            stock       INTEGER DEFAULT 0,
            category    TEXT,
            image_url   TEXT
        );
        CREATE TABLE IF NOT EXISTS cart (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id    INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity   INTEGER DEFAULT 1,
            FOREIGN KEY (user_id)    REFERENCES users(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        );
        CREATE TABLE IF NOT EXISTS orders (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id    INTEGER NOT NULL,
            total      REAL    NOT NULL,
            status     TEXT    DEFAULT 'pending',
            created_at TEXT    DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)

    if db.execute("SELECT COUNT(*) FROM products").fetchone()[0] == 0:
        products = [
            ("Wireless Headphones", "Premium noise-cancelling audio",
             149.99, 25, "Electronics",
             "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400"),
            ("Minimalist Watch", "Swiss movement, sapphire glass",
             299.99, 10, "Accessories",
             "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"),
            ("Running Shoes", "Carbon-fibre plate, cushioned",
             89.99, 50, "Footwear",
             "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400"),
            ("Leather Wallet", "Full-grain Italian leather",
             49.99, 30, "Accessories",
             "https://images.unsplash.com/photo-1627123424574-724758594913?w=400"),
            ("Mechanical Keyboard", "TKL, RGB, hot-swap switches",
             129.99, 15, "Electronics",
             "https://images.unsplash.com/photo-1601445638532-1f2aba1d6b43?w=400"),
            ("Sunglasses", "Polarised UV400 lenses",
             79.99, 40, "Accessories",
             "https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=400"),
        ]
        sql = """INSERT INTO products
                 (name, description, price, stock, category, image_url)
                 VALUES (?,?,?,?,?,?)"""
        db.executemany(sql, products)

    db.commit()
    db.close()


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    db = get_db()
    products = db.execute("SELECT * FROM products LIMIT 6").fetchall()
    db.close()
    return render_template("index.html", products=products)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]
        db = get_db()
        try:
            db.execute(
                "INSERT INTO users (username, email, password) VALUES (?,?,?)",
                (username, email, generate_password_hash(password))
            )
            db.commit()
            flash("Account created! Please log in.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Username or email already exists.", "error")
        finally:
            db.close()
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip()
        password = request.form["password"]
        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE email=?", (email,)
        ).fetchone()
        db.close()
        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            session["is_admin"] = bool(user["is_admin"])
            flash("Welcome back, " + user["username"] + "!", "success")
            return redirect(url_for("dashboard"))
        flash("Invalid credentials.", "error")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    db = get_db()
    orders = db.execute(
        "SELECT * FROM orders WHERE user_id=? ORDER BY created_at DESC",
        (session["user_id"],)
    ).fetchall()
    db.close()
    return render_template("dashboard.html", orders=orders)


@app.route("/products")
def products():
    category = request.args.get("category", "")
    db = get_db()
    if category:
        prods = db.execute(
            "SELECT * FROM products WHERE category=?", (category,)
        ).fetchall()
    else:
        prods = db.execute("SELECT * FROM products").fetchall()
    cats = db.execute("SELECT DISTINCT category FROM products").fetchall()
    db.close()
    return render_template(
        "products.html", products=prods, categories=cats, selected=category
    )


@app.route("/cart")
def cart():
    if "user_id" not in session:
        return redirect(url_for("login"))
    db = get_db()
    items = db.execute("""
        SELECT c.id, c.quantity, p.name, p.price, p.image_url
        FROM cart c JOIN products p ON c.product_id = p.id
        WHERE c.user_id = ?
    """, (session["user_id"],)).fetchall()
    db.close()
    total = sum(i["price"] * i["quantity"] for i in items)
    return render_template("cart.html", items=items, total=total)


@app.route("/cart/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    db = get_db()
    existing = db.execute(
        "SELECT * FROM cart WHERE user_id=? AND product_id=?",
        (session["user_id"], product_id)
    ).fetchone()
    if existing:
        db.execute(
            "UPDATE cart SET quantity=quantity+1 WHERE id=?",
            (existing["id"],)
        )
    else:
        db.execute(
            "INSERT INTO cart (user_id, product_id) VALUES (?,?)",
            (session["user_id"], product_id)
        )
    db.commit()
    db.close()
    flash("Added to cart!", "success")
    return redirect(request.referrer or url_for("products"))


@app.route("/cart/remove/<int:item_id>", methods=["POST"])
def remove_from_cart(item_id):
    if "user_id" not in session:
        return redirect(url_for("login"))
    db = get_db()
    db.execute(
        "DELETE FROM cart WHERE id=? AND user_id=?",
        (item_id, session["user_id"])
    )
    db.commit()
    db.close()
    return redirect(url_for("cart"))


@app.route("/payment", methods=["GET", "POST"])
def payment():
    if "user_id" not in session:
        return redirect(url_for("login"))
    db = get_db()
    items = db.execute("""
        SELECT c.id, c.quantity, p.name, p.price
        FROM cart c JOIN products p ON c.product_id = p.id
        WHERE c.user_id = ?
    """, (session["user_id"],)).fetchall()
    total = sum(i["price"] * i["quantity"] for i in items)
    if request.method == "POST":
        if not items:
            flash("Your cart is empty.", "error")
            return redirect(url_for("cart"))
        db.execute(
            "INSERT INTO orders (user_id, total, status) VALUES (?,?,?)",
            (session["user_id"], total, "paid")
        )
        db.execute(
            "DELETE FROM cart WHERE user_id=?",
            (session["user_id"],)
        )
        db.commit()
        db.close()
        flash("Payment successful! Order placed.", "success")
        return redirect(url_for("dashboard"))
    db.close()
    return render_template("payment.html", items=items, total=total)


@app.route("/admin")
def admin():
    if not session.get("is_admin"):
        flash("Admin access required.", "error")
        return redirect(url_for("index"))
    db = get_db()
    products = db.execute("SELECT * FROM products").fetchall()
    users = db.execute(
        "SELECT id, username, email, is_admin FROM users"
    ).fetchall()
    orders = db.execute("""
        SELECT o.*, u.username
        FROM orders o
        JOIN users u ON o.user_id = u.id
        ORDER BY o.created_at DESC
    """).fetchall()
    db.close()
    return render_template(
        "admin.html", products=products, users=users, orders=orders
    )


@app.route("/admin/product/add", methods=["POST"])
def admin_add_product():
    if not session.get("is_admin"):
        return redirect(url_for("index"))
    db = get_db()
    db.execute(
        """INSERT INTO products
           (name, description, price, stock, category, image_url)
           VALUES (?,?,?,?,?,?)""",
        (
            request.form["name"],
            request.form["description"],
            float(request.form["price"]),
            int(request.form["stock"]),
            request.form["category"],
            request.form["image_url"]
        )
    )
    db.commit()
    db.close()
    flash("Product added.", "success")
    return redirect(url_for("admin"))


@app.route("/admin/product/delete/<int:product_id>", methods=["POST"])
def admin_delete_product(product_id):
    if not session.get("is_admin"):
        return redirect(url_for("index"))
    db = get_db()
    db.execute("DELETE FROM products WHERE id=?", (product_id,))
    db.commit()
    db.close()
    flash("Product deleted.", "success")
    return redirect(url_for("admin"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)