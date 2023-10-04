class Cpf:
    value = ''
    def __init__(self, value:str):
        self.value = value

    @staticmethod
    def validate(param:str)-> bool:
        return isinstance(param:str)
        
cpf_a_validar = 'xx-xxxx-xxxx-'
cpf = Cpf('')

print(cpf.validate(cpf_a_validar))
print(Cpf.validate(cpf_a_validar))
