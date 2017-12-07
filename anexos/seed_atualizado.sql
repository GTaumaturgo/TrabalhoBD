insert into bd_enem_2015.CorProva values(0, "Azul");
insert into bd_enem_2015.CorProva values(1, "Amarelo");
insert into bd_enem_2015.CorProva values(2, "Branco");
insert into bd_enem_2015.CorProva values(3, "Rosa");
insert into bd_enem_2015.CorProva values(4, "Branco - Adaptada(Braille)");
insert into bd_enem_2015.CorProva values(5, "Azul - Reaplicação");
insert into bd_enem_2015.CorProva values(6, "Amarelo - Reaplicação");
insert into bd_enem_2015.CorProva values(7, "Branco - Reaplicação");
insert into bd_enem_2015.CorProva values(8, "Rosa - Reaplicação");
insert into bd_enem_2015.CorProva values(9, "Cinza");
insert into bd_enem_2015.CorProva values(10, "Cinza - Adaptada(Braille)");
insert into bd_enem_2015.CorProva values(11, "Cinza - Reaplicação");

insert into bd_enem_2015.AreaConhecimento values(0, "CN", "Ciências da Natureza");
insert into bd_enem_2015.AreaConhecimento values(1, "CH", "Ciências Humanas");
insert into bd_enem_2015.AreaConhecimento values(2, "LC", "Linguagens e códigos");
insert into bd_enem_2015.AreaConhecimento values(3, "MT", "Matemática");


insert into bd_enem_2015.TipoProva values(231, "AEAEADECEADEDBDACBBCEEECBADCEBCEACBBBDADCCABD",1,0);
insert into bd_enem_2015.TipoProva values(232, "DADCCABDEACBCEEDECBABBCEBCDECBBEADBDAAEAEADEC",1,1);
insert into bd_enem_2015.TipoProva values(233, "DADCCABDEACBCEEDECBABBCEBCDECBBEADBDAAEAEADEC",1,2);
insert into bd_enem_2015.TipoProva values(234, "ADECAEAEDBDADEEACEBCECBACBBCEEBBDEACBCABDDADC",1,3);
insert into bd_enem_2015.TipoProva values(235, "DCCDBCAAEBECBAADADBDEDEEBBBCABCCEAAEEDCBDDCEA",0,0);
insert into bd_enem_2015.TipoProva values(236, "AEDCADBCABCCBBBBEEDCEAABECBDDCCDEAEEDEDAADBCA",0,1);
insert into bd_enem_2015.TipoProva values(237, "EADDCCBEEDCEAABBBEEADBCABCDEDAADBECBAEBCACDDC",0,2);
insert into bd_enem_2015.TipoProva values(238, "DDCEEEABBBAADDEDBECBCABCAEDCBCAADBCEAAEEDCBCD",0,3);
insert into bd_enem_2015.TipoProva values(239, ",CDEAADCDBABDEBECECCDBBEBEABBABDCDADEEDCDAECCABBDCE",2,1);
insert into bd_enem_2015.TipoProva values(240, "AACDEBACDDBEDDCEABBAECCDCDDEEEABBABDCDABEBDBCECCBE",2,9);
insert into bd_enem_2015.TipoProva values(241, "DEAACDCBDAEBDABBBEDEEBABDCDADBBEBDCDAECCEABDCECECC",2,0);
insert into bd_enem_2015.TipoProva values(242, "CEDAABDACDBDEDBDCDDCEDCDABEBAECCEABCECCBABDEEBEABB",2,3);
insert into bd_enem_2015.TipoProva values(243, "CEDAABDACDBDEDBDCDDCEDCDABEBAECCEABCECCBABDEEBEABB",3,1);
insert into bd_enem_2015.TipoProva values(244, "EBCCBEEDABDBDECDACCEDCCECAAEADCBEDAEACABADDBB",3,9);
insert into bd_enem_2015.TipoProva values(245, "BADEBCCDACCCACAAECEADCBEDAEAABDEDCBDECDBBBEED",3,0);
insert into bd_enem_2015.TipoProva values(246, "DBBBADCADAEAEDCADCBECAAEDACCCEBDECABDBEEDEBCC",3,3);


-- Views
CREATE VIEW IF NOT EXISTS NotaFinalAluno AS
	SELECT
		IdCandidato, (SUM(CadernoProva.Nota)+Redacao.Nota)/5 as Nota
	FROM
		Candidato
	JOIN
		UnidadeFederativa ON UnidadeFederativa.idUF = Candidato.UnidadeFederativa_idUF
	JOIN
		Prova ON Prova.Candidato_idCandidato = Candidato.idCandidato
	JOIN
		CadernoProva ON CadernoProva.Prova_idProva = Prova.idProva
	JOIN 
		Redacao ON Redacao.Candidato_IdCandidato = IdCandidato
	GROUP BY IdCandidato;
CREATE VIEW IF NOT EXISTS SexoIdade AS SELECT Sexo, Idade FROM Candidato;
CREATE VIEW IF NOT EXISTS CandidatosDF AS SELECT Candidato.* FROM Candidato JOIN UnidadeFederativa ON UnidadeFederativa.idUF = Candidato.UnidadeFederativa_idUF WHERE SiglaUF = 'DF';
CREATE VIEW IF NOT EXISTS CandidatosSP AS SELECT Candidato.* FROM Candidato JOIN UnidadeFederativa ON UnidadeFederativa.idUF = Candidato.UnidadeFederativa_idUF WHERE SiglaUF = 'SP';
CREATE VIEW IF NOT EXISTS CandidatosRJ AS SELECT Candidato.* FROM Candidato JOIN UnidadeFederativa ON UnidadeFederativa.idUF = Candidato.UnidadeFederativa_idUF WHERE SiglaUF = 'RJ';
CREATE VIEW MediaHomens AS SELECT AVG(Nota) AS Media FROM Candidato NATURAL JOIN NotaFinalAluno WHERE Sexo = 'M' GROUP BY Sexo;
CREATE VIEW MediaMulheres AS SELECT AVG(Nota) AS Media FROM Candidato NATURAL JOIN NotaFinalAluno WHERE Sexo = 'F' GROUP BY Sexo;


-- Procedures

DROP PROCEDURE IF EXISTS melhores_alunos_estado;
DELIMITER //
CREATE PROCEDURE melhores_alunos_estado
(IN numero_candidatos INT, IN estado VARCHAR(45))
  BEGIN
  DROP TABLE IF EXISTS melhores_alunos_estado;
  CREATE TABLE melhores_alunos_estado
    SELECT
      Candidato.*, Nota
    FROM
		Candidato
	JOIN
		UnidadeFederativa ON UnidadeFederativa.idUF = Candidato.UnidadeFederativa_idUF
	JOIN
		NotaFinalAluno ON NotaFinalAluno.IdCandidato = Candidato.IdCandidato
	WHERE
      SiglaUF = estado
	ORDER BY Nota DESC LIMIT numero_candidatos;
	SELECT * FROM melhores_alunos_estado;
	END //


DROP PROCEDURE IF EXISTS melhores_alunos_escola;
DELIMITER //
CREATE PROCEDURE melhores_alunos_escola
(IN numero_candidatos INT, IN escola VARCHAR(45))
	BEGIN
	DROP TABLE IF EXISTS melhores_alunos_escola;
	CREATE TABLE melhores_alunos_escola
		SELECT
		  Candidato.*, Nota
		FROM
			Candidato
		JOIN
			UnidadeFederativa ON UnidadeFederativa.idUF = Candidato.UnidadeFederativa_idUF
		JOIN
			Prova ON Prova.Candidato_idCandidato = Candidato.IdCandidato
		JOIN
			CadernoProva ON CadernoProva.Prova_idProva = Prova.idProva
		WHERE
			CASE WHEN escola = 'publica' THEN
				TipoEscolaEM = 2
			WHEN escola = 'privada' THEN
				TipoEscolaEM = 3
			ELSE
				TipoEscolaEM = -1
			END 
		ORDER BY Nota DESC LIMIT numero_candidatos;
	SELECT * FROM melhores_alunos_escola;
	END //

-- Triggers

DROP TRIGGER IF EXISTS backup_candidato;
CREATE TABLE IF NOT EXISTS backup_candidato SELECT * FROM Candidato LIMIT 0;
CREATE TRIGGER backup_candidato BEFORE UPDATE ON Candidato FOR EACH ROW
  INSERT INTO backup_candidato
    (idCandidato, CorRaca, AnoConcluEM, EstadoCivil, Nacionalidade, TipoEscolaEM,SituacaoConcluEM,TipoDeEnsiEM,Sexo,Idade,UnidadeFederativa_IdUF, Municipio_IdMunic, Escola_IdEscola)
  VALUES
    (OLD.idCandidato, OLD.CorRaca, OLD.AnoConcluEM, OLD.EstadoCivil, OLD.Nacionalidade, OLD.TipoEscolaEM, OLD.SituacaoConcluEM, OLD.TipoDeEnsiEM, OLD.Sexo, OLD.Idade, OLD.UnidadeFederativa_IdUF, OLD.Municipio_IdMunic, OLD.Escola_IdEscola);

DROP TRIGGER IF EXISTS backup_caderno_prova;
CREATE TABLE IF NOT EXISTS backup_caderno_prova SELECT * FROM CadernoProva LIMIT 0;
CREATE TRIGGER backup_caderno_prova BEFORE UPDATE ON CadernoProva FOR EACH ROW
  INSERT INTO backup_caderno_prova
    (Prova_IdProva, Presenca, Nota, Resposta, TipoProva_CodTipo)
  VALUES
    (OLD.Prova_IdProva, OLD.Presenca, OLD.Nota, OLD.Resposta, OLD.TipoProva_CodTipo);


DROP TRIGGER IF EXISTS backup_escola;
CREATE TABLE IF NOT EXISTS backup_escola SELECT * FROM Escola LIMIT 0;
CREATE TRIGGER backup_escola BEFORE UPDATE ON Escola FOR EACH ROW
  INSERT INTO backup_escola
    (IdEscola, TipoDependAdmin, TipoLocalizEscol, TipoSituFunc, UnidadeFederativa_IdUF, Municipio_IdMunic)
  VALUES
    (OLD.IdEscola, OLD.TipoDependAdmin, OLD.TipoLocalizEscol, OLD.TipoSituFunc, OLD.UnidadeFederativa_IdUF, OLD.Municipio_IdMunic);

DROP TRIGGER IF EXISTS backup_prova;
CREATE TABLE IF NOT EXISTS backup_prova SELECT * FROM Prova LIMIT 0;
CREATE TRIGGER backup_prova BEFORE UPDATE ON Prova FOR EACH ROW
  INSERT INTO backup_prova
    (IdProva, TipoLingua, Candidato_idCandidato, UnidadeFederativa_IdUF, Municipio_IdMunic)
  VALUES
    (OLD.IdProva, OLD.TipoLingua, OLD.Candidato_idCandidato, OLD.UnidadeFederativa_IdUF, OLD.Municipio_IdMunic);

DROP TRIGGER IF EXISTS backup_redacao;
CREATE TABLE IF NOT EXISTS backup_redacao SELECT * FROM Redacao LIMIT 0;
CREATE TRIGGER backup_redacao BEFORE UPDATE ON Redacao FOR EACH ROW
  INSERT INTO backup_redacao
    (IdRedacao, Situacao, Candidato_idCandidato, Nota)
  VALUES
    (OLD.IdRedacao, OLD.Situacao, OLD.Candidato_idCandidato, OLD.Nota);