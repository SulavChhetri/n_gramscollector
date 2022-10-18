import pandas as pd


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

bigram_global =[]
trigram_global =[]
def main():
    data = pd.read_csv('3_govt_urls_state_only.csv')
    data = data['Note']
    for item in data:
        note = item.split("--")[0]
        for number in range(2,4):
            n_gram = ngramchecker(note,number)
            for i in n_gram:
                if number==2:
                    bigram_global.append(i)
                else:
                    trigram_global.append(i)


main()
print(bigram_global)
print(trigram_global)

