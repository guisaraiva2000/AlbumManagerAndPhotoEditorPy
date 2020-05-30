from imagem import *

print("\n--- criando algumas Imagens para testes ---\n")

#1
ursoLocal = Imagem("urso.jpg")
ursoLocal.adicionarEtiqueta("animais")
ursoLocal.retirarEtiqueta("genérica")
print(ursoLocal.getNome())
#2
ursoOutraPasta = Imagem("urso.jpg", "pasta_sem_exif")
ursoOutraPasta.adicionarEtiqueta("animais")
ursoOutraPasta.retirarEtiqueta("genérica")
print(ursoOutraPasta.getNome())
#3
costaLocal = Imagem("costa.jpg")
costaLocal.adicionarEtiqueta("férias")
costaLocal.adicionarEtiqueta("paisagens")
costaLocal.retirarEtiqueta("genérica")
print(costaLocal.getNome())
#4
patoOutraPasta = Imagem("pato.jpg", "pasta_sem_exif/subpasta_sem_exif")
patoOutraPasta.adicionarEtiqueta("animais")
print(patoOutraPasta.getNome())
#5
ursoMaiscosta = ursoLocal + costaLocal
patoOutraPasta.retirarEtiqueta("genérica")
print(ursoMaiscosta.getNome())

print("\n--- testando o construtor de Album e 5 getters básicos ---\n")

meuAlbum = Album("Meu Álbum de 27 de Maio")
print(meuAlbum.getNome())
print(meuAlbum.getImagens())

print("\n--- testando __setitem__ (operação proibida) ---\n")

try:
  meuAlbum[2] = ursoMaiscosta
except Exception as e:
  print("Uma operação falhou:", e)

print("\n--- testando carregarImagemPreProcessada e 2 getters ---\n")

meuAlbum.carregarImagemPreProcessada(ursoLocal)
meuAlbum.carregarImagemPreProcessada(ursoOutraPasta)
meuAlbum.carregarImagemPreProcessada(ursoMaiscosta)
meuAlbum.carregarImagemPreProcessada(costaLocal)
meuAlbum.carregarImagemPreProcessada(patoOutraPasta)
print([str(imagem) for imagem in meuAlbum.getImagens()]) # por ordem de entrada!
print(len(meuAlbum))

# Se a aplicação executar a partir de 0 Imagem's criadas previamente, a
# 3ª Imagem criada pela aplicação será a número 3, e assim sucessivamente.
# Nesse caso, terceiraDestaSessao == 3. 
# Em geral, é preciso interrogar quais os números de Imagem disponíveis, para
# não gerar um erro de índice.

# a 3ª Imagem criada nesta sessão entrou em 4º lugar no meuAlbum
# portanto está no índice 3 da lista meuAlbum.getImagens()
primeiraDestaSessao = meuAlbum.getImagens()[1].getNumero()

print("\n--- testando __getitem__ ---\n")

print(meuAlbum[primeiraDestaSessao])
#meuAlbum[primeiraDestaSessao].show()

print("\n--- testando __delitem__ ---\n")

del meuAlbum[primeiraDestaSessao]
print([str(imagem) for imagem in meuAlbum.getImagens()]) # por ordem de entrada!
print(len(meuAlbum))

print("\n--- testando carregarImagemDeFicheiro ---\n")

print("--- validar = False, imagem nova ---")
meuAlbum.carregarImagemDeFicheiro("rallyPro.jpg")
print([str(imagem) for imagem in meuAlbum.getImagens()])
print(len(meuAlbum))
#meuAlbum[6].show()  # ver comentário acima: só é 6 se a numeração começar em 1

print("\n--- validar = True, imagem pré-carregada ---")
meuAlbum.carregarImagemDeFicheiro("pato.jpg",
                                  pasta = "pasta_sem_exif/subpasta_sem_exif",
                                  validar = True)  # imagem 4, numeradas desde 1

print([str(imagem) for imagem in meuAlbum.getImagens()])
print(len(meuAlbum))

print("\n--- validar = False, imagem pré-carregada ---")
meuAlbum.carregarImagemDeFicheiro("pato.jpg",
                                  pasta = "pasta_sem_exif/subpasta_sem_exif")
                                                   # imagem 4, numeradas desde 1
                               
print([str(imagem) for imagem in meuAlbum.getImagens()])
print(len(meuAlbum))
#meuAlbum[7].show()  # 7, supondo que a numeração começa em 1

print("\n--- testando dump ---\n")

meuAlbum.dump("guardaEsteAlbum", "pastaDeposito")

print("\n--- testando @staticmethod recriarAlbum ---\n")

meuAlbumRecriado = Album.recriarAlbum("guardaEsteAlbum", "pastaDeposito")
print([str(imagem) for imagem in meuAlbumRecriado.getImagens()])
print(len(meuAlbumRecriado))
#meuAlbumRecriado[7].show()  # 7, supondo que a numeração começa em 1

print("\n--- testando o construtor de AlbumPlus e 6 getters básicos ---\n")

# não há meuAlbumPlus1 neste ficheiro

print("\n--- a partir de um Album ---")
meuAlbumPlus2 = AlbumPlus(meuAlbum)
print(meuAlbumPlus2.getNome())
#print(meuAlbumPlus2.getImagens())
print([str(imagem) for imagem in meuAlbumPlus2.getImagens()])#ou listarImagens()
print(len(meuAlbumPlus2))
print(meuAlbumPlus2)
print(repr(meuAlbumPlus2))

print("\n--- testando setNome sobre meuAlbumPlus2 ---\n")

meuAlbumPlus2.setNome("Meu Álbum Plus Dois de 27 de Maio")
print(meuAlbumPlus2.getNome())

print("\n--- testando o tipo de meuAlbumPlus2 ---\n")

print(type(meuAlbumPlus2))
print(isinstance(meuAlbumPlus2, Album), isinstance(meuAlbumPlus2, AlbumPlus))

print("\n--- testando listarImagens sobre meuAlbumPlus2 ---\n")

print(meuAlbumPlus2.listarImagens())

print("\n--- testando pesquisarImagens ---\n")

print("\n--- pesquisa por nome exacto ---\n")
print(meuAlbumPlus2.pesquisarImagens("costa"))
print([str(imagem) for imagem in meuAlbumPlus2.pesquisarImagens("costa")])
print(meuAlbumPlus2.pesquisarImagens("urso"))
print([str(imagem) for imagem in meuAlbumPlus2.pesquisarImagens("urso")])

print("\n--- pesquisa por nome com tolerância ---\n")
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens("ursinho", 2)])
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens("ursinho", 3)])

print("\n--- pesquisa por intervalo de dataHora ---\n")
print("todas (sem qualquer pesquisa):")
print(meuAlbumPlus2.getImagens())
print("\napenas em Outubro ou Novembro de 2014:")
dataHoraInf = datetime.datetime(2014,10,1,0,0,0)
dataHoraSup = datetime.datetime(2014,11,30,23,59,59)
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens(intervaloDataHora = \
                                      (dataHoraInf, dataHoraSup))])

print("\n--- pesquisa por etiquetas ---\n")
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens(etiquetas = ["animais"])])
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens(etiquetas = ["férias"])])
# supondo que a numeração começa em 1, a lista de Imagem's seguinte inclui 0007:
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens(etiquetas = ["genérica"])])

print("\n--- pesquisa por intervalo de dataHora, e por etiquetas ---\n")

dataHoraInf = datetime.datetime(2010,4,25,0,0,0)
dataHoraSup = datetime.datetime(2020,12,24,23,59,59)
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens(intervaloDataHora = \
                                      (dataHoraInf, dataHoraSup), \
                                      etiquetas = ["férias", "genérica"])])

print("\n--- pesquisa por nome com tolerância, e por etiquetas ---\n")
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens("urssa", 2, etiquetas = ["animais"])])
print([str(imagem) for imagem in \
       meuAlbumPlus2.pesquisarImagens("urssa", 1, etiquetas = ["animais"])])


# NÃO GUARDAMOS O CONTADOR DE IMAGENS, PARA REINICIAR A ZERO NA PRÓXIMA EXECUÇÃO

##print("\n--- usando @classmethod guardarNumeroDeImagens para actualizar ---\n")
##
##Imagem.guardarNumeroDeImagens()
