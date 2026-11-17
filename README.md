# ASD-STE100 (pt-BR) — Português Técnico Simplificado

Uma skill para Claude Code e outros agentes de IA que reescreve texto denso ou ambíguo em **português do Brasil** seguindo a disciplina da [ASD-STE100](https://www.asd-ste100.org/), a norma de linguagem controlada que a indústria aeroespacial criou para que instruções de manutenção não sejam lidas de forma errada.

A ASD-STE100 define apenas o inglês. Esta skill é uma adaptação para o português, não uma norma oficial.

## Por que STE, e por que para agentes

A STE existe porque uma instrução lida de forma errada em uma aeronave pode matar, e os leitores em geral não tinham o inglês como língua materna nem um autor para consultar. A correção da norma: um sentido por palavra, voz ativa, tempos simples, uma instrução por frase, frases curtas, nenhuma palavra omitida.

Um agente de IA que interpreta a saída de outro agente, uma descrição de ferramenta ou uma mensagem de erro está na mesma posição. Não há canal de volta para perguntar "você quis dizer X ou Y?". O português acrescenta fontes próprias de dúvida: sujeito que some, `seu` sem dono, `pode` com três sentidos, `apaga-se` sem agente, gerúndio que encadeia sem explicar, `realizar a verificação de` no lugar de `verificar`.

## Antes / depois

| Antes | Depois |
|---|---|
| "Esta ferramenta irá tentar realizar a sincronização do estado entre os diversos backends que tenham sido configurados, e caso seja detectado algum conflito, o mesmo poderá ser resolvido automaticamente conforme a estratégia que tiver sido definida; do contrário, o conflito será apresentado para revisão manual." | "A ferramenta tenta sincronizar o estado entre os backends configurados. Se a ferramenta encontra um conflito, ela lê a estratégia configurada. Se a estratégia permite resolução automática, a ferramenta pode resolver o conflito sem um usuário. Se a ferramenta não resolve o conflito, ela apresenta o conflito para revisão manual." |
| "Pode ter ocorrido um erro durante o processamento da sua requisição em virtude de uma possível incompatibilidade no formato dos dados esperado, a qual pode ter sido ocasionada por uma versão desatualizada do cliente." | "Sua requisição pode ter falhado. A causa pode ser um formato de dados diferente do que o servidor espera. Uma versão desatualizada do cliente pode causar essa diferença. Verifique a versão do seu cliente." |

Mais exemplos, inclusive as regras da STE ilustradas em português, em [`examples/antes-depois.md`](examples/antes-depois.md).

## O que a skill faz

1. Escolhe um modo. **Estrito** cobre procedimentos, mensagens de erro, descrições de ferramentas e instruções entre agentes. **Flexível** cobre READMEs, descrições de PR e prosa explicativa, com a disciplina de frase mas sem vocabulário fixo.
2. Lê o texto para entender o sentido.
3. Marca cada violação frase a frase: passiva e sujeito escondido, formas de instrução misturadas, gerundismo e gerúndio encadeando, tempos compostos, nominalização, burocratês, gíria e verbo anglicizado, pronome sem dono, condição depois da ação, frase longa, ponto e vírgula, abreviação, `(a)` e `(s)`, palavra de marketing, rotação de sinônimos.
4. Reescreve cada frase marcada sem perder nenhum fato, condição, qualificador de escopo ou grau de certeza. Se a forma mais curta perderia precisão, mantém a forma longa e sinaliza.
5. Devolve só o texto reescrito, mais uma linha `Mantido como está:` quando deixou algo sem simplificar de propósito.

Peça a explicação ("mostre o diff", "quais regras ele quebrou", "antes/depois") e a skill devolve uma tabela com cada regra.

## Linter

`scripts/ste-lint-ptbr.py` é um linter determinístico, só com a biblioteca padrão do Python. Ele verifica o que uma expressão regular encontra: ponto e vírgula, frase longa, nominalização, palavras de marketing, burocratês, gerundismo, gíria e verbos anglicizados, abreviações, `(a)` e `(s)`, rotação de sinônimos e conjunção solta em item de lista. Como achados consultivos: voz passiva, `se` passivo, tempo composto, gerúndio, cadeia de `que`, forma indireta de instrução, `o mesmo`, `etc.` e ponto de milhar.

Ele nunca marca ressalvas (`pode`, `talvez`, `provavelmente`): grau de certeza é conteúdo, não estilo.

```bash
python3 scripts/ste-lint-ptbr.py texto.md
echo "Deve-se realizar a verificação do log; favor conferir." | python3 scripts/ste-lint-ptbr.py --json
python3 scripts/ste-lint-ptbr.py --selftest
python3 -m pytest tests/
```

Sai com 1 quando as violações duras passam de `--baseline` (padrão 0). `--disable regra1,regra2` silencia regras. Para prosa (modo Flexível), use `--disable rotacao-de-sinonimos`.

O linter não verifica cadeias de `de`, homógrafos, pronome sem dono, sujeito oculto nem `pode` e `deve` ambíguos. Isso precisa de análise sintática. A skill verifica à mão.

A prosa deste repositório não passa limpa no linter: as tabelas de regras citam os padrões que proíbem. Rode com `--baseline` e leia os achados como exemplos.

## Instalação

```bash
git clone https://github.com/vladesouza7/asd-ste100-pt_BR-skill ~/.claude/skills/asd-ste100-pt-br
```

Ou, com a [skills CLI](https://skills.sh/):

```bash
npx skills add vladesouza7/asd-ste100-pt_BR-skill
```

## Uso

```
Simplifique esta descrição de ferramenta
Reescreva esta mensagem de erro para um agente não interpretar errado
Aplique STE em português a este procedimento
Tire a ambiguidade deste texto
```

Você recebe o texto reescrito e nada mais. Para ver as regras aplicadas, acrescente "mostre o diff" ou "explique as mudanças".

## Escopo

Feito para: mensagens entre agentes, descrições de ferramentas e funções, mensagens de erro, prompts de sistema, procedimentos, manuais, textos de interface. Qualquer texto em português que uma máquina ou um leitor com pouco domínio da língua precisa interpretar sem ninguém para perguntar.

Não feito para: texto criativo, de marketing ou persuasivo. Texto em inglês: use [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill).

Um limite que vale declarar: a skill corrige a forma do texto, não a substância. Um parágrafo sem conteúdo sai curto, limpo e ainda vazio.

## Estrutura

```
SKILL.md                         instruções da skill
references/regras-de-escrita.md  mapeamento STE → português, modalidade, fontes
references/substituicoes.md      tabelas: burocratês, anglicismos, conectivos, homógrafos
examples/antes-depois.md         regras ilustradas e cinco exemplos analisados
scripts/ste-lint-ptbr.py         linter
tests/                           testes do linter
evals/                           casos de teste da skill
```

## Projetos relacionados

- [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill), a skill em inglês que este projeto adapta.
- [g4lb/asd-ste100-hebrew-skill](https://github.com/g4lb/asd-ste100-hebrew-skill), a adaptação para o hebraico que serviu de modelo.

## Fontes

- [ASD-STE100, site oficial](https://www.asd-ste100.org/)
- [Simplified Technical English — Wikipedia](https://en.wikipedia.org/wiki/Simplified_Technical_English)
- [Acordo Ortográfico de 1990 — Decreto 6.583/2008](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/decreto/d6583.htm)
- [Diretivas ISO/IEC, Parte 2 — formas verbais](https://www.iso.org/sites/directives/current/part2/index.xhtml)
- [Manual de Redação da Presidência da República (2018)](https://www4.planalto.gov.br/centrodeestudos/assuntos/manual-de-redacao-da-presidencia-da-republica/manual-de-redacao.pdf)

## Licença

MIT — veja [LICENSE](LICENSE).
