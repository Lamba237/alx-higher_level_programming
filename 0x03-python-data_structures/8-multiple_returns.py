#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == []:
        tup = (len(sentence), None)
        return tup
    else:
        return (len(sentence), sentence[0])
