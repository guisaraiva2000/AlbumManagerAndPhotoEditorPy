from PIL import Image, ImageOps, ImageFilter  # módulos
from pathlib import Path  # classe
from PIL.ExifTags import TAGS
import os
import datetime
import pickle
from jellyfish import levenshtein_distance as levDistance


### classe Imagem ###

class Imagem:
    """ Wrapper para a classe Image do módulo pillow (classe PIL.Image.Image)

  Acrescenta atributos de informação relativa à imagem.
  Dota as imagens de operações que permitem produzir novas imagens usando
  uma sintaxe de expressões numéricas e Booleanas: a partir de instâncias
  Imagem existentes, obtém-se novas Imagem's por alteração e/ou concatenação.
  """

    # numeroDeImagens é uma variável sempre inicializada:
    # é o contador de instâncias de Imagem já criadas
    try:
        with open("numeroDeImagens.txt") as fichIn:
            numeroDeImagens = int(fichIn.read())
    except Exception:
        numeroDeImagens = 0
        # print("\nNÚMERO DE IMAGENS INICIADO A ZERO\n")

    NUM_DIGITOS = 4  # constante: número de dígitos no pretty print de self.numero

    @classmethod
    def guardarNumeroDeImagens(cls):
        try:
            with open("numeroDeImagens.txt", "w") as fichOut:
                fichOut.write(str(cls.numeroDeImagens))
        except:
            raise ValueError("Impossível guardar contagem de imagens")

    @classmethod
    def alterarNumeroDeImagens(cls, delta):
        """ Requires: delta é int, delta >= -1
    Ensures: altera o parâmetro de classe numeroDeImagens, adicionando-lhe
      delta.
    """
        cls.numeroDeImagens += delta

    def _obterDataHoraDeFicheiro(self):
        """ Método auxiliar de __init__, para obter a dataHora a partir de ficheiro

    Usado no momento da inicialização do objecto Imagem. Relevante apenas
    quando a Imagem é criada por importação da imagem de um ficheiro.
    Tenta obter a dataHora lendo o campo DateTime de entre os campos exif
    guardados no atributo self.imagem, o qual é instanciado a partir do ficheiro
    cujo path fica guardado em self.path. Caso não tenha sido possível obter
    do ficheiro uma secção exif com DateTime, é usada a data/hora da última
    modificação do ficheiro.
    Ensures: um objecto datetime.datetime
    """
        dateTime = None
        # o ficheiro de onde foi lida a imagem tem informação exif, e esta contém
        # o campo "DateTime"?
        dadosExif = self.imagem.getexif()  # dicionário
        listaFiltraDateTime = [v for k, v in dadosExif.items() \
                               if TAGS.get(k) == "DateTime"]
        if listaFiltraDateTime != []:  # há pelo menos 1 ocorrência de "DateTime"
            dateTime = listaFiltraDateTime[0]  # e.g. '2001:06:09 15:17:32'
            dateTime = dateTime.replace(":", " ")  # e.g. '2001 06 09 15 17 32'
            dateTime = dateTime.split()  # e.g. ['2001', '06', '09', '15', '17', '32']
            dateTime = list(map(int, dateTime))
            dataHora = datetime.datetime(*dateTime)  # unpacking dos elementos da lista
        if dateTime == None:  # não foi possível encontrar info exif "DateTime"
            # data e hora da última modificação
            timestampModif = os.path.getmtime(self.pathFicheiro)
            dataHora = datetime.datetime.fromtimestamp(timestampModif)
        return dataHora

    def __init__(self, nome, pasta=".", imagem=None):
        """ Inicializador para cada Imagem, independentemente da sua origem

    Tem 2 modos de funcionamento: i) para Imagem's importadas de ficheiro;
    ii) para imagens criadas internamente a partir de Imagem's pré-existentes,
    sem referência explícita a ficheiros.
    No modo i), imagem tem de ser None. nome é o nome do ficheiro a importar
    (incluindo a extensão) e pasta é o nome da pasta onde está o ficheiro (por
    omissão, a pasta de trabalho actual).
    No modo ii), nome é o nome que se quer dar à nova Imagem, independentemente
    da ou das Imagem's usadas na sua construção.
    Requires:
      no modo i), nome e pasta são strings denotando um path de ficheiro válido
      e acessível, imagem é None;
      no modo ii), nome é uma string, pasta é irrelevante, e imagem é instância
      de PIL.Image.Image
    """
        self.nome = nome
        if imagem == None:  # vamos importar uma imagem de um ficheiro
            self.pathPasta = Path(pasta)
            self.pathFicheiro = self.pathPasta / nome
            try:
                self.imagem = Image.open(self.pathFicheiro)
                self.dataHora = self._obterDataHoraDeFicheiro()
            except:
                raise ValueError("Programa interrompido: ficheiro inacessível")
        else:  # é passada uma imagem (instância de PIL.Image.Image) ao inicializador
            self.imagem = imagem
            self.dataHora = datetime.datetime.today()  # momento da criação
            self.pathFicheiro = None  # a imagem não foi obtida de um ficheiro
        self.etiquetas = ["genérica"]
        self.descricao = "Imagem sem descrição."
        Imagem.numeroDeImagens += 1  # incrementa o contador global de Imagem's
        self.numero = Imagem.numeroDeImagens

    def getNumero(self):
        return self.numero

    def getNome(self):
        return self.nome

    # uma versão mais sofisticada filtraria sufixos .jpg, .JPG, .png, etc.
    def getNomeSemSufixo(self):
        if "." in self.nome:  # nome tem um sufixo (que indica formato da imagem)
            apagarDesde = self.nome.rindex(".")
            nomeSemSufixo = self.nome.replace(self.nome[apagarDesde:], "")
        else:  # sem necessidade de alteração, pois não há sufixo
            nomeSemSufixo = self.nome
        return nomeSemSufixo

    def ehDeFicheiro(self):
        """ Informa se esta Imagem foi obtida de ficheiro

    Caso não tenha sido obtida de ficheiro, é porque resulta de
    pós-processamento interno.
    Ensures: um bool que é True SSE a Imagem foi directamente criada de ficheiro
    """
        return self.pathFicheiro != None

    def getPathFicheiro(self):
        return self.pathFicheiro

    def getTamanho(self):
        """ Devolve o tamanho de self.imagem em píxeis

    Ensures: um par de int, ambos os int >=1, correspondente a (width, height).
    """
        return self.imagem.size  # usa a API de PIL.Image.Image

    def getLargura(self):
        return self.imagem.width  # usa a API de PIL.Image.Image

    def getAltura(self):
        return self.imagem.height  # usa a API de PIL.Image.Image

    def getDataHora(self):
        """ Devolve a dataHora desta Imagem

    Ensures: um objecto datetime.datetime
    """
        return self.dataHora

    def getEtiquetas(self):
        return self.etiquetas

    def getDescricao(self):
        return self.descricao

    def adicionarEtiqueta(self, etiqueta):
        if etiqueta not in self.etiquetas:
            self.etiquetas.append(etiqueta)

    def retirarEtiqueta(self, etiqueta):
        if etiqueta in self.etiquetas:
            self.etiquetas.remove(etiqueta)

    def setDescricao(self, descricao):
        """ Requires: descricao é uma string. """
        self.descricao = descricao

    def show(self):
        """ Mostra a imagem no ecrã.

    Em Windows, cria um ficheiro PNG temporário e mostra-o.
    Método usado apenas em debugging.
    """
        # self.imagem.show(title = self.__repr__())  # title sem efeito em Windows
        self.imagem.show()  # mesmo efeito que linha de cima, em Windows

    def __add__(self, other):
        """ Método especial de suporte à "adição" de Imagem's

    A "adição" de Imagem's corresponde à concatenação de 2 Imagem's,
    ficando o operando esquerdo da "adição" do lado esquerdo, e o operando
    direito do lado direito, da nova Imagem resultante.
    Note-se que o operando esquerdo é o self.
    Antes da concatenação, o atributo other.imagem é resize'd de modo a essa
    imagem ficar com a mesma altura de self.imagem.
    Requires: other é instância de Imagem.
    Ensures:
      uma nova Imagem com self.pathFicheiro == None, i.e., obtida no modo ii)
        de __init__;
      novaImagem.nome é a concatenação dos nomes (sem sufixo) das duas Imagem's
        "adicionadas", com o carácter "+" de permeio;
      novaImagem.etiquetas contém a união das etiquetas das duas Imagem's
        "adicionadas" (sem repetições de etiquetas);
      novaImagem.descricao é a concatenação das descrições das duas Imagem's
        "adicionadas", com mudança de linha entre uma e outra descrição.
    """
        # obtém uma cópia de other.imagem com a mesma altura de self.imagem
        # usa a API de PIL.Image.Image
        otherImagemResize = other.imagem.resize( \
            (int(other.getLargura() * self.getAltura() / other.getAltura()),
             self.getAltura()))
        # cria uma imagem em branco onde vai colocar, lado a lado,
        # self.imagem e otherImagemResize
        # nota de implementação: acesso directo ao atributo otherImagemResize.width
        tela = Image.new('RGB',  # usa a API de PIL.Image.Image
                         (self.getLargura() + otherImagemResize.width, self.getAltura()),
                         'white')
        tela.paste(self.imagem, (0, 0))  # usa a API de PIL.Image.Image
        tela.paste(otherImagemResize, (self.getLargura(), 0))
        novoNome = self.getNomeSemSufixo() + "+" + other.getNomeSemSufixo()
        novasEtiquetas = self.etiquetas[:]  # evitar o aliasing!
        for etiqueta in other.etiquetas:
            if etiqueta not in novasEtiquetas:
                novasEtiquetas.append(etiqueta)
        novaDescricao = self.descricao + "\n" + other.descricao
        novaImagem = Imagem(novoNome, imagem=tela)
        novaImagem.etiquetas = novasEtiquetas  # acesso directo ao atributo
        novaImagem.setDescricao(novaDescricao)
        return novaImagem

    def __mul__(self, num):
        """ Método especial de suporte à "multiplicação" de uma Imagem por um int

    A "multiplicação" desta Imagem por um int num corresponde à concatenação
    de num cópias desta Imagem lado a lado. Visualmente, o resultado é
    semelhante a "adicionar" a imagem contida no self a ela própria num-1 vezes.
    No entanto:
      os atributos da Imagem resultante são específicos do método __mul__;
      tem de se garantir que, à saida do método, o contador
        Imagem.numeroDeImagens tem 1 unidade a mais que à entrada do método,
        como acontece sempre que um método devolve uma nova Imagem por ele
        criada.
    Requires: num é int e num >= 1.
    Ensures:
      uma nova Imagem com self.pathFicheiro == None, i.e., obtida no modo ii)
        de __init__;
      novaImagem.nome é a concatenação do nome (sem sufixo) desta Imagem
        com a string "_rep"+str(num)
      novaImagem.etiquetas contém as mesmas etiquetas de self, mais a etiqueta
        "replicada" acrescentada no fim da lista (com eventual repetição de
        "replicada" nessa lista);
      novaImagem.descricao é obtida copiando a descrição da Imagem self,
        fazendo uma mudança de linha, e acrescentando a string
        "A imagem descrita acima resulta de replicar " + self.getNomeSemSufixo()
        + " " + str(num) + " vezes."
    """
        self.numeroDeImagens += 1

        tela = Image.new('RGB',  # usa a API de PIL.Image.Image
                         (self.getLargura() * num, self.getAltura()),
                         'white')
        tela.paste(self.imagem, (0, 0))  # usa a API de PIL.Image.Image
        for i in range(2, num):
            tela.paste(self.imagem, (self.getLargura() * i, 0))

        novoNome = self.getNomeSemSufixo() + "_rep" + str(num)
        novasEtiquetas = self.etiquetas[:]
        for etiqueta in self.etiquetas:
            if etiqueta not in novasEtiquetas:
                novasEtiquetas.append(etiqueta)
        novasEtiquetas.append("replicada")
        novaDescricao = self.descricao + "\nA imagem descrita acima resulta de replicar " \
                                       + self.getNomeSemSufixo() + " " + str(num) + " vezes."
        novaImagem = Imagem(novoNome, imagem=tela)
        novaImagem.etiquetas = novasEtiquetas  # acesso directo ao atributo
        novaImagem.setDescricao(novaDescricao)
        return novaImagem

    def __rmul__(self, num):
        """ Método especial de suporte à "multiplicação" de um int por uma Imagem

    A "multiplicação" de um int por esta Imagem tem exactamente o mesmo
    resultado da "multiplicação" desta Imagem por esse int.
    A diferença é que, aqui, o int é o operando esquerdo.
    Se este método especial não estivesse definido, a multiplicação com int
    à esquerda falharia.
    Requires: num é int e num >= 1.
    """
        return self.__mul__(num)

    def __invert__(self):
        """ Método especial de suporte à "negação bitwise" (inversão) de uma Imagem

    A "negação" desta Imagem consiste em aplicar o método PIL.ImageOps.invert
    à imagem guardada no self. Obtém-se assim um negativo da imagem do self:
    a mesma imagem, mas com as cores invertidas.
    Ensures:
      uma nova Imagem com self.pathFicheiro == None, i.e., obtida no modo ii)
        de __init__;
      novaImagem.nome é a concatenação do nome (sem sufixo) desta Imagem
        com a string "_negativo"
      novaImagem.etiquetas contém as mesmas etiquetas de self, mais a etiqueta
        "negativo" acrescentada no fim da lista (com eventual repetição de
        "negativo" nessa lista);
      novaImagem.descricao é obtida repetindo a descrição da Imagem self,
        fazendo uma mudança de linha, e acrescentando a string
        "A imagem descrita acima foi sujeita a inversão."
    """
        tela = Image.new('RGB',  # usa a API de PIL.Image.Image
                         (self.getLargura(), self.getAltura()),
                         'white')
        tela.paste(self.imagem, (0, 0))  # usa a API de PIL.Image.Image
        tela = ImageOps.invert(tela)

        novoNome = self.getNomeSemSufixo() + "_negativo"
        novasEtiquetas = self.etiquetas[:]
        for etiqueta in self.etiquetas:
            if etiqueta not in novasEtiquetas:
                novasEtiquetas.append(etiqueta)
        novasEtiquetas.append("negativo")
        novaDescricao = self.descricao + "\nA imagem descrita acima foi sujeita a inversão."
        novaImagem = Imagem(novoNome, imagem=tela)
        novaImagem.etiquetas = novasEtiquetas  # acesso directo ao atributo
        novaImagem.setDescricao(novaDescricao)
        return novaImagem

    def __and__(self, other):
        """ Suporta a "conjunção bitwise" de 2 Imagem's ou de 1 Imagem e 1 Filtro

    Suporta a sintaxe de uso do operador & em duas variantes:
      objectoImagem & objectoImagem
      objectoImagem & objectoFiltro
    Se other for Imagem, é criada e devolvida uma nova Imagem cuja imagem
    armazenada mistura as imagens dos dois operandos, usando a função
    PIL.Image.blend com 50% de peso para cada imagem.
    Se other for Filtro, é criada e devolvida uma nova Imagem cuja imagem
    armazenada resulta de filtrar a imagem do self com o método PIL.Image.filter
    usando o filtro armazenado no other.
    Requires: other é instância de Imagem ou de Filtro.
    Ensures:
      uma nova Imagem com self.pathFicheiro == None, i.e., obtida no modo ii)
        de __init__;
     Caso em que other é Imagem:
      novaImagem.nome é a concatenação dos nomes (sem sufixo) das duas Imagem's
        "conjugadas" (misturadas), com a string "_mix_" de permeio;
      novaImagem.etiquetas contém a união das etiquetas das duas Imagem's
        "conjugadas", à qual é acrescentada, no fim da lista, a etiqueta
        "mistura" (eliminando-se repetições de etiquetas);
      novaImagem.descricao começa com a concatenação das descrições das duas
        Imagem's "conjugadas", com mudança de linha entre uma e outra descrição;
        seguem-se nova mudança de linha, e a string "A imagem descrita acima
        resulta de uma mistura."
     Caso em que other é Filtro:
      novaImagem.nome é a concatenação do nome (sem sufixo) desta Imagem
        com a string "_comFiltro_" + str(other)
      novaImagem.etiquetas é uma cópia das etiquetas do self, à qual é
        acrescentada, no fim da lista, a etiqueta "filtrada" (eliminando-se
        repetições de etiquetas);
      novaImagem.descricao é obtida repetindo a descrição da Imagem self,
        fazendo uma mudança de linha, e acrescentando a string
        "A imagem descrita acima foi filtrada."
    """
        if isinstance(other, Imagem):
            otherResize = other.imagem.resize(self.getTamanho())
            blend = Image.blend(self.imagem, otherResize, 0.5)
            novoNome = self.getNomeSemSufixo() + "_mix_" + other.getNomeSemSufixo()
            novasEtiquetas = self.etiquetas[:]  # evitar o aliasing!
            for etiqueta in other.etiquetas:
                if etiqueta not in novasEtiquetas:
                    novasEtiquetas.append(etiqueta)
            if "mistura" not in novasEtiquetas:
                novasEtiquetas.append("mistura")
            novaDescricao = self.descricao + "\n" + other.descricao + "\n" + \
                            "A imagem descrita acima resulta de uma mistura."
            novaImagem = Imagem(novoNome, imagem=blend)
        else:  # other é uma instância da classe Filtro
            filtrada = self.imagem.filter(other.getFiltro())
            novoNome = self.getNomeSemSufixo() + "_comFiltro_" + str(other)
            novasEtiquetas = self.etiquetas[:]  # evitar o aliasing!
            if "filtrada" not in novasEtiquetas:
                novasEtiquetas.append("filtrada")
            novaDescricao = self.descricao + "\n" + \
                            "A imagem descrita acima foi filtrada."
            novaImagem = Imagem(novoNome, imagem=filtrada)
        novaImagem.etiquetas = novasEtiquetas  # acesso directo ao atributo
        novaImagem.setDescricao(novaDescricao)
        return novaImagem

    def __rand__(self, objectoFiltro):  # o único tipo possível para other é Filtro
        """ Suporta a "conjunção bitwise" de 1 Filtro e 1 Imagem

    A "conjunção bitwise" de um Filtro com esta Imagem tem exactamente o mesmo
    resultado da "conjunção bitwise" desta Imagem com esse Filtro.
    A diferença é que, aqui, o Filtro é o operando esquerdo.
    Se este método especial não estivesse definido, a conjunção com Filtros
    à esquerda falharia.
    Requires: objectoFiltro é instância de Filtro.   
    """
        """filtrada = self.imagem.filter(objectoFiltro.getFiltro())
        novoNome = self.getNomeSemSufixo()
        novasEtiquetas = self.etiquetas
        novaDescricao = self.descricao
        novaImagem = Imagem(novoNome, imagem=filtrada)
        novaImagem.etiquetas = novasEtiquetas  # acesso directo ao atributo
        novaImagem.setDescricao(novaDescricao)
        return novaImagem"""
        return self.__and__(objectoFiltro)

    def __str__(self):
        """ Representa abreviadamente o self como uma string

    Representação informal e abreviada do self.
    A representação é uma string que resulta de concatenar:
      o número da Imagem ocupando Imagem.NUM_DIGITOS caracteres (preencher com
        zeros a esquerda se necessário);
      o underscore "_";
      e finalmente o nome desta Imagem (com sufixo, caso exista)
    Ensures: uma string com o formato descrito acima.
    """
        string = ''
        if len(str(self.numero)) < self.NUM_DIGITOS:
            miss = self.NUM_DIGITOS - len(str(self.numero))
            string += miss * '0'
        return string + str(self.numero) + "_" + self.getNome()


    def __repr__(self):
        """ Suporta a função repr invocada sobre self

    Ensures: uma string com representação mais detalhada do self do que a que
      é dada por __str__.
    """
        return str(self.numero).zfill(Imagem.NUM_DIGITOS) + ", " + \
               self.nome + ", " + \
               str(self.getLargura()) + "x" + str(self.getAltura()) + ", " + \
               str(self.dataHora) + ", " + \
               "format: " + str(self.imagem.format_description) + ", " + \
               "mode: " + str(self.imagem.mode)

    def guardarVisual(self, pastaOut=".", nomeOut=None,
                      formato='JPEG'):
        """ Faz um dump da imagem do self para ficheiro

    Guarda a imagem do self de modo permanente no sistema de ficheiros.
    Requires:
      pastaOut é uma string que representa a pasta onde o ficheiro será criado;
        por omissão, é a pasta de trabalho actual;
      nomeOut é o nome desejado para o ficheiro, exceptuando sufixo; se for
        None, será usado self.getNomeSemSufixo()
      formato é uma string que denota um dos formatos de ficheiro suportados
        e que estão listados em
        https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html
        por omissão, será 'JPEG'
    Side-effects: surge no sistema de ficheiros um ficheiro com as propriedades
      descritas acima; se já existia um com o mesmo path, é reescrito.
    """
        if nomeOut == None:
            nomeOut = self.getNomeSemSufixo()
        nomeOut = nomeOut + "." + formato
        pathPastaOut = Path(pastaOut)
        pathFicheiroOut = pathPastaOut / nomeOut
        visual = self.imagem
        if formato == 'JPEG' and self.imagem.mode == 'RGBA':  # save() impossível
            # ver todos os modos suportados, em https://
            #   pillow.readthedocs.io/en/latest/handbook/concepts.html#concept-modes
            visual = self.imagem.convert('RGB')
        try:
            visual.save(pathFicheiroOut, formato)
        except:
            raise ValueError("Programa interrompido: impossível criar ficheiro")

    # de acordo com a PEP465, o uso de um escalar como operando de @ deveria
    # levantar um erro; para o (ab)uso presente, isso é irrelevante
    # https://www.python.org/dev/peps/pep-0465/
    def __matmul__(self, escala):
        """ Concretiza o redimensionamento de uma Imagem por um float

    Suporta o uso da sintaxe objectoImagem @ float, onde @ é o símbolo que
    corresponde normalmente à multiplicação de duas matrizes.
    Aqui, o significado da operação é criar uma nova Imagem cujas dimensões
    resultam de multiplicar as dimensões desta Imagem uniformemente pelo factor
    escala.
    Trata-se portanto de um abuso da sintaxe, mas que não cria ambiguidade no
    presente domínio, onde não há a verdadeira multiplicação matricial.
    Requires: escala é float;
      escala >= max(1/self.getLargura(), 1/self.getAltura())
    Ensures:
      uma nova Imagem com self.pathFicheiro == None, i.e., obtida no modo ii)
        de __init__;
      novaImagem.nome é a concatenação do nome (sem sufixo) desta Imagem
        com a string "_" + "redim"      
      novaImagem.etiquetas contém as mesmas etiquetas de self, mais a etiqueta
        "redimensionada" acrescentada no fim da lista (desde que isso não
        provoque repetição de "redimensionada" nessa lista);
      novaImagem.descricao é obtida repetindo a descrição da Imagem self,
        fazendo uma mudança de linha, e acrescentando a string
        "A imagem descrita acima foi redimensionada."
    """

        otherImagemResize = self.imagem.resize((int(self.getLargura() * escala), int(self.getAltura() * escala)))

        tela = Image.new('RGB',  # usa a API de PIL.Image.Image
                         (int(self.getLargura() * escala), int(self.getAltura() * escala)),
                         'white')
        tela.paste(otherImagemResize, (0, 0))  # usa a API de PIL.Image.Image

        novoNome = self.getNomeSemSufixo() + "_redim"
        novasEtiquetas = self.etiquetas[:]
        for etiqueta in self.etiquetas:
            if etiqueta not in novasEtiquetas:
                novasEtiquetas.append(etiqueta)
        if "redimensionada" not in novasEtiquetas:
            novasEtiquetas.append("redimensionada")
        novaDescricao = self.descricao + "\nA imagem descrita acima foi redimensionada."
        novaImagem = Imagem(novoNome, imagem=tela)
        novaImagem.etiquetas = novasEtiquetas
        novaImagem.setDescricao(novaDescricao)
        return novaImagem

    def __rmatmul__(self, escala):
        """ Método parceiro de __matmul__ que permite ter escala à esquerda de @

    Se este método especial não estivesse definido, a operação @ com o factor
    de escala à esquerda falharia.
    Requires: escala é float;
      escala >= max(1/self.getLargura(), 1/self.getAltura())
    """
        return self.__matmul__(escala)


### classe Filtro ###

class Filtro:
    """ Wrapper para um subconjunto de filtros do módulo PIL.ImageFilter

  A usar em operações & (suportadas por __and__) com objectos Imagem.
  Por simplicidade, apenas se suporta os filtros pré-definidos em
  PIL.ImageFilter, conforme a tabelaDeFiltros abaixo.
  """

    """ Aliases para os objectos filtro pré-definidos em PIL.ImageFilter """
    tabelaDeFiltros = {'BLUR': ImageFilter.BLUR,
                       'CONTOUR': ImageFilter.CONTOUR,
                       'DETAIL': ImageFilter.DETAIL,
                       'EDGE_ENHANCE': ImageFilter.EDGE_ENHANCE,
                       'EDGE_ENHANCE_MORE': ImageFilter.EDGE_ENHANCE_MORE,
                       'EMBOSS': ImageFilter.EMBOSS,
                       'FIND_EDGES': ImageFilter.FIND_EDGES,
                       'SHARPEN': ImageFilter.SHARPEN,
                       'SMOOTH': ImageFilter.SMOOTH,
                       'SMOOTH_MORE': ImageFilter.SMOOTH_MORE}

    @classmethod
    def listarFiltros(cls):
        """ Informa o cliente de quais os filtros disponíveis

    Devolve uma lista com aliases de filtros disponíveis, que podem portanto
    ser usados no construtor da classe.
    Ensures: uma lista de strings como descrito.
    """
        return list(Filtro.tabelaDeFiltros.keys())

    def __init__(self, filtro):
        """ Inicializador para cada Imagem

    Requires:
      filtro é uma string;
      filtro é o nome de uma das instâncias filtro pré-definidas de
      PIL.ImageFilter que se encontram em Filtro.tabelaDeFiltros, ou seja,
        filtro é uma chave desse dicionário
    """
        self.nome = filtro
        self.filtro = Filtro.tabelaDeFiltros[filtro]

    def getFiltro(self):
        return self.filtro

    def __str__(self):
        return self.nome

    def __repr__(self):
        return repr(self.filtro)


### classe Album ###

class Album:
    """ Concretiza o tipo de dados Álbum de Imagem's

  Oferece algumas operações básicas de criação de álbuns virtuais carregando
  Imagem's de dois modos:
  -- Imagem's previamente criadas (ou seja, objectos Imagem obtidos
  previamente de maneira independente);
  -- Imagem's carregadas a partir de ficheiro, por solicitação ao próprio Álbum.
  Expõe um interface externo parcialmente semelhante ao de um dicionário, mas
  em que certas operações dos dicionários estão suprimidas, e novas operações
  são acrescentadas.
  """

    @staticmethod
    def recriarAlbum(nomeFich, pasta="."):  # nome SEM a extensão ".album"
        """ Recria um Album a partir de um ficheiro

    Recria uma instância de Album, portanto também qualquer instância de uma
    sub-classe de Album, a partir de um ficheiro num formato binário próprio
    usado pelo módulo pickle.
    Ou seja,
    -- constitui uma operação de des-serialização, a qual
    -- tem o efeito inverso do método dump definido para as instâncias de Album
       (o qual efectua uma serialização do objecto Album para um ficheiro).
    Requires:
      nomeFich é uma string igual ao nome do ficheiro a des-serializar (sem o
      sufixo .album);
      pasta é uma string indicando onde está o ficheiro a des-serializar (por
      omissão, a pasta actual de trabalho)
    Ensures: um novo objecto Album que é um clone de um objecto previamente
      serializado através do método dump.
    """
        # nota de implementação: na verdade, o pickle permitiria serializar (dump)
        # e des-serializar (recriar) vários outros tipos de objectos Python, não
        # necessariamente um Album
        path = Path(pasta) / (nomeFich + ".album")
        fichIn = open(path, "rb")  # modo de leitura, binário
        albumRecriado = pickle.load(fichIn)
        fichIn.close()
        return albumRecriado
        # quando um Album é recriado, pode-se verificar o seu tipo concreto com
        # type()

    def __init__(self, nomeAlbum):
        """ Inicializa um objecto Album contendo 0 (zero) Imagem's

    A string nomeAlbum ficará sendo o nome do Album.
    Requires: nomeAlbum é uma string.
    """
        self.nomeAlbum = nomeAlbum
        # o dicionário self.imagensCarregadas irá guardar as Imagem's carregadas;
        # os items do dicionário serão da forma int:Imagem, onde o int usado como
        # chave corresponde ao número da Imagem
        self.imagensCarregadas = {}

    def dump(self, nome, pasta="."):  # nome SEM a extensão ".album"
        """ Guarda os atributos deste Album num ficheiro

    Guarda os atributos deste objecto Album num ficheiro no formato binário
    próprio do módulo pickle.
    Ou seja,
    -- constitui uma operação de serialização, a qual
    -- tem o efeito inverso do método estático Album.recriarAlbum (o qual
    efectua uma des-serialização de um objecto Album a partir de ficheiro);
    -- um Album tem que ser primeiro dump'ed; só depois pode ser recriado.
    Requires:
      nome é uma string que será usada como nome do ficheiro que vai guardar
        a serialização do self (sem o sufixo .album);
      pasta é uma string indicando onde ficará esse ficheiro (por omissão,
        a pasta actual de trabalho).
    Side-effects: surge no sistema de ficheiros um ficheiro com as propriedades
      descritas acima; se já existia um com o mesmo path, é reescrito.
    """
        with open(pasta+"/"+nome+'.album', 'wb') as f:
            pickle.dump(self, f)
        f.close()


    def getNome(self):
        return self.nomeAlbum

    def setNome(self, novoNome):
        self.nomeAlbum = novoNome

    def __len__(self):
        """ Devolve o número de Imagem's carregadas neste Album

    Suporta a invocação de len() por parte do código cliente.
    Ensures: um int não-negativo, que é o número de Imagem's carregadas.
    """
        return len(self.imagensCarregadas)

    def __getitem__(self, numero):
        """ Devolve a Imagem carregada neste Album, com o número de Imagem indicado

    Suporta o uso do operador de indexação [] por parte do código cliente.
    Requires: numero é um número de Imagem de uma Imagem carregada no Album.
    Ensures: o objecto Imagem (único) cujo atributo numero é igual ao
      parâmetro numero.
    """
        return self.imagensCarregadas[numero]

    # apenas para informar o cliente de que a operação correspondente não está
    # disponível, no caso improvável de o cliente a tentar;
    # consistiria em colocar um item chave:valor directamente no dicionário
    # self.imagensCarregadas;
    # não se permite ao cliente esse privilégio de acesso ao dicionário
    def __setitem__(self, chave, valor):
        raise Exception("Operação proibida")

    def __delitem__(self, numero):
        """ Elimina deste Album a Imagem que tem o número de Imagem indicado

    Suporta o uso do operador del por parte do código cliente.
    Requires: numero é um número de Imagem de uma Imagem carregada no Album.
    Side-effects: este Album deixa de conter a Imagem cujo atributo numero é
      igual ao parâmetro numero.
    """
        del self.imagensCarregadas[numero]

    def carregarImagemPreProcessada(self, objectoImagem):
        """ Carrega para este Album um objecto Imagem

    Se a Imagem já tiver sido carregada para este Album num carregamento
    anterior, e não tiver sido eliminada entretanto do Album,
    -- é carregada de novo;
    -- essa operação será silenciosa;
    -- a Imagem mantém o número que já tinha, e continua a ser acedida por
       esse número.
    Requires: o parâmetro objectoImagem é uma instância da classe Imagem
    """

        self.imagensCarregadas.update({objectoImagem.getNumero(): objectoImagem})

    def carregarImagemDeFicheiro(self, nome, pasta=".", validar=False):
        """ Cria um objecto Imagem a partir de ficheiro e carrega-o condicionalmente

    Desde que o ficheiro esteja acessível, é criado um novo objecto Imagem, que
    recebe portanto (provisoriamente) um novo número, sequencialmente na
    numeração da classe Imagem.
    nome é o nome do ficheiro a importar (incluindo a extensão) e pasta é o nome
    da pasta onde está o ficheiro (por omissão, a pasta de trabalho actual).   
    Se o parâmetro validar for False, a Imagem criada é sempre carregada, mesmo
    que uma Imagem semelhante (por exemplo, do mesmo ficheiro) tenha sido
    anteriormente carregada para este Album. A nova Imagem será sempre diferente
    da antiga no atributo numero.
    Se o parâmetro validar for True, só carrega a Imagem recém-criada se ainda
    não existir neste Album uma Imagem com o mesmo nome, tamanho e dataHora.
    Se já existir neste Album uma Imagem com o mesmo nome, tamanho e dataHora,
    -- o contador de Imagem's é "reposto" (i.e., decrementado em 1 unidade);
    -- o objecto Imagem recém-criado é descartado no final da execução deste
       método, pois deixa de haver referência para ele.
    Requires: nome e pasta são strings denotando um path de ficheiro válido e
      acessível.
    Side-effects: se (validar == False) ou (validar == True e a Imagem criada
      passar no teste de originalidade), essa Imagem fica a fazer parte deste
      Album.
    Nota de uso: se a validação for desnecessária, o parâmetro validar deve ser
      False, por razões de eficiência.
    """
        novaImagem = Imagem(nome, pasta)
        if validar and \
                any((imagem.getNome() == novaImagem.getNome() and \
                     imagem.getTamanho() == novaImagem.getTamanho() and \
                     imagem.getDataHora() == novaImagem.getDataHora()) \
                    for imagem in self.imagensCarregadas.values()):
            # print("Imagem", imagem.getNome(), "já carregada no álbum")
            Imagem.alterarNumeroDeImagens(-1)  # anula a catalogação da Imagem acima
        else:  # carrega a Imagem sem qualquer validação
            self.imagensCarregadas[novaImagem.getNumero()] = novaImagem

    def getImagens(self):
        """ Devolve uma lista com as Imagens carregadas neste Album

    Ensures: uma lista com as próprias Imagem's carregadas neste Album, e não
      clones dessas Imagem's.
    """
        lst = []
        for key in self.imagensCarregadas:
            lst.append(self.imagensCarregadas[key])

        return lst

    def __str__(self):
        return "Album " + self.nomeAlbum

    def __repr__(self):
        return "Album " + self.nomeAlbum + \
               " com " + str(len(self.imagensCarregadas)) + " imagens "


### classe AlbumPlus ###

class AlbumPlus(Album):
    """ Um Album especializado

  Novas operações:
  Permite carregar múltiplas pastas contendo ficheiros de imagem.
  Possibilita pesquisas complexas dentro do Album,
  -- exactamente por número de Imagem, ou
  -- por uma combinação de nome, data e etiquetas da Imagem, em que os termos
     da pesquisa não têm de ser exactos (tolerância a imprecisão do input).
  Permite conhecer a data de criação de cada AlbumPlus.
  Permite inicializar um AlbumPlus a partir das Imagem's existentes numa outra
  instância de Album (esta instância pode ser da classe Album ou de qualquer
  sub-classe, incluindo AlbumPlus).
  Oferece uma listagem breve e legível do conteúdo: método listarImagens.
  """

    # extensões reconhecidas como sendo de ficheiros de imagens
    extensoesFicheirosImagem = ['jpg', 'JPG', 'jpeg', 'JPEG', 'png', 'PNG',
                                'gif', 'GIF']

    def __init__(self, albumOuString):
        """ Inicializa um AlbumPlus a partir de uma instância de Album ou de string

    Se albumOuString for um Album, a colecção das suas Imagem's é copiada para
    este AlbumPlus, e o seu nome é usado para construir o nome deste AlbumPlus.
    -- A cópia da colecção é superficial, i.e., as Imagem's não são clonadas.
    -- O novo nome obtém-se acrescentando " -cópia" ao nome do Album recebido.
    Se albumOuString for uma string, essa string ficará sendo o nome deste
    AlbumPlus, e o mesmo será inicializado com 0 (zero) Imagem's.
    É inicializada a nova propriedade dataCriacao, que fica com o valor dado
    pela timestamp do momento da criação do objecto.    
    Requires: albumOuString é instância de Album ou de str.
    """
        if isinstance(albumOuString, Album):  # fica com uma versão alterada do nome
            self.nomeAlbum = albumOuString.nomeAlbum + " -cópia"  # acessa atributo
            self.imagensCarregadas = albumOuString.imagensCarregadas.copy()
            if isinstance(albumOuString, AlbumPlus):
                # em eventuais versões futuras:
                # copiar atributos exclusivos de AlbumPlus excepto dataCriacao
                pass
        else:  # albumOuString é string, usada para dar nome a um novo AlbumPlus
            # inicializa os atributos de um Album sem Imagem's
            super().__init__(albumOuString)
            # em eventuais versões futuras:
            # inicializar atributos exclusivos de AlbumPlus excepto dataCriacao
        self.dataCriacao = datetime.datetime.today()  # novo atributo de AlbumPlus

    def getDataCriacao(self):
        """ Devolve a data de criação deste AlbumPlus

    Ensures: a data de criação deste AlbumPlus como um objecto datetime.datetime
    """
        return self.dataCriacao

    # pastas onde as imagens existentes são carregadas para o álbum
    def carregarPastas(self, pastas, recursivo=False, validarImagens=False):
        """ Cria Imagem's a partir de pastas, e carrega as Imagem's condicionalmente

    Executa o método carregarImagemDeFicheiro() da classe Album sobre todos os
    ficheiros de imagem que encontra na lista de pastas passada como parâmetro.
    Um ficheiro é considerado de imagem se a sua extensão estiver na lista de
    extensões reconhecidas pela classe AlbumPlus como de ficheiro de imagem.
    Se recursivo == True, é pesquisada cada pasta da lista passada, bem como as
    respectivas sub-pastas. Pode ser demorado!
    Se validarImagens = True, o método carregarImagemDeFicheiro() é invocado com
    validar = True para cada um dos ficheiros.  
    Requires:
      pastas é uma lista de strings em que cada uma denota um path de pasta
        válido e acessível;
      recursivo é Booleano;
      validarImagens é Booleano.
    Side-effects: este AlbumPlus é carregado com novas Imagem's de acordo com as
      regras de inclusão dos paths e validação dos ficheiros, acima descritas.
    Nota de uso: se a validação for desnecessária, o parâmetro validarImagens
      deve ser False, por razões de eficiência.
    """
        for pasta in pastas:
            pathPasta = Path(pasta)
            if not recursivo:
                pesquisarEm = pathPasta.iterdir()  # ficheiros desta pasta
            else:  # recursivo == True
                pesquisarEm = pathPasta.rglob("*.*")  # fich. desta pasta e sub-pastas
            for path in pesquisarEm:
                if path.suffix[1:] in AlbumPlus.extensoesFicheirosImagem:
                    nomeFich, pastaFich = (path.name, str(path.parent))
                    self.carregarImagemDeFicheiro(nomeFich, pastaFich,
                                                  validar=validarImagens)

    def listarImagens(self):
        """ Devolve uma lista com o str() de cada Imagem carregada """
        return [str(imagem) for imagem in self.getImagens()]

    def pesquisarImagens(self, nome=None, tolerancia=0,
                         intervaloDataHora=None, etiquetas=None):
        """ Pesquisa Imagem's por nome, intervalo de dataHora, etiquetas

    Pesquisa Imagem's pelo nome exacto (sem sufixo) ou com uma tolerância para
    o número de caracteres alterados em relação ao nome exacto.
    E/ou pesquisa as Imagem's cuja dataHora esteja no intervalo de tempo
    indicado.
    E/ou pesquisa as Imagem's que tenham pelo menos uma das etiquetas em comum
    com a lista de input etiquetas.
    Requires:
      nome é uma string;
      tolerância é um int >= 0;
      intervaloDataHora é um par de objectos datetime.datetime ordenados por
        ordem crescente;
      etiquetas é uma lista de strings;
      pelo menos 1 dos parâmetros nome, intervaloDataHora, etiquetas, tem de ser
        instanciado.
    Ensures: a lista de Imagem's que verificam todos os critérios de pesquisa
      que estejam activados.
      Se nome != None e tolerancia == 0, são incluídas todas as Imagem's cujo
        nome seja igual ao nome passado por parâmetro.
      Se nome != None e tolerancia > 0, são incluídas todas as Imagem's cujo
        nome dista do nome passado por parâmetro até um número de caracteres
        dado pela tolerância, sendo usada a distância de Levenshtein.
      Se intervaloDataHora != None, são incluídas todas as Imagem's cuja
        dataHora está dentro do intervalo de tempo indicado por esse parâmetro.
      Se etiquetas != None, são incluídas todas as Imagem's que tenham pelo
        menos uma das etiquetas em comum com a lista de input etiquetas.
    """
        if nome == None:
            iteravelAPesquisar = self.imagensCarregadas.values()
        else:  # nome != None
            if tolerancia == 0:  # só se aceita nomes exactamente iguais
                iteravelAPesquisar = [imagem \
                                      for imagem in self.imagensCarregadas.values() \
                                      if imagem.getNomeSemSufixo() == nome]
            else:  # tolerancia >= 1; aceita-se nomes alterados em até tolerância letras
                iteravelAPesquisar = [imagem \
                                      for imagem in self.imagensCarregadas.values() \
                                      if levDistance(imagem.getNomeSemSufixo(), nome) <= tolerancia]
        if intervaloDataHora != None:
            iteravelMaisRestrito = [imagem \
                                    for imagem in iteravelAPesquisar \
                                    if imagem.getDataHora() >= intervaloDataHora[0] and \
                                    imagem.getDataHora() <= intervaloDataHora[1]]
            iteravelAPesquisar = iteravelMaisRestrito

        if etiquetas != None:
            iteravelAindaMaisRestrito = [imagem
                                         for imagem in iteravelAPesquisar
                                         if bool(set(imagem.getEtiquetas()) & set(etiquetas))]
            iteravelAPesquisar = iteravelAindaMaisRestrito

        return iteravelAPesquisar[:]
