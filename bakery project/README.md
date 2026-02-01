# Bakery Web App 🍞

**Aspiring backend project:** Bakery web app using Flask with basic HTML/CSS.

## Features
- View and order bakery products
- Manage customer orders
- Best sellers display
- Contact form for inquiries
- Backend logic handled with Flask routes and MySQL database

## Tech Stack
- **Backend:** Python (Flask)
- **Database:** MySQL (via PyMySQL)
- **Frontend:** HTML, CSS, Jinja2 templates
- **Styling:** Custom CSS with Google Fonts

## Getting Started

### Prerequisites
- Python 3.x installed
- MySQL server (XAMPP or standalone)
- Git (for cloning)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/bakery.git
   cd bakery
   ```

2. **Install Python dependencies:**
   ```bash
   pip install Flask Flask-SQLAlchemy PyMySQL
   ```

3. **Set up the database:**
   - Start your MySQL server (via XAMPP or command line)
   - Create a database named `db_bakery`
   - Update the database URI in `app.py` if needed:
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/db_bakery'
     ```

4. **Initialize the database:**
   - Run the app once to create tables, or use Flask-Migrate if set up

### How to Run

1. **Run the Flask app:**
   ```bash
   python app.py
   ```

2. **Open your browser:**
   - Go to `http://localhost:5000` (or the port Flask uses)

3. **Explore the app:**
   - Home page with best sellers
   - Products page to browse and order
   - Order form with automatic checkbox selection
   - Contact page

## Project Structure
```
bakery/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── database.py            # Database configuration
├── templates/             # HTML templates
│   ├── home.html
│   ├── products.html
│   ├── order.html
│   ├── order_success.html
│   └── contact.html
├── static/                # CSS, images
│   ├── style.css
│   └── images/
└── README.md
```

## Contributing
Feel free to fork and submit pull requests. This is a learning project, so contributions are welcome!

## License
This project is for educational purposes.