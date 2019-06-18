CREATE TABLE Login (
	CPF int,
	Senha VARCHAR(255),
	PRIMARY KEY (CPF, Senha),
	FOREIGN KEY (CPF, Senha) REFERENCES Cadastro (CPFCadastro, SenhaCadastro)
);

CREATE TABLE Cadastro (
	Nome VARCHAR(255),
	CPFCadastro VARCHAR(9),
	SenhaCadastro VARCHAR(255),
	DataNascimento VARCHAR(255),
	CNH VARCHAR(11),
	Carro VARCHAR(255),
	Placa VARCHAR(255),
	Vagas VARCHAR(255),
	PRIMARY KEY(CPFCadastro, SenhaCadastro)
);
