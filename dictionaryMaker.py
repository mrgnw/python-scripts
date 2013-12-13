# TODO: Use =, and () as separators
#
import os.path
from os import chdir
import glob
import re

# commands to enter at any time to exit quiz or skip question
# could create interpretAnswer function to accept multiple parameters? Nah
exitKeys = ["x", "exit"]
openKeys = ["open", "read"]
newKeys  = ["new", "add"]

# put newKeys & openKeys in another list?
commandList = exitKeys + newKeys + openKeys

mainPrompt = "Whatcha want?"
helpText = "  read (open), new (add), exit (x)\n  >>"

terms = {}


def remove_comments(dirty_line):
    """ ADD ability to clear a multi-line string of comments """
    if '#' in dirty_line:
        dirty_line= dirty_line.partition('#')[0] # inspired by http://stackoverflow.com/questions/1706198/

    return dirty_line.rstrip()


def is_quote(string):
    '''Says if a string is a quotation mark (single or double)
    Doesn't handle triple quotes yet.
    '''
    if string == '\"':
        return True
    else :
        return False


def remove_strings(fat_string, verbose = False):
    ''' currently just iterates through fat_string character-by-character to return a copy
    '''

    in_quote = False
    quote_type = "" # Will be changed to represent the type of quote

    new_string = ""
    for c in fat_string:
        if is_quote(c):
            if in_quote:
                if verbose: print c, "= quote #2"
                in_quote = False # get out of the quote
            else:
                if verbose: print c,  "skipped"
                in_quote = True # start skipping characters
        elif in_quote:
            if verbose: print c, "skipped"
        else :
            new_string += c # Change new string to show each time a character is evaluated
            if verbose : print "\t" + new_string

    return new_string


def clean(dirty_line):
    new_line = remove_comments(dirty_line)
    new_line = remove_strings(new_line)

    new_line = re.sub("[^a-zA-Z_]", ' ', dirty_line)

    return new_line


def ask(prompt=mainPrompt+"\n"+helpText, starting_dictionary = terms):
    response = raw_input(prompt + "\t")
    if response.lower() in commandList:
        return response.lower()
    else : return response


def read_dictionary(filename):
    dictionary = {}

    # Press *.whatever to read ALL files of .whatever type
    if filename[0] == "*":
        print filename
        for files in glob.glob(filename):
            print files

            with open(files) as f:
                for line in f:
                    line = clean(line)
                    print " >>", line

                    word_list = line.split(" ")
                    for x in word_list:
                        dictionary[x] = ""

    # Read just one file.
    elif os.path.isfile(filename):
        with open(filename) as target:
            for line in target.readlines():

                line = clean(line)
                print line
                #print "\t" + line # + "\t>>\t",

                word_list = line.split(" ")
                for x in word_list:
                    dictionary[x] = ""

        print # blank line
    print dictionary
    return dictionary


def type_dictionary():
    dictionary = {}
    go = True
    while go:
        # ask for key
        new_key = ask("  key")
        if new_key in exitKeys :
            return dictionary
        else :
            # ask for value - still creates key if an exitKey is entered for value
            new_value = ask("value")
            if new_value in exitKeys :
                dictionary[new_key] = ""
                return dictionary
            else :
                dictionary[new_key] = new_value
                print


def write_to_file(dictionary):
    fname = raw_input("Write to file:")


    f = open(fname, 'w')
    for i in dictionary:
        f.write(i + "\t" + dictionary[i] + "\n")
    #target = open(filename, 'w')

    f.close()
    return dictionary


def dict_string(dictionary):
    p = ""

    ordered = sorted(dictionary)

    for x in ordered:
        p += x + "\t" + dictionary[x] + "\n"

    return p


#terms = {"a" : "alpha", "b" : "bravo", "c" : "charlie"}
terms = {}


go = True
while go:
    main_input = ask()

    if main_input in commandList:
        if main_input in exitKeys:
            write_to_file(terms)
            go = False

        elif main_input in newKeys:
            print terms
            terms.update(type_dictionary())
            print terms

        elif main_input in openKeys:
            filename = ask("Read dictionary:")
            terms.update(read_dictionary(filename))
        else : print "Let's try that again...\n"



dirty = "lovely...\nis the root of all \t 5*5+2/5\\ is silly."

print "Here's what we ended up with:\n"
print dict_string(terms)
print clean(dirty)
