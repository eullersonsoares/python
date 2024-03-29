class Pessoa:
    def __init__(self, nome, cpf, dataNascimento):
        self.nome = nome;
        self.cpf = self._validaCPF(cpf);
        self.dataNascimento = dataNascimento;

    def _validaCPF(self, cpf):
        return cpf;

eu = Pessoa("Eullerson Soares", "123.465.789-96", "14/12/2000");

print(f"Eu me chamo {eu.nome}. \nCPF: {eu.cpf}.\nData de Nascimento {eu.dataNascimento}");