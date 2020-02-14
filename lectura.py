# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:16:02 2019

@author: Eliseo-AGonzalez
"""
import os
import spacy
from spacy import displacy
nlp = spacy.load('es_core_news_sm')

import nltk
#nltk.download('punkt')
#nltk.download('stopwords')

from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer

def extraerCorreos(rootdir):
    ham_list = []
    spam_list = []
    print(rootdir)
    try:
        for directories, subdirs, files in os.walk(rootdir):
            if (os.path.split(directories)[1]  == 'ham'):
                for filename in files:      
                    with open(os.path.join(directories, filename), encoding="latin-1") as f:
                        data = f.read()
                        ham_list.append(data)


            if (os.path.split(directories)[1]  == 'spam'):
                for filename in files:
                    with open(os.path.join(directories, filename), encoding="latin-1") as f:
                        data = f.read()
                        spam_list.append(data)
        print(len(ham_list),len(spam_list))
        return [ham_list,spam_list]
    except IOError as e:
        print("Directorios no existen!")

"""	
try:
   f = open("foo.txt")
except IOError as e:
   print("Uh oh! Esto no existe")
print("Number of cpu: ",multiprocessing.cpu_count() )
directorios = ['C:\\Users\\Eliseo-AGonzalez\\Documents\\TRABAJOS\\MineriaDatos\\ProyectoCorreos\\enron\\enron1','C:\\Users\\Eliseo-AGonzalez\\Documents\\TRABAJOS\\MineriaDatos\\ProyectoCorreos\\enron\\enron2','C:\\Users\\Eliseo-AGonzalez\\Documents\\TRABAJOS\\MineriaDatos\\ProyectoCorreos\\enron\\enron3','C:\\Users\\Eliseo-AGonzalez\\Documents\\TRABAJOS\\MineriaDatos\\ProyectoCorreos\\enron\\enron4','C:\\Users\\Eliseo-AGonzalez\\Documents\\TRABAJOS\\MineriaDatos\\ProyectoCorreos\\enron\\enron5','C:\\Users\\Eliseo-AGonzalez\\Documents\\TRABAJOS\\MineriaDatos\\ProyectoCorreos\\enron\\enron6']
jobs = []

if __name__ == '__main__':
    start_time = time()
    
    # por default toma 
    p = Pool(6) # el tamaño de la agrupación es 2, por lo que dos ejecuciones de la función work_log suceden en paralelo
    # cuando una de las funciones de procesamiento finaliza, selecciona el siguiente argumento y así sucesivamente
    correosTotales = p.map(extraerCorreos,directorios) # lanzamiento 
 
    elapsed_time = time() - start_time
    print("Tiempo : %d" % elapsed_time)
    print("Tamaño de la variable que contiene los correos(ham,spam) en cada carpeta enron ",len(correosTotales))
    print("Total de correos ham y spam en carpeta enron1 ",len(correosTotales[0][0]),len(correosTotales[0][1]))
    print(correosTotales[0][0][300])
"""
def bolsaPalabras(arreglo):
    palabras = []
    for i in range(len(arreglo[0])): # recorre los textos que estan en cada carpeta enron1 al 6
        for j in range(len(arreglo[0][i])):
            texto = arreglo[0][i][j]
            
            doc = nlp(str(texto))
            for token in doc:
                #print(token.text, token.lemma_, token.pos_)
                if token.lemma_ not in palabras and token.lemma_ not in arreglo[1]: # ingresa el verbo a la var, sin repetir verbos
                    palabras.append(token.lemma_)
    return palabras
                
def bW(arreglo):
    palabras = []
    for i in range(len(arreglo[0])): # recorre los textos que estan en cada carpeta enron
        for j in range(500): # Correos a utilizar, como solo sera 1000, seran 500ham, 500spam
            texto = str(arreglo[0][i][j])
            doc = arreglo[2](str(texto))
            for token in doc:
                #print(token.text, token.lemma_, token.pos_)
                if token.pos_=='PROPN' or token.pos_=='VERB' or token.pos_=='NOUN' or token.pos_=='ADJ':
                    if token.lemma_ not in palabras and token.lemma_ not in arreglo[1]: # ingresa el verbo a la var, sin repetir verbos
                        palabras.append(token.lemma_)
    return palabras


def filtradoNLTK(wordsArray):
    filtrado = []
    basura = []
    doc = nltk.pos_tag(wordsArray)
    #print(doc[0])
    for token in doc:
        if token[1]=='NN' or token[1]=='JJR' or token[1]=='JJS' or token[1]=='NNP' or token[1]=='NNS' or token[1]=='RB' or token[1]=='VB':
            filtrado.append(token[0])
        else:
            basura.append(token[0])
    return [filtrado,basura]
