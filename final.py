import pandas as pd
import json
import csv

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

def main():
    with open("./initial/bigram.json",'r') as file:
        bigram_20 = json.load(file)
    with open("./initial/trigram.json",'r') as file:
        trigram_20 =json.load(file)
    
    data = pd.read_csv('3_govt_urls_state_only.csv')
    data = data['Note']
    
    with open('bi_output.csv','w', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(["Note","Topic"])
        for item in data:
            note = item.split("--")[0]
            n_gram = ngramchecker(note,2)
            for item in n_gram:
                if item in bigram_20.keys():
                    writer.writerow([f"{note}",f"{item}"])
    
    with open('tri_output.csv','w', encoding='UTF8') as file:
        writer = csv.writer(file)
        writer.writerow(["Note","Topic"])
        for item in data:
            note = item.split("--")[0]
            n_gram = ngramchecker(note,3)
            for item in n_gram:
                if item in trigram_20.keys():
                    writer.writerow([f"{note}",f"{item}"])
                    



main()