#######################################
# DATA
#######################################

# 1. Students dictionary
student1  = { "name":"Karthic",
        "marks" : [91, 95, 92, 93]
    }
student2  = { "name":"student2",
        "marks" : [91, 95, 92, 93]
    }
student3  = { "name":"student3",
        "marks" : [91, 95, 92, 93]
}

# Function for calculating average
def getAverage(student):
    return str(student["marks"][0])+" + "+str(student["marks"][1])+" + "+str(student["marks"][2])+" + "+str(student["marks"][3])
    " / "+str(len(student["marks"]))
# Determine student grade
def assignLetterGrade(average):
    print("Student1 Average = "+str(average/4))
    if average >= 90: return "A"
    elif average >= 80: return "B"
    elif average >= 70: return "C"
    elif average >= 60: return "D"
    else : return "E"


#######################################
# LEXER
#######################################


from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('DIV', r'/')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()


################# PARSER ##################

from parser import Parser

print(getAverage(student1))

text_input = "print("+getAverage(student1)+");"

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token);

pg = Parser()
pg.parse()
parser = pg.get_parser()
#print("Student1 Grade = "+assignLetterGrade(parser.parse(tokens).eval()))

