
class ParserError(Exception):
    pass

class Sentence:
    
    def __init__(self, subject=None, verb=None, object=None):
        """ By default the sentence begins with player. If you type 'run north' you mean 'player run north' 
            We take tuples e.g. ('noun','princess') """
        if(subject):
            self.subject = subject[1]
        if(verb):
            self.verb = verb[1]
        if(object):
            self.object = obj[1]
        
          
    def peek(self, word_list):
        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None
            
        
    def match(self, word_list, expecting):
        if word_list:
            word = word_list.pop(0)
            
            if word[0] == expecting:
                return word[1]
            else:
                return None
        else:
            return None
            

    def skip(self, word_list, word_type):
        """ Skip as many 'stop' words as possible (a, the, and...) """
        while self.peek(word_list) == word_type:
            self.match(word_list, word_type)
            
            
    def parse_verb(self, word_list):
        self.skip(word_list, 'stop')
        
        if self.peek(word_list) == 'verb':
            self.verb = self.match(word_list, 'verb')

        else:
            raise ParserError("Expected a verb next!")
            
            
    def parse_object(self, word_list):
        self.skip(word_list, 'stop')
        next_word = self.peek(word_list)
        
        if next_word == 'noun':
            self.object = self.match(word_list, 'noun')
        elif next_word == 'direction':
            self.object = self.match(word_list, 'direction')
        else:
            raise ParserError("Expected an object next!")
            
            
    def parse_subject(self, word_list):
        self.skip(word_list, 'stop')
        next_word = self.peek(word_list)
        
        if next_word == 'noun':
            self.subject = self.match(word_list, 'noun')
        elif next_word == 'verb':
            self.subject = 'player' # subject defaults to 'player'
        else:
            raise ParserError("Expected a subject or verb next.")

            
    def parse_sentence(self, word_list):
        self.parse_subject(word_list)
        self.parse_verb(word_list)
        self.parse_object(word_list)
        
        return self
