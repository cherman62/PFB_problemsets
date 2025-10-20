#Question 1
import re

def print60nt_atatime(dna_input):
    divdna = re.sub(r'(.{1,60})',r'\1\n',dna_input)
    return divdna

dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
print(print60nt_atatime(dna))
#how come this doesn't introduce literal "\n" in the string?

#Question 2
def print60nt_atatime_allformat(dna_input):
    dna_split = dna_2.split("\n")
    flattened_string = ''.join(dna_split)
    flattened_string = flattened_string.rstrip()
    flattened_string = flattened_string.strip()
    sepdna = re.sub(r'(.{1,60})',r'\1\n',flattened_string)
    return sepdna

dna_2 = '''GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACC
GTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACG
CTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCC
TCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAA
TGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATG
CCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCT
GTCATCTTCT'''

print(print60nt_atatime_allformat(dna_2))

#Question 3
def print_x_chars_per_line(dna, width):
    divdna = re.sub(rf'(.{{,{width}}})',r'\1\n',dna)
    #in order to susbtitute a variable into regex, you need to put it with f string (rf instead of r). Additionally, you need to put variable into curly braces. There is an extra set of curly braces to escape.
    return divdna

dna_3 = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
width = 80
print(print_x_chars_per_line(dna_3, width))

#Question 4
#!/usr/bin/env python3
import re
import sys

def print_x_chars_per_line_in_fasta(file_name, seq_width):
    with open(file_name, 'r') as py6fasta, open('python10problemsetq4output.txt','w') as p10q4out:
        py6fasta_dict = {}
        for line in py6fasta:
            line = line.rstrip()
            if line.startswith('>'):
                geneID = line
                py6fasta_dict[geneID] = ''
            else:
                py6fasta_dict[geneID] += line
        py6fasta_key = []
        py6fasta_value = []
        for i in py6fasta_dict:
            seq = py6fasta_dict[i]
            p10q4out.write(i)
            p10q4out.write('\n')
            divdna = re.sub(rf'(.{{1,{seq_width}}})',r'\1\n',seq)
    #keep in mind that 1 is needed in the bracket. Initially I had nothing (ie {{,{width}}}). Because that is implicitly 0, it also includes "nothing" or "new lines" so that's why there was a space between seq and the next seqID.
            p10q4out.write(divdna)
    return p10q4out

fasta_name = sys.argv[1]
length_of_seq = sys.argv[2]
print(print_x_chars_per_line_in_fasta(fasta_name, length_of_seq))

#Question 5
def gc_content(dna):
    dna_upper = dna.upper()
    Gcount = dna_upper.count('G')
    Ccount = dna_upper.count('C')
    total_DNA_length = len(dna_upper)
    GCcontent = (Gcount + Ccount)/total_DNA_length
    return GCcontent

dna_5 = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
print(f'{gc_content(dna_5):.2%}')

#Question 6
def reverse_complement(dna):
    comp = dna.replace('C','g').replace('G','c').replace('A','t').replace('T','a')
    revcomp = comp[::-1]
    revcomp = revcomp.upper()
    return revcomp

dna_6 = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT'
print(reverse_complement(dna_6))

#Question 7
import subprocess
subprocess.run(["wc", "-l", "Alfred.txt"])
subprocess.run(["ls"])
