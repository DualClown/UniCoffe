
class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'postgres://lbgfhnwkajstyg:71fd7225c498f8775ebc07ed83861fa516b582e91163a7fd993f69bb62d17abd@ec2-107-22-216-53.compute-1.amazonaws.com:5432/d3h39bq8fe0rtb'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'tiendadelcafe19@gmail.com'
    MAIL_PASSWORD = 'admintdc'
