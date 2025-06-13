''' XOR encryption by siroyasha '''
class XOR_encryptor:
    def __init__(self,message):
        self.message=[ord(m) for m in message.upper() ]
        self.ciphertext=[] # the encrypted text after xor operatrion
        self.key_str=[] # holds the ascii values of self.key synced with self.message 
        self.key="KEY"
    def _xor(self):
        def match_key(message:str,key:str )->str:
            assert len(message)>=len(key),'::>>KEY STRING SHOULD NOT BE GREATER THAN THE MESSAGE STRING'
            l_m,l_k=len(message),len(key)
            match,pivot=[0,1,2],[i for i in range(len(message)-len(key))]
            p=0
            for i in range(len(pivot)):
                if p<len(message):
                    key=key+''.join(key[p])
                    p+=1
                else:
                    p=0
                    key=key+''.join(key[p])
                    p+=1
            return key
        self.key_str=match_key(self.message,self.key)
        self.key_str=[ord(i) for i in self.key_str]
        self.ciphertext=[self.message[i]^self.key_str[i] for i in range(len(self.message))]
        return self.key_str,self.ciphertext
    def decryption(self):
        decrypt="".join([chr(self.key_str[i]^self.ciphertext[i]) for i in range(len(self.key_str))])
        return decrypt
A=XOR_encryptor("priyanshu")
A.message
A._xor()
A.decryption()
