from imagem import *

print("\n--- criando algumas Imagens para testes ---\n")

# 1
chimpLocal = Imagem("chimp.jpg")
chimpLocal.adicionarEtiqueta("animais")
chimpLocal.retirarEtiqueta("genérica")
print(chimpLocal.getNome())
# 2
chimpOutraPasta = Imagem("chimp.jpg", "sem_info")
chimpOutraPasta.adicionarEtiqueta("animais")
chimpOutraPasta.retirarEtiqueta("genérica")
print(chimpOutraPasta.getNome())
# 3
wedLocal = Imagem("canon-ixus.jpg")
wedLocal.adicionarEtiqueta("casamentos")
wedLocal.retirarEtiqueta("genérica")
print(wedLocal.getNome())
# 4
wedOutraPasta = Imagem("canon-ixus.jpg", "com_info_exif")
wedOutraPasta.adicionarEtiqueta("casamentos")
print(wedOutraPasta.getNome())
# 5
chimpMaisWed = chimpLocal + wedLocal
wedOutraPasta.retirarEtiqueta("genérica")
print(chimpMaisWed.getNome())

print("\n--- testando o construtor de Album e 5 getters básicos ---\n")

meuAlbum = Album("Meu Álbum")
print(meuAlbum.getNome())
print(meuAlbum.getImagens())
print(len(meuAlbum))
print(meuAlbum)
print(repr(meuAlbum))

print("\n--- testando __setitem__ (operação proibida) ---\n")

try:
    meuAlbum[2] = chimpMaisWed
except Exception as e:
    print("Uma operação falhou:", e)

print("\n--- testando carregarImagemPreProcessada e 2 getters ---\n")

meuAlbum.carregarImagemPreProcessada(chimpLocal)
meuAlbum.carregarImagemPreProcessada(chimpOutraPasta)
meuAlbum.carregarImagemPreProcessada(chimpMaisWed)
meuAlbum.carregarImagemPreProcessada(wedLocal)
meuAlbum.carregarImagemPreProcessada(wedOutraPasta)
print([str(imagem) for imagem in meuAlbum.getImagens()])  # por ordem de entrada!
print(len(meuAlbum))

# Se a aplicação executar a partir de 0 Imagem's criadas previamente, a
# 3ª Imagem criada pela aplicação será a número 3, e assim sucessivamente.
# Nesse caso, terceiraDestaSessao == 3. 
# Em geral, é preciso interrogar quais os números de Imagem disponíveis, para
# não gerar um erro de índice.

# a 3ª Imagem criada nesta sessão entrou em 4º lugar no meuAlbum
# portanto está no índice 3 da lista meuAlbum.getImagens()
terceiraDestaSessao = meuAlbum.getImagens()[3].getNumero()

print("\n--- testando __getitem__ ---\n")

print(meuAlbum[terceiraDestaSessao])
# meuAlbum[terceiraDestaSessao].show()

print("\n--- testando __delitem__ ---\n")

del meuAlbum[terceiraDestaSessao]
print([str(imagem) for imagem in meuAlbum.getImagens()])  # por ordem de entrada!
print(len(meuAlbum))

print("\n--- testando carregarImagemDeFicheiro ---\n")

print("--- validar = False, imagem nova ---")
meuAlbum.carregarImagemDeFicheiro("CoronaVirusWikipedia.jpg")
print([str(imagem) for imagem in meuAlbum.getImagens()])
print(len(meuAlbum))
# meuAlbum[6].show()  # ver comentário acima: só é 6 se a numeração começar em 1

print("\n--- validar = True, imagem pré-carregada ---")
meuAlbum.carregarImagemDeFicheiro("canon-ixus.jpg", pasta="com_info_exif",
                                  validar=True)  # imagem 4, numeradas desde 1

print([str(imagem) for imagem in meuAlbum.getImagens()])
print(len(meuAlbum))

print("\n--- validar = False, imagem pré-carregada ---")
meuAlbum.carregarImagemDeFicheiro("canon-ixus.jpg", pasta="com_info_exif")
# imagem 4, numeradas desde 1

print([str(imagem) for imagem in meuAlbum.getImagens()])
print(len(meuAlbum))
# meuAlbum[7].show()  # 7, supondo que a numeração começa em 1

print("\n--- testando dump ---\n")

meuAlbum.dump("guardaMeuAlbum")

print("\n--- testando @staticmethod recriarAlbum ---\n")

meuAlbumRecriado = Album.recriarAlbum("guardaMeuAlbum")
print([str(imagem) for imagem in meuAlbumRecriado.getImagens()])
print(len(meuAlbumRecriado))
# meuAlbumRecriado[7].show()  # 7, supondo que a numeração começa em 1

print("\n--- testando o construtor de AlbumPlus e 6 getters básicos ---\n")

print("--- a partir de uma string (nomeAlbum) ---")
meuAlbumPlus1 = AlbumPlus("Meu Álbum Plus Um")
print(meuAlbumPlus1.getNome())
print(meuAlbumPlus1.getImagens())
print(len(meuAlbumPlus1))
print(meuAlbumPlus1)
print(repr(meuAlbumPlus1))
print(meuAlbumPlus1.getDataCriacao())

print("\n--- a partir de um Album ---")
meuAlbumPlus2 = AlbumPlus(meuAlbum)
print(meuAlbumPlus2.getNome())
# print(meuAlbumPlus2.getImagens())
print([str(imagem) for imagem in meuAlbumPlus2.getImagens()])  # ou listarImagens()
print(len(meuAlbumPlus2))
print(meuAlbumPlus2)
print(repr(meuAlbumPlus2))
print(meuAlbumPlus2.getDataCriacao())

print("\n--- testando setNome sobre meuAlbumPlus2 ---\n")

meuAlbumPlus2.setNome("Meu Álbum Plus Dois")
print(meuAlbumPlus2.getNome())

print("\n--- testando o tipo de meuAlbumPlus2 ---\n")

print(type(meuAlbumPlus2))
print(isinstance(meuAlbumPlus2, Album), isinstance(meuAlbumPlus2, AlbumPlus))

print("\n--- testando carregarPastas recursivo, validando, meuAlbumPlus1 ---\n")

meuAlbumPlus1.carregarPastas(["./sem_info"],
                             recursivo=True, validarImagens=True)
print([str(imagem) for imagem in meuAlbumPlus1.getImagens()])  # ou listarImagens()
print(len(meuAlbumPlus1))
print(meuAlbumPlus1)
print(repr(meuAlbumPlus1))

print("\n--- de novo carregarPastas recursivo, validando, meuAlbumPlus1 ---\n")

meuAlbumPlus1.carregarPastas(["./sem_info"],
                             recursivo=True, validarImagens=True)
print([str(imagem) for imagem in meuAlbumPlus1.getImagens()])  # ou listarImagens()
print(len(meuAlbumPlus1))
print(meuAlbumPlus1)
print(repr(meuAlbumPlus1))

print("\n--- testando carregarPastas não recursivo, não validando, ")
print("meuAlbumPlus1 ---\n")

meuAlbumPlus1.carregarPastas(["./sem_info"])
print([str(imagem) for imagem in meuAlbumPlus1.getImagens()])  # ou listarImagens()
print(len(meuAlbumPlus1))
print(meuAlbumPlus1)
print(repr(meuAlbumPlus1))

print("\n--- testando listarImagens sobre meuAlbumPlus2 ---\n")

print(meuAlbumPlus2.listarImagens())

print("\n--- testando pesquisarImagens ---\n")

print("\n--- pesquisa por nome exacto ---\n")
print(meuAlbumPlus2.pesquisarImagens("canon-ixus"))
print([str(imagem) for imagem in meuAlbumPlus2.pesquisarImagens("canon-ixus")])
print(meuAlbumPlus2.pesquisarImagens("chimp"))
print([str(imagem) for imagem in meuAlbumPlus2.pesquisarImagens("chimp")])

print("\n--- pesquisa por nome com tolerância ---\n")
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens("chimpanzé", 3)])
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens("chimpanzé", 4)])

print("\n--- pesquisa por intervalo de dataHora ---\n")
print("todas (sem qualquer pesquisa):")
print(meuAlbumPlus2.getImagens())
print("\napenas em Maio ou Junho de 2001:")
dataHoraInf = datetime.datetime(2001, 5, 1, 0, 0, 0)
dataHoraSup = datetime.datetime(2001, 6, 30, 23, 59, 59)
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens(intervaloDataHora= \
                                          (dataHoraInf, dataHoraSup))])

print("\n--- pesquisa por etiquetas ---\n")
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens(etiquetas=["animais"])])
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens(etiquetas=["casamentos"])])
# supondo que a numeração começa em 1, a lista de Imagem's seguinte inclui 0007:
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens(etiquetas=["genérica"])])

print("\n--- pesquisa por intervalo de dataHora, e por etiquetas ---\n")

dataHoraInf = datetime.datetime(2001, 5, 1, 0, 0, 0)
dataHoraSup = datetime.datetime(2020, 12, 24, 23, 59, 59)
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens(intervaloDataHora= \
                                          (dataHoraInf, dataHoraSup), \
                                      etiquetas=["casamentos", "genérica"])])

print("\n--- pesquisa por nome com tolerância, e por etiquetas ---\n")
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens("ximpa", 3, etiquetas=["animais"])])
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens("ximpa", 2, etiquetas=["animais"])])

# NÃO GUARDAMOS O CONTADOR DE IMAGENS, PARA REINICIAR A ZERO NA PRÓXIMA EXECUÇÃO

##print("\n--- usando @classmethod guardarNumeroDeImagens para actualizar ---\n")
##
##Imagem.guardarNumeroDeImagens()
