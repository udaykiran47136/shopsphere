<div align="center">

# 🛍️ ShopSphere

### A Modern Full-Stack E-Commerce Web Application

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

<br>

### 🌐 [Live Demo → https://shopsphere-udaykiran.onrender.com](https://shopsphere-udaykiran.onrender.com)

> ⚠️ First load may take 30–60 seconds (free tier spins down when inactive)

<br>

![ShopSphere Preview](https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=900&h=300&fit=crop&q=80)

</div>

---

## 📌 Table of Contents

- [About](#-about)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Routes](#-routes)
- [Developer](#-developer)

---

## 💡 About

**ShopSphere** is a complete full-stack e-commerce web application built from scratch using **Python Flask**. It includes user authentication, product catalogue with category filters, shopping cart, payment checkout, user dashboard, and a full admin panel — all wrapped in a stunning dark luxury design with amber gold accents.

---

## 🌐 Live Demo

| Link | Description |
|------|-------------|
| 🔗 [shopsphere-udaykiran.onrender.com](https://shopsphere-udaykiran.onrender.com) | Live Website |
| 🐙 [github.com/udaykiran47136/shopsphere](https://github.com/udaykiran47136/shopsphere) | GitHub Repository |

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🏠 **Homepage** | Hero section with stats and featured products |
| 🛍️ **Products Page** | Browse all products with category filter buttons |
| 🔐 **Authentication** | Secure register, login and logout system |
| 🛒 **Shopping Cart** | Add, remove and manage cart items |
| 💳 **Payment Page** | Checkout with card details and order placement |
| 📊 **User Dashboard** | View order history and account statistics |
| 👑 **Admin Panel** | Full CRUD — manage products, users and orders |
| 📱 **Responsive** | Works perfectly on all screen sizes |
| 🎨 **Dark UI** | Luxury dark theme with amber gold accents |
| ⚡ **Fast** | Lightweight SQLite database, no heavy dependencies |

---

## 📸 Screenshots

<div align="center">

| 🏠 Homepage | 🛍️ Products |
|:-----------:|:-----------:|
| ![Home](https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=400&h=250&fit=crop) | ![Products](https://images.unsplash.com/photo-1472851294608-062f824d29cc?w=400&h=250&fit=crop) |

| 🔐 Login | 📊 Dashboard |
|:--------:|:-----------:|
| ![Login](https://images.unsplash.com/photo-1555421689-d68471e189f2?w=400&h=250&fit=crop) | ![Dashboard](https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400&h=250&fit=crop) |

</div>

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Python 3 | Core programming language |
| **Framework** | Flask | Web server and routing |
| **Database** | SQLite3 | Data storage |
| **Security** | Werkzeug | Password hashing |
| **Templating** | Jinja2 | Dynamic HTML rendering |
| **Frontend** | HTML5 | Page structure |
| **Styling** | CSS3 | Design and animations |
| **Interactivity** | JavaScript | Tabs, card formatting |
| **Fonts** | Google Fonts | Playfair Display + DM Sans |

---

## 📁 Project Structure

```
shopsphere/
│
├── app.py                 # Main Flask app — all routes & logic
├── config.py              # App configuration & secret key
├── requirements.txt       # Python dependencies
├── database.db            # SQLite database (auto-created)
│
├── templates/
│   ├── base.html          # Base layout — navbar & footer
│   ├── index.html         # Homepage with hero section
│   ├── login.html         # User login page
│   ├── register.html      # User registration page
│   ├── dashboard.html     # User dashboard & order history
│   ├── products.html      # Products catalogue with filters
│   ├── cart.html          # Shopping cart page
│   ├── payment.html       # Checkout & payment page
│   └── admin.html         # Admin control panel
│
└── static/
    └── style.css          # Complete design system & animations
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation & Run

**1. Clone the repository**
```bash
git clone https://github.com/udaykiran47136/shopsphere.git
cd shopsphere
```

**2. Install dependencies**
```bash
pip install flask werkzeug
```

**3. Run the application**
```bash
python app.py
```

**4. Open in browser**
```
http://127.0.0.1:5000
```

The database is created automatically on first run with 6 demo products! ✅

---

## 👤 User Accounts

| Role | How to Access |
|------|--------------|
| **New User** | Register at `/register` |
| **Admin** | Set `is_admin = 1` in SQLite database |

---

## 📋 Routes

| Route | Page | Access Level |
|-------|------|-------------|
| `/` | Homepage | Public |
| `/products` | Products Catalogue | Public |
| `/register` | Create Account | Public |
| `/login` | Sign In | Public |
| `/logout` | Sign Out | Logged In |
| `/dashboard` | User Dashboard | Logged In |
| `/cart` | Shopping Cart | Logged In |
| `/cart/add/<id>` | Add to Cart | Logged In |
| `/cart/remove/<id>` | Remove from Cart | Logged In |
| `/payment` | Checkout | Logged In |
| `/admin` | Admin Panel | Admin Only |
| `/admin/product/add` | Add Product | Admin Only |
| `/admin/product/delete/<id>` | Delete Product | Admin Only |

---

## 🎨 Design System

```
Theme:       Dark Luxury Editorial
Background:  #0c0c0e (Deep charcoal)
Accent:      #f5a623 (Amber gold)
Text:        #e8e8ec (Off white)
Cards:       #1a1a1e (Dark surface)
Font 1:      Playfair Display (headings)
Font 2:      DM Sans (body text)
Animations:  Fade-up entrance, hover effects
```

---

## 📦 Dependencies

```
flask>=3.0.0
werkzeug>=3.0.0
```

Only **2 dependencies** — lightweight and fast!

---

## 🔧 Configuration

Edit `config.py`:

```python
class Config:
    SECRET_KEY = "your-secret-key-here"
    DATABASE   = "database.db"
    DEBUG      = True
```

---

## 📝 License

This project is open source under the [MIT License](LICENSE).

---

## 👨‍💻 Developer

<div align="center">

### Mandla Uday Kiran

[![GitHub](https://img.shields.io/badge/GitHub-udaykiran47136-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/udaykiran47136)

</div>

---

<div align="center">

### ⭐ If you like this project, please give it a star!

**Built with ❤️ using Python Flask**

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=udaykiran47136.shopsphere)

</div>
