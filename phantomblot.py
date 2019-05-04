#########################################################################################
# Phantom Blot
# API to interact with iTunes Music Library XML file
# Author: Rodrigo Nobrega
# 20190427-20190428
#########################################################################################
__version__ = 0.005


# import libraries
# import os


# global variables
# SCOPE = 'Global'


# Class name
class Library(object):
    """
    Takes the contents of an iTunes Music Library XML file and provides methods to interact with it
    ----------------------
    ATTRIBUTES
    artists: list
    file: string
    library: list of dictionaries
    ----------------------
    METHODS
    findartist(): returns true or false if artist exists (case insensitive)
    getalbums(): returns a set of albums for the artist. Parameters: artist, whole
    getartistlist(): returns an ordered list of Artists
    getlibrary(): returns a list with dictionaries for the library XML file
    getsongs(): returns an ordered list of songs. Parameters: artist, album, whole
    """
    def __init__(self, xmlfile):
        self.file = xmlfile
        self.library = self.getlibrary()
        self.artists = self.getartistlist()

    def getlibrary(self):
        musiclist = []
        musicentry = {}
        musicxml = open(self.file, 'r')
        for line in musicxml:
            if '<dict>' in line:
                musicentry = {}
            if '</dict>' in line:
                musiclist.append(musicentry)
            if any(x in line for x in ['<key>Artist</key>', '<key>Album Artist</key>', '<key>Album</key>',
                                       '<key>Track Number</key>', '<key>Year</key>', '<key>Name</key>']):
                musicentry[line.split('>')[1].split('<')[0]] = line.split('>')[3].split('<')[0].replace('&#38;', '&')
        musicxml.close()
        return musiclist

    def getartistlist(self):
        artistlist = set()
        for i in self.library:
            try:
                artistlist.add(i['Artist'])
            except:
                pass
        return sorted(artistlist)

    def findartist(self, artist):
        lowerartists = [i.lower() for i in self.artists]
        # return artist.lower() in lowerartists
        return any(artist.lower() in x for x in lowerartists)

    def getalbums(self, artist, whole=True):
        albumlist = set()
        for i in self.library:
            try:
                if whole:
                    if artist.lower() == i['Artist'].lower():
                        albumlist.add(i['Album'])
                elif artist.lower() in i['Artist'].lower():
                    albumlist.add(i['Album'])
                else:
                    pass
            except:
                pass
        return albumlist

    def getsongs(self, artist=None, album=None, whole=True):
        songset = set()
        if artist:
            for i in self.library:
                try:
                    if whole:
                        if artist.lower() == i['Artist'].lower():
                            songset.add(i['Name'])
                    elif artist.lower() in i['Artist'].lower():
                        songset.add(i['Name'])
                    else:
                        pass
                except:
                    pass
        elif album:
            for i in self.library:
                try:
                    if whole:
                        if album.lower() == i['Album'].lower():
                            songset.add(i['Name'])
                    elif album.lower() in i['Album'].lower():
                        songset.add(i['Name'])
                    else:
                        pass
                except:
                    pass
        else:
            pass
        return sorted([i for i in songset])


# main loop
def main():
    print('\n===========================================================================')
    print('                         iTunes Music Library API')
    print('===========================================================================\n')
    # '/Users/rodrigo/Google Drive/Personal Stuff/Music Library/2019 iTunes Music Library.xml'
    print('USAGE:')
    print('>>> from phantomblot import *')
    print(">>> mylib = Library('<iTunes Music Library.xml>')")
    print('>>> mylib.library')
    print('>>> mylib.getartistlist()')
    print('>>> mylib.findartist("chico science")')
    print('>>> mylib.getalbums("can")')
    print('>>> mylib.getalbums("can", whole=False)')
    print('>>> mylib.getsongs("neil young")')
    print('>>> mylib.getsongs("neil young", whole=False)')
    print('\n=========================== END OF PROGRAM ==============================--\n')


# main, calling main loop
if __name__ == '__main__':
    main()
