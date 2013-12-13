# Choose the two lowest frequencies
# Combine these frequencies as the parent frequency for both nodes
    # Left branches = 0  (lesser used = 0)
    # Right branches = 1 (  more used = 1)
# Repeat

# PriorityQueue makes it easy to manage the data
import PriorityQueue


def count_chars(str):
    dict = {}
    for char in str:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def queue_dict(dict):
    term_queue = PriorityQueue()
    for t in dict:
        this_q_item = Q_item(t, dict[t])
        term_queue.add(this_q_item)

    return term_queue


def count_and_q(str):
    return queue_dict(count_chars(str))

def huffmanate(str):
    pq = count_and_q(str)
    bitdict = {}
    while len(pq) > 1:
        #1 POP first two
        alpha = pq.remove()
        bravo = pq.remove()

        #2 Prepend bitstrings to letters (in bitdict)
        for a in alpha.thing:
            if a in bitdict:
                bitdict[a] = '0' + bitdict[a]
            else:
                bitdict[a] = '0'
        for b in bravo.thing:
            if b in bitdict:
                bitdict[b] = '1' + bitdict[b]
            else:
                bitdict[b] = '1'

        omega = alpha + bravo
        pq.add(omega)


    # Generate bitstring
    bitstr = ''
    word = ''
    for a in str:
        word += a
        if word in bitdict:
            bitstr += bitdict[word]
            word = ''

    return bitstr, bitdict

def flip_dictionary(dictionary):
    #return dict((dictionary[k], k) for k in dictionary)
    new_dict = {}
    for k in dictionary:
        new_dict.update({dictionary[k] : k})
    return new_dict


def dehuffmanate(bitstring, bitdict):
    bit2char = flip_dictionary(bitdict)

    str = ''
    word = ''
    for a in bitstring:
        word += a
        if word in bit2char:
            str += bit2char[word]
            word = ''

    return str


def q_test():
    alan = Q_item('alan', 3)
    brad = Q_item('brad', 2)
    carl = Q_item('carl', 1)
    alanbrad = alan + brad

    tesco = PriorityQueue()
    tesco.add(brad)
    tesco.add(alan)
    tesco.add(carl)
    tesco.add(alanbrad)
    print tesco

    return 'q_test done'

#q_test()

def huff_setup():
    ex1 = 'abacabbac'
    ex2 = 'alskdjflwweltkjh;lkj;lwker'
    ex3 = 'aaaabbbcccdddeefffggggggzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
    #    answer should be a 0110 / b 0111 / c 010 / d 00 / e 1 : 111001100110101101011001100110111110110111
    count_chars(ex1)

    dex1 = count_and_q(ex1)
    dex2 = count_and_q(ex2)
    dex3 = count_and_q(ex3)

    print dex1
    #print dex2
    print dex3

    return 'huff_setup done!'

def encode_decode(str):
    a_string, a_dict =  huffmanate(str)
    decoded = dehuffmanate(a_string, a_dict)
    print 'original %s' % str
    print ' encoded %s' % a_string
    print ' bitdict %s' % a_dict
    print ' decoded %s' % decoded

    print '\toriginal == decoded?', decoded == str
    print
    print
    return decoded == str

ex0 = 'eeedeedeeceeceedeedeebeeaeee'
ex1 = 'abacabbac'
ex2 = 'alskdjflwweltkjh;lkj;lwker'
ex3 = 'aaaabbbcccdddeefffggggggzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'

encode_decode(ex0)
encode_decode(ex1)
encode_decode(ex2)
encode_decode(ex3)
