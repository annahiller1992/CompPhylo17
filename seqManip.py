DNA = str("aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg")
#reads in sequence as object DNA
print(DNA)
#prints out sequence
print("prints sequence data to screen")
#prints note to screen
print(DNA.replace("t", "u"))
#replaces 't' with 'u' to make RNA version
print(DNA.replace("a", "x").replace("t", "a").replace("x", "t").replace("g", "y").replace("c", "g").replace("y", "c"))
#introduces a temporary variable to replace multiple characters
print(DNA[37:43])
#prints 13th and 14th codons (1 codon is 3 nucleotides)
AAs  = str("FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG")
Base1  = str("TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG")
Base2  = str("TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG")
Base3  = str("TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG")
#reads in the translate table
print(AAs)
print(Base1)
print(Base2)
print(Base3)
#prints out table for reference
def translate(DNA):
     trip = [DNA[i:i+3]for i in range(0,len(DNA),3)]
#the above for loop searches through file DNA by sets of three, if you remove final '3' after len(DNA) then it will print out single characters at end and misread
     for codon in trip:
         if codon in ['ttt','ttc']:
             print("Phe"), 
         elif codon in ['tta', 'ttg', 'ctt', 'cta', 'ctc', 'ctg']:
             print ("Leu"),
         elif codon in ['att', 'atc']:
             print ("Ile"),
         elif codon in ['ata', 'atg']:
             print ("Met"),
         elif codon in ['gtt','gtc', 'gta', 'gtg']:
             print ("Val"),
         elif codon in ['tct', 'tcc', 'tca', 'tcg']:
             print ("Ser"),
         elif codon in ['cct', 'ccc', 'cca', 'ccg']:
             print ("Pro"),
         elif codon in ['act' , 'acc', 'aca' , 'acg']:
             print ("Thr"),
         elif codon in ['gct' , 'gcc', 'gca' , 'gcg']:
             print ("Ala"),
         elif codon in ['tat' , 'tac']:
             print ("Tyr"),
         elif codon in ['taa' , 'tag']:
             print ("Ter"),
         elif codon in ['cat' , 'cac']:
             print ("His"),
         elif codon in ['caa' , 'cag']:
             print ("Gln"),
         elif codon in ['aat' , 'aac']:
             print ("Asn"),
         elif codon in ['aaa' , 'aag']:
             print ("Lys"),
         elif codon in ['gat' , 'gac']:
             print ("Asp"),
         elif codon in ['gaa' , 'gag']:
             print ("Glu"),
         elif codon in ['tgt' , 'tgc']:
             print ("Cys"),
         elif codon in ['tga' , 'tgg']:
             print ("Trp"),
         elif codon in ['cgt' , 'cgc' , 'cga' , 'cgg']:
             print ("Arg"),
         elif codon in ['agt' , 'agc']:
             print ("Ser"),
         elif codon in ['aga' , 'agg']:
             print ("Ter"),
         elif codon in ['ggt' , 'ggc' , 'gga' , 'ggg']:
             print ("Gly"),
         else:
            print("science!")
#this defines the amino acid codes by their various triplet nucleotide sequences. Not sure what to do with the start codons...
translate(DNA)
#then executes function and prints to screen all in one vertical column
#remove comma to get rid of 'new line'
#am still confused about the difference between [] and ()
#[] for functions, () for objects

