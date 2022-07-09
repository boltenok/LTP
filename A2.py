def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    get_length('ATCGAT')
    6
    get_length('ATCG')
    4
    """

    return len(dna)


# print(get_length('ATCGAT'))
# print(get_length('ATCG'))


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    is_longer('ATCG', 'AT')
    True
    is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


# print(is_longer('ATCG', 'AT'))
# print(is_longer('ATCG', 'ATCGGA'))


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    count_nucleotides('ATCGGC', 'G')
    2
    count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


# print(count_nucleotides('ATCGGC', 'G'))
# print(count_nucleotides('ATCTA', 'G'))


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    contains_sequence('ATCGGC', 'GG')
    True
    contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1


# print(contains_sequence('ATCGGC', 'GG'))
# print(contains_sequence('ATCGGC', 'GT'))


def is_valid_sequence(dna1):
    """ (str) -> bool
    Return True if and only if DNA contains no characters other than 'A', 'T',
    'C', and 'G'
    is_valid_sequence('ATGCEFJKASDFJKJSDF')
    False
    is_valid_sequence('ATGC')
    True
    is_valid_sequence('atgc')
    False
    is_valid_sequence('ATGCGGCTAT')
    True
    """

    valid_elements = ['A', 'T', 'C', 'G']
    elem_count = 0
    for elem in dna1:
        if elem not in valid_elements:
            elem_count += 1

    return elem_count == 0


# print(is_valid_sequence('ATGCEFJKASDFJKJSDF'))
# print(is_valid_sequence('ATGC'))
# print(is_valid_sequence('atgc'))
# print(is_valid_sequence('ATGCGGCTAT'))


def insert_sequence(dna1, dna_insert_element, dna_insert_element_index):
    """ (str, str, int) -> str
    Return a new dna sequence with the inserted element on the specified place

    insert_sequence(’CCGC’, ’AT’, 2)
    ’CCATGC’
    insert_sequence(’CCGC’, ’AT’, 0)
    ’ATCCGC’
    insert_sequence(’CCGC’, ’AT’, -1)
    ’CCGATC’

    """
    return dna1[:dna_insert_element_index] + dna_insert_element + dna1[dna_insert_element_index:]


# print(insert_sequence('CCGC', 'AT', 2))
# print(insert_sequence('CCGC', 'AT', 0))
# print(insert_sequence('CCGC', 'AT', -1))


def get_complement(nucleotide):
    """(str) -> str

    Returns  the complimented sequence if initial string 'A'<-> 'T' and 'C' <-> 'G'
    get_compliment('A')
    'T'
    get_compliment('C')
    'G'

    """
    complimented_nucl = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    return complimented_nucl[nucleotide]


# print(get_compliment('A'))
# print(get_compliment('C'))
# print(get_compliment('T'))
# print(get_compliment('G'))


def get_complementary_sequence(dna):
    """ (str) -> str
    Return the DNA sequence that is complementary to the given DNA sequence.

    >> > get_complimentary_sequence('ATA')
    'TAT'
    >> > get_complimentary_sequence('CGC')
    'GCG'
    >> > get_complimentary_sequence('CACT')
    'AGTG'
    """
    complement_nucl = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complement_nucl[base] for base in dna[::-1]])


# print(get_complimentary_sequence('ATA'))
# print(get_complimentary_sequence('CGC'))
# print(get_complimentary_sequence('CACT'))
