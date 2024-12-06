from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os

# Scopes for Gmail and Google Calendar API
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.compose',
    'https://www.googleapis.com/auth/calendar',
]

# Path to the credentials file (credentials.json)
CREDENTIALS_FILE = 'credentials.json'

# Path to save the token
TOKEN_FILE = 'token.json'


def get_credentials():
    """
    Retrieves an access token via OAuth 2.0 and saves it to a file.
    If the token already exists, it will be loaded from the file.
    """
    creds = None

    # Check if the token already exists
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # If the token is missing or invalid, start the authorization process
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save the token to a file
        with open(TOKEN_FILE, 'w') as token_file:
            token_file.write(creds.to_json())

    return creds


if __name__ == '__main__':
    # Get the token and print a message about successful authorization
    credentials = get_credentials()
    print("Token successfully obtained and saved to", TOKEN_FILE)