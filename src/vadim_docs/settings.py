import os

SIMPLE_SETTINGS = {
    'OVERRIDE_BY_ENV': True,
}

BASE_PATH = os.getcwd()

GOOGLE_API_URL = 'https://www.googleapis.com'
GOOGLE_API_AUTH_URL = f'{GOOGLE_API_URL}/auth'
GOOGLE_API_SCOPES = list(map(
    lambda x: f'{GOOGLE_API_AUTH_URL}/{x}',
    [
        'presentations.readonly',
        'spreadsheets.readonly',
        'drive',
        'drive.file',
        'drive.file',
        'drive.metadata.readonly',
        'drive.metadata',
        'drive.photos.readonly',
    ]
))

GOOGLE_API_FOLDER = BASE_PATH
GOOGLE_API_CREDENTIALS_FILE = os.path.join(GOOGLE_API_FOLDER, '_credentials.json')
GOOGLE_API_TOKEN_FILE = os.path.join(GOOGLE_API_FOLDER, '_token.json')
