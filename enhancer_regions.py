"""This script is designed to take in two files: a .csv of SNPs
   and a .txt file of enhancer regions. Each should be formatted so that
   the last three columns are Chromosome, starting location, and finishing location.

   The output is a file identical to the SNP csv, with any ehancer regions
   containing the SNP appended in an additional column."""

"""ASSIGN THE FOLLOWING VARIABLES BEFORE RUNNING"""

enhancer_file = "Enhancers_genes_interest.txt"
enhancer_header_toggle = False
#not implemented yet
SNP_file = "gwas_test.csv"
SNP_header_toggle = False
#not implemented yet


def Main():
    enhancers = enhancer_stripper(get_raw_data(enhancer_file))
    SNPs = SNP_stripper(get_raw_data(SNP_file))
    print(SNPs[0])
    find_overlap(enhancers, SNPs)
    return None

def find_overlap(enhancers, SNPs):
    """takes in output of enhancer_stripper, SNP_stripper
    returns SNP list with each element appended with a list of enhancers it overlaps"""
    matches = []
    for SNP in SNPs:
        enhancer_match = []
        for enhancer in enhancers:
            if contain_SNP(SNP, enhancer):
                enhancer_match.append(enhancer)
        matches.append([SNP,enhancer_match])
    return matches


def write_data(matches, outputFile):
    #TO DO
    return None

def enhancer_stripper(rawData):
    """takes in the contents of the enhancer file and returns a list of lists
    formatted as [chr, start allele int, end allele int] """
    cleanData = []
    for line in rawData:
        line = line.split('_')[1:]
        cleanData.append([line[0], int(line[1]), int(line[2])])

    #merge overlapping enhancers?
    return cleanData

def SNP_stripper(rawData):
    """takes the contents of the SNP file and returns a list of lists
    each line [[rest of data], [chr, start allele, end allele]]"""
    cleanData = []
    for line in rawData:
        line = line.split(',')
        loc = line[-1].split(':')
        line = [line[:-1],[loc[0],loc[1].split('-')[0]]]
        cleanData.append(line)
    return cleanData


def get_raw_data(fileName):
    """ takes in file, returns list of file lines"""

    with open(fileName, 'r') as f:
        contents = f.read()
    return contents.splitlines()

def contain_SNP(SNP, enhancer):
    if SNP[1][0] == enhancer[0]:
    #and (SNP[1] >= enhancer[1][1]) and (SNP[1] <= enhancer[1][2]):
       return True
    return False

Main()