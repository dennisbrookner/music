# Music

A package for creation of various musical entities including notes, chords, and scales.  Created as an exercise in class and package development  

## Notes
Note objects have a name, a number (1-12 starting with C), and an accidental type. The Note constructor can take either name or number, and will automatically assign the other, so `Note('D')` and `Note(3)` both create the same note with name 'D' and number 3.  

#### Accidentals and enharmonics
For all notes with two possible enharmonic representations (excluding double sharps and flats, which are not supported), the `Note.to_sharp()` and `Note.to_flat()` methods can change these representations.  These methods are also safe to use on notes that are already sharped or flatted, or which don't have an enharmonic respelling.  These methods do __not__ change the value of the note; to, say, change a G to a G#, read on:  

#### Transposition
Notes can be transposed up or down by up to 11 half-steps.  Importantly, the transpose function does not work in place, meaning usage should look like `new_note = old_note.transpose(number)`  
  
#### Circle of fifths
The 'distance' method can find the circle-of-fifths distance between two notes.  Usage is made clearer with an example:
```python
from Music import Note

C = Note('C')
G = Note('G')

C.distance(G) # is 1, while
G.distance(C) # is 11
```
  
## Chords
Just as chords are comprised of notes, a Chord object is comprised of three (or four) Note objects. Each Note is an attribute of the chord, accessible as Chord.root(), Chord.third(), etc.  When using chords, there is no need to manually make notes; construction of notes is wrapped into the chord constructor.  The Chord class currently supports all diatonically occurring triads and seventh chords.
  
#### Constructing a chord
The Chord constructor takes a single string, which starts with the name of the root, and continues with a suffix indicating the chord type:  
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
print(Chord('Cbm')) # prints B minor, because Cb minor would have an Ebb
```
This works for 7ths too:
```python
print(Chord('CbM7')) # successfully prints Cb major 7
print(Chord('Cbm')) # prints B minor 7, because Cb minor would have an Ebb and a Bbb
print(Chord('Cb7')) # prints B7, because the 7th of Cb7 would be Bbb
```
#### Displaying a chord
Printing a chord is verbose and includes a description of the chord's name and type:
```python
print(Chord('Cm7'))
```
returns
```
Cm7 chord: C Eb G Bb
```
whereas the direct return from repr is terser:
```python
repr(Chord('Cm7'))
```
returns
```
'C Eb G Bb'
```
and would support something like:
```python
chord_as_text = repr(Chord('Cm7')).split()
print(chord_as_text)
```
which returns
```
['C', 'Eb', 'G', 'Bb']
```

#### Transposing a chord
Like a Note, a Chord can be easily transposed:
```python
old_chord = Chord('CM7')
new_chord = old_chord.transpose(3)
print(new_chord)
```
and the new chord has been transposed up by 3 half steps:
```
EbM7 chord: Eb G Bb D
```
The transpose method supports values between -11 and 11 (inclusive).  Additionally, the transpose method will always give back the same type of chord.  Future functionality may support a "Key" class that can intelligently change chord type along with transposition.
