#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:32:58 2020

@author: dennisbrookner
"""

from Music.notes import Note
from Music.chords import Chord

sev_type = dict(M = 11,
                m = 10)

class Sevchord(Chord):
    def __init__(self, string):
        
        kind = parser(string)  
        
        super(Sevchord, self).__init__(kind[0])
        
        self._kind = kind
        
        if kind[1]:
            seventh = self.root().transpose(sev_type[kind[1]]).name()
            self.seventh(seventh)
        
    def seventh(self, seventh=None):
        if seventh:
            self._seventh = Note(seventh)
        return self._seventh
    
    def sevspell(self):
        return
    
    def sevtranspose(self):
        return



    def __str__(self):
        if self._kind[1]:
            
            return (f'{self.root()}{self._kind[2]} chord: ' + 
                       f'{self.root()} {self.third()} {self.fifth()} {self.seventh()}')
        else:
            return (f'{self._kind[0]} chord: ' + 
                       f'{self.root()} {self.third()} {self.fifth()}')

    def __repr__(self):
        if self._kind[1]:      
            return f'{self.root()} {self.third()} {self.fifth()} {self.seventh()}'
        else:
            return f'{self.root()} {self.third()} {self.fifth()}'
     
def parser(string):
    
    if string[-1] != '7':
        chstring = string
        sevstring = None
        sevkind = None
    
    elif 'M' in string:
        chstring = string[:-1]
        sevstring = 'M'
        sevkind = 'M7'
    
    elif 'm' in string:
        chstring = string[:-1]
        sevstring = 'm'
        sevkind = 'm7'

    else:
        chstring = f'{string[:-1]}M'
        sevstring = 'm'
        sevkind = '7'
        
    return chstring, sevstring, sevkind
        
def main():
        
#    notes = ['C', 'G', 'D', 'A', 'E', 'Cb', 'B', 'F#', 'Gb', 'C#', 'Db', 'Ab',
#             'G#', 'Eb', 'D#', 'Bb', 'A#', 'F']
    notes = ['C','Db']

    print(Sevchord('CM7'))
    print(Sevchord('Cm7'))
    print(Sevchord('C7'))  
    print(Sevchord('CM'))
    print(Sevchord('Cm'))
      
    
# 'make everything run' workaround
if __name__ == '__main__': main()