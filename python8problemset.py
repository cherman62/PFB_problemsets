#Question 1
with open('Python_08.fasta.txt','r') as py8fasta:
    geneName_ntcount = {}
    for line in py8fasta:
        line = line.rstrip()
        print(line)
        if line.startswith('>'):
            seqID = line
            geneName_ntcount[seqID] = {'A':0, 'G':0, 'C':0, 'T':0}
        else:
            geneName_ntcount[seqID]['A'] += line.count("A")
            geneName_ntcount[seqID]['T'] += line.count("T")
            geneName_ntcount[seqID]['C'] += line.count("C")
            geneName_ntcount[seqID]['G'] += line.count("G")
print(geneName_ntcount)

#Question 2
