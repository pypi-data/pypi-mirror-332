## WordWiz: A wizard of words!

WordWiz was inspired by [PyDictionary](https://github.com/geekpradd/PyDictionary). It can get defintions from the [dictionaryapi](https://dictionaryapi.dev). For synonyms and antonyms, it uses [synonym.com](https://synonym.com). This library uses Requests and BeautifulSoup4 to power WordWiz!

### Installation
```
pip install WordWiz
```

### Definitions
```
import WordWiz

term = input("Enter a term: ")
print(WordWiz.get_definitions(term))
```

### Synonyms
```
import WordWiz

term = input("Enter a term: ")
print(WordWiz.get_synonyms(term))
```

### Antonyms
```
import WordWiz

term = input("Enter a term: ")
print(WordWiz.get_antonyms(term))
```

### Errors
```
import WordWiz
from WordWiz import errors

term = input("Enter a term: ")

try:
    print(WordWiz.get_definitions(term))
except errors.APIException as e:
    print("Term not found in the api.")
```
```
import WordWiz
from WordWiz import errors

term = input("Enter a term: ")

try:
    print(WordWiz.get_definitions(term))
except errors.TermException as e:
    print("Term must be a single word.")
```

### About
Current Version: 0.0.2 devs_des1re