#!/bin/python3
# with basicshell.py
# import this file to basicshell.py
TT_int = 'TT_int'
TT_float = 'TT_float'
TT_plus = 'TT_plus'
TT_minus = 'TT_minus'
TT_mul = 'TT_mul'
TT_div = 'TT_div'
TT_lparen = 'TT_lparen'
TT_rparen = 'TT_rparen'


class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.detials}'
        return result


class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)


class Token:
    def __init__(self, type_, value=None):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.currrent_char in '\t':
                self.adcance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_plus))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_mul))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_div))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_minus))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_lparen))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_rparen))
                self.advance()
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError(' ' + char)
        return tokens, None


        def make_number(self):
            num_str = ''
            dot_count = 0

            while self.current_char != None and self.current_char in DIGITS + '.':
                if self.current_char == '.':
                    if dot_count == 1: break
                    dot_count += 1
                    num_str += '.'
                else:
                    num_str += self.current_char

            if dot_count == 0:
                return Token(TT_int, int(num_str))
            else:
                return Token(TT_float, float(num_str))
            self.advance()


def run(text):
    lexer_text = Lexer(text)
    tokens, error = lexer_text.make_tokens()
    return tokens, error
