<div align="center">

# 🛍️ ShopSphere

### A Modern Full-Stack E-Commerce Web Application

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org)

<br>

![ShopSphere](https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=900&h=300&fit=crop&q=80)

<br>

[![GitHub Repo](https://img.shields.io/badge/GitHub-View_Repository-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/udaykiran47136/shopsphere)
[![Stars](https://img.shields.io/github/stars/udaykiran47136/shopsphere?style=for-the-badge&color=yellow)](https://github.com/udaykiran47136/shopsphere/stargazers)

</div>

---

## 🔗 Links

| | Link |
|---|---|
| 🐙 **GitHub** | [github.com/udaykiran47136/shopsphere](https://github.com/udaykiran47136/shopsphere) |
| 💻 **Local Demo** | http://127.0.0.1:5000 |

> ⚠️ **Note:** The local demo link `http://127.0.0.1:5000` only works on your own computer after running `python app.py`

---

## 💡 About

**ShopSphere** is a complete full-stack e-commerce web application built from scratch using **Python Flask**. It features user authentication, product catalogue with category filters, shopping cart, payment checkout, user dashboard, and a full admin panel — all in a stunning dark luxury design with amber gold accents.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🏠 **Homepage** | Hero section with stats and featured products |
| 🛍️ **Products** | Browse products with category filter buttons |
| 🔐 **Auth System** | Secure register, login and logout |
| 🛒 **Shopping Cart** | Add, remove and manage cart items |
| 💳 **Payment** | Checkout with card details and order placement |
| 📊 **Dashboard** | View order history and account statistics |
| 👑 **Admin Panel** | Manage products, users and orders |
| 📱 **Responsive** | Works on all screen sizes |
| 🎨 **Dark UI** | Luxury dark theme with amber gold accents |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Language** | Python 3 | Core backend language |
| **Framework** | Flask | Web server and routing |
| **Database** | SQLite3 | Data storage |
| **Security** | Werkzeug | Password hashing |
| **Templates** | Jinja2 | Dynamic HTML rendering |
| **Markup** | HTML5 | Page structure |
| **Styling** | CSS3 | Design and animations |
| **Scripts** | JavaScript | Interactivity |
| **Fonts** | Google Fonts | Playfair Display + DM Sans |

---

## 📁 Project Structure

```
shopsphere/
│
├── app.py                 # Main Flask app
├── config.py              # Configuration
├── requirements.txt       # Dependencies
│
├── templates/
│   ├── base.html          # Base layout
│   ├── index.html         # Homepage
│   ├── login.html         # Login
│   ├── register.html      # Register
│   ├── dashboard.html     # Dashboard
│   ├── products.html      # Products
│   ├── cart.html          # Cart
│   ├── payment.html       # Payment
│   └── admin.html         # Admin panel
│
└── static/
    └── style.css          # Stylesheet
```

---

## 🚀 Getting Started

### Step 1 — Clone the repo
```bash
git clone https://github.com/udaykiran47136/shopsphere.git
cd shopsphere
```

### Step 2 — Install dependencies
```bash
pip install flask werkzeug
```

### Step 3 — Run the app
```bash
python app.py
```

### Step 4 — Open in browser
```
http://127.0.0.1:5000
```

> ✅ Database and demo products are created automatically on first run!

---

## 👤 Accounts

| Role | How to Get Access |
|------|------------------|
| **User** | Register at `http://127.0.0.1:5000/register` |
| **Admin** | Set `is_admin = 1` in database |

---

## 📋 All Pages

| Route | Full URL | Access |
|-------|----------|--------|
| `/` | http://127.0.0.1:5000 | Public |
| `/products` | http://127.0.0.1:5000/products | Public |
| `/register` | http://127.0.0.1:5000/register | Public |
| `/login` | http://127.0.0.1:5000/login | Public |
| `/dashboard` | http://127.0.0.1:5000/dashboard | Login Required |
| `/cart` | http://127.0.0.1:5000/cart | Login Required |
| `/payment` | http://127.0.0.1:5000/payment | Login Required |
| `/admin` | http://127.0.0.1:5000/admin | Admin Only |

---

## 🎨 Design

```
Theme      →  Dark Luxury Editorial
Background →  #0c0c0e  (Deep charcoal)
Accent     →  #f5a623  (Amber gold)
Text       →  #e8e8ec  (Off white)
Heading    →  Playfair Display
Body       →  DM Sans
```

---

## 📦 Requirements

```
flask>=3.0.0
werkzeug>=3.0.0
```

---

## 📝 License

This project is open source under the [MIT License](LICENSE).

---

<div align="center">

## 👨‍💻 Developer

### Mandla Uday Kiran

[![GitHub](https://img.shields.io/badge/GitHub-udaykiran47136-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/udaykiran47136)

---

### ⭐ Star this repo if you found it helpful!

**Built with ❤️ using Python Flask**

</div>
