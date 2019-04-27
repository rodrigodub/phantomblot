#########################################################################################
# Phantom Blot
# API to interact with iTunes Music Library XML file
# Author: Rodrigo Nobrega
# 20190427
#########################################################################################
__version__ = 0.002


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
    file
    library
    ----------------------
    METHODS
    getartistlist(): returns a set of Artists
    getlibrary(): returns a list with dictionaries for the library XML file
    """
    def __init__(self, xmlfile):
        self.file = xmlfile
        self.library = self.getlibrary()

    def getlibrary(self):
        musiclist = []
        musicentry = {}
        # musicentry = []
        musicxml = open(self.file, 'r')
        for line in musicxml:
            if '<dict>' in line:
                musicentry = {}
                # musicentry = []
            if '</dict>' in line:
                musiclist.append(musicentry)
            if any(x in line for x in ['<key>Artist</key>', '<key>Album Artist</key>', '<key>Album</key>',
                                       '<key>Track Number</key>', '<key>Year</key>', '<key>Name</key>']):
                # musicentry.append([line.split('>')[1].split('<')[0], line.split('>')[3].split('<')[0]])
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
        # artistlist = {i[1] for i in self.library if i[0] == 'Artist'}
        return artistlist


# main loop
def main():
    print('\n===========================================================================')
    print('                         iTunes Music Library API')
    print('===========================================================================\n')
    # '/Users/rodrigo/Google Drive/Personal Stuff/Music Library/2019 iTunes Music Library.xml'
    print('\n=========================== END OF PROGRAM ==============================--\n')


# main, calling main loop
if __name__ == '__main__':
    main()
