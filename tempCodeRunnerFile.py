
if __name__ == "__main__":
    with app.app_context():
        # Drop all existing tables (useful during development)
        # db.drop_all()
        # Create tables again with updated schema
        db.create_all()
    app.run(debug=True, port=8000)