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
def takeSecond(elem):
    return elem[1]

bidict = {}
tridict = {}
def main():
    bigram_global ={}
    trigram_global ={}
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

    templist1 = sorted(bidict.items(),key=takeSecond,reverse=True)[:20]
    templist2 = sorted(tridict.items(),key=takeSecond,reverse=True)[:20]
    for item in templist1:
        bigram_global[item[0]]=item[1]
    
    for item in templist2:
        trigram_global[item[0]]=item[1]

    with open("bigram.json",'w')as file:
        json.dump(bigram_global,file)
    
    with open("trigram.json",'w')as file:
        json.dump(trigram_global,file)

main()


