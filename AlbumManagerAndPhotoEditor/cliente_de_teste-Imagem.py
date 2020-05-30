from imagem import *

print("\n--- testando o construtor ---\n")

chimpLocal = Imagem("chimp.jpg")
chimpOutraPasta = Imagem("chimp.jpg", "sem_info")

wedLocal = Imagem("canon-ixus.jpg")
wedOutraPasta = Imagem("canon-ixus.jpg", "com_info_exif")

print("\n--- testando setters e getters ---\n")

print(chimpLocal.getNumero())
print(chimpOutraPasta.getNumero())
print(wedLocal.getNumero())
print(wedOutraPasta.getNumero())

print(chimpLocal.getNome())
print(chimpOutraPasta.getNome())
print(wedLocal.getNome())
print(wedOutraPasta.getNome())

print(chimpLocal.getNomeSemSufixo())
print(chimpOutraPasta.getNomeSemSufixo())
print(wedLocal.getNomeSemSufixo())
print(wedOutraPasta.getNomeSemSufixo())

print(chimpLocal.ehDeFicheiro())
print(chimpOutraPasta.ehDeFicheiro())
print(wedLocal.ehDeFicheiro())
print(wedOutraPasta.ehDeFicheiro())

print(chimpLocal.getPathFicheiro())
print(chimpOutraPasta.getPathFicheiro())
print(wedLocal.getPathFicheiro())
print(wedOutraPasta.getPathFicheiro())

print(chimpLocal.getTamanho())
print(chimpOutraPasta.getTamanho())
print(wedLocal.getTamanho())
print(wedOutraPasta.getTamanho())

print(chimpLocal.getLargura())
print(chimpOutraPasta.getLargura())
print(wedLocal.getLargura())
print(wedOutraPasta.getLargura())

print(chimpLocal.getAltura())
print(chimpOutraPasta.getAltura())
print(wedLocal.getAltura())
print(wedOutraPasta.getAltura())

print(chimpLocal.getDataHora())
print(chimpOutraPasta.getDataHora())
print(wedLocal.getDataHora())
print(wedOutraPasta.getDataHora())

print(chimpLocal.getEtiquetas())
print(chimpOutraPasta.getEtiquetas())
print(wedLocal.getEtiquetas())
print(wedOutraPasta.getEtiquetas())

print(chimpLocal.getDescricao())
print(chimpOutraPasta.getDescricao())
print(wedLocal.getDescricao())
print(wedOutraPasta.getDescricao())

chimpLocal.adicionarEtiqueta("animais")
chimpOutraPasta.adicionarEtiqueta("animais")
wedLocal.adicionarEtiqueta("casamentos")
wedOutraPasta.adicionarEtiqueta("casamentos")

chimpLocal.retirarEtiqueta("genérica")
chimpOutraPasta.retirarEtiqueta("genérica")
wedLocal.retirarEtiqueta("genérica")
wedOutraPasta.retirarEtiqueta("genérica")

print(chimpLocal.getEtiquetas())
print(chimpOutraPasta.getEtiquetas())
print(wedLocal.getEtiquetas())
print(wedOutraPasta.getEtiquetas())

chimpLocal.setDescricao("Chimpazé no meio de pessoas.")
chimpOutraPasta.setDescricao("Chimpazé no meio de pessoas.")
wedLocal.setDescricao("Os noivos.")
wedOutraPasta.setDescricao("Os noivos.")

print(chimpLocal.getDescricao())
print(chimpOutraPasta.getDescricao())
print(wedLocal.getDescricao())
print(wedOutraPasta.getDescricao())

##chimpLocal.show()
##wedLocal.show()

print("\n--- testando __add__ ---\n")

chimpMaisWed = chimpLocal + wedLocal
#chimpMaisWed.show()
print(chimpMaisWed.getNumero())
print(chimpMaisWed.getNome())
print(chimpMaisWed.getNomeSemSufixo())
print(chimpMaisWed.getTamanho())
print(chimpMaisWed.getLargura())
print(chimpMaisWed.getAltura())
print(chimpMaisWed.getDataHora())
print(chimpMaisWed.getEtiquetas())
print(chimpMaisWed.getDescricao())

print("\n--- testando ehDeFicheiro == False após este __add__ ---\n")

print(chimpMaisWed.ehDeFicheiro())

print("\n--- testando __mul__ ---\n")

chimpVezes3 = chimpLocal * 3
#chimpVezes3.show()
print(chimpVezes3.getNumero())
print(chimpVezes3.getNome())
print(chimpVezes3.getNomeSemSufixo())
print(chimpVezes3.getTamanho())
print(chimpVezes3.getLargura())
print(chimpVezes3.getAltura())
print(chimpVezes3.getDataHora())
print(chimpVezes3.getEtiquetas())
print(chimpVezes3.getDescricao())

print("\n--- testando __rmul__ ---\n")

TresVezesChimp = 3 * chimpLocal
#TresVezesChimp.show()
print(TresVezesChimp.getNumero())
print(TresVezesChimp.getNome())
print(TresVezesChimp.getNomeSemSufixo())
print(TresVezesChimp.getTamanho())
print(TresVezesChimp.getLargura())
print(TresVezesChimp.getAltura())
print(TresVezesChimp.getDataHora())
print(TresVezesChimp.getEtiquetas())
print(TresVezesChimp.getDescricao())

print("\n--- testando __invert__ ---\n")

chimpNegativo = ~chimpLocal
#chimpNegativo.show()  #
print(chimpNegativo.getNumero())
print(chimpNegativo.getNome())
print(chimpNegativo.getNomeSemSufixo())
print(chimpNegativo.getTamanho())
print(chimpNegativo.getLargura())
print(chimpNegativo.getAltura())
print(chimpNegativo.getDataHora())
print(chimpNegativo.getEtiquetas())
print(chimpNegativo.getDescricao())

print("\n--- testando __invert__ 2 vezes ---\n")

chimpPositivo = ~~chimpLocal
#chimpPositivo.show()
print(chimpPositivo.getNumero())
print(chimpPositivo.getNome())
print(chimpPositivo.getNomeSemSufixo())
print(chimpPositivo.getTamanho())
print(chimpPositivo.getLargura())
print(chimpPositivo.getAltura())
print(chimpPositivo.getDataHora())
print(chimpPositivo.getEtiquetas())
print(chimpPositivo.getDescricao())

print("\n--- testando __rmul__ (portanto __mul__), __add_ e __invert__ ---\n")

mixordia = 2 * (chimpLocal + wedLocal) + ~chimpLocal
#mixordia.show()
#mixordia.guardarVisual()
print(mixordia.getNumero())
print(mixordia.getNome())
print(mixordia.getNomeSemSufixo())
print(mixordia.getTamanho())
print(mixordia.getLargura())
print(mixordia.getAltura())
print(mixordia.getDataHora())
print(mixordia.getEtiquetas())
print(mixordia.getDescricao())

print("\n--- testando __and__ com dois operandos Imagem ---\n")

chimpMixWed = chimpLocal & wedLocal
#chimpMixWed.show()
#chimpMixWed.guardarVisual()
print(chimpMixWed.getNumero())
print(chimpMixWed.getNome())
print(chimpMixWed.getNomeSemSufixo())
print(chimpMixWed.getTamanho())
print(chimpMixWed.getLargura())
print(chimpMixWed.getAltura())
print(chimpMixWed.getDataHora())
print(chimpMixWed.getEtiquetas())
print(chimpMixWed.getDescricao())

print("\n--- testando str() e repr() da classe Imagem ---\n")

print(chimpLocal)
print(repr(chimpLocal))
print(mixordia)
print(repr(mixordia))

#print(chimpLocal.imagem)
#print(repr(chimpLocal.imagem))

print("\n--- testando str() e repr() da classe Filtro ---\n")

filtroContornos = Filtro("CONTOUR")
print(filtroContornos)
print(repr(filtroContornos))

print("\n--- testando @classmethod listarFiltros (classe Filtro) ---\n")

print(Filtro.listarFiltros())

print("\n--- testando getFiltro da classe Filtro ---\n")

print(filtroContornos.getFiltro())

print("\n--- testando __and__ com Imagem & Filtro ---\n")

chimpContornos = (chimpLocal & filtroContornos) + chimpLocal  # usar parênteses
#chimpContornos.show()
print(chimpContornos.getNumero())
print(chimpContornos.getNome())
print(chimpContornos.getNomeSemSufixo())
print(chimpContornos.getTamanho())
print(chimpContornos.getLargura())
print(chimpContornos.getAltura())
print(chimpContornos.getDataHora())
print(chimpContornos.getEtiquetas())
print(chimpContornos.getDescricao())

print("\n--- testando __and__ com Filtro & Imagem, i.e., __rand__ ---\n")

chimpContornos2 = filtroContornos & chimpLocal
#chimpContornos2.show()  # OK
print(chimpContornos2.getNumero())
print(chimpContornos2.getNome())
print(chimpContornos2.getNomeSemSufixo())
print(chimpContornos2.getTamanho())
print(chimpContornos2.getLargura())
print(chimpContornos2.getAltura())
print(chimpContornos2.getDataHora())
print(chimpContornos2.getEtiquetas())
print(chimpContornos2.getDescricao())

print("\n--- antes de testar guardarVisual(), inspeccionar imagens ---\n")

print("chimpLocal")
print("format ->", chimpLocal.imagem.format)
print("format_description ->", chimpLocal.imagem.format_description)
print("mode ->", chimpLocal.imagem.mode)
print("chimpContornos")
print("format ->", chimpContornos.imagem.format)
print("format_description ->", chimpContornos.imagem.format_description)
print("mode ->", chimpContornos.imagem.mode)

print("\n--- testando guardarVisual() com argumentos default ---\n")

chimpContornos.guardarVisual()
print("(verificar criação correcta do ficheiro)")

print("\n--- testando guardarVisual() com argumentos instanciados ---\n")

chimpContornos.guardarVisual(pastaOut = "pastaOut", nomeOut = "novoNome",
                            formato = 'PNG')
print("(verificar criação correcta do ficheiro)")


print("\n--- testando __matmul__ com Imagem & float ---\n")

chimpMaior = chimpLocal @ 1.2
#chimpMaior.show()
print(chimpMaior.getNumero())
print(chimpMaior.getNome())
print(chimpMaior.getNomeSemSufixo())
print(chimpMaior.getTamanho())
print(chimpMaior.getLargura())
print(chimpMaior.getAltura())
print(chimpMaior.getDataHora())
print(chimpMaior.getEtiquetas())
print(chimpMaior.getDescricao())

print("\n--- testando __matmul__ com float @ Imagem, i.e., __rmatmul__ ---\n")

chimpMenor = 0.6 @ chimpLocal
#chimpMenor.show()
print(chimpMenor.getNumero())
print(chimpMenor.getNome())
print(chimpMenor.getNomeSemSufixo())
print(chimpMenor.getTamanho())
print(chimpMenor.getLargura())
print(chimpMenor.getAltura())
print(chimpMenor.getDataHora())
print(chimpMenor.getEtiquetas())
print(chimpMenor.getDescricao())

print("\n--- testando @classmethod alterarNumeroDeImagens ---\n")

print("Adicionando +10 ao contador de imagens")
Imagem.alterarNumeroDeImagens(10)
chimpLocalRecopiado = Imagem("chimp.jpg")
print(chimpLocalRecopiado.getNumero())
print(chimpLocalRecopiado.getNome())


# NÃO GUARDAMOS O CONTADOR DE IMAGENS, PARA REINICIAR A ZERO NA PRÓXIMA EXECUÇÃO

##print("\n--- testando @classmethod guardarNumeroDeImagens ---\n")
##
##Imagem.guardarNumeroDeImagens()

