from googleapiclient.discovery import build
import json

API_KEY = 'private API Key goes here.'

# Create a YouTube Data API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# This will be a search function in the future
search="jihyo fancam"

# Call the API to retrieve information about the video
# Read documentation for more search parameters
response = youtube.search().list(
    part='snippet',
    maxResults=250,
    order="viewCount",
    q=search #the search function
).execute()

# Create a json file with data
with open(f'{search}.json', 'w') as convert_file:
    convert_file.write(json.dumps(response))




# Print the JSON response

# print(json.dumps(response, indent=2))