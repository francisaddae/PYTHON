import string
def countWords(document):
    document = list(document)
    for i in range(len(document)):
        if not(document[i] in string.ascii_letters):
            document[i] =' '
        else:
            continue
    document = ''.join(document)
    document = document.lower().split()
    value = list()
    for key in document:
        value +=[document.count(key)]
    document = dict(zip(document,value))
    
    return document


document = '''US Ambassador to the United Nations Nikki Haley said Monday that North Korean leader Kim Jong Un was "begging for war" as she urged the UN Security Council to adopt the strongest sanctions measures possible to stop Pyongyang's nuclear program. to

Speaking at a Security Council emergency meeting, Haley said North Korea's sixth nuclear test was a clear sign that "the time for half measures" from the UN had to end.

"Enough is enough," Haley said. "We have taken an incrementation approach, and despite the best of intentions, it has not worked."'''
print(countWords(document))
print('\n')
document = '''
He will be the president of the company; right now
he is a vice president. 
But he ..... himself,  is no sure of it...
(Later he will see the imporance of these.)
'''
print(countWords(document))

