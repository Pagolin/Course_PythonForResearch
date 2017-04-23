inputfile = "../week_three/translation/dna.txt"

def read_seq(inputfile):
    with open(inputfile, "r") as f:
        seq = f.read()
        #get rid of linebreaks
        #strings are immutable so replace returns a new String
    seq= seq.replace("\n", "")
    seq= seq.replace("\r", "")
    return seq

def translate(seq):
    """This is an example of a docstring, specifying the function and
    props of a function in this case of translate(seq). The function translates sequencs of DNA nucleotides to a sequence of amino acids using a cododn table
    
    :param seq: sequence of nucleotides as capital letter string, \n and \r will be removed
    :return: sequence of aminoacids as capital letter string
    """
    code_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

    protein = ""
    # make shure seq_length  is divisible by three

    if(len(seq)%3 ==0):
        print("ok")
        # create a range obect to codon-wise step over the sequence
        first_letters = list(range(0, len(seq), 3))
        for i in first_letters:
            codon = seq[i:i+3]
            protein += code_table[codon]

    else:
        print("Remainder= ", len(seq)%3)
    # loop over seq and 1.translate codon 2. store result
    print("Proteinsequence: "+ protein)


translate("GCC")