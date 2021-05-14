import spacy

python -m spacy download ("en_core_web_sm")
python -m spacy download ("en_core_web_sm")

nlp = spacy download ("en_core_web_sm")

nlp = spacy.load("en_core_web_sm")

with codecs.open("BitcoinProcessedUni3.txt","r",encoding="UTF-8") as f:
    text = f.read().replace ("\n\n", " ").replace("\n", " ")
    RT = text.split("RT ")[1:]
    
