#!/usr/bin/env python3
#Made by 0xDarkStar and onyxid on GitHub
import os
import platform
import time
from progressbar import AnimatedMarker, ProgressBar
from pytube import YouTube

#TO DO: convert file type, and make gif

audio = ("audio", "Audio", "AUDIO", "aUDIO", "a")
video = ("video", "Video", "VIDEO", "vIDEO", "vid", "v")
illegalChars = ('"', "/", "\\", "?", ":", "<", ">", "|")

def main():
	OSname = platform.system()
	if OSname == "Windows":
		os.system("cls")
	elif OSname == "Darwin":
		os.system("clear")
	elif OSname == "Linux":
		os.system("clear")
	global link, NameChange, NewName, OnlyWebm
	link = YouTube(input("Paste link: ")) #I'm using this to test https://youtu.be/EfgAd6iHApE
	print("\nFile name: " + link.title) #Prints title of YouTube video
	if "/" in link.title:
		OnlyWebm = True
	else:
		OnlyWebm = False
	NameChange = input("\nDo you want to change the file name? Y or N\n") #Asks if users want to change the name
	if NameChange == "y" or NameChange == "Y":
		NewName = input("What do you want to name the file? ") #Asks what file should be renamed to
		a = 0
		while a < 8:
			NewName = NewName.replace(illegalChars[a], "")
			link.title = link.title.replace(illegalChars[a], "")
			a += 1
main()

def typeFunc():
	fileType = input("\nDo you want audio or video? ")

	if fileType in audio: #If audio is requested
		if OnlyWebm == True:
			for stream in link.streams.filter(only_audio=True, file_extension="webm"): #Names that have a / in them don't work with mp4 for some reason...
				print(f"itag: {stream.itag}, codec: {stream.audio_codec}, "f"abr: {stream.abr}, file type: {stream.mime_type.split('/')[1]}")
		else:
			for stream in link.streams.filter(only_audio=True):
				print(f"itag: {stream.itag}, codec: {stream.audio_codec}, "f"abr: {stream.abr}, file type: {stream.mime_type.split('/')[1]}")

	elif fileType in video: #If video is requested
		for stream in link.streams.filter(progressive=True):
			print(f"itag: {stream.itag}, resolution: {stream.resolution}, fps: {stream.fps}, "f"bitrate: {stream.abr},  file type: {stream.mime_type.split('/')[1]}")

	else:
		print("Sorry, I did not understand.")
		typeFunc()
typeFunc()

def final():
	while True: #Verifies input of user, confirming it is an integer
		try:
			num = int(input("Enter itag: "))
		except ValueError:
			print("Please enter a number.")
		else:
			if num in link.streams.itag_index: #Confirms it is a legitimate itag
				stream = link.streams.get_by_itag(num)
				def loading():
					pbar = ProgressBar(widgets=['Working: ', AnimatedMarker()])
					for i in pbar((i for i in range(50))):
						time.sleep(0.1)
						stream.download()
				loading()						
				if NameChange == "y" or NameChange == "Y": #If they wanted the name change, then we change it here
					os.rename(f"{link.title}.{stream.mime_type.split('/')[1]}", f"{NewName}.{stream.mime_type.split('/')[1]}")
				break
			else:
				print("You didn't input a proper itag, try again")
final()
