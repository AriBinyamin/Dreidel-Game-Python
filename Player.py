class Player:
    def __init__(self, name, num_tokens):
        self.name = name
        self.tokens = num_tokens

    def modify_tokens(self, token_change):
        self.tokens += token_change

    def __str__(self):
        return f'{self.name}, {self.tokens}'
