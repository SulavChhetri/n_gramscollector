import pandas as pd
import json

def ngramchecker(strings,n_grams):
    finallist = []
    finalstring = ''
    splitlist = strings.split()
    n_grams_range = len(splitlist)-n_grams+1
    if (len(strings.split())<n_grams):
        return [strings]
    else:
        for x in range(n_grams_range): 
            for i in range(n_grams):  
                finalstring =finalstring+' '+splitlist[x+i]
            finallist.append(finalstring.lstrip())
            finalstring = ''
        return finallist

bidict = {}
tridict = {}
def main():
    bigram_global =[]
    trigram_global =[]
    data = pd.read_csv('3_govt_urls_state_only.csv')
    data = data['Note']
    for item in data:
        note = item.split("--")[0]
        for number in range(2,4):
            n_gram = ngramchecker(note,number)
            for i in n_gram:
                if number==2:
                    if i not in bidict.keys():
                        bidict[i]=1
                    else:
                       bidict[i] =bidict[i]+1
                else:
                    if i not in tridict.keys():
                        tridict[i]=1
                    else:
                       tridict[i] =tridict[i]+1

    for key in bidict.keys():
        if bidict[key]>15:
            bigram_global.append(key)

    for key in tridict.keys():
        if tridict[key]>8:
            trigram_global.append(key)

    with open("bigram.json",'w')as file:
        json.dump(bigram_global,file)
    
    with open("trigram.json",'w')as file:
        json.dump(trigram_global,file)

main()


