import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from simple_settings import LazySettings

settings = LazySettings('vadim_docs.settings')


def get_creds() -> Credentials:
    creds = None
    if os.path.exists(settings.GOOGLE_API_TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(settings.GOOGLE_API_TOKEN_FILE, settings.GOOGLE_API_SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                settings.GOOGLE_API_CREDENTIALS_FILE,
                settings.GOOGLE_API_SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(settings.GOOGLE_API_TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return creds


def get_presentation_details(presentation_id: str, creds: Credentials):
    try:
        service = build('slides', 'v1', credentials=creds)
        presentation = service.presentations().get(presentationId=presentation_id).execute()
        slides = presentation.get('slides')
        print('The presentation contains {} slides:'.format(len(slides)))
        for i, slide in enumerate(slides):
            print('- Slide #{} contains {} elements.'.format(i + 1, len(slide.get('pageElements'))))
    except HttpError as err:
        print(err)
