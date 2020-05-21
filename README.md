# Music

A package for creation of chord and note objects (and maybe scales eventually).  Created as an exercise in class and package development

Currently supports major and minor triads through the "Triad" class, and major 7, minor 7, and 7 chords through the "Chord" class (Chord inherits from Triad, so Chord can be used for triads, as in the example below).

#### Usage
Chord constructor both takes a single string, which starts with the root, and continues with a suffix indicating the chord type:  
M - major  
m - minor  
M7 - major seventh  
m7 - minor seventh  
7 - seventh ('major-minor-seventh')  

##### Example
```python
from Music import *

# make a D major chord
Dmaj = Chord('DM')
print(Dmaj)

# make an Eb minor 7 chord
Ebm7 = Chord('Ebm7')
print(Ebm7)

# if spelling the chord with the given root would require a double sharp or double flat,
# the root is rewritten as the enharmonic
print(Chord('CbM')) # successfully prints Cb major
print(Chord('Cbm')) # prints B minor, becasue Cb minor would have an Ebb

# this works for 7ths too:
print(Chord('CbM7')) # successfully prints Cb major 7
print(Chord('Cbm')) # prints B minor 7, becasue Cb minor would have an Ebb and a Bbb
print(Chord('Cb7')) # prints B7, because the 7th of Cb7 would be Bbb
```
##### String vs. repr
Printing a chord is more verbose and includes a description of the chord:
```
In [1]: print(Chord('Cm7'))
Cm7 chord: C Eb G Bb
```
whereas the direct return from repr is terser:
```
In [2]: Chord('Cm7')
Out[2]: C Eb G Bb
```
and would support something like:
```python
text_chord = repr(Chord('Cm7')).split()
```
