from scripts.Respounder import *

social_grammer = ['how are you', 'do you like something']

class Social():
    def social(self, social):
        self.social = social
        i = 0
        while i < len(social_grammer):
            if social == social_grammer[i]:
                Social().social_response(i)
                break
            i += 1
    def social_response(self, i):
        self.i = i
        if i == 0:
            rnd = random.randint(0, 2)
            respone = ['im fine thank you', 'it is little hot today', 'im ok']
            Respounder.respound(respone[rnd])
        elif i == 1:
            rnd = random.randint(0, 1)
            respone = ['yes i do', 'yeah']
            Respounder.respound(respone[rnd])