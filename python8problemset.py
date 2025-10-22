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
#             for j in range(1,4):
#                 line_app_revcomp = line+'-frame-'+str(j)+'-codons-revcomp'
#                 seqID.append(line_app_revcomp)
#             DNAseq = ''
#             seq.append(DNAseq)
#         else:
#             seq[-1] += line
# print(seqID)

# seq_with_codon_space_3frame = []
# seq_revcomp = []
# for a in seq:
#     a = str(a)
#     a_comp = a.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
#     a_revcomp = a_comp[::-1]
#     a_revcomp_uppercase = a_revcomp.upper()
#     seq_revcomp.append(a_revcomp_uppercase)

# seq_seq_revcomp = []

# for item1,item2 in zip(seq, seq_revcomp):
#     seq_seq_revcomp.append(item1)
#     seq_seq_revcomp.append(item2)

# seq_with_codon_space_6frame = []
# for k in seq_seq_revcomp:
#     for l in range(3):
#         seq_space = re.sub(r'(.{3})',r'\1 ',k[l:])
#         seq_with_codon_space_6frame.append(seq_space)

# print(seq_with_codon_space_6frame)

# zip_seqID_seq_6frame = zip(seqID, seq_with_codon_space_6frame)
# fasta_with_codon_space_6frame = dict(zip_seqID_seq_6frame)
# print(fasta_with_codon_space_6frame)


# with open('Python_08.codons-6frames.nt.txt', 'w') as p8q4out:
#     for m in fasta_with_codon_space_6frame:
#         gene_name = fasta_with_codon_space_6frame[m]
#         p8q4out.write(m)
#         p8q4out.write('\n')
#         p8q4out.write(gene_name)
#         p8q4out.write('\n')

#Question 5
# import re
# import pprint

# translation_table = {
#     'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
#     'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
#     'AAT':'N', 'AAC':'N',
#     'GAT':'D', 'GAC':'D',
#     'TGT':'C', 'TGC':'C',
#     'CAA':'Q', 'CAG':'Q',
#     'GAA':'E', 'GAG':'E',
#     'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
#     'CAT':'H', 'CAC':'H',
#     'ATT':'I', 'ATC':'I', 'ATA':'I',
#     'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
#     'AAA':'K', 'AAG':'K',
#     'ATG':'M',
#     'TTT':'F', 'TTC':'F',
#     'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
#     'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
#     'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
#     'TGG':'W',
#     'TAT':'Y', 'TAC':'Y',
#     'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
#     'TAA':'*', 'TGA':'*', 'TAG':'*'
# }

# print("translation_table")
# pprint.pprint(translation_table)
# print('')
# print('')
# print('')
# print('')

# with open('Python_06.fasta', 'r') as py8fasta:
#     seqID = []
#     seq = []
#     for line in py8fasta:
#         line = line.rstrip()
#         if line.startswith('>'):
#             for i in range(1,4):
#                 line_app = line+'-frame-'+str(i)+'-codons'
#                 seqID.append(line_app)
#             for j in range(1,4):
#                 line_app_revcomp = line+'-frame-'+str(j)+'-codons-revcomp'
#                 seqID.append(line_app_revcomp)
#             DNAseq = ''
#             seq.append(DNAseq)
#         else:
#             seq[-1] += line

# print("seqID")
# pprint.pprint(seqID)
# print('')
# print('')
# print('')
# print('')

# print("seq")
# pprint.pprint(seq)
# print('')
# print('')
# print('')
# print('')

# seq_revcomp = []
# for a in seq:
#     a = str(a)
#     a_comp = a.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
#     a_revcomp = a_comp[::-1]
#     a_revcomp_uppercase = a_revcomp.upper()
#     seq_revcomp.append(a_revcomp_uppercase)

# print("seq_revcomp")
# pprint.pprint(seq_revcomp)
# print('')
# print('')
# print('')
# print('')

# seq_seq_revcomp = []
# for item1,item2 in zip(seq, seq_revcomp):
#     seq_seq_revcomp.append(item1)
#     seq_seq_revcomp.append(item2)

# print("seq_seq_revcomp")
# print(seq_seq_revcomp)
# print('')
# print('')
# print('')
# print('')

# seq_with_codon_space_6frame = []
# for k in seq_seq_revcomp:
#     for l in range(3):
#         seq_space = re.sub(r'(.{3})',r'\1 ',k[l:])
#         seq_with_codon_space_6frame.append(seq_space)

# print("seq_with_codon_space_6frame")
# pprint.pprint(seq_with_codon_space_6frame)
# print('')
# print('')
# print('')
# print('')

# seq_normalized = []
# for sep_seq in seq_with_codon_space_6frame:
#     sep_seq = str(sep_seq)
#     delete_noncodon = re.sub(r'\S{1,2}$',r'',sep_seq)
#     seq_normalized.append(delete_noncodon)

# print("seq_normalized")
# pprint.pprint(seq_normalized)
# print('')
# print('')
# print('')
# print('')

# seq_with_codon_normalized = []
# for normalized_item in seq_normalized:
#     for codon, amino_acid in translation_table.items():
#         if codon in normalized_item:
#             normalized_item = normalized_item.replace(codon, amino_acid)
#     seq_with_codon_normalized.append(normalized_item)

# print("seq_with_codon_normalized")
# pprint.pprint(seq_with_codon_normalized)
# print('')
# print('')
# print('')
# print('')

# zip_seqID_aa_6frame = zip(seqID, seq_with_codon_normalized)
# fasta_with_aa_space_6frame = dict(zip_seqID_aa_6frame)
# pprint.pprint(fasta_with_aa_space_6frame)

# with open('Python_08.translated.aa.txt', 'w') as p8q5out:
#     for dict_key in fasta_with_aa_space_6frame:
#         amino_acid_complete = fasta_with_aa_space_6frame[dict_key]
#         p8q5out.write(dict_key)
#         p8q5out.write('\n')
#         p8q5out.write(amino_acid_complete)
#         p8q5out.write('\n')

#Question 6
import re
import pprint

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

print("translation_table")
pprint.pprint(translation_table)
print('')
print('')
print('')
print('')

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

print("seqID")
pprint.pprint(seqID)
print('')
print('')
print('')
print('')

print("seq")
pprint.pprint(seq)
print('')
print('')
print('')
print('')

seq_revcomp = []
for a in seq:
    a = str(a)
    a_comp = a.replace('A','t').replace('T','a').replace('C','g').replace('G','c')
    a_revcomp = a_comp[::-1]
    a_revcomp_uppercase = a_revcomp.upper()
    seq_revcomp.append(a_revcomp_uppercase)

print("seq_revcomp")
pprint.pprint(seq_revcomp)
print('')
print('')
print('')
print('')

seq_seq_revcomp = []
for item1,item2 in zip(seq, seq_revcomp):
    seq_seq_revcomp.append(item1)
    seq_seq_revcomp.append(item2)

print("seq_seq_revcomp")
print(seq_seq_revcomp)
print('')
print('')
print('')
print('')

seq_with_codon_space_6frame = []
for k in seq_seq_revcomp:
    for l in range(3):
        seq_space = re.sub(r'(.{3})',r'\1 ',k[l:])
        seq_with_codon_space_6frame.append(seq_space)

print("seq_with_codon_space_6frame")
pprint.pprint(seq_with_codon_space_6frame)
print('')
print('')
print('')
print('')

seq_normalized = []
for sep_seq in seq_with_codon_space_6frame:
    sep_seq = str(sep_seq)
    delete_noncodon = re.sub(r'\S{1,2}$',r'',sep_seq)
    seq_normalized.append(delete_noncodon)

print("seq_normalized")
pprint.pprint(seq_normalized)
print('')
print('')
print('')
print('')

seq_with_codon_normalized = []
for normalized_item in seq_normalized:
    for codon, amino_acid in translation_table.items():
        if codon in normalized_item:
            normalized_item = normalized_item.replace(codon, amino_acid)
    seq_with_codon_normalized.append(normalized_item)

print("seq_with_codon_normalized")
pprint.pprint(seq_with_codon_normalized)
print('')
print('')
print('')
print('')

zip_seqID_aa_6frame = zip(seqID, seq_with_codon_normalized)
fasta_with_aa_space_6frame = dict(zip_seqID_aa_6frame)

print("fasta_with_aa_space_6frame")
pprint.pprint(fasta_with_aa_space_6frame)
print('')
print('')
print('')
print('')

aalengthlist = []
for seqkey, aavalue in fasta_with_aa_space_6frame.items():
    aalength = re.findall(r'M.+?\*',aavalue)
    if len(aalength) > 1:
        aalengthmin = min(aalength, key=len)
        aalengthminlist = [aalengthmin]
        aalengthlist.append(aalengthminlist)
    else:
        aalengthlist.append(aalength)

print("aalengthlist")
print(aalengthlist)
print('')
print('')
print('')
print('')

zip_seqID_aa_shortestORF = zip(seqID, aalengthlist)
fasta_with_aa_shortestORF = dict(zip_seqID_aa_shortestORF)

print("fasta_with_aa_shortestORF")
print(fasta_with_aa_shortestORF)

#the plan is to do a for loop (while loop?) over the ">seqi" i being repeated 6 times
#then isolate only the longest string in a list
#if it's empty then remove entirely




# with open('Python_08.translated.aa.txt', 'w') as p8q5out:
#     for dict_key in fasta_with_aa_space_6frame:
#         amino_acid_complete = fasta_with_aa_space_6frame[dict_key]
#         p8q5out.write(dict_key)
#         p8q5out.write('\n')
#         p8q5out.write(amino_acid_complete)
#         p8q5out.write('\n')