#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 12:02:43 2020

@author: dennisbrookner
"""
#Globals
nn = {'B#': 1,
      'C' : 1,
      'C#': 2,
      'Db': 2,
      'D' : 3,
      'D#': 4,
      'Eb': 4,
      'E' : 5,
      'Fb': 5,
      'E#': 6,
      'F' : 6,
      'F#': 7,
      'Gb': 7,
      'G' : 8,
      'G#': 9,
      'Ab': 9,
      'A' : 10,
      'A#': 11,
      'Bb': 11,
      'B' : 12,
      'Cb': 12}


nnr = dict(map(reversed, nn.items()))

fs = dict(C = 'B#',
          Db = 'C#',
          D = 'D',
          Eb = 'D#',
          Fb = 'E',
          F = 'E#',
          Gb = 'F#',
          G = 'G',
          Ab = 'G#',
          A = 'A',
          Bb = 'A#',
          Cb = 'B')

sf = dict(map(reversed, fs.items()))


class Note:
    def __init__(self, name):
        """
        Constructor, uses name to assign name and number
        """
        if isinstance(name, str):
            self.name(name)
        elif isinstance(name, int):
            self.num(name)
        else:
            raise ValueError('Notes can only be initialized with strings or ints')
      
    def name(self, name = None):
        """
        setter/getter for note name (changes name and number)
        """
        if name:
            
            if name in nn:
                self._name = name
                self._num = nn[name]
            elif name in sf:
                self._name = name
                self._num = nn[sf[name]]
            elif name in fs:
                self._name = name
                self._num = nn[name]

            else:
                raise KeyError('Name must be a valid note name')
            
            if 'b' in name:
                self.acc('f')
            elif '#' in name:
                self.acc('s')
            else:
                self.acc('n')

        
        return self._name
    
    def num(self, num = None):
        """
        setter/getter for note number (changes name and number)
        """
        if num in nnr:
            self._num = num
            self._name = nnr[num]
            
            if 'b' in self.name():
                self.acc('f')
            elif '#' in self.name():
                self.acc('s')
            else:
                self.acc('n')

        elif isinstance(num, int):
            raise KeyError('Number must be between 1 and 12, inclusive')
        elif num:
            raise KeyError('Note.num() requires a numeric argument')
        return self._num
    
    
    def acc(self, acc = None):
        """
        Is this note natural sharp, or flat?
        """
        if acc:
            self._acc = acc
        return self._acc
  
      
    def to_sharp(self):
        
        if self.name() in fs:
            self.name(fs[self.name()])
        return self

            
    def to_flat(self):
        
        if self.name() in sf:
            self.name(sf[self.name()])
        return self
        
    
    def transpose(self, change):
        """
        Handle transposition
        """
        if not isinstance(change, int):
            raise TypeError('Transpositions must be by integer values')
        elif change >= 12 or change <= -12:
            raise ValueError('Don\'t transpose by more than an octave!')
        elif change == 0:
            transposed = self
        elif self.num() + change >= 1 and self.num() + change <= 12:
            transposed = Note(self.num() + change)
        elif self.num() + change > 12:
            transposed = Note(self.num() + change - 12)
        elif self.num() + change < 1:
            transposed = Note(self.num() + change + 12)
        
        return transposed
    
    def distance(self, other):
        """
        Find the distance along the circle of fifths between
        two notes 'self' and 'other', returning an integer
        """
        count = 0
        while(self.num() != other.num()):
            count += 1
            self = self.transpose(7)
        
        return(count)
        
            
    def __str__(self):
        return f'{self.name()}'
    
    def __repr__(self):
        return f'{self.name()}'
        
        
def main():
    
    a = Note('C')
    print(a)
    print(a.to_sharp())
    b = Note('E#')
    print(b)
    print(b.to_flat())

   
# 'make everything run' workaround
if __name__ == '__main__': main()

        