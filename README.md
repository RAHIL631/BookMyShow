# BookMySeat - Movie Booking Platform

A premium, production-ready BookMyShow clone built with Django. This platform features a sleek glassmorphism UI, robust booking flows, and advanced admin capabilities.

## 🚀 Key Features

- **Dynamic Homepage**: Hero section with search, categorized carousels for Movies, Events, Plays, and Sports.
- **Advanced Filtering**: Sidebar filters for categories and languages.
- **Interactive Seat Selection**: Real-time price calculation and visual seat grid.
- **Booking Confirmation**: Seamless redirection to a detailed success summary.
- **User Dashboard**: View booking history and profile details.
- **Production Ready**: Optimized for Vercel with environment variable support and WhiteNoise static serving.

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML5, Vanilla CSS (Glassmorphism), Bootstrap 4
- **Database**: SQLite (Local), PostgreSQL (Production)
- **Deployment**: Vercel, WhiteNoise

## 🏁 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/RAHIL631/BookMyShow.git
cd BookMyShow
```

### 2. Set Up Environment
Create a `.env` file in the root directory based on `.env.example`:
```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Development Server
```bash
python manage.py runserver
```

## 📦 Deployment on Vercel

1. Connect your GitHub repository to Vercel.
2. Add the environment variables from `.env.example` to Vercel.
3. Deploy! The `vercel.json` is already configured for the Django WSGI application.

## 🤝 Contributing

Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License
[MIT](https://choosealicense.com/licenses/mit/)