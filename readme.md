This project will take a text file of German text and provide the 30 most common words with the English translation. It can also read a text file to remove words that are already known. 

before running make sure to install spaCy via `pip install spacy` and download the German model for their [site](https://spacy.io/usage/models). 

To call it run it with the parameters `python3 -in <text file> -ex <excluded word file>`

German has separable verbs where the prefix of the verb is separated and put at the end of the sentence. For example, the verb ‘anrufen’, example sentence Ich *rufe* sie *an*. To capture these verbs correct I used the library [spaCy](https://spacy.io/) which does natural language processing. This library was also used to de- conjugate the verbs. 

To do the translation the program needs a text file dictionary. I used [Dict.cc](https://www1.dict.cc/translation_file_request.php?l=e) that can be downloaded for personal use, and is not included in this repository. 

The original goal for this project was to use it to find the most common words in a text that I would use as part of teaching myself German. 

