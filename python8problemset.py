# # Question 1
# with open('Python_08.fasta.txt','r') as py8fasta:
#     geneName_ntcount = {}
#     for line in py8fasta:
#         line = line.rstrip()
#         print(line)
#         if line.startswith('>'):
#             seqID = line
#             geneName_ntcount[seqID] = {'A':0, 'G':0, 'C':0, 'T':0}
#         else:
#             geneName_ntcount[seqID]['A'] += line.count("A")
#             geneName_ntcount[seqID]['T'] += line.count("T")
#             geneName_ntcount[seqID]['C'] += line.count("C")
#             geneName_ntcount[seqID]['G'] += line.count("G")
# print(geneName_ntcount)

# #Question 2
# import re

# with open('Python_08.fasta.txt', 'r') as py8fasta:
#     seqID = []
#     seq = []
#     for line in py8fasta:
#         line = line.rstrip()
#         if line.startswith('>'):
#             geneID = line
#             seqID.append(geneID)
#             DNAseq = ''
#             seq.append(DNAseq)
#         else:
#             seq[-1] += line
# print(seqID)
# print(seq)

# seq_with_codon_space = []
# for i in seq:
#     seq_space = re.sub(r'(.{3})',r'\1 ',i)
#     seq_with_codon_space.append(seq_space)
# print(seq_with_codon_space)

# zip_seqID_seq = zip(seqID, seq_with_codon_space)
# fasta_with_codon_space = dict(zip_seqID_seq)
# print(fasta_with_codon_space)

# with open('Python_08.codons-frame-1.nt.txt', 'w') as p8q2out:
#     for j in fasta_with_codon_space:
#             gene_name = fasta_with_codon_space[j]
#             p8q2out.write(j)
#             p8q2out.write('\n')
#             p8q2out.write(gene_name)
#             p8q2out.write('\n')

# #Question 3
# import re

# with open('Python_06.fasta', 'r') as py8fasta:
#     seqID = []
#     seq = []
#     for line in py8fasta:
#         line = line.rstrip()
#         if line.startswith('>'):
#             for i in range(1,4):
#                 line_app = line+'-frame-'+str(i)+'-codons'
#                 seqID.append(line_app)
#             DNAseq = ''
#             seq.append(DNAseq)
#         else:
#             seq[-1] += line
# print(seqID)
# print('')
# print('')
# print('')
# print('')
# print(seq)
# print('')
# print('')
# print('')
# print('')
# seq_with_codon_space_3frame = []
# for i in seq:
#     for j in range(3):
#         seq_space = re.sub(r'(.{3})',r'\1 ',i[j:])
#         seq_with_codon_space_3frame.append(seq_space)

# print(seq_with_codon_space_3frame)

# print('')
# print('')
# print('')
# print('')
# zip_seqID_seq = zip(seqID, seq_with_codon_space_3frame)
# fasta_with_codon_space_3frame = dict(zip_seqID_seq)
# print(fasta_with_codon_space_3frame)

# with open('Python_08.codons-3frames.nt.txt', 'w') as p8q3out:
#     for k in fasta_with_codon_space_3frame:
#             gene_name = fasta_with_codon_space_3frame[k]
#             p8q3out.write(k)
#             p8q3out.write('\n')
#             p8q3out.write(gene_name)
#             p8q3out.write('\n')

#Question 4
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
            for j in range(1,4):
                line_app_revcomp = line+'-frame-'+str(j)+'-codons-revcomp'
                seqID.append(line_app_revcomp)
            DNAseq = ''
            seq.append(DNAseq)
        else:
            seq[-1] += line
print(seqID)

seq_with_codon_space_3frame = []
seq_revcomp = []
for a in seq:
    a = str(a)
    a_comp = a.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
    a_revcomp = a_comp[::-1]
    a_revcomp_uppercase = a_revcomp.upper()
    seq_revcomp.append(a_revcomp_uppercase)

seq_seq_revcomp = []

for item1,item2 in zip(seq, seq_revcomp):
    seq_seq_revcomp.append(item1)
    seq_seq_revcomp.append(item2)

seq_with_codon_space_6frame = []
for k in seq_seq_revcomp:
    for l in range(3):
        seq_space = re.sub(r'(.{3})',r'\1 ',k[l:])
        seq_with_codon_space_6frame.append(seq_space)

print(seq_with_codon_space_6frame)
print('')
print('')
print('')
print('')

zip_seqID_seq_6frame = zip(seqID, seq_with_codon_space_6frame)
fasta_with_codon_space_6frame = dict(zip_seqID_seq_6frame)
print(fasta_with_codon_space_6frame)
print('')
print('')
print('')
print('')

with open('Python_08.codons-6frames.nt.txt', 'w') as p8q4out:
    for m in fasta_with_codon_space_6frame:
        gene_name = fasta_with_codon_space_6frame[m]
        p8q4out.write(m)
        p8q4out.write('\n')
        p8q4out.write(gene_name)
        p8q4out.write('\n')

