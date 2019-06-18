

CREATE TABLE Cadastro (
	Nome VARCHAR(255),
	CPFCadastro VARCHAR(11),
	SenhaCadastro VARCHAR(255),
	DataNascimento VARCHAR(255),
	CNH VARCHAR(11),
	Carro VARCHAR(255),
	Placa VARCHAR(255),
	Vagas VARCHAR(255),
	email VARCHAR (255),
	genero VARCHAR(255)
	PRIMARY KEY(CPFCadastro)
);

CREATE TABLE viagens (
	nome VARCHAR(255),
	origem VARCHAR(255),
	destino VARCHAR(255),
	dataviagem VARCHAR(255),
	horario VARCHAR(255),
	vagas VARCHAR(255)
);
