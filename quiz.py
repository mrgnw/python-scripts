# quiz.py
# A simple command-line quiz
# LearnPythonTheHardWay.org recommended making flash cards to memorize the items in dictionary
# Since I was just learning Pythong, I decided to use Python to learn Python
    # by making this quiz

import random

# What python gets when it asks for a term that's not in the dictionary
default = 'WRONG'

# Determines if the loop continues to run.
contin = "y"

# commands to enter at any time to exit quiz or skip question
# could create interpretAnswer function to accept multiple parameters? Nah
exitKeys = ["x", "exit"]
skipKeys = ["", "skip"]
flipKeys = ["flip", "\\"]
commandList = exitKeys + skipKeys + flipKeys

# dictionary of escape sequences
dictionary = {
        "\\\\" : "backslash",
        "\\'" : "apostrophe",
        "\\\"" : "quote",
        "\\a" : "ASCII bell",
        "\\b" : "backspace",
        "\\f" : "formfeed",
        "\\n" : "linefeed",
        "\\r" : "carriage return",
        "\\t" : "tab",
        "\\v" : "vertical tab"
}

def displayPercent(good, bad):
        if good+bad == 0 : return 0
        else : return "{:.0%}".format(good/(good+bad))

def displayFinalScore(good, bad):                
        print "\n","SCORE"
        print displayPercent(right, wrong)
        print "%d/%d" % (right, right+wrong)

# Asks a question
def askTerm(dictionary):
        qToAsk = random.choice(dictionary.keys())
        print dictionary[qToAsk],

        response = raw_input("\t")

        # Respons is a command from commandList, not an attempt at an answer
        if response.lower() in commandList :
                return response.lower()
        # RIGHT ANSWER:
        elif dictionary.get(qToAsk, default) == dictionary.get(response, default) :
                return response
        else :
                print " \tAnswer: %s" % qToAsk
                return "WRONG"
        
# Asks for the value instead of key
# Returns copy of dictionary with flipped keys and values
def flipDictionary(dictionary):
        return dict((dictionary[k], k) for k in dictionary)

right = 0.0
wrong = 0.0

# creates a flipped version of dictionary dictionary
# (makes values into keys, keys into values)
flippy = flipDictionary(dictionary)
quizDictionary = dictionary

qnum = 0
while contin.lower() == "y" or contin.lower() == "yes":
        qnum += 1
        print qnum,

        new_answer = askTerm(quizDictionary)
        
        if new_answer.lower() in exitKeys :
                contin = "n"
                displayFinalScore(right, wrong)

        # Switch between term view and definition view at any prompt
        if new_answer in flipKeys :
                newDictionary = flipDictionary(quizDictionary)
                quizDictionary = newDictionary
                print "\tFlipping..."

        if new_answer in quizDictionary :
                if len(quizDictionary) > 1 :
                        quizDictionary.pop(new_answer)
                        right += 1
                        print " +1\t%s (%d/%d)" % (displayPercent(right,wrong), right, right+wrong)
                else : 
                        contin = "n"
                        print "\nYay, you're done!"        
                        displayFinalScore(right, wrong)

        elif new_answer == "WRONG" :
                wrong += 1
                print "  1-\t%s (%d/%d)" % (displayPercent(right,wrong), right, right+wrong)
        
else : print ""