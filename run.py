from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
    # app.run(host='YOUR IP HERE', debug=True) # FOR RUNNING IN A IP
    app.run(debug=True)  # FOR RUNNING LOCALLY
