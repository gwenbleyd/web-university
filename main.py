from app import application, db

if __name__ == "__main__":
    application.run(debug=True, host="127.0.0.10", port=9000)