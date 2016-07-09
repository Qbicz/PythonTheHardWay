import logging


def is_int(s):
    try:
        number = int(s)
        return number
    except ValueError:
        return False
        

class lexicon(object):
        
    types = {'direction':   ('north','south', 'east'),
             'verb':        ('go', 'kill', 'eat'),
             'stop':        ('the', 'in', 'of'),
             'noun':        ('bear', 'princess')}
    
    def __init__(self):
        pass
    
    
    @staticmethod
    def scan(input):
        """scan for types of words that user used: direction, verb, noun or stop word. Integers are of 'number' type. If the type is not in the list recognize it as 'error'"""
        logging.debug('scan:')
        
        words = input.split()
        output_list = []
        
        for word in words:
            logging.debug('append %s' % word)
            checked_input = None
            
            if is_int(word):
                checked_input = ('number', int(word))
            
            # search in static class variable
            for key, value in lexicon.types.items(): # iteritems() in python 2
                if word in value:
                    checked_input = (key, word)
        
            if checked_input:
                output_list.append(checked_input)
            else:
                output_list.append(('error', word))
        
        return output_list
        

    def main():
        scan('north', 'south')
        
if __name__ == "__main__":
    main()