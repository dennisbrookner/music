#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:28:30 2020

@author: dennisbrookner
"""

from Music.notes import Note
from Music.chords import Chord
import numpy as np

scale_numbers = [0,2,4,5,7,9,11,12,14,16,17,19,21]
modes = ['major', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'minor', 'locrian']

class Scale():
    '''
    Scale objects have a 'scale_type' attribute, and 
    seven note attributes for the root through seventh
    
    Important: scale types are 1-indexed, like in normal music
    '''
    
    def __init__(self, root_name, mode=1):
    
            
        self._mode_num = mode
        self._mode = modes[self._mode_num-1]
        
        root = Note(root_name)
        self._root_name = root.name()
        
        t = np.array(scale_numbers[self._mode_num-1:self._mode_num+6]) - scale_numbers[self._mode_num-1]
        
        self._notes = [root.transpose(i.item()) for i in t]
        
        self.spell()
        
        return
    
    def get_notes(self, num=None):
        
        if num:
            return self._notes[num-1]
        else:
            return self._notes
        
    def spell(self):
        
        major_root = self._notes[0].num() - scale_numbers[self._mode_num-1]
        if major_root < 1:
            major_root += 12
        d = Note('F').distance(Note(major_root))
        
        if d in range(3,6):
            self._notes = [i.to_sharp() for i in self._notes]
            
        elif d in range(9,12):
            self._notes = [i.to_flat() for i in self._notes]
        
        elif d in range(6,9):
            if self._notes[0].acc() == 'f':
                self._notes = [i.to_flat() for i in self._notes]
            else:
                self._notes = [i.to_sharp() for i in self._notes]
        
        elif d in range(0,3):
            for i in self._notes:
                if i.num() == 1: # C
                    i.to_flat()
                elif i.num() == 5: # E
                    i.to_sharp()
                elif i.num() == 12: # B
                    i.to_sharp()
            
        else:
            raise ValueError('Unexpected transposition error in Scale.spell')
        return self       
    
    def __str__(self):
        return f'{self._root_name} {self._mode} scale: {str(self.get_notes())}'
    
    def __repr__(self):
        return str(self.get_notes())

def main():
    print(Scale('D'))
    print(Scale('Eb', mode=6))
    print(Scale('G#', mode=3))

        
if __name__ == '__main__': main()
        
        
        
        
        
