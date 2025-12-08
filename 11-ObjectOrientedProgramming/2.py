# class definition
class Song:
   def __init__(self,artist,track_title, album, year):
      self.artist = artist
      self.track_title = track_title
      self.album = album
      self.year = year
   def __str__(s):
      return f' artist: {self.artist}, track title: {self.track_title}, album: {self.album},'
      

# object creation
song1 = Song("Playboi Carti","Rockstar Made","Whole Lotta Red","2020")
song2 = Song()


## object usage
print(song1)