from imagem import *

print("\n--- testando o construtor ---\n")

ursoLocal = Imagem("urso.jpg")
costaLocal = Imagem("costa.jpg")
# encontra o pato com as duas sintaxes: usando slash / OU backslash \
patoOutraPasta = Imagem("pato.jpg", "pasta_sem_exif/subpasta_sem_exif")

#patoOutraPasta.show()

print("\n--- testando alguns setters e getters ---\n")

ursoLocal.adicionarEtiqueta("animais")
costaLocal.adicionarEtiqueta("férias")
costaLocal.adicionarEtiqueta("paisagens")
patoOutraPasta.adicionarEtiqueta("animais")

ursoLocal.retirarEtiqueta("genérica")
costaLocal.retirarEtiqueta("genérica")

ursoLocal.setDescricao("Urso na Natureza.")
costaLocal.setDescricao("Podíamos fazer férias aqui.")
patoOutraPasta.setDescricao("If it walks like a duck and it quacks...")

print(ursoLocal.getDescricao())
print(costaLocal.getDescricao())
print(patoOutraPasta.getDescricao())

##ursoLocal.show()
##costaLocal.show()

print("\n--- testando __mul__ ---\n")

ursoVezes4 = ursoLocal * 4
#ursoVezes4.show()
print(ursoVezes4.getNumero())
print(ursoVezes4.getNome())
print(ursoVezes4.getNomeSemSufixo())
print(ursoVezes4.getTamanho())
print(ursoVezes4.getLargura())
print(ursoVezes4.getAltura())
print(ursoVezes4.getDataHora())
print(ursoVezes4.getEtiquetas())
print(ursoVezes4.getDescricao())

print("\n--- testando __rmul__ ---\n")

TresVezesUrso = 3 * ursoLocal
#TresVezesUrso.show()
print(TresVezesUrso.getNumero())
print(TresVezesUrso.getNome())
print(TresVezesUrso.getNomeSemSufixo())
print(TresVezesUrso.getTamanho())
print(TresVezesUrso.getLargura())
print(TresVezesUrso.getAltura())
print(TresVezesUrso.getDataHora())
print(TresVezesUrso.getEtiquetas())
print(TresVezesUrso.getDescricao())

print("\n--- testando __invert__ ---\n")

ursoNegativo = ~ursoLocal
#ursoNegativo.show()  #
print(ursoNegativo.getNumero())
print(ursoNegativo.getNome())
print(ursoNegativo.getNomeSemSufixo())
print(ursoNegativo.getTamanho())
print(ursoNegativo.getLargura())
print(ursoNegativo.getAltura())
print(ursoNegativo.getDataHora())
print(ursoNegativo.getEtiquetas())
print(ursoNegativo.getDescricao())

print("\n--- testando __invert__ 2 vezes ---\n")

ursoPositivo = ~~ursoLocal
#ursoPositivo.show()
print(ursoPositivo.getNumero())
print(ursoPositivo.getNome())
print(ursoPositivo.getNomeSemSufixo())
print(ursoPositivo.getTamanho())
print(ursoPositivo.getLargura())
print(ursoPositivo.getAltura())
print(ursoPositivo.getDataHora())
print(ursoPositivo.getEtiquetas())
print(ursoPositivo.getDescricao())

print("\n--- testando __rmul__ (portanto __mul__), __add_ e __invert__ ---\n")

mixordia = 2 * (ursoLocal + costaLocal) + ~ursoLocal
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

ursoMixcosta = ursoLocal & costaLocal
#ursoMixcosta.show()
#ursoMixcosta.guardarVisual()
print(ursoMixcosta.getNumero())
print(ursoMixcosta.getNome())
print(ursoMixcosta.getNomeSemSufixo())
print(ursoMixcosta.getTamanho())
print(ursoMixcosta.getLargura())
print(ursoMixcosta.getAltura())
print(ursoMixcosta.getDataHora())
print(ursoMixcosta.getEtiquetas())
print(ursoMixcosta.getDescricao())

print("\n--- testando str() e repr() da classe Imagem ---\n")

print(ursoLocal)
print(repr(ursoLocal))
print(mixordia)
print(repr(mixordia))

#print(ursoLocal.imagem)
#print(repr(ursoLocal.imagem))

print("\n--- testando __and__ com Imagem & Filtro ---\n")

print("\n--- para isso, cria-se um filtro EDGE_ENHANCE_MORE ---\n")
filtroEdge = Filtro("EDGE_ENHANCE_MORE")

ursoEdge = (ursoLocal & filtroEdge) + ursoLocal  # usar parênteses
#ursoEdge.show()
print(ursoEdge.getNumero())
print(ursoEdge.getNome())
print(ursoEdge.getNomeSemSufixo())
print(ursoEdge.getTamanho())
print(ursoEdge.getLargura())
print(ursoEdge.getAltura())
print(ursoEdge.getDataHora())
print(ursoEdge.getEtiquetas())
print(ursoEdge.getDescricao())

print("\n--- testando __and__ com Filtro & Imagem, i.e., __rand__ ---\n")

ursoEdge2 = filtroEdge & ursoLocal
#ursoEdge2.show()  # OK
print(ursoEdge2.getNumero())
print(ursoEdge2.getNome())
print(ursoEdge2.getNomeSemSufixo())
print(ursoEdge2.getTamanho())
print(ursoEdge2.getLargura())
print(ursoEdge2.getAltura())
print(ursoEdge2.getDataHora())
print(ursoEdge2.getEtiquetas())
print(ursoEdge2.getDescricao())

print("\n--- testando __matmul__ com Imagem & float ---\n")

ursoMaior = ursoLocal @ 1.4
#ursoMaior.show()
print(ursoMaior.getNumero())
print(ursoMaior.getNome())
print(ursoMaior.getNomeSemSufixo())
print(ursoMaior.getTamanho())
print(ursoMaior.getLargura())
print(ursoMaior.getAltura())
print(ursoMaior.getDataHora())
print(ursoMaior.getEtiquetas())
print(ursoMaior.getDescricao())

print("\n--- testando __matmul__ com float @ Imagem, i.e., __rmatmul__ ---\n")

ursoMenor = 0.9 @ ursoLocal
#ursoMenor.show()
print(ursoMenor.getNumero())
print(ursoMenor.getNome())
print(ursoMenor.getNomeSemSufixo())
print(ursoMenor.getTamanho())
print(ursoMenor.getLargura())
print(ursoMenor.getAltura())
print(ursoMenor.getDataHora())
print(ursoMenor.getEtiquetas())
print(ursoMenor.getDescricao())

print("\n--- mais um teste com o pato: pato & costa ---\n")

patoMixcosta = patoOutraPasta & costaLocal
#patoMixcosta.show()
#patoMixcosta.guardarVisual()

print("\n--- testando __mul__ de novo (aplicado 2 vezes) ---\n")

patoMixcostaVezes6 = patoMixcosta * 2 * 3
#patoMixcostaVezes6.show()
print(patoMixcostaVezes6.getNumero())
print(patoMixcostaVezes6.getNome())
print(patoMixcostaVezes6.getNomeSemSufixo())
print(patoMixcostaVezes6.getTamanho())
print(patoMixcostaVezes6.getLargura())
print(patoMixcostaVezes6.getAltura())
print(patoMixcostaVezes6.getDataHora())
print(patoMixcostaVezes6.getEtiquetas())
print(patoMixcostaVezes6.getDescricao())


# NÃO GUARDAMOS O CONTADOR DE IMAGENS, PARA REINICIAR A ZERO NA PRÓXIMA EXECUÇÃO

##print("\n--- testando @classmethod guardarNumeroDeImagens ---\n")
##
##Imagem.guardarNumeroDeImagens()

