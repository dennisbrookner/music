# Music

A package for creation of chord and note objects (and maybe scales eventually).  Created as an exercise in class and package development

Currently supports major and minor triads through the "Triad" class, and major 7, minor 7, and 7 chords through the "Chord" class.

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
print(dmaj)

# make an Eb minor 7 chord
Ebm7 = Chord('Ebm7')
print(Ebm7)
```
