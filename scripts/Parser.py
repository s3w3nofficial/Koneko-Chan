social_grammer = ['how are you', 'do you like something']

class main_parser():
    def parse_rec(self, text):
        self.text = text
        social_text = text
        text = text.split(' ')

        call = []
        i = 0
        play = False
        for word in text:
            
            if play == True:
                call.append(word)

            if word == 'search' or word == 'find':
                call.append('0')
            elif word == 'open' or word == 'run':
                call.append('1')
                call.append(text[i+1].lower())
                break
            elif word == 'wake' or word == 'set alarm':
                call.append('2')
                break
            elif word == 'play':
                call.append('3')
                play = True
                break

    #search parser
            if word == 'for':
                #append everithink next
                i += 1
                while i < len(text):
                    if len(text) - 1 == i:
                        call.append(text[i]) #dont add space to last word of array    
                    else:
                        call.append(text[i] + " ")
                    i += 1
            i += 1
        """
        #check for social
        for social in social_grammer:
            print social_text, social
            if social_text == social:
                call.append('3')
                call.append(social_text.lower())
            break
        """
        #merge strings after for
        if len(call) > 2:
            call[1:len(call)] = [''.join(call[1:len(call)])]
            print call[1]
        print call[0]
        return call #return call