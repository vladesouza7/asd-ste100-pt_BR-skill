# Português Técnico Simplificado — regras e fontes

Este arquivo mapeia as categorias públicas de regras da ASD-STE100 para o português do Brasil. Ele parafraseia *categorias* de regras. Não reproduz o texto da norma nem o dicionário dela. A ASD-STE100 define apenas o inglês. Não existe versão oficial em português, então toda adaptação abaixo pertence a este projeto, não à ASD.

## Sumário

1. O que é a ASD-STE100
2. Regras que passam sem mudança
3. Regras adaptadas para o português
4. Regras só para o português
5. Modalidade: deve, pode, convém
6. O que o linter verifica
7. Fontes

## 1. O que é a ASD-STE100

A ASD-STE100 é uma linguagem controlada para o inglês. A primeira versão saiu em 1986, pela associação que hoje se chama ASD (AeroSpace and Defence Industries Association of Europe). As companhias aéreas europeias pediram a norma porque a maioria dos técnicos de manutenção não tinha o inglês como língua materna. Uma instrução lida de forma errada em uma aeronave pode matar. A edição atual é a Issue 9 (janeiro de 2025). Ela tem 53 regras de escrita em 9 seções e um dicionário de cerca de 900 palavras aprovadas, cada uma com um só sentido e uma só classe gramatical.

A norma é gratuita para obter, mas não para redistribuir. Peça pelo [formulário oficial de download](https://www.asd-ste100.org/STE_downloads.html). Quando o texto final precisa de conformidade real com a STE (documentação de manutenção aeronáutica, por exemplo), use a norma em inglês e verifique palavra por palavra.

## 2. Regras que passam sem mudança

- Sem ponto e vírgula (Regra 8.1). Escreva frases separadas.
- Uma instrução por frase.
- Um tema por parágrafo, com no máximo 6 frases.
- Lista numerada ou com marcadores para 3 ou mais passos ou condições.
- Uma instrução de segurança começa com o comando ou com a condição, nunca os esconde no meio da frase.
- Mantenha a modalidade. `pode`, `talvez`, `provavelmente`, `é possível que`, `tenta` mantêm a força que têm na fonte.
- Não acrescente fatos: nenhuma causa, frequência ou mecanismo novo.
- Sem palavras de marketing: `robusto`, `poderoso`, `inovador`, `revolucionário`, `intuitivo`, `perfeito`, `de ponta`, `sem esforço`, `de forma fluida`, `sem precedentes`, `de classe mundial`.
- Voz ativa em procedimentos. Passiva só em descrição, e só quando quem age é desconhecido ou irrelevante.
- Não omita partes da frase para encurtá-la. A norma avisa que isso cria ambiguidade em vez de clareza.

## 3. Regras adaptadas para o português

| Regra da STE | Regra em português | Por que muda |
|---|---|---|
| ≤ 20 palavras (instruções), ≤ 25 (descrições) | ≤ 25 palavras (instruções), ≤ 30 (descrições) | O português usa artigo antes de possessivo e de nome próprio, mais preposições e menos substantivos compostos. A mesma informação ocupa cerca de 15% a 25% mais espaço do que em inglês. Os limites sobem na mesma proporção. |
| Grupos nominais ≤ 3 palavras | Cadeia de "de" ≤ 3 substantivos: `válvula da bomba de combustível` é o limite | O português não empilha substantivos. Ele os liga com `de`. Cada `de` a mais cria uma dúvida de encaixe: em `bomba de combustível de alta pressão`, o que é de alta pressão? Divida com uma oração ou um adjetivo colado ao substantivo certo. |
| Voz ativa | Evite a passiva analítica (`é apagado`), a passiva sintética (`apaga-se`), o sujeito indeterminado (`apagaram`, `apaga-se`) e o sujeito oculto em descrição (`Reinicia o serviço.`) | Todas essas formas escondem quem age. O português deixa o sujeito cair com facilidade, então a regra precisa ser explícita. |
| Verbo, não substantivo (Regra 3.7) | `verifique`, não `realize a verificação de`. `instale`, não `efetue a instalação de`. `analise`, não `proceda à análise de`. `inicie`, não `dê início a` | O verbo-suporte (`realizar`, `efetuar`, `proceder a`, `fazer`, `promover`, `dar`) não carrega sentido. A ação fica escondida no substantivo. É o traço mais comum do burocratês brasileiro. |
| Sem verbos frasais (Regra 9.3) | Sem gíria, idiomatismo ou verbo anglicizado: `deployar`, `setar`, `logar`, `mergear`, `comitar`, `debugar`, `bugar`, `subir o serviço`, `derrubar o servidor`, `dar um jeito` | O português não tem verbos frasais. A gíria e o anglicismo conjugado causam o mesmo problema: o sentido não vem das palavras, e a grafia não é fixa. Um anglicismo consolidado pode ficar como substantivo (`o deploy`, `o commit`), com entrada no glossário. |
| Só tempos simples | Presente, pretérito perfeito simples, futuro (simples ou `ir + infinitivo`), imperativo, infinitivo, particípio como adjetivo. Evite `tem falhado`, `havia sido processado`, `está sendo enviado`, `vai estar enviando` | O português tem dois problemas que o inglês não tem. O pretérito perfeito composto (`tem falhado`) significa repetição, não um fato concluído, e vale mantê-lo só quando a repetição é a informação. O gerundismo (`vai estar enviando`) é enchimento puro. |
| Formas de -ing só como substantivo técnico | Gerúndio só dentro de uma locução que a informação exige (`está processando` = neste exato momento). Nunca para encadear ações nem para abrir uma frase | `Abrindo o arquivo, verificando a linha 3` não diz se é sequência, condição ou causa. `Clicando em Salvar, o sistema fecha` não diz quem clica. |
| Imperativo em instruções | Imperativo na forma `você` (`Abra`, `Verifique`, `Remova`) em toda instrução. Nunca misture com infinitivo (`Abrir`), `deve-se`, `favor`, `é necessário`, `recomenda-se`, `deverá` nem com a forma `tu` (`Abre`) | O português oferece pelo menos seis formas para uma instrução. Um documento que mistura várias faz o leitor se perguntar se `deve-se` é mais fraco que `abra`. A forma `você` é o padrão dos manuais brasileiros e é neutra em gênero. |
| Sem palavras omitidas | Mantenha o artigo e o objeto. Mantenha o sujeito em frases descritivas. Sem estilo de manchete | `Apagar arquivo temporário.` não diz qual arquivo. `Reinicia o serviço.` não diz quem. |
| Uma palavra, um sentido | Um verbo para uma ação, sempre. `verificar` ou `checar` ou `conferir`, não os três. `apagar` ou `excluir` ou `remover`, não os três | Dentro de um documento, a consistência é verificável. Qual é a palavra "aprovada" não é, sem dicionário. |
| Uma classe gramatical por palavra | Prefira a forma que não cria dupla leitura. `O comando interrompe o serviço`, não `O comando para o serviço` | Depois do Acordo Ortográfico de 1990, `para` (verbo) perdeu o acento e virou homógrafo da preposição. |

## 4. Regras só para o português

- **Pronome com um só dono.** `seu`, `sua`, `dele`, `ele`, `ela`, `este`, `esse`, `o mesmo`, `o referido` precisam de um único antecedente possível. Se há dois, repita o substantivo. Se há um só (`Puxe a tampa para trás e retire-a`), o pronome serve, e repetir o substantivo na mesma frase só pesa o texto. `O agente envia o arquivo ao usuário e apaga sua cópia` não diz de quem é a cópia. `O mesmo` como pronome é burocratês e sai sempre.
- **Condição antes da instrução.** `Se o LED estiver vermelho, não abra o painel.` O leitor que age frase a frase precisa da condição antes do verbo. `Não abra o painel se o LED estiver vermelho` chega tarde. Use `Se`, não `Caso`, `Na hipótese de`, `Em caso de`, e use sempre a mesma palavra.
- **`Apenas` ao lado do que limita.** `só`, `apenas`, `somente` mudam de sentido conforme a posição. `O administrador só pode apagar o arquivo` tem três leituras. Coloque `apenas` imediatamente antes da palavra que ele limita, e use uma só dessas três palavras no documento.
- **Sem gerúndio para encadear ou abrir frase.** Veja a tabela acima. `Sendo assim`, `Considerando que`, `Visando` também saem.
- **Sem abreviações.** `por exemplo`, não `ex.:`. `também`, não `tb`. `para`, não `p/`. `observação`, não `obs.:`. Em vez de `etc.`, liste os itens ou diga quantos são. Siglas consolidadas (`API`, `URL`, `CPF`) ficam, definidas uma vez se não forem de conhecimento geral.
- **Sem `(a)`, `(s)`, `x`, `@` para gênero ou número.** `o(s) arquivo(s) selecionado(s)` tem quatro leituras. Escolha uma (`os arquivos selecionados`) ou reestruture (`cada arquivo selecionado`). Para pessoas, use o substantivo genérico (`o usuário`) ou um termo neutro (`a pessoa usuária`, `quem usa`), com consistência.
- **Código, caminhos e rótulos de interface marcados.** Código e identificadores em crase (`` `config.yaml` ``). Rótulos de botão e menu em negrito ou entre aspas, com a grafia exata da tela (`Clique em **Salvar**`). Não traduza identificadores. Não conjugue verbos em inglês.
- **Números para máquina ler.** O padrão brasileiro é vírgula decimal (`1,5`) e ponto ou espaço de milhar (`1.500`). Um sistema treinado em inglês lê `1.500` como um e meio. Em texto que uma máquina interpreta, escreva `1500` ou `1 500`, e sempre com a unidade (`1500 registros`, `2,5 s`).
- **Homógrafos.** `para` (verbo/preposição), `se` (conjunção/pronome), `como` (interrogativo/comparação), `ainda` (ainda não/mesmo assim), `até` (até que/no máximo), `então` e `logo` (sequência/consequência). Quando as duas leituras cabem, troque a palavra: `interrompe`, `no máximo`, `até que`, `depois`, `por isso`.
- **Ortografia e variante.** Use o Acordo Ortográfico de 1990, em vigor no Brasil. Não misture português brasileiro e europeu (`arquivo`/`ficheiro`, `tela`/`ecrã`, `usuário`/`utilizador`, `está fazendo`/`está a fazer`). Se a fonte está em português europeu, mantenha e avise.
- **Concordância.** Depois de cada troca de pronome por substantivo, de passiva por ativa ou de gerúndio por frase, verifique gênero e número do artigo, do adjetivo e do verbo.

## 5. Modalidade: deve, pode, convém

O português concentra em dois verbos o que o inglês espalha em `must`, `shall`, `should`, `may`, `can`, `might`. As Diretivas ISO/IEC, que a ABNT adota, fixam um uso por forma. Esta skill segue esse uso:

| Sentido | Forma | Exemplo |
|---|---|---|
| Requisito (obrigação) | `deve` | "O arquivo deve existir antes do passo 3." |
| Recomendação | `convém que`, `recomenda-se` (só quando a fonte recomenda, não obriga) | "Convém que o backup seja diário." |
| Permissão | `pode` ou `tem permissão para` | "O administrador tem permissão para apagar o arquivo." |
| Capacidade | `consegue`, `é capaz de` | "O serviço consegue processar 100 requisições por segundo." |
| Possibilidade (ressalva) | `talvez`, `é possível que`, `provavelmente`, `pode ter` | "A requisição pode ter falhado." / "Talvez o proxy tenha bloqueado a conexão." |

Dois erros aparecem o tempo todo:

- **`deve` epistêmico.** `O serviço deve estar fora do ar` é suposição, não obrigação. Escreva `O serviço provavelmente está fora do ar`.
- **`pode` com três leituras.** `O usuário pode apagar o arquivo` cabe como permissão, capacidade e possibilidade. Escolha a leitura que a fonte quis e use a forma da tabela. Se a fonte é ambígua de verdade, mantenha `pode` e sinalize com `Mantido como está:`.

O que **não** é erro: `pode` seguido de infinitivo onde só a possibilidade cabe (`a requisição pode ter falhado`, `o timeout pode gerar artefatos parciais`, `os capacitores podem estar carregados`). Essa é a ressalva natural do português. Trocar cada uma por `talvez` deixa o texto artificial sem tirar nenhuma ambiguidade. Do mesmo modo, `pode` como permissão fica quando o contexto já exclui as outras leituras (`Você pode ligar o equipamento sem a tampa apenas para teste`).

Quando a regra dos tempos simples e a regra da modalidade entram em conflito, a modalidade vence. `Pode ter falhado` mantém um tempo composto porque apagar o auxiliar apagaria a dúvida junto.

## 6. O que o linter verifica

`scripts/ste-lint-ptbr.py` verifica só o que uma expressão regular encontra:

| Regra | Nível |
|---|---|
| `ponto-e-virgula`, `tamanho-da-frase` (> 30 palavras), `nominalizacao` (verbo-suporte + substantivo de ação listado), `marketing`, `burocrates` (lista fixa), `gerundismo`, `giria`, `abreviacao`, `parenteses-de-genero`, `rotacao-de-sinonimos`, `conjuncao-solta` | dura |
| `nominalizacao` (verbo-suporte + outra palavra), `burocrates` (conectivos ambíguos: `através de`, `caso`, `deverá`, `ao + infinitivo`), `o-mesmo`, `gerundio`, `forma-de-instrucao`, `voz-passiva`, `se-passivo`, `tempo-composto`, `cadeia-de-que` (3 ou mais `que` na frase), `etc`, `ponto-de-milhar` | consultiva |

Ele não verifica cadeias de `de`, homógrafos, pronome sem dono, sujeito oculto, posição de `apenas`, `pode` e `deve` ambíguos nem a regra do imperativo único. Isso precisa de análise sintática. Verifique à mão.

## 7. Fontes

- [ASD-STE100, site oficial](https://www.asd-ste100.org/)
- [ASD-STE100 — About STE](https://www.asd-ste100.org/about_STE.html)
- [ASD Europe — Simplified Technical English](https://www.asd-europe.org/standards-specifications/simplified-technical-english/)
- [Simplified Technical English — Wikipedia](https://en.wikipedia.org/wiki/Simplified_Technical_English)
- [Acordo Ortográfico da Língua Portuguesa de 1990 — Decreto 6.583/2008](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/decreto/d6583.htm)
- [Vocabulário Ortográfico da Língua Portuguesa (VOLP) — Academia Brasileira de Letras](https://www.academia.org.br/nossa-lingua/busca-no-vocabulario)
- [Diretivas ISO/IEC, Parte 2 — formas verbais para requisitos, recomendações e permissões](https://www.iso.org/sites/directives/current/part2/index.xhtml)
- [Manual de Redação da Presidência da República, 3ª edição (2018)](https://www4.planalto.gov.br/centrodeestudos/assuntos/manual-de-redacao-da-presidencia-da-republica/manual-de-redacao.pdf), sobre clareza, concisão e o uso do imperativo e das formas de tratamento
- [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill), a skill em inglês que este projeto adapta
- [g4lb/asd-ste100-hebrew-skill](https://github.com/g4lb/asd-ste100-hebrew-skill), a adaptação para o hebraico que serviu de modelo
