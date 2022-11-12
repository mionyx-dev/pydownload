from pytube import YouTube

audio = ("audio", "Audio", "AUDIO", "aUDIO")
video = ("video", "Video", "VIDEO", "vIDEO")

def main():
	link = YouTube(input("Paste link: "))
	print("\n" + link.title) # Prints title of YouTube video
main()

def typeFunc():
	fileType = input("\nWhich do you want?\n Audio or Video? ")

	if fileType in audio: 
    	for stream in link.streams.filter(only_audio=True): # To print on seperate lines
        	print(f'itag: {stream.itag}, codec: {stream.audio_codec}, 'f'abr: {stream.abr}, file type: {stream.mime_type.split("/")[1]}')

	elif fileType in video:
    	for stream in link.streams.filter(progressive=True):
        	print(f'itag: {stream.itag}, resolution: {stream.resolution}, fps: {stream.fps}, 'f' ,  file type: {stream.mime_type.split("/")[1]}')

	else:
   		print("Sorry, I did not understand.")
		typeFunc()
typeFunc()

while True: # Verifies input of user, confirming it is an integer
    try:
        num = int(input('Enter itag: '))
        break
    except ValueError:
        print('Please enter a number.')

stream = link.streams.get_by_itag(num)
stream.download()
