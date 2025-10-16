#Question 1&2

#!/usr/bin/env python3

with open("Python_06.txt","r") as p6read, open("python6psetq1b.txt","w") as p6write:
    for line in p6read:
        print(line.upper())
        p6write.write(line.upper())

#Question 3

with open("Python_06.seq.txt","r") as p6seqread:
    for line in p6seqread:
        line = line.rstrip()
        lsplit = line.split('\t')
        item = lsplit[1]
        complsplit = item.replace('G','c').replace('C','g').replace('A','t').replace('T','a')
        revcomplsplit = complsplit[::-1]
        revcomplsplit = revcomplsplit.upper()
        print(lsplit[0]," Reverse complement","\t",revcomplsplit,sep='')

#Question 4

linenumber = 0
charnumber = 0
with open("Python_06.fastq.txt","r") as p6fastq:
    for line in p6fastq:
        line = line.rstrip()
        char = len(line)
        charnumber += char
        line = 1
        linenumber += line
    seqIDnumber = linenumber/4
    seqIDnumber = int(seqIDnumber)
    avglinelength = charnumber/linenumber
    avglinelength = int(avglinelength)
    print("Total # of lines:",linenumber)
    print("Total # of characters:",charnumber)
    print("Total # of sequence ID:",seqIDnumber)
    print("Average line length of all the lines:",avglinelength)

seqlinecount = 0
totalntcount = 0
with open("Python_06.fastq.txt","r") as p6fastq:
    for line in p6fastq:
        line = line.rstrip()
        if all(char in ['A','T','C','G'] for char in line):
# remember that the block of code underneath if statement will run if whatever follows if is TRUE. The line above is true if ALL characters in a line has a match to A,T,C, or G
            seqlinecount += 1
            totalntcount += len(line)
    avglinelengthwithseq = totalntcount/seqlinecount
    avglinelengthwithseq = int(avglinelengthwithseq)
    print("Total # of lines with DNA sequence:", seqlinecount)
    print("Total # of nucleotides:", totalntcount)
    print("Average line length of the lines that contain sequences:", avglinelengthwithseq)