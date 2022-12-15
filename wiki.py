import wikipedia

def pesquisa(self) :
    wikipedia.set_lang('pt')
    resultado = wikipedia.summary(self, 2)
    return resultado

sobre = "David Hilbert"

print(str(pesquisa(sobre)))

## Otput: David Hilbert (Königsberg, 23 de janeiro de 1862 — Göttingen, 14 de fevereiro de 1943) foi um matemático alemão. Foi eleito membro estrangeiro da Royal Society em 1928.

        



