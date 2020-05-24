#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:32:58 2020

@author: dennisbrookner
"""
from Music.notes import Note
from Music.triads import Triad
from Music.triads import trparser

sev_types = dict(M = ['F', 11],
                m = ['D', 10])

class Chord(Triad):
    def __init__(self, string):
        
        kind = parser(string)  
        
        super(Chord, self).__init__(f'{kind[0]}{kind[1]}')
        
        self._sev_type = kind[2], kind[3]
        
        if self._sev_type[0]:
            seventh = self.root().transpose(sev_types[self._sev_type[0]][1]).name()
            self.seventh(seventh)
        
        self.spell()
        
    def seventh(self, seventh=None):
        if seventh:
            self._seventh = Note(seventh)
        return self._seventh
   
    
    def spell(self):
        
        self.trspell()
        if self._sev_type[0]:
            base = sev_types[self._sev_type[0]][0]
            d = Note(base).distance(self.root())

            if d in range(1,6):
                respell = self._triad_type != self._sev_type[0] and self.root().acc() == 'f'
                if d in range(3,6) and respell:
                    self.root().to_sharp()
                    self.spell()
                else:
                    self.seventh().to_sharp()
            elif d in range(9,12):
                self.seventh().to_flat()
            
            elif d in range(6,9):
                if self.root().acc() == 'f':
                    self.seventh().to_flat()
                else:
                    self.seventh().to_sharp()
                    
            elif d == 0:
                if base == 'F':
                    self.seventh().to_sharp()
                else:
                    self.seventh().to_flat()
            else:
                raise ValueError(f'Unexpected transposition error with d = {d}')                
        return
    
    def transpose(self, number):
        new_root_name = self.root().transpose(number).name()
        if self._sev_type[1]:
            kind = self._sev_type[1]
        else:
            kind = self._triad_type
        return Chord(f'{new_root_name}{kind}')
        



    def __str__(self):
        if self._sev_type[0]:
            
            return (f'{self.root()}{self._sev_type[1]} chord: ' + 
                       f'{self.root()} {self.third()} {self.fifth()} {self.seventh()}')
        else:
            return (f'{self.root()}{self._triad_type} chord: ' + 
                       f'{self.root()} {self.third()} {self.fifth()}')

    def __repr__(self):
        if self._sev_type[0]:      
            return f'{self.root()} {self.third()} {self.fifth()} {self.seventh()}'
        else:
            return f'{self.root()} {self.third()} {self.fifth()}'
     
def parser(string):
    
    if string[-1] != '7':
        trstring = string
        sevstring = None
        sevkind = None
    
    elif 'M' in string:
        trstring = string[:-1]
        sevstring = 'M'
        sevkind = 'M7'
    
    elif 'm' in string:
        trstring = string[:-1]
        sevstring = 'm'
        sevkind = 'm7'
        
    elif 'hd' in string:
        trstring = f'{string[:-3]}d'
        sevstring = 'm'
        sevkind = 'hd7'

    else:
        trstring = f'{string[:-1]}M'
        sevstring = 'm'
        sevkind = '7'
        
    name, triad_type = trparser(trstring)
    
    
    return name, triad_type, sevstring, sevkind
        
def main():
        
#    notes = ['C', 'G', 'D', 'A', 'E', 'Cb', 'B', 'F#', 'Gb', 'C#', 'Db', 'Ab',
#             'G#', 'Eb', 'D#', 'Bb', 'A#', 'F']
    notes = ['C','Db', 'Gb', 'Cb']
    suffixes = ['M', 'm', 'M7', 'm7', '7']
    
    for i in notes:
        for j in suffixes:
            print(Chord(f'{i}{j}'))
        print('')
    

    # print(Chord('CM7'))
    # print(Chord('Cm7'))
    # print(Chord('C7'))  
    # print(Chord('CM'))
    # print(Chord('Cm'))
      
    
# 'make everything run' workaround
if __name__ == '__main__': main()
