# album

def make_album(artist,album,tracks=''):
	
	''' Creating  a function that builds a dictionary with an optional argument'''
	record = {'artist':artist.title(),'album':album.title()}
	if tracks:
		record['track']=tracks
	return record

information = make_album('Michael Jackson','Bad',tracks=9)
print(information)

