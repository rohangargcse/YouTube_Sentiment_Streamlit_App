
from googleapiclient.discovery import build
import re

def extract_video_id(url_or_id):
    match = re.search(r"(?:v=|youtu\.be/)([\w-]+)", url_or_id)
    return match.group(1) if match else url_or_id

def fetch_comments(video_id, max_comments=100):
    api_key = "AIzaSyBTFsKQEe1dwvQ1aZCGdGlbKVl9FDEYN48"
    video_id = extract_video_id(video_id)
    youtube = build('youtube', 'v3', developerKey=api_key)
    comments = []
    req = youtube.commentThreads().list(
        part='snippet', videoId=video_id,
        maxResults=100, textFormat='plainText'
    )
    while req and len(comments) < max_comments:
        res = req.execute()
        for item in res['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        req = youtube.commentThreads().list_next(req, res)
    return comments[:max_comments]
