# Question 1
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
import re

with open('Python_08.fasta.txt', 'r') as py8fasta:
    seqID = []
    seq = []
    for line in py8fasta:
        line = line.rstrip()
        if line.startswith('>'):
            geneID = line
            seqID.append(geneID)
            DNAseq = ''
            seq.append(DNAseq)
        else:
            seq[-1] += line
print(seqID)
print(seq)

seq_with_codon_space = []
for i in seq:
    seq_space = re.sub(r'(.{3})',r'\1 ',i)
    seq_with_codon_space.append(seq_space)
print(seq_with_codon_space)

zip_seqID_seq = zip(seqID, seq_with_codon_space)
fasta_with_codon_space = dict(zip_seqID_seq)
print(fasta_with_codon_space)

with open('Python_08.codons-frame-1.nt.txt', 'w') as p8q2out:
    for j in fasta_with_codon_space:
            gene_name = fasta_with_codon_space[j]
            p8q2out.write(j)
            p8q2out.write('\n')
            p8q2out.write(gene_name)
            p8q2out.write('\n')

#Question 3
import re

with open('Python_06.fasta', 'r') as py8fasta:
    seqID = []
    seq = []
    for line in py8fasta:
        line = line.rstrip()
        if line.startswith('>'):
            for i in range(1,4):
                line_app = line+'-frame-'+str(i)+'-codons'
                seqID.append(line_app)
            DNAseq = ''
            seq.append(DNAseq)
        else:
            seq[-1] += line
print(seqID)
print('')
print('')
print('')
print('')
print(seq)
print('')
print('')
print('')
print('')
seq_with_codon_space_3frame = []
for i in seq:
    for j in range(3):
        seq_space = re.sub(r'(.{3})',r'\1 ',i[j:])
        seq_with_codon_space_3frame.append(seq_space)

print(seq_with_codon_space_3frame)

print('')
print('')
print('')
print('')
zip_seqID_seq = zip(seqID, seq_with_codon_space_3frame)
fasta_with_codon_space_3frame = dict(zip_seqID_seq)
print(fasta_with_codon_space_3frame)

with open('Python_08.codons-3frames.nt.txt', 'w') as p8q3out:
    for k in fasta_with_codon_space_3frame:
            gene_name = fasta_with_codon_space_3frame[k]
            p8q3out.write(k)
            p8q3out.write('\n')
            p8q3out.write(gene_name)
            p8q3out.write('\n')

