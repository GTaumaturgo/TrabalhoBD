# -*- coding: latin-1 -*-

import mysql.connector
import csv


cnx = mysql.connector.connect( user='root',
								  password='',
								  host='127.0.0.1',
								  database='bd_enem_2015')


cont_reg_prova = 0
cont_reg_cand = 0

cursor = cnx.cursor()
i = 0
with open('output0.csv','r',encoding='latin-1') as csvfile:
	spamreader = csv.reader(csvfile,delimiter=',')
	#indices relevantes para cada entidade
	uf_index = [4,11,21,82,86]
	mun_index = [2,9,19,84]
	school_index = [8,13,14,15,9,11]
	cand_index = [28,24,27,18,25,23,26,17,16,4,2,8]
	test_index = [104,86,84]
	prova_cad_index = [[88,96,100,92],[89,97,101,93],[90,98,102,94],[91,99,103,95]]
	muns = set()
	ufs = set()
	schools = set()
	cands = []
	tests = []
	cads = []
	redacaos = []
	presenca_index = [88,89,90,91]
	redacao_index = [109,115]
	cods_index = [92,93,94,95]
	codProva = set()
	cod_to_info = {}
	cods_to_add = []
	cod_to_info[251] = (1,4)
	cod_to_info[252] = (0,4)
	cod_to_info[253] = (2,10)
	cod_to_info[254] = (3,10)
	cod_to_info[271] = (1,5)
	cod_to_info[272] = (1,6)
	cod_to_info[273] = (1,7)
	cod_to_info[274] = (1,8)
	cod_to_info[275] = (0,5)
	cod_to_info[276] = (0,6)
	cod_to_info[277] = (0,7)
	cod_to_info[278] = (0,8)
	cod_to_info[279] = (2,6)
	cod_to_info[280] = (2,11)
	cod_to_info[281] = (2,5)
	cod_to_info[282] = (2,8)
	cod_to_info[283] = (3,6)
	cod_to_info[284] = (3,11)
	cod_to_info[285] = (3,5)
	cod_to_info[286] = (3,8)



	for i in range(16):
		codProva.add(i + 231)
	i = 0
	for row in spamreader:
		if(i == 0):
			i = i + 1
			continue
		if(i == 280000):
			break


		# cadastro das ufs
		for idx in cods_index:
			if(row[idx] != ''):

				if(int(row[idx]) not in codProva):
					codProva.add(int(row[idx]))
					aux = []
					aux += [int(row[idx])]
					if (str.isnumeric(row[idx+13])):
						aux += [int(row[idx+13])]
					else:
						aux += [row[idx+13]]
					t = cod_to_info[int(row[idx])]
					aux += [t[0]]
					aux += [t[1]]
					cods_to_add += [tuple(aux)]

		for idx in uf_index:
			if row[idx] != '':
				ufs.add((row[idx],row[idx+1]))
		# cadastro municipios
		for idx in mun_index:
			if row[idx] != '':
				muns.add((row[idx],row[idx+1]))
		aux = []
		# escola
		if(row[school_index[0]] != ''):
			for idx in school_index:
				aux += [row[idx]]
			schools.add(tuple(aux))

		aux = []
		aux += [str(cont_reg_cand)]
		for idx in cand_index:
			if(row[idx] != ''):
				aux += [row[idx]]
			else:
				aux += [None]
		cands += [(tuple(aux))]

		aux = []
		aux += [str(cont_reg_prova)]
		for idx in test_index:
			if(row[idx] != ''):
				aux += [row[idx]]
			else:
				aux += [None]
		aux += [str(cont_reg_cand)]
		tests += [tuple(aux)]

		for cont1 in range(4):
			aux = []
			if(row[presenca_index[cont1]] == '1'):
				aux += [cont_reg_prova]
				for cont2 in range(4):
					aux += [row[prova_cad_index[cont1][cont2]]]
				cads += [tuple(aux)]

		aux = []
		aux += [cont_reg_prova]
		for idx in redacao_index:
			if(row[idx] != ''):
				aux += [row[idx]]
			else:
				aux += [None]
		aux += [str(cont_reg_cand)]
		redacaos += [tuple(aux)]

		cont_reg_cand = cont_reg_cand + 1
		cont_reg_prova = cont_reg_prova + 1
		i = i + 1


add_cod = ("INSERT INTO bd_enem_2015.TipoProva "
       "(CodTipo, VetGabarito, AreaConhecimento_idAreaConhecimento, CorProva_idCorProva) "
       "VALUES (%s, %s, %s, %s);\n")


add_uf = ("INSERT INTO bd_enem_2015.UnidadeFederativa "
       "(IdUF, SiglaUF) "
       "VALUES (%s, %s);\n")


add_mun = ("INSERT INTO bd_enem_2015.Municipio "
       "(IdMunic, NomeMunic) "
       "VALUES (%s, %s);\n")
add_school = ("INSERT INTO bd_enem_2015.Escola "
       "(IdEscola, TipoDependAdmin, TipoLocalizEscol, TipoSituFunc, Municipio_IdMunic, UnidadeFederativa_IdUF) "
       "VALUES (%s, %s, %s, %s, %s, %s);\n")
add_cand = ("INSERT INTO bd_enem_2015.Candidato "
       "(IdCandidato, CorRaca,AnoConcluEM,"
       "EstadoCivil, Nacionalidade,TipoEscolaEM,"
       "SituacaoConcluEM, TipoDeEnsiEM,Sexo,"
       "Idade, UnidadeFederativa_IdUF,Municipio_IdMunic, Escola_IdEscola) "
       'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);\n')



add_prova = ("INSERT INTO bd_enem_2015.Prova "
       "(IdProva, TipoLingua, UnidadeFederativa_IdUF,Municipio_IdMunic,Candidato_IdCandidato) "
       "VALUES (%s, %s, %s, %s, %s)")

add_caderno = ("INSERT INTO bd_enem_2015.CadernoProva "
       "(Prova_IdProva, Presenca, Nota, Resposta,TipoProva_CodTipo) "
       "VALUES (%s, %s, %s, %s, %s)")

add_red = ("INSERT INTO bd_enem_2015.Redacao "
       "(IdRedacao, Situacao, Nota,Candidato_IdCandidato) "
       "VALUES (%s, %s, %s, %s)")


print("Cadastrando cods de prova")
for cod in cods_to_add:
	cursor.execute(add_cod, cod)
	cnx.commit()


print("cadastrando ufs")
for uf in ufs:
	cursor.execute(add_uf, uf)
	cnx.commit()

print("cadastrando muns")
for mun in muns:
	cursor.execute(add_mun, mun)
	cnx.commit()

print("cadastrando escolas")
for school in schools:
	cursor.execute(add_school,school)
	cnx.commit()


print("cadastrando candidatos")
for cand in cands:
	cursor.execute(add_cand,cand)
	cnx.commit()

print("cadastrando provas")
for test in tests:
	cursor.execute(add_prova,test)
	cnx.commit()

print("Cadastrando cadernos")
for cad in cads:
	cursor.execute(add_caderno, cad)
	cnx.commit()

print("Cadastrando redacoes")

for red in redacaos:
	cursor.execute(add_red, red)
	cnx.commit()

cursor.close()
cnx.close()
