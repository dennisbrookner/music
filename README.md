# Music

A package for creation of chord and note objects (and maybe scales and keys eventually).  Created as an exercise in class and package development

Currently supports all diatonically occurring triads and seventh chords.  All are available in the "Chord" class; the parent "Triad" class could also be used for triads, but there's no advantage to doing so.

#### Constructing a chord
The Chord constructor takes a single string, which starts with the root, and continues with a suffix indicating the chord type:  
M - major  
m - minor  
d - diminished  
M7 - major seventh  
m7 - minor seventh  
7 - seventh ('major-minor-seventh')  
hd7 - half-diminished seventh  

##### Examples
```python
from Music import *

# make a D major chord
Dmaj = Chord('DM')
print(Dmaj)

# make an Eb minor 7 chord
Ebm7 = Chord('Ebm7')
print(Ebm7)
```
If spelling the chord with the given root would require a double sharp or double flat, the root is rewritten as the enharmonic and then spelled:
```python
print(Chord('CbM')) # successfully prints Cb major
print(Chord('Cbm')) # prints B minor, becasue Cb minor would have an Ebb
```
This works for 7ths too:
```python
print(Chord('CbM7')) # successfully prints Cb major 7
print(Chord('Cbm')) # prints B minor 7, becasue Cb minor would have an Ebb and a Bbb
print(Chord('Cb7')) # prints B7, because the 7th of Cb7 would be Bbb
```
#### Displaying a chord
Printing a chord is verbose and includes a description of the chord's name and type:
```python
print(Chord('Cm7'))
```
returns
```python
Cm7 chord: C Eb G Bb
```
whereas the direct return from repr is terser:
```python
repr(Chord('Cm7'))
```
returns
```python
'C Eb G Bb'
```
and would support something like:
```python
chord_as_text = repr(Chord('Cm7')).split()
print(chord_as_text)
```
which returns
```python
['C', 'Eb', 'G', 'Bb']
```

#### Transposing a chord
A Chord can be easily transposed:
```python
old_chord = Chord('CM7')
new_chord = old_chord.transpose(3)
print(new_chord)
```
and the new chord has been transposed up by 3 half steps:
```python
EbM7 chord: Eb G Bb D
```
The transpose method only supports values between 1 and 11 (inclusive).  Additionally, the transpose method will always give back the same type of chord.  Future functionality may support a "Key" class that can intelligently change chord type along with transposition.
