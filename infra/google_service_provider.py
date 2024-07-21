from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os.path
import pickle

from infra.config_provider import ConfigProvider


class GoogleServiceProvider:
    def __init__(self):
        self.config = ConfigProvider.load_from_file()
        self.CLIENT_SECRET_FILE = '../client_secret.json'
        self.TOKEN_PICKLE_FILE = '../token.pickle'
        # Scopes for the API
        self.SCOPES = self.config['api-scopes']

    def authenticate_google_service(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first time.
        if os.path.exists(self.TOKEN_PICKLE_FILE):
            with open(self.TOKEN_PICKLE_FILE, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.CLIENT_SECRET_FILE,
                                                                 self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.TOKEN_PICKLE_FILE, 'wb') as token:
                pickle.dump(creds, token)
        print("Authenticated successfully!")
        service = build('calendar', 'v3', credentials=creds)
        return service
