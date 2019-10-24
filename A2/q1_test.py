import nltk

def attempt_to_parse(sentence, grammar, should_parse=True):

    print()
    head_string = '\n(' + sentence + ')'
    if should_parse:
        head_string = head_string + ' (Should parse)'
    else:
        head_string = head_string + ' (Should not parse)'
    print(head_string + '\n')

    parser = nltk.parse.BottomUpChartParser(grammar)
    for tree in parser.parse(sentence.split()):
        print(tree)


def main():

    with open('q1.txt', 'r') as afile:
        cfg_string = afile.read()
    grammar = nltk.grammar.CFG.fromstring(cfg_string)

    ###Test Cases###
    attempt_to_parse('people walk their dogs in parks', grammar)
    attempt_to_parse('who walk their dogs', grammar)
    attempt_to_parse('who walk their dogs quickly', grammar)
    attempt_to_parse('who walk their dogs slowly in parks', grammar)
    attempt_to_parse('who walk', grammar)

    attempt_to_parse('what will people walk', grammar)
    attempt_to_parse('what will people walk quickly', grammar)
    attempt_to_parse('what people walk quickly in parks', grammar, False)
    attempt_to_parse('what should people walk their dogs quickly in parks', grammar, False)
    attempt_to_parse('where walk their dogs quickly in parks', grammar, False)

    attempt_to_parse('who walk their dogs quickly in parks', grammar)
    attempt_to_parse('what will people walk quickly in parks', grammar)
    attempt_to_parse('where should people walk their dogs quickly', grammar)
    attempt_to_parse('should people walk their dogs quickly in parks', grammar)
    
    attempt_to_parse('where should the red dogs eat', grammar)
    attempt_to_parse('what should the red dogs eat', grammar)
    attempt_to_parse('who should the red dogs eat', grammar)
    attempt_to_parse('walk your dogs', grammar)

    attempt_to_parse('who walk their dogs in parks', grammar)
    attempt_to_parse('who walk their dogs in parks quickly', grammar)
    attempt_to_parse('what will people walk in parks', grammar)
    attempt_to_parse('where should people walk their dogs', grammar)
    attempt_to_parse('should people walk their dogs in parks', grammar)

    attempt_to_parse('what people walk in parks', grammar, should_parse=False)
    attempt_to_parse('what should people walk their dogs in parks', grammar, should_parse=False)
    attempt_to_parse('where walk their dogs in parks', grammar, should_parse=False)
    
    attempt_to_parse('where will people walk their dogs in parks', grammar)

    ###Interrogative who (subject is missing)###
    attempt_to_parse('who eat the dogs under the statues', grammar)

    ###Interrogative what (thing is missing) ###
    attempt_to_parse('what should people walk in parks', grammar)
    attempt_to_parse('what will people eat', grammar)
    attempt_to_parse('what should people eat under red statues', grammar)

    ###Interrogative where (location is missing) ###
    attempt_to_parse('where should people walk their dogs in parks', grammar)
    attempt_to_parse('where will people walk their dogs in parks', grammar)

    attempt_to_parse('people eat their dogs to the parks', grammar)
    attempt_to_parse('people eat the dogs to the dogs', grammar)

    attempt_to_parse('should people eat the dogs to the dogs', grammar)
    attempt_to_parse('should people eat their statues to the statues', grammar)

    attempt_to_parse('who eat on statues', grammar, False)
    attempt_to_parse('walk your dogs to the statues', grammar)
    attempt_to_parse('walk your dogs the dogs', grammar)
    attempt_to_parse('walk in the parks', grammar)



    #TEST False:
    attempt_to_parse('what people walk quickly in parks', grammar, False)
    attempt_to_parse('what should people walk their dogs quickly in parks', grammar, False)
    attempt_to_parse('where walk their dogs quickly in parks', grammar, False)

    attempt_to_parse('who walk their dogs quickly in parks', grammar)
    attempt_to_parse('what will people walk quickly in parks', grammar)
    attempt_to_parse('where should people walk their dogs quickly', grammar)
    attempt_to_parse('should people walk their dogs quickly in parks', grammar)



if __name__ == '__main__':
    main()