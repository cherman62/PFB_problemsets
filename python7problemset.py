#Question 1
import re

with open('Python_07_nobody.txt','r') as py7nobody:
    for line in py7nobody:
        found = re.search(r"Nobody",line)
        print(found)

#Question 2
with open('Python_07_nobody.txt','r') as py7nobody, open('Alfred.txt','w') as py7alfred:
    for line in py7nobody:
        alfred = re.sub(r"Nobody", r"Alfred", line)
        py7alfred.write(alfred)

#Question 3
with open('Python_07.fasta.txt','r') as p7fasta:
    for line in p7fasta:
        for headerline in re.findall(r"^>.+", line):
            print(headerline)

#Question 4
seqIDdesc = {}
with open('Python_07.fasta.txt','r') as p7fasta:
    for line in p7fasta:
        for headerline in re.findall(r"^>.+", line):
            splitheaderline = headerline.split(' ')
            key = splitheaderline[0]
            value = " ".join(splitheaderline[1:])
            seqIDdesc[key] = value
print(seqIDdesc)

#Question 5
seqIDs = []
DNAs = []
with open("Python_06.fasta","r") as python6fasta:
    for line in python6fasta:
        line = line.rstrip()
        for seqID in re.findall(r'^>.+', line):
            seqIDs.append(seqID)
        for DNA in re.findall(r'^[AGTC].+', line):
            DNAs.append(DNA)
print(seqIDs)
print(DNAs)
seqDNA = dict(zip(seqIDs,DNAs))
print(seqDNA)

#Question 6
with open("Python_07_ApoI.fasta.txt","r") as py7fasta:
    for line in py7fasta:
        line = line.rstrip()
        for ApoI in re.findall(r"[AG]AATT[CT]", line):
            print(ApoI)

#Question 7
DNA_RE_site = ''
with open("Python_07_ApoI.fasta.txt","r") as py7fasta:
    for line in py7fasta:
        line = line.rstrip()
        visiblesite = re.sub(r'([AG])AATT([CT])', r'\1^AATT\2', line)
        print(visiblesite)

#Question 8
DNA_RE_split = []
seq = ''
with open("Python_07_ApoI.fasta.txt","r") as py7fasta:
    next(py7fasta)
    for line in py7fasta:
        line = line.rstrip()
        visiblesite = re.sub(r'([AG])AATT([CT])', r'\1^AATT\2', line)
        seq += visiblesite
        visiblesite_split = seq.split('^')
        visiblesite_split = sorted(visiblesite_split, key=len, reverse=True)
print(visiblesite_split)

#Question 9
RElist = {}
with open("bionet.txt",'r') as py7relist:
    for i in range(10):
        next(py7relist)
    for line in py7relist:
        line = line.rstrip()
        for (res_enzyme,cut_site) in re.findall(r'(^\S+ ?\S+) {2,}(\S+)', line):
            #go to regex101.com to see how many groups come out of the regex. If there are three groups, there will be three variables that need to go into the () right after for. Since there are only two groups, there are only two variables in the ()
            print(res_enzyme, cut_site)
            RElist[res_enzyme] = cut_site
print(RElist)

#Question 10
