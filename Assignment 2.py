"""
Assignment 2

Pick a song and list 3 atrributes towards it.
Create 3 functions related to these.

"""



ArtistTitle = "Linkin Park"
SongTitle = "Numb"
AlbumTitle = "Meteora"


def Song(Name):
    Action = SongTitle
    return Action
Song = Song(SongTitle)

def Artist(ArtistTitle):
    Action = ArtistTitle
    return Action
Artist = Artist(ArtistTitle)

def Album(AlbumTitle):
    Action = AlbumTitle
    return Action
Album = Album(AlbumTitle)

print(Artist)
print(Album)
print(Song)



#print(10 == 10)

PeakChartPosUs = 1
PeakChartPosIre = 16
PeakChartPosUk = 1

#Top10 = > 0 and <= 10

def Top10Ire(PeakChartPosIre):
    if PeakChartPosIre > 0 and PeakChartPosIre <= 10:
        return True
    else:
        return False
IreTop10 = Top10Ire(PeakChartPosIre)

print(IreTop10)



def Top10Us(PeakChartPosUs):
    if PeakChartPosUs > 0 and PeakChartPosUs <= 10:
        return True
    else:
        return False
UsTop10 = Top10Us(PeakChartPosUs)

print(UsTop10)



def Top10Uk(PeakChartPosUk):
    if PeakChartPosUk > 0 and PeakChartPosUk <= 10:
        return True
    else:
        return False
UkTop10 = Top10Uk(PeakChartPosUk)

print(UkTop10)