from src import app

def main():
    app.run(debug=True, port=6500, threaded=True)

if __name__ == "__main__":
    main()
