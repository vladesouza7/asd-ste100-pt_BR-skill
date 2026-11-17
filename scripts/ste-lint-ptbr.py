#!/usr/bin/env python3
"""Linter determinístico para as regras estruturais do Português Técnico
Simplificado (adaptação da ASD-STE100 para o pt-BR).

Adaptado de danyuchn/asd-ste100-skill e g4lb/asd-ste100-hebrew-skill (MIT).
Verifica só o que uma expressão regular encontra sem analisador morfológico.
Nunca marca ressalvas nem modalidade (pode, talvez, provavelmente,
possivelmente, é possível que): grau de certeza é conteúdo, não estilo.

Uso:
    ste-lint-ptbr.py ARQUIVO [ARQUIVO ...]
    echo "texto" | ste-lint-ptbr.py [--json]
    ste-lint-ptbr.py --baseline 5 ARQUIVO      # passa até 5 violações duras
    ste-lint-ptbr.py --disable voz-passiva,gerundio ARQUIVO
    ste-lint-ptbr.py --selftest

Pula código, front matter YAML e qualquer trecho entre <!-- ste-lint: off -->
e <!-- ste-lint: on --> (por exemplo, um texto "antes" que é ruim de propósito).

Sai com 1 quando as violações duras passam do baseline (padrão 0). Sai com 2
quando um arquivo não pode ser lido ou uma opção não tem valor válido.
Achados consultivos nunca falham a execução.
"""
import json
import re
import sys

LET = "A-Za-zÀ-ÖØ-öø-ÿ"
START = rf"(?<![{LET}0-9_])"
END = rf"(?![{LET}0-9_])"


def alt(*forms):
    return "(?:" + "|".join(forms) + ")"


def term(*forms, flags=re.IGNORECASE):
    return re.compile(START + alt(*forms) + END, flags)


# Terminações regulares. A 1ª pessoa do singular em -o fica de fora: "uso",
# "salvo", "checo" colidem com substantivos e adjetivos comuns.
AR = ["ar", "a", "as", "am", "amos", "ei", "ou", "aram", "ava", "avam", "ará",
      "arão", "aremos", "aria", "ariam", "e", "em", "emos", "ando", "ado",
      "ada", "ados", "adas"]
ER = ["er", "e", "es", "em", "emos", "i", "eu", "eram", "ia", "iam", "erá",
      "erão", "eremos", "eria", "eriam", "a", "am", "amos", "endo", "ido",
      "ida", "idos", "idas"]
IR = ["ir", "e", "es", "em", "imos", "i", "iu", "iram", "ia", "iam", "irá",
      "irão", "iremos", "iria", "iriam", "a", "am", "amos", "indo", "ido",
      "ida", "idos", "idas", "ído", "ída", "ídos", "ídas", "íram", "ía", "íam"]
CLASSES = {"ar": AR, "er": ER, "ir": IR}


def verb(stems, cls, extra=(), exclude=()):
    """Alternação com todas as formas regulares de um verbo (um ou mais radicais)."""
    if isinstance(stems, str):
        stems = [stems]
    forms = [s + suf for s in stems for suf in CLASSES[cls]]
    forms += list(extra)
    forms = [f for f in forms if f not in exclude]
    return alt(*sorted(set(forms), key=len, reverse=True))


# --- Nominalização ------------------------------------------------------------
LIGHT_VERBS = alt(
    verb("realiz", "ar"), verb("efetu", "ar"), verb("execut", "ar"),
    verb("promov", "er"), verb("proced", "er", extra=["proceda", "procedam"]),
    alt("fazer", "faz", "fazem", "faço", "fez", "fizeram", "fazia", "faziam",
        "fará", "farão", "faremos", "faria", "fariam", "faça", "façam",
        "façamos", "fazendo", "feito", "feita", "feitos", "feitas"),
)
ACTION_NOUNS = alt(
    "verificação", "verificações", "análise", "análises", "instalação",
    "configuração", "configurações", "atualização", "atualizações",
    "correção", "correções", "validação", "validações", "remoção",
    "exclusão", "leitura", "gravação", "envio", "carregamento", "execução",
    "teste", "testes", "cópia", "limpeza", "busca", "pesquisa",
    "comparação", "avaliação", "revisão", "sincronização", "inicialização",
    "reinicialização", "restauração", "importação", "exportação",
    "conexão", "criação", "alteração", "edição", "inserção", "consulta",
    "cadastro", "ajuste", "ajustes", "montagem", "desmontagem", "inspeção",
    "medição", "substituição", "troca", "registro", "apuração",
    "levantamento", "conferência", "checagem", "seleção", "liberação",
    "bloqueio", "desbloqueio", "abertura", "fechamento", "encerramento",
    "finalização", "reinício", "pagamento", "cobrança", "entrega",
    "implantação", "publicação", "migração", "conversão", "compilação",
    "geração", "impressão", "exibição", "cancelamento", "aprovação",
    "autenticação", "autorização", "replicação", "redirecionamento",
    "armazenamento", "processamento", "tratamento", "manutenção", "reparo",
    "retirada", "aplicação", "lubrificação", "aperto", "fixação", "drenagem",
    "contagem", "cálculo", "ordenação", "filtragem", "formatação",
    "transferência", "upload", "download", "login", "logout", "backup",
    "deploy", "merge", "commit", "rollback",
)
NO_PT_VERB = {"upload", "download", "login", "logout", "backup", "deploy",
              "merge", "commit", "rollback"}
DET = r"(?:\s+(?:a|o|as|os|um|uma|uns|umas|à|às|ao|aos|da|do|das|dos))?"
NOMINAL_MSG = ("Ação congelada em substantivo. Use o verbo "
               "(verifique, não realize a verificação).")
NOMINAL_RE = re.compile(START + LIGHT_VERBS + DET + r"\s+" + ACTION_NOUNS + END,
                        re.IGNORECASE)
NOMINAL_ANY_RE = re.compile(
    START + alt(verb("realiz", "ar"), verb("efetu", "ar"),
                verb("proced", "er", extra=["proceda", "procedam"]) + r"\s+(?:a|à|ao|às|aos)")
    + DET + rf"\s+(?!{ACTION_NOUNS}{END})[{LET}]{{3,}}", re.IGNORECASE)
DAR_RE = re.compile(
    START + alt(verb("d", "ar", extra=["dá", "dão", "dê", "deem", "dei", "deu",
                                       "deram", "dando", "dado", "dada"],
                     exclude=["da", "das", "de", "dem"]))
    + r"\s+" + alt("início", "continuidade", "andamento", "prosseguimento",
                   "entrada", "baixa", "suporte", "manutenção", "sequência",
                   "seguimento") + END, re.IGNORECASE)

# --- Marketing ------------------------------------------------------------------
MARKETING = term(
    r"robust[oa]s?", r"poderos[oa]s?", r"inovador(?:a|es|as)?",
    r"revolucionári[oa]s?", r"intuitiv[oa]s?", r"perfeit[oa]s?",
    r"de ponta", r"de última geração", r"sem esforço", r"de forma fluida",
    r"de maneira fluida", r"sem fricção", r"sem atrito", r"incrível",
    r"incríveis", r"fantástic[oa]s?", r"ultrarrápid[oa]s?", r"extremamente",
    r"de classe mundial", r"líder de mercado", r"melhor do mercado",
    r"sem precedentes", r"disruptiv[oa]s?", r"impecável", r"impecáveis",
    r"excepciona(?:l|is)", r"100% segur[oa]s?", r"de forma transparente",
    r"altamente (?:escalável|eficiente|confiável|seguro|segura)",
)

# --- Burocratês -------------------------------------------------------------------
BUREAU_HARD = term(
    "outrossim", "destarte", r"no que tange", r"no tocante a", r"em virtude de",
    r"a fim de", r"visando", r"no sentido de", r"face a", r"em face de",
    r"haja vista", r"por conseguinte", r"com vistas a", r"tendo em vista",
    r"supracitad[oa]s?", r"supramencionad[oa]s?", r"retromencionad[oa]s?",
    r"em tela", r"em epígrafe", r"cumpre (?:informar|salientar|ressaltar|destacar)",
    r"vale (?:ressaltar|destacar|salientar|lembrar|frisar)",
    r"é importante (?:ressaltar|destacar|salientar|frisar|notar|mencionar)",
    r"cabe (?:salientar|ressaltar|destacar|frisar|mencionar)",
    r"ressalte-se", r"registre-se", r"frise-se", r"insta salientar",
    r"a nível de", r"em nível de", r"trata-se de", r"faz-se necessári[oa]",
    r"levar a efeito", r"levar a cabo", r"de modo a", r"de forma a",
    r"na medida em que", r"sob pena de", r"ante o exposto", r"isto posto",
    r"no âmbito d[eoa]s?", r"ora,?",
)
BUREAU_ADVISORY = term(
    r"através d[eoa]s?", r"junto a[oà]s?", r"mediante", r"por parte d[eoa]s?",
    r"em questão", r"referid[oa]s?", r"em caso de", r"caso",
    r"deverá", r"deverão", r"ao (?:[a-zà-ú]+[aei]r)\b",
)
MESMO_RE = re.compile(
    START + r"(?:[oa]s? mesm[oa]s?)" + r"(?=\s*(?:[.,;:)]|$|"
    + alt("é", "são", "foi", "foram", "será", "serão", "está", "estão",
          "deve", "devem", "pode", "podem", "não", "que", "tem", "têm",
          "para", "ser", "e", "ou") + END + "))",
    re.IGNORECASE)

# --- Gerúndio -------------------------------------------------------------------
GER = rf"[{LET}]+(?:ando|endo|indo)"
GERUNDISMO = re.compile(
    START + alt("vou", "vai", "vamos", "vão", "irei", "irá", "iremos", "irão",
                "ir", "iria", "iriam", "poderei", "poderá", "poderemos",
                "poderão", "pode", "podem", "devo", "deve", "devem", "deverá",
                "deverão", "deveria", "deveriam", "posso", "poderia",
                "poderiam", "vir", "passar a", "passa a", "passam a")
    + r"\s+estar\s+" + GER + END, re.IGNORECASE)
ESTAR_GER = re.compile(
    START + alt("está", "estão", "estava", "estavam", "estará", "estarão",
                "esteja", "estejam", "estar", "estando", "esteve", "estiveram",
                "fica", "ficam", "ficou", "ficaram", "continua", "continuam",
                "vem", "vêm", "vinha", "vinham")
    + r"\s+" + GER + END, re.IGNORECASE)
NOT_GERUND = {"comando", "comandos", "segundo", "segundos", "fundo", "fundos",
              "mundo", "quando", "profundo", "redondo", "bando", "ando",
              "orlando", "fernando", "rolando", "armando"}
GER_START = re.compile(rf"^\s*(?:[-*+]|\d+[.)])?\s*(?:\*\*)?({GER})\b", re.IGNORECASE)

# --- Gíria e verbos anglicizados ----------------------------------------------
SLANG = term(
    r"deploy(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"comit(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"merg(?:ear|eia|eiam|eou|earam|eando|eado|eada|eados|eadas|eie|eiem|eei)",
    r"set(?:ar|ou|aram|ando|ado|ada|ados|adas|ei|e|em)",
    r"log(?:ar|ou|aram|ando|ado|ada|ados|adas|ue|uem|uei)",
    r"print(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"start(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"restart(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"bug(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|ue|uem|uei)",
    r"up(?:ar|ou|aram|ando|ado|ada|ados|adas|ei)",
    r"mock(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"build(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"debug(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|ue|uem|uei)",
    r"link(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"drop(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"fork(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"push(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"pull(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"crash(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"flag(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|ue|uem|uei)",
    r"zip(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"reset(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"perform(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"boot(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"attach(?:ar|a|am|ou|aram|ando|ado|ada|ados|adas|e|em|ei)",
    r"render(?:izar|iza|izam|izou|izando|izado|izada)",
    r"dar um jeito", r"dá um jeito", r"deu um jeito", r"quebrar o galho",
    r"quebra-galho", r"na mão grande", r"no braço", r"na raça",
    r"pisar na bola", r"pisou na bola", r"cair fora", r"dar pau", r"deu pau",
    r"dá pau", r"deu ruim", r"dar ruim", r"ficar de olho", r"fique de olho",
    r"mão na roda", r"correr atrás", r"no automático", r"de boa", r"na boa",
    r"tipo assim", r"meio que", r"pra caramba", r"beleza\?",
)

# --- Abreviações ------------------------------------------------------------------
ABBREV = re.compile(
    r"(?<![\w/])(?:p/|c/|s/|q/|qdo|qdo\.|vc|vcs|pq|tb|tbm|obs\.|obs:|ex\.:|ex:|"
    r"msg|msgs|cfg|cfe\.|conf\.|ref\.|resp\.|aprox\.|aprox|n[º°]|nº\.|"
    r"V\.?\s?S[a.]\.?|V\.?\s?Ex[a.]\.?|Sr\.|Sra\.|Dr\.|Dra\.|pag\.|pág\.|"
    r"fls\.|art\.|arts\.|inc\.|par\.|qq|qqr|td|tds|ñ|q)(?![\w/])",
    re.IGNORECASE)
ETC = re.compile(START + r"etc\.?" + r"(?![\w])", re.IGNORECASE)

# --- "(a)" e "(s)" ---------------------------------------------------------------
GENDER_PAREN = re.compile(rf"[{LET}]+\((?:a|as|s|es|o|os|oa|ao)\)", re.IGNORECASE)

# --- Forma indireta de instrução ---------------------------------------------------
INDIRECT = re.compile(
    r"^\s*(?:[-*+]|\d+[.)])?\s*(?:\*\*)?"
    + alt("Deve-se", "Devem-se", "É necessário", "É preciso", "Faz-se necessário",
          "Favor", "Por favor,?", "Por gentileza,?", "Gentileza", "Recomenda-se",
          "Sugere-se", "Solicita-se", "Solicitamos", "Pede-se", "Pedimos",
          "Deverá", "Deverão", "Deve ser", "Devem ser", "É recomendável",
          "É recomendado", "É obrigatório", "Orienta-se", "Fica a cargo",
          "Cabe ao", "Cabe à", "Compete ao", "Compete à")
    + END, re.IGNORECASE)

# --- Voz passiva ------------------------------------------------------------------
AUX = alt("é", "são", "foi", "foram", "será", "serão", "seria", "seriam", "era",
          "eram", "ser", "sendo", "sido", "seja", "sejam", "fosse", "fossem",
          "está", "estão", "estava", "estavam", "estará", "estarão", "fica",
          "ficam", "ficou", "ficaram", "ficará", "ficarão")
PARTICIPLE = alt(rf"[{LET}]{{2,}}(?:ad|id|íd)[oa]s?",
                 r"feit[oa]s?", r"post[oa]s?", r"escrit[oa]s?", r"abert[oa]s?",
                 r"dit[oa]s?", r"vist[oa]s?", r"pag[oa]s?", r"gast[oa]s?",
                 r"aceit[oa]s?", r"impress[oa]s?", r"salv[oa]s?", r"entregues?",
                 r"expuls[oa]s?", r"extint[oa]s?", r"suspens[oa]s?", r"fix[oa]s?",
                 r"inclus[oa]s?", r"preench[oa]s?", r"cobert[oa]s?", r"descobert[oa]s?",
                 r"reabert[oa]s?", r"refeit[oa]s?", r"desfeit[oa]s?")
NOT_PARTICIPLE = {"lado", "lados", "estado", "estados", "mercado", "resultado",
                  "resultados", "dado", "dados", "grado", "cuidado", "cuidados",
                  "teclado", "teclados", "sentido", "sentidos", "ouvido",
                  "ouvidos", "partido", "partidos", "conteúdo", "pedido",
                  "pedidos", "vestido", "tido", "obrigado", "obrigada",
                  "ouvido", "passado", "resultado", "significado", "significados",
                  "certificado", "certificados", "comunicado", "comunicados",
                  "empregado", "empregados", "delegado", "advogado", "errado",
                  "errada", "errados", "erradas", "rápido", "rápida", "rápidos",
                  "rápidas", "válido", "válida", "válidos", "válidas", "sólido",
                  "líquido", "ácido", "cômodo", "pesado", "pesada", "privado",
                  "privada", "privados", "privadas", "sagrado"}
PASSIVE = re.compile(START + AUX + r"\s+(?:sendo\s+|sido\s+)?(" + PARTICIPLE + ")" + END,
                     re.IGNORECASE)
SE_PASSIVE = re.compile(
    rf"(?<![{LET}-])(?!(?:deve|devem|recomenda|sugere|solicita|pede|orienta|faz|trata|ressalte|registre|frise)-se)"
    rf"([{LET}]{{3,}}(?:a|e|am|em|ou|ará|arão|erá|erão|irá|irão|ia|iam|aram|eram|iram))-se{END}",
    re.IGNORECASE)

# --- Tempo composto -------------------------------------------------------------
# "tenha falhado" (depois de "talvez") e "pode ter falhado" são ressalvas, não
# tempos compostos a corrigir. O subjuntivo fica de fora e "ter" só conta sem
# um modal antes.
MODAL_BEFORE = "".join(f"(?<!{m} )" for m in
                       ("pode", "podem", "poderia", "poderiam", "deve", "devem",
                        "deveria", "deveriam", "Pode", "Podem", "Deve", "Devem"))
COMPOUND = re.compile(
    START + alt("tem", "têm", "tinha", "tinham", "terá", "terão", "teria",
                "teriam", MODAL_BEFORE + "ter", "tendo", "havia", "haviam", "haver")
    + r"\s+(?:sido\s+)?(" + PARTICIPLE + ")" + END, re.IGNORECASE)

# --- Rotação de sinônimos -----------------------------------------------------------
SYNONYM_GROUPS = [
    (("verificar", verb("verific", "ar") + "|" + verb("verifiqu", "ar")),
     ("checar", verb("chec", "ar") + "|" + verb("chequ", "ar")),
     ("conferir", alt("conferir", "confere", "conferem", "conferiu", "conferiram",
                      "conferia", "conferiam", "conferirá", "conferirão", "confira",
                      "confiram", "conferindo", "conferido", "conferida",
                      "conferidos", "conferidas"))),
    (("apagar", verb("apag", "ar") + "|" + verb("apagu", "ar")),
     ("excluir", verb("exclu", "ir")),
     ("remover", verb("remov", "er")),
     ("deletar", verb("delet", "ar"))),
    (("exibir", verb("exib", "ir", extra=["exiba", "exibam"])),
     ("mostrar", verb("mostr", "ar")),
     ("apresentar", verb("apresent", "ar"))),
    (("usar", verb("us", "ar", exclude=["usa", "usas"])),  # "usa" também é sigla/nome
     ("utilizar", verb("utiliz", "ar"))),
    (("encerrar", verb("encerr", "ar")),
     ("finalizar", verb("finaliz", "ar")),
     ("terminar", verb("termin", "ar"))),
    (("iniciar", verb("inici", "ar")),
     ("começar", verb("começ", "ar") + "|" + verb("comec", "ar"))),
    (("parar", alt("parar", "pare", "parem", "parou", "pararam", "parará",
                   "pararão", "parando", "parado", "parada", "parados", "paradas")),
     ("interromper", verb("interromp", "er"))),
    (("salvar", verb("salv", "ar", exclude=["salva", "salvas"])),  # "salva" = tiro de salva
     ("gravar", verb("grav", "ar"))),
    (("enviar", verb("envi", "ar")),
     ("mandar", verb("mand", "ar"))),
]
SYNONYM_RES = [[(name, re.compile(START + "(?:" + pat + ")" + END, re.IGNORECASE))
                for name, pat in group] for group in SYNONYM_GROUPS]

# --- Número com ponto de milhar -----------------------------------------------------
THOUSANDS = re.compile(r"(?<![\d.,])\d{1,3}\.\d{3}(?![\d.,%])")

MAX_WORDS = 30  # limite de descrições. O limite de instruções (25) precisa de contexto.
QUE_CHAIN = 3

RULES = [
    ("ponto-e-virgula", "hard", re.compile(r";"),
     "A STE proíbe o ponto e vírgula (Regra 8.1). Divida em frases separadas."),
    ("nominalizacao", "hard", NOMINAL_RE, NOMINAL_MSG),
    ("nominalizacao", "hard", DAR_RE, NOMINAL_MSG),
    ("nominalizacao", "advisory", NOMINAL_ANY_RE,
     "Possível nominalização. Se o substantivo nomeia uma ação, use o verbo. "
     "Se nomeia uma coisa (realizar o pedido), prefira um verbo preciso (enviar, criar)."),
    ("marketing", "hard", MARKETING,
     "Palavra de marketing. Apague, ou substitua pela medida que sustenta a afirmação."),
    ("burocrates", "hard", BUREAU_HARD,
     "Burocratês. Use a palavra simples (para, sobre, por, porque). Enchimento como "
     "'vale ressaltar que' sai inteiro."),
    ("burocrates", "advisory", BUREAU_ADVISORY,
     "Possível burocratês ou conectivo ambíguo. 'através de' → 'por' ou 'com'. "
     "'caso' / 'em caso de' → 'se'. 'deverá' → 'deve' ou imperativo. "
     "'ao + infinitivo' → 'quando' ou 'depois de'."),
    ("o-mesmo", "advisory", MESMO_RE,
     "'O mesmo' como pronome. Repita o substantivo."),
    ("gerundismo", "hard", GERUNDISMO,
     "Gerundismo. Use o tempo simples (vai enviar, não vai estar enviando)."),
    ("gerundio", "advisory", ESTAR_GER,
     "Gerúndio. Prefira o presente simples, a menos que 'neste momento' seja parte da informação."),
    ("giria", "hard", SLANG,
     "Gíria ou verbo anglicizado. Use o verbo padrão (implantar, configurar, registrar, "
     "mesclar, depurar). Um anglicismo consolidado fica como substantivo, nunca conjugado."),
    ("abreviacao", "hard", ABBREV,
     "Abreviação. Escreva a palavra inteira (por exemplo, também, para, com, observação)."),
    ("etc", "advisory", ETC,
     "'etc.' esconde itens. Liste todos ou diga quantos são."),
    ("parenteses-de-genero", "hard", GENDER_PAREN,
     "'(a)' ou '(s)' deixa duas leituras. Escreva uma forma, ou reestruture."),
    ("forma-de-instrucao", "advisory", INDIRECT,
     "Instrução indireta. Em procedimentos, use o imperativo na forma 'você' "
     "(Abra, Verifique, Remova) e mantenha uma única forma no documento."),
    ("voz-passiva", "advisory", PASSIVE,
     "Possível voz passiva. Diga quem age e use o verbo ativo, a menos que o agente "
     "seja desconhecido ou irrelevante."),
    ("se-passivo", "advisory", SE_PASSIVE,
     "Possível 'se' passivo ou sujeito indeterminado (apaga-se o arquivo). Diga quem age."),
    ("tempo-composto", "advisory", COMPOUND,
     "Tempo composto. Use o pretérito perfeito simples (recebemos, não temos recebido), "
     "a menos que a repetição seja parte da informação."),
    ("ponto-de-milhar", "advisory", THOUSANDS,
     "Número com ponto de milhar. Uma máquina pode ler 1.500 como 1,5. "
     "Escreva 1500 ou 1 500, e sempre com a unidade."),
]

CODE_FENCE = re.compile(r"^(```|~~~)")
INLINE_CODE = re.compile(r"`[^`]*`")
WORD_CHAR = re.compile(r"\w")
LIST_ITEM_START = re.compile(
    r"^(?P<indent> {0,3})(?P<marker>[-*+]|[0-9]+[.)])(?P<gap> +)(?P<body>.*)$"
)
CONJUNCTION_END = re.compile(rf"(?<![{LET}])(?:e|ou|nem|mas|como|que|se)\s*$", re.IGNORECASE)
TABLE_SEPARATOR_CELL = re.compile(r"^:?-{3,}:?$")
LINT_MARKER = re.compile(r"^<!--\s*ste-lint:\s*(off|on)\s*-->$")
SENTENCE_SPLIT = re.compile(r"(?:(?<=[.!?])|(?<=[.!?][*)\"”])|(?<=[.!?]\*\*))\s+")
QUE_RE = re.compile(START + r"que" + END, re.IGNORECASE)
URL_RE = re.compile(r"https?://\S+|www\.\S+")


def _finding(filename, line, col, rule, level, match, message):
    return {"file": filename, "line": line, "col": col, "rule": rule,
            "level": level, "match": match, "message": message}


def _word_count(text):
    return sum(1 for token in text.split() if WORD_CHAR.search(token))


def _leading_spaces(line):
    return len(line) - len(line.lstrip(" "))


def _is_list_continuation(line, content_indent):
    if not line.strip():
        return True
    if LIST_ITEM_START.match(line):
        return False
    return _leading_spaces(line) >= content_indent


def _split_table_row(line):
    left = len(line) - len(line.lstrip())
    right = len(line.rstrip())
    content = line[left:right]
    if "|" not in content:
        return None
    if content.startswith("|"):
        content = content[1:]
        left += 1
    if content.endswith("|"):
        content = content[:-1]
    raw_cells = re.split(r"(?<!\\)\|", content)
    if len(raw_cells) < 2:
        return None
    cells = []
    column = left
    for raw_cell in raw_cells:
        leading = len(raw_cell) - len(raw_cell.lstrip())
        cells.append((raw_cell.strip(), column + leading))
        column += len(raw_cell) + 1
    return cells


def _markdown_table_cells(lines):
    table_cells = {}
    index = 1
    while index < len(lines):
        separator = _split_table_row(lines[index])
        header = _split_table_row(lines[index - 1])
        if (not separator or not header or len(separator) != len(header)
                or not all(TABLE_SEPARATOR_CELL.fullmatch(cell)
                           for cell, _ in separator)):
            index += 1
            continue
        table_cells[index - 1] = header
        table_cells[index] = []
        index += 1
        while index < len(lines):
            row = _split_table_row(lines[index])
            if not row or len(row) != len(separator):
                break
            table_cells[index] = row
            index += 1
    return table_cells


def _blank_skipped(lines):
    """Apaga front matter YAML e regiões <!-- ste-lint: off -->, mantendo os números de linha."""
    out = list(lines)
    if out and out[0].strip() == "---":
        for end in range(1, len(out)):
            if out[end].strip() == "---":
                out[:end + 1] = [""] * (end + 1)
                break
    in_fence = False
    skipping = False
    for i, line in enumerate(out):
        stripped = line.strip()
        if CODE_FENCE.match(stripped):
            in_fence = not in_fence
        marker = None if in_fence else LINT_MARKER.match(stripped)
        if marker:
            skipping = marker.group(1) == "off"
            out[i] = ""
        elif skipping:
            out[i] = ""
    return out


def _dangling_conjunction_findings(lines, filename):
    findings = []
    in_fence = False
    index = 0
    while index < len(lines):
        line = lines[index]
        if CODE_FENCE.match(line.strip()):
            in_fence = not in_fence
            index += 1
            continue
        start = None if in_fence else LIST_ITEM_START.match(line)
        if not start:
            index += 1
            continue
        content_indent = (len(start.group("indent")) + len(start.group("marker"))
                          + len(start.group("gap")))
        item_lines = [(index, start.group("body"))]
        next_index = index + 1
        item_fence = False
        while next_index < len(lines):
            candidate = lines[next_index]
            if CODE_FENCE.match(candidate.strip()):
                item_fence = not item_fence
                next_index += 1
                continue
            if item_fence:
                next_index += 1
                continue
            if not _is_list_continuation(candidate, content_indent):
                break
            item_lines.append((next_index, candidate))
            next_index += 1
        meaningful = [(i, INLINE_CODE.sub(" CODE ", text).strip())
                      for i, text in item_lines]
        meaningful = [(i, text) for i, text in meaningful if text]
        if meaningful:
            end_index, end_text = meaningful[-1]
            if CONJUNCTION_END.search(end_text):
                col = (start.start("marker") + 1 if end_index == index
                       else _leading_spaces(lines[end_index]) + 1)
                findings.append(_finding(
                    filename, end_index + 1, col, "conjuncao-solta", "hard",
                    end_text,
                    "Item de lista termina com conjunção (e, ou, nem, mas). "
                    "Complete o item ou junte-o ao próximo."))
        index = next_index
    return findings


def _run_rules(line, lineno, source_column, filename):
    findings = []
    for rule_id, level, pattern, msg in RULES:
        for m in pattern.finditer(line):
            matched = m.group(0)
            if rule_id == "voz-passiva" or rule_id == "tempo-composto":
                if m.group(1).lower() in NOT_PARTICIPLE:
                    continue
            if rule_id == "nominalizacao" and level == "hard":
                last = matched.split()[-1].lower()
                if last in NO_PT_VERB:
                    continue
            findings.append(_finding(filename, lineno, source_column + m.start() + 1,
                                     rule_id, level, matched, msg))
    # Um gerundismo já cobre o "estar + -ndo" dentro dele: não marque duas vezes.
    spans = [(f["col"], f["col"] + len(f["match"])) for f in findings if f["rule"] == "gerundismo"]
    findings = [f for f in findings if not (
        f["rule"] == "gerundio" and any(a <= f["col"] < b for a, b in spans))]
    m = GER_START.match(line)
    if m and m.group(1).lower() not in NOT_GERUND:
        findings.append(_finding(
            filename, lineno, source_column + m.start(1) + 1, "gerundio", "advisory",
            m.group(1),
            "Oração com gerúndio abre a frase: a relação com o resto (quando? se? "
            "porque?) e o sujeito ficam implícitos. Use 'Quando', 'Se', 'Depois de'."))
    return findings


def lint(text, filename="<stdin>"):
    """Retorna (achados, total_de_palavras)."""
    findings = []
    words_total = 0
    in_fence = False
    lines = _blank_skipped(text.splitlines())
    table_cells = _markdown_table_cells(lines)
    seen_synonyms = {}
    for lineno, raw_line in enumerate(lines, 1):
        if CODE_FENCE.match(raw_line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for segment, source_column in table_cells.get(lineno - 1, [(raw_line, 0)]):
            line = URL_RE.sub(" URL ", INLINE_CODE.sub("", segment))
            counted = URL_RE.sub(" URL ", INLINE_CODE.sub(" CODE ", segment))
            words_total += _word_count(counted)
            findings.extend(_run_rules(line, lineno, source_column, filename))
            for gi, group in enumerate(SYNONYM_RES):
                for name, pattern in group:
                    if (gi, name) in seen_synonyms:
                        continue
                    m = pattern.search(line)
                    if m:
                        seen_synonyms[(gi, name)] = (
                            lineno, source_column + m.start() + 1, m.group(0))
            for sentence in SENTENCE_SPLIT.split(counted):
                n = _word_count(sentence)
                if n > MAX_WORDS:
                    findings.append(_finding(
                        filename, lineno, source_column + 1, "tamanho-da-frase",
                        "hard", f"{n} palavras",
                        f"Frase com {n} palavras (limite {MAX_WORDS}). Divida."))
                ques = QUE_RE.findall(sentence)
                if len(ques) >= QUE_CHAIN:
                    m = QUE_RE.search(line)
                    findings.append(_finding(
                        filename, lineno, source_column + (m.start() if m else 0) + 1,
                        "cadeia-de-que", "advisory", f"{len(ques)}× que",
                        "Várias orações com 'que' na mesma frase. Mantenha uma e "
                        "divida o resto em frases."))
    for gi, group in enumerate(SYNONYM_RES):
        present = sorted((seen_synonyms[(gi, name)], name) for name, _ in group
                         if (gi, name) in seen_synonyms)
        if len(present) > 1:
            first_name = present[0][1]
            for (lineno, col, match), name in present[1:]:
                findings.append(_finding(
                    filename, lineno, col, "rotacao-de-sinonimos", "hard", match,
                    f"'{name}' e '{first_name}' nomeiam a mesma ação. "
                    "Escolha um e use sempre."))
    findings.extend(_dangling_conjunction_findings(lines, filename))
    findings.sort(key=lambda f: (f["line"], f["col"]))
    return findings, words_total


def report(findings, words_total, as_json, hard_count, baseline):
    rate = round(len(findings) * 100 / words_total, 1) if words_total else 0.0
    if as_json:
        print(json.dumps({"violations": findings, "count": len(findings),
                          "hard_count": hard_count, "baseline": baseline,
                          "words": words_total, "per_100_words": rate},
                         indent=2, ensure_ascii=False))
        return
    for f in findings:
        print(f"{f['file']}:{f['line']}:{f['col']} {f['rule']} ({f['level']}): "
              f"{f['message']} [{f['match']}]")
    print(f"\n{len(findings)} achados ({hard_count} duros, baseline {baseline}), "
          f"{words_total} palavras, {rate} por 100 palavras")
    print("Ressalvas (pode, talvez, provavelmente, possivelmente) nunca são marcadas: "
          "grau de certeza é conteúdo.")


# (regra, texto que deve disparar, texto que não deve disparar)
SELFTEST_CASES = [
    ("ponto-e-virgula", "Abra o arquivo; leia a linha.", "Abra o arquivo. Leia a linha."),
    ("tamanho-da-frase", " ".join(["palavra"] * 31) + ".", " ".join(["palavra"] * 30) + "."),
    ("conjuncao-solta", "- Defina o destino e\n- Registre o resultado",
     "- Defina o destino\n- Registre o resultado"),
    ("conjuncao-solta", "1. Abra o arquivo ou\n2. Feche o arquivo",
     "1. Abra o arquivo\n2. Feche o arquivo"),
    ("nominalizacao", "Realize a verificação do filtro.", "Verifique o filtro."),
    ("nominalizacao", "Efetuou a instalação do pacote.", "Instalou o pacote."),
    ("nominalizacao", "Proceda à análise do log.", "Analise o log."),
    ("nominalizacao", "Fazer o teste da conexão.", "Testar a conexão."),
    ("nominalizacao", "Dar início ao processo.", "Iniciar o processo."),
    ("nominalizacao", "Realizar o pedido.", "Enviar o pedido."),
    ("marketing", "Solução robusta e inovadora.", "Solução que responde em 20 ms."),
    ("marketing", "Integra-se de forma fluida.", "Integra-se ao sistema."),
    ("burocrates", "Vale ressaltar que o serviço parou.", "O serviço parou."),
    ("burocrates", "A fim de evitar perdas, salve o arquivo.", "Para evitar perdas, salve o arquivo."),
    ("burocrates", "Trata-se de um erro de rede.", "É um erro de rede."),
    ("burocrates", "Envie o relatório através do portal.", "Envie o relatório pelo portal."),
    ("burocrates", "Ao clicar em Salvar, o sistema fecha.", "Quando você clica em Salvar, o sistema fecha."),
    ("o-mesmo", "Abra o arquivo. O mesmo deve existir.", "Abra o mesmo arquivo de ontem."),
    ("gerundismo", "Vou estar enviando o relatório.", "Vou enviar o relatório."),
    ("gerundio", "O serviço está sendo processado.", "O sistema processa o serviço."),
    ("gerundio", "Clicando em Salvar, a janela fecha.", "Quando você clica em Salvar, a janela fecha."),
    ("gerundio", "Sendo assim, reinicie.", "Comando executado com sucesso."),
    ("giria", "Precisa deployar o serviço.", "Implante o serviço."),
    ("giria", "Ele setou a variável.", "Ele definiu a variável."),
    ("giria", "O sistema bugou.", "O sistema falhou."),
    ("giria", "Dá um jeito nisso.", "Corrija isso."),
    ("abreviacao", "Salve p/ a pasta.", "Salve para a pasta."),
    ("abreviacao", "Obs.: o serviço reinicia.", "Observação: o serviço reinicia."),
    ("abreviacao", "Vc precisa reiniciar.", "Você precisa reiniciar."),
    ("etc", "Arquivos, pastas etc.", "Arquivos e pastas."),
    ("parenteses-de-genero", "Apague o(s) arquivo(s).", "Apague os arquivos."),
    ("parenteses-de-genero", "O(a) usuário(a) entra.", "O usuário entra."),
    ("forma-de-instrucao", "Deve-se reiniciar o serviço.", "Reinicie o serviço."),
    ("forma-de-instrucao", "Favor reiniciar o serviço.", "Reinicie o serviço."),
    ("forma-de-instrucao", "- É necessário reiniciar.", "- Reinicie."),
    ("voz-passiva", "O arquivo é apagado.", "O agente apaga o arquivo."),
    ("voz-passiva", "A configuração foi feita ontem.", "O técnico configurou ontem."),
    ("voz-passiva", "Os dados foram salvos.", "O sistema tem dados."),
    ("voz-passiva", "O backup está sendo gerado.", "O sistema está do lado esquerdo."),
    ("se-passivo", "Apaga-se o arquivo.", "O agente apaga o arquivo."),
    ("se-passivo", "Verificam-se os logs.", "Deve-se verificar os logs."),
    ("tempo-composto", "O serviço tem falhado.", "O serviço falhou."),
    ("tempo-composto", "O arquivo havia sido apagado.", "O agente apagou o arquivo."),
    ("cadeia-de-que", "O arquivo que o agente que iniciou o processo criou, que não está na pasta, sumiu.",
     "O arquivo que o agente criou está na pasta."),
    ("rotacao-de-sinonimos", "Verifique o arquivo. Depois cheque a saída.",
     "Verifique o arquivo. Verifique a saída."),
    ("rotacao-de-sinonimos", "O agente apaga o arquivo. Depois ele exclui a pasta.",
     "O agente apaga o arquivo. Depois ele apaga a pasta."),
    ("rotacao-de-sinonimos", "Use o comando. Utilize a opção.", "Use o comando. Use a opção."),
    ("ponto-de-milhar", "O limite é 1.500 registros.", "O limite é 1500 registros. Versão 1.2.3 em 10.0.0.1."),
]

HEDGES = ("A requisição pode ter falhado. Talvez a conexão tenha falhado. "
          "Talvez a causa seja o proxy. O serviço deve ter parado. "
          "Provavelmente o disco está cheio. É possível que o servidor não responda. "
          "A ferramenta tenta sincronizar o estado.")


def _rules(text):
    return {f["rule"] for f in lint(text)[0]}


def selftest():
    for rule, bad, good in SELFTEST_CASES:
        assert rule in _rules(bad), (rule, bad, lint(bad)[0])
        assert rule not in _rules(good), (rule, good, lint(good)[0])
    assert lint(HEDGES)[0] == [], lint(HEDGES)[0]
    print("selftest OK")


def main(argv):
    if "--selftest" in argv:
        selftest()
        return 0
    as_json = "--json" in argv
    baseline = 0
    disabled = set()
    paths = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a in ("--baseline", "--disable"):
            if i + 1 >= len(argv):
                print(f"erro: {a} precisa de um valor", file=sys.stderr)
                return 2
            i += 1
            if a == "--disable":
                disabled = set(argv[i].split(","))
            elif re.fullmatch(r"[0-9]+", argv[i]):
                baseline = int(argv[i])
            else:
                print(f"erro: --baseline precisa de um número inteiro, recebeu {argv[i]!r}",
                      file=sys.stderr)
                return 2
        elif a in ("--json", "--selftest"):
            pass
        elif a.startswith("--"):
            print(f"erro: opção desconhecida {a}", file=sys.stderr)
            return 2
        else:
            paths.append(a)
        i += 1

    findings, words_total = [], 0
    if paths:
        for p in paths:
            try:
                with open(p, encoding="utf-8-sig") as fh:
                    text = fh.read()
            except (OSError, UnicodeDecodeError) as exc:
                print(f"erro: não foi possível ler {p}: {exc}", file=sys.stderr)
                return 2
            f, w = lint(text, filename=p)
            findings.extend(f)
            words_total += w
    else:
        findings, words_total = lint(sys.stdin.read())

    findings = [f for f in findings if f["rule"] not in disabled]
    hard_count = sum(1 for f in findings if f["level"] == "hard")
    report(findings, words_total, as_json, hard_count, baseline)
    return 1 if hard_count > baseline else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
