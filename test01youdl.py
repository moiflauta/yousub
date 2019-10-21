import youtube_dl
import ffmpeg

lavidamodernaYoutube = "https://www.youtube.com/watch?v=tEhaJ4r15zA"

#ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
ydl = youtube_dl.YoutubeDL()

with ydl:
    result = ydl.extract_info(
        lavidamodernaYoutube,
        download=False  # We just want to extract the info
    )

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

#print(video)
#video_url = video['url']
#print(video_url)

for key in video['requested_formats']:
    print("key:", key)
    #print(video['requested_formats'][key])

