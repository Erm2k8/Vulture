from app.app import app
from app.views import main_bp
from app.models.user import create_users_table
from app.database import connect_db

def main():
    connect_db()

    app.register_blueprint(main_bp)

    create_users_table()

    app.run(debug=True)


if __name__ == '__main__':
    main()