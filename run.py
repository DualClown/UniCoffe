from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='172.17.92.32', debug=True)
