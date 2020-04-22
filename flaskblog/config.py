import os

class Config:

	SECRET_KEY = os.environ.get('KEY')
	SQLALCHEMY_DATABASE_URI = os.environ.get('URI')
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('DB_USER')
	MAIL_PASSWORD = os.environ.get('DB_PASS')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	"""SECRET_KEY = 'de5b170d0ce49061761f1dd2e6a96459'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'"""