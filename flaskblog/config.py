
class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_DATABASE_URI = 'postgres://rixpfyostssdju:a1e7842eb193cca8bc217454b093e07a0bf63650e05543cdbf06fce61a971e84@ec2-107-21-126-201.compute-1.amazonaws.com:5432/dce4h8cq2iqff'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'tiendadelcafe19@gmail.com'
    MAIL_PASSWORD = 'admintdc'
