import os

#Import the various bot secret and tokens from the os enviromental variables, you need to set these
OAUTH2_CLIENT_ID = os.environ['OAUTH_CLIENT_ID']
OAUTH2_CLIENT_SECRET = os.environ['OAUTH_CLIENT_SECRET']
OAUTH2_REDIRECT_URI = 'http://localhost:5000/callback' #This will need to be changed when the bot website is hosted
API_BASE_URL = os.environ.get('API_BASE_URI','https://discordapp.com/api')

#Store the urls for the bot
AUTHORIZATION_BASE_URL = API_BASE_URL + '/oauth2/authorize'
TOKEN_URL = API_BASE_URL + '/oauth2/token'

#Store the location of the upload folder and the allowed data type
UPLOAD_FOLDER="songs"
ALLOWED_EXTENSIONS = {'mp3'}
ALLOWED_LENGTH = 500 #max allowed length in seconds
