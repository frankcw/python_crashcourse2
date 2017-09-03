# user albums

def make_album(artist,album,tracks=''):
	
	''' Creating  a function that builds a dictionary with an optional argument and a while loop'''
	record = {'artist':artist.title(),'album':album.title()}
	if tracks:
		record['track']=tracks
	return record

while True:
	print("Please tell me an artist's name and album.")
	print("enter 'q' at any time to quit!")

	f_artist = input("Artist's name: ")
	if f_artist == 'q':
		break
	f_album = input("Album's name: ")
	if f_artist == 'q':
		break
	f_tracks = input("Album's tracks? if you don't know, please leave blank: ")
	if f_tracks == 'q':
		break


	information = make_album(f_artist,f_album,f_tracks)
	print('\n')
	print(information)

