#########################################################################################
# Phantom Blot
# API to interact with iTunes Music Library XML file
# Author: Rodrigo Nobrega
# 20190427
#########################################################################################
__version__ = 0.004


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
    getalbums(): returns a set of albums for the artist
    getartistlist(): returns an ordered list of Artists
    getlibrary(): returns a list with dictionaries for the library XML file
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

    def getalbums(self, artist):
        #TODO: use a flag to decide if artist is part of the name or full name
        albumlist = set()
        for i in self.library:
            try:
                if artist.lower() in i['Artist'].lower():
                    albumlist.add(i['Album'])
            except:
                pass
        return albumlist


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
    print('>>> ')
    print('>>> ')
    print('>>> ')
    print('\n=========================== END OF PROGRAM ==============================--\n')


# main, calling main loop
if __name__ == '__main__':
    main()
