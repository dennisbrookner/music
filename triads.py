#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:27:54 2020

@author: dennisbrookner
"""

from Music.notes import Note

chord_type = dict(M = ['C', 4, 7],
                  m = ['A', 3, 7]
#                  ,
#                  aug = [4, 8],
#                  dim = [3, 6]
                  )

class Triad():
    def __init__(self, string):
        
        name, kind = parser(string)

        if kind not in chord_type:
            raise ValueError(f'Unsupported chord type: "{kind}"')
        
        self._kind = kind
        
        self.root(name)
        
        third = self.root().transpose(chord_type[kind][1]).name()
        fifth = self.root().transpose(chord_type[kind][2]).name()
        
        self.third(third)
        self.fifth(fifth)
        
        # How should we display the root?
        self.trspell(kind)
        
                         
    def root(self, root = None):
        if root:
            self._root = Note(root)
        return self._root
    
    def third(self, third = None):
        if third:
            self._third = Note(third)
        return self._third
    
    def fifth(self, fifth = None):
        if fifth:
            self._fifth = Note(fifth) 
        return self._fifth
    
    def trspell(self, kind):
        base = chord_type[kind][0]
        d = Note(base).distance(self.root())
        if d in range(1,5): 
            self.root().to_sharp()
            self.third().to_sharp()
            self.fifth().to_sharp()
        elif d in range(8,12):
            self.root().to_flat()
            self.third().to_flat()
            self.fifth().to_flat()
            
        elif d in range(5,8):
            if self.root().acc() == 'f':
                self.root().to_flat()
                self.third().to_flat()
                self.fifth().to_flat()
            else:
                self.root().to_sharp()
                self.third().to_sharp()
                self.fifth().to_sharp()
                
        elif d == 0:
            if base == 'C':
                self.root().to_flat()
                self.third().to_sharp()
            else:
                self.third().to_flat()
                self.fifth().to_sharp()
        
        else:
            raise ValueError(f'Unexpected transposition error with d = {d}')
    
    def trtranspose(self, number):
        new_root_name = self.root().transpose(number).name()
        kind = self._kind
        return Triad(f'{new_root_name}{kind}')
    
    def __str__(self):
        return (f'{self.root()}{self._kind} chord: ' + 
                   f'{self.root()} {self.third()} {self.fifth()}')

    def __repr__(self):
        return f'{self.root()} {self.third()} {self.fifth()}'

def parser(string):
    
    name = string[:-1]
    kind = string[-1]
    
    return name, kind

def main():
        
#    notes = ['C', 'G', 'D', 'A', 'E', 'Cb', 'B', 'F#', 'Gb', 'C#', 'Db', 'Ab',
#             'G#', 'Eb', 'D#', 'Bb', 'A#', 'F']
    notes = ['C','Db']
    for root in notes:
        print(Triad(f'{root}M'))
#    print('')
    for root in notes:
        print(Triad(f'{root}m'))
      
    
# 'make everything run' workaround
if __name__ == '__main__': main()
