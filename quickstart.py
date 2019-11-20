from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import events

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def main():

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API

    deadlines_list = events.main()

    deadlines_present_summary = []
    deadlines_present_time = []
  


    page_token = None
    #Gets existing events 
    while True:
        event_list = service.events().list(calendarId='primary', pageToken=page_token).execute()
        for event in event_list['items']:
            try:
                deadlines_present_summary.append(event['summary'])
                deadlines_present_time.append(event['start']['dateTime'])
            except KeyError:
                pass
        page_token = event_list.get('nextPageToken')
        if not page_token:
            break

    create_event(deadlines_list,deadlines_present_summary, deadlines_present_time,service)


def create_event(deadlines_list, deadlines_present_summary,deadlines_present_time,service):
    deadlines_list_summary = [deadlines_list[i]['summary'] for i in range(len(deadlines_list))]

    deadlines_list_time = [deadlines_list[i]['start']['dateTime'] for i in range(len(deadlines_list))]

    for x in range(len(deadlines_list)):
        #Checks if event exists already 
        
        if (deadlines_list_summary[x] not in deadlines_present_summary) and (deadlines_list_time[x] not in deadlines_present_time):
            service.events().insert(calendarId='primary', body=deadlines_list[x]).execute()




if __name__ == '__main__':
    main()







