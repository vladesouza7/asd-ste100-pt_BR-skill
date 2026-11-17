---
name: asd-ste100-pt-br
description: "Use quando um texto em português do Brasil precisa ser interpretado sem um humano para resolver ambiguidade — descrições de ferramentas, mensagens de erro, instruções entre agentes, prompts de sistema, procedimentos, manuais técnicos, textos de interface — e uma leitura errada tem custo real, ou quando o texto está denso, burocrático, cheio de ressalvas ou fácil de interpretar errado. Gatilhos: simplifique este texto, português técnico simplificado, STE em português, ASD-STE100 pt-BR, reescreva para um agente não interpretar errado, tire a ambiguidade, linguagem controlada, texto técnico claro, reescreva este manual/procedimento/erro, simplify this Portuguese. Não use para texto criativo ou de marketing, nem para texto em inglês."
license: MIT
metadata:
  version: 0.2.0
---

# Português Técnico Simplificado (baseado na ASD-STE100)

A ASD-STE100 é uma norma de linguagem controlada para o inglês. A indústria aeroespacial e de defesa a criou para que técnicos de manutenção não lessem uma instrução de forma errada. A norma elimina as duas maiores fontes de leitura errada: palavras com mais de um sentido e frases com mais de uma estrutura possível.

Esta skill aplica a mesma disciplina ao **português do Brasil**. O português traz fontes próprias de ambiguidade. O sujeito some da frase. O pronome `seu` pode apontar para qualquer pessoa da frase. O verbo `poder` significa permissão, capacidade ou probabilidade. O `se` esconde quem age (`apaga-se o arquivo`). O gerúndio junta ações sem dizer a relação entre elas. O burocratês troca verbos por `realizar a verificação de`. Uma instrução aparece em quatro formas no mesmo documento (`Abra`, `Abrir`, `Deve-se abrir`, `Favor abrir`).

O leitor desta skill é, em primeiro lugar, um **agente de IA ou um sistema** que interpreta o texto sem ninguém para perguntar o que o autor quis dizer. Em segundo lugar, é um leitor humano de texto técnico, inclusive quem tem pouca familiaridade com a língua ou com o domínio.

A ASD-STE100 define apenas o inglês. Toda regra em português abaixo é uma adaptação desta skill, não uma norma oficial.

## Quando usar esta skill

- Um texto em português está denso, burocrático ou ambíguo. Exemplos: descrição de ferramenta, mensagem de erro, instrução entre agentes, prompt de sistema, procedimento, manual, texto de interface, mensagem de log.
- O texto vai para um agente, uma pipeline de tradução ou um leitor com pouco domínio do português, e uma leitura errada tem custo.
- O usuário quer uma tabela antes/depois que nomeie cada regra violada. A saída padrão é só o texto reescrito (veja Formato de saída).

Não use em texto criativo, de marketing ou persuasivo. O resultado desta skill é plano e literal por desenho. Não use em texto em inglês: a skill `asd-ste100` cobre o inglês.

## Dois modos

Escolha um modo antes de reescrever. Se o usuário não disser qual, deduza pelo tipo de texto. Mantenha a escolha interna, a menos que o usuário peça a tabela de regras.

**Estrito**: procedimentos, mensagens de erro, descrições de ferramentas e funções, instruções entre agentes, textos de segurança. Qualquer lugar onde uma leitura errada tem custo. Aplique todas as regras, inclusive os limites de tamanho, uma palavra para um sentido e o imperativo em toda instrução.

**Flexível**: READMEs, descrições de PR, changelogs, prosa explicativa. Aplique as regras estruturais por completo. Trate as regras lexicais (uma palavra para um sentido, uma classe gramatical por palavra) como orientação. Prosa precisa de alguma variação de vocabulário, e uma reescrita estrita de prosa troca a personalidade do texto em vez de esclarecê-lo.

## Fonte e escopo

As categorias de regras vêm da ASD-STE100 Issue 9 (janeiro de 2025): 53 regras de escrita em 9 seções e um dicionário de cerca de 900 palavras aprovadas em inglês. Esta skill não reproduz esse dicionário. A norma é gratuita para obter, mas não para redistribuir, e é em inglês de qualquer forma. A skill aplica o princípio: use a palavra mais simples e comum do português, e use-a sempre do mesmo jeito. O mapeamento completo e as fontes estão em `references/regras-de-escrita.md`. Uma tabela de substituições (burocratês, verbos anglicizados, conectivos) está em `references/substituicoes.md`.

## Regras de reescrita

As regras da STE se dividem em dois tipos. As **regras estruturais** descrevem a forma da frase e você as aplica a partir da descrição. As **regras lexicais** dependem de um dicionário de palavras aprovadas, que não existe para o português. Sem esse dicionário, elas viram uma preferência por palavras simples e consistentes. Aplique as estruturais com confiança. Aplique as lexicais como direção, e não sugira conformidade com um dicionário que você não tem.

### Regras estruturais — aplique sempre

<!-- ste-lint: off -->

| Regra | Faça | Não faça |
|---|---|---|
| Voz ativa, sujeito explícito | "O agente apaga o arquivo." | "O arquivo é apagado." / "Apaga-se o arquivo." / "Apagaram o arquivo." — a menos que quem age seja desconhecido ou irrelevante |
| Uma forma de instrução | Imperativo na forma "você", sempre: "Abra o arquivo. Leia a linha 3." | Misturar "Abra", "Abrir", "Deve-se abrir", "Favor abrir", "É necessário abrir", "Abre" |
| Uma instrução por frase | "Abra o arquivo. Leia a linha 3." | "Abra o arquivo e leia a linha 3, verificando então se ela confere." |
| Tamanho da frase | ≤ 25 palavras em instruções, ≤ 30 em descrições | Frases com orações encadeadas |
| Sem ponto e vírgula (Regra 8.1) | Frases separadas | Qualquer `;` |
| Cadeias de "de" | ≤ 3 substantivos ligados: "válvula da bomba de combustível" | "conjunto da válvula de entrada da bomba de combustível de alta pressão" — não se sabe o que é de alta pressão |
| Uma oração com "que" | "O arquivo que o agente criou está na pasta." | "O arquivo que o agente que iniciou o processo criou, que não está na pasta que..." |
| Sem gerúndio para encadear | "Abra o arquivo. Depois verifique a linha 3." / "Quando você clica em Salvar, o sistema fecha a janela." | "Abrindo o arquivo, verificando a linha 3..." / "Clicando em Salvar, o sistema fecha a janela." — a relação entre as ações (quando? se? porque?) fica implícita, e não se sabe quem clica |
| Sem gerundismo | "O sistema vai enviar o relatório." | "O sistema vai estar enviando o relatório." |
| Tempos simples | Presente, pretérito perfeito simples, futuro (simples ou "ir + infinitivo"), imperativo, infinitivo, particípio como adjetivo | "tem falhado", "havia sido processado", "está sendo enviado" — exceto quando a repetição ou o "neste momento" é informação |
| Sem palavras omitidas | "Apague o arquivo temporário." / "O sistema reinicia o serviço." | "Apagar arquivo temporário." (qual?) / "Reinicia o serviço." (quem?) |
| Pronome com um só dono | "O agente envia o arquivo ao usuário e apaga a cópia do agente." / "Puxe a tampa para trás e retire-a." (um só antecedente: o pronome serve) | "O agente envia o arquivo ao usuário e apaga sua cópia." — de quem? Repita o substantivo quando há dois donos possíveis, não em toda frase: "Puxe a tampa para retirar a tampa" é repetição sem ganho |
| Mantenha a modalidade | "A requisição pode ter falhado." fica assim | "A requisição falhou." — uma ressalva virou um fato |
| Uma ressalva por afirmação incerta | "Talvez a conexão tenha falhado. Talvez a causa seja o proxy." | "A conexão pode ter falhado por causa do proxy." — a fonte duvidava das duas coisas |
| Condição antes da instrução | "Se o LED estiver vermelho, não abra o painel." | "Não abra o painel se o LED estiver vermelho." — o leitor age antes de chegar à condição |
| "Apenas" ao lado do que limita | "Apenas o administrador apaga o arquivo." / "O administrador apaga apenas o arquivo." | "O administrador só pode apagar o arquivo." — só ele? só apagar? só o arquivo? |
| Código e identificadores em crase | "Edite `config.yaml`. Clique em **Salvar**." | Nome de arquivo solto no texto, verbo em inglês conjugado |
| Sem abreviações | "por exemplo", "e também", "observação" | "ex.:", "tb", "p/", "c/", "vc", "obs.:", "etc." — liste os itens |
| Sem "(a)" e "(s)" | "Apague os arquivos selecionados." ou "Apague o arquivo selecionado." | "Apague o(s) arquivo(s) selecionado(s)." / "o(a) usuário(a)" — qual leitura vale? |
| Parágrafos e listas | Um tema por parágrafo, ≤ 6 frases. Uma lista para 3 ou mais passos ou condições | Uma sequência escondida dentro de uma frase |

<!-- ste-lint: on -->

### Regras lexicais — direção, não norma

<!-- ste-lint: off -->

| Regra | Faça | Não faça |
|---|---|---|
| Uma palavra, um sentido | Sempre "verificar" para uma ação | Alternar "verificar", "checar", "conferir", "validar" para a mesma ação |
| Verbo, não substantivo (Regra 3.7) | "Verifique o log." / "Instale o pacote." | "Realize a verificação do log." / "Efetue a instalação do pacote." / "Proceda à análise." |
| "Deve" só para obrigação | "O arquivo deve existir." (requisito) / "O serviço provavelmente está fora do ar." (probabilidade) | "O serviço deve estar fora do ar." — obrigação ou suposição? |
| "Pode" sem dupla leitura | "A requisição pode ter falhado." (só cabe possibilidade: fica) / Permissão: "O usuário pode apagar o arquivo. O operador não pode." / Capacidade: "O serviço consegue processar 100 requisições." | "O usuário pode apagar o arquivo." sozinho, quando permissão, capacidade e possibilidade cabem ao mesmo tempo — aí troque pela forma que a fonte quis. Não troque todo "pode" por "talvez": "pode" é a ressalva natural do português |
| Sem burocratês | "para", "sobre", "por", "porque", "por isso" | "a fim de", "no que tange a", "em virtude de", "visando", "outrossim", "destarte", "haja vista", "o mesmo" como pronome |
| Sem gíria e verbo anglicizado | "implantar", "configurar", "registrar", "mesclar", "depurar", "enviar" | "deployar", "setar", "logar", "mergear", "debugar", "comitar", "dar um jeito", "subir o serviço" |
| Homógrafos | "O comando interrompe o serviço." / "Pare o serviço." | "O comando para o serviço." — "para" é verbo ou preposição? |
| Termos de domínio | Mantenha o termo técnico necessário. Defina-o uma vez se não for português comum. Um anglicismo consolidado fica como substantivo (`deploy`, `commit`), nunca conjugado | Jargão que nunca é definido |

<!-- ste-lint: on -->

## Lista de verificação

Procure estes dez hábitos antes de reescrever qualquer coisa. Cada um é mecânico: você aponta a palavra ou o sinal que quebra a regra.

1. **Rotação de sinônimos**: uma coisa com vários nomes (`o usuário`, `o cliente`, `o operador`). Escolha um nome.
2. **Ressalvas e enchimento**: `vale ressaltar que`, `é importante destacar que`, `cabe salientar`, `talvez possa eventualmente`. Afirme ou apague. Mantenha uma ressalva honesta por afirmação incerta.
3. **Nominalização**: `realizar`, `efetuar`, `proceder a`, `fazer`, `executar`, `promover`, `dar` + substantivo de ação. Use o verbo.
4. **Palavras de marketing**: `robusto`, `poderoso`, `inovador`, `intuitivo`, `de ponta`, `sem esforço`, `de forma fluida`. Apague, ou dê a medida que sustenta a afirmação.
5. **Frases-rio**: ponto e vírgula, cadeias de `que`, de `e`, de gerúndios. Uma ideia por frase.
6. **Gíria e verbo anglicizado**: `deployar`, `setar`, `bugou`, `subir`, `derrubar`. Use o verbo padrão do português.
7. **Passiva e sujeito escondido**: `é apagado`, `apaga-se`, `apagaram`, `foi configurado`. Diga quem age.
8. **Formas de instrução misturadas**: imperativo, infinitivo, `deve-se`, `favor`, `é necessário` lado a lado. Use o imperativo.
9. **Pronomes sem dono**: `seu`, `sua`, `ele`, `ela`, `o mesmo`, `este`, `esse` com dois antecedentes possíveis. Repita o substantivo.
10. **Gerúndio**: `vai estar enviando`, `clicando em Salvar`, `sendo assim`. Troque por tempo simples ou por `quando`, `se`, `depois de`.

## Processo

1. Escolha o modo. Diga qual só quando o usuário pedir a tabela de regras.
2. Leia o texto inteiro uma vez para entender o sentido. Não reescreva antes de saber o que o texto ainda precisa dizer depois.
3. Percorra frase por frase. Marque cada violação das tabelas e cada item da lista de verificação. No modo Flexível, marque as regras lexicais mas não as imponha. Para uma primeira passada mecânica, rode `python3 <diretório desta skill>/scripts/ste-lint-ptbr.py` (arquivos ou stdin, `--json` para saída estruturada). Suas regras duras são: ponto e vírgula, tamanho de frase, nominalização, palavras de marketing, burocratês, gerundismo, gíria e verbos anglicizados, abreviações, "(a)" e "(s)", rotação de sinônimos. Também marca conjunção solta no fim de item de lista. Seus achados consultivos são voz passiva, "se" passivo, tempo composto, gerúndio, cadeia de "que", forma indireta de instrução, "o mesmo" e "etc.". Ele nunca marca ressalvas. Ele não verifica cadeias de "de", homógrafos, pronome sem dono, sujeito omitido nem "pode" e "deve" ambíguos. Verifique esses à mão.
4. Reescreva cada frase marcada e preserve o sentido com exatidão. Se a reescrita perder precisão necessária, mantenha a forma mais longa e sinalize. Precisão necessária inclui uma condição de segurança, um qualificador de escopo e um número.
   - **Prefira a forma natural que ainda é inequívoca.** Esta skill tira ambiguidade, não naturalidade. "Pode ter falhado" e "pode gerar artefatos parciais" são ressalvas claras: deixe assim. Reserve "talvez" para quando "pode" também leria como permissão. "Você pode ligar o equipamento sem a tampa apenas para teste" é permissão clara pelo contexto: não precisa virar "tem permissão para". Um texto que soa como tradução literal faz o leitor desconfiar do sentido.
   - **Verifique a modalidade antes de fechar a reescrita.** `pode`, `talvez`, `possivelmente`, `provavelmente`, `é possível que`, `às vezes`, e verbos de tentativa como `tenta` e `vai tentar` carregam a confiança do autor, e confiança é conteúdo. Conte as afirmações incertas na fonte. Mantenha uma ressalva para cada uma, mesmo quando dividir ou juntar frases. Uma frase mais curta que transforma ressalva em fato é uma afirmação diferente, não uma simplificação. Esse é o jeito mais comum de uma reescrita STE bem-intencionada dar errado, porque as ressalvas são exatamente o que um limite de tamanho tenta cortar.
   - **Declare a leitura que você escolheu.** Às vezes a fonte tem duas leituras e o contexto não decide: `seu` com dois donos possíveis, `para` verbo ou preposição, `a mesma` com dois antecedentes. A reescrita precisa escolher uma, porque a meta é tirar a ambiguidade. Mas escolher em silêncio esconde uma decisão de negócio dentro de uma reescrita de forma. Escreva a leitura mais provável e registre a escolha na linha `Leitura escolhida:` (veja Formato de saída). Quando o contexto decide, não há o que declarar.
   - Nunca acrescente um fato que a fonte não afirmou. Uma reescrita que lê melhor porque inventou uma causa, uma frequência ou um mecanismo deixou de ser reescrita.
   - Mantenha a concordância de gênero e número correta depois de cada mudança. Quando trocar um pronome pelo substantivo, verifique o artigo e o adjetivo.
   - Mantenha a variante. Se a entrada está em português europeu (`ficheiro`, `ecrã`, `utilizador`, `estar a fazer`), diga isso e não misture variantes. Converta para pt-BR só se o usuário pedir.
   - Mantenha a ortografia do Acordo Ortográfico de 1990, que vale no Brasil.
5. Produza o texto reescrito (veja Formato de saída).
6. Se a entrada já está conforme, diga isso. Não force mudanças em texto que já cumpre as regras.

## Formato de saída

**Padrão: o texto reescrito, e nada mais.** Quem chama esta skill quase sempre quer um resultado para colar direto em uma descrição de ferramenta, uma mensagem de erro ou um prompt. Sem preâmbulo, sem anúncio de modo, sem contagem de violações, sem resumo das mudanças, sem tabela de regras, sem oferta de explicar mais.

Há duas adições permitidas, depois do texto, uma linha cada:

- `Mantido como está:` quando o passo 4 manteve uma forma mais longa de propósito. A linha nomeia o trecho e a precisão que uma versão mais curta perderia.
- `Leitura escolhida:` quando a fonte tinha duas leituras e o contexto não decidia. A linha cita o trecho original e a leitura usada, por exemplo: `Leitura escolhida: "seu e-mail" = e-mail do solicitante. "para o serviço" = interrompe o serviço.` Assim quem colou o texto confirma a decisão antes de usá-lo.

Não use essas linhas para explicar uma ressalva mantida ou uma regra aplicada. Omita cada linha quando não há o que relatar.

**A pedido: a tabela de regras.** Exemplos de pedido: "mostre o diff", "quais regras ele quebrou", "explique as mudanças", "antes/depois", "mostre a tabela". Para esses pedidos, produza isto no lugar:

```markdown
<!-- ste-lint: off -->

| Regra violada | Original | Simplificado |
|---|---|---|
| Nominalização | "Realize a verificação do log." | "Verifique o log." |
| Voz passiva | "O arquivo é apagado." | "O agente apaga o arquivo." |

<!-- ste-lint: on -->

Modo: Estrito. 2 violações encontradas.
```

Depois da tabela, acrescente uma linha sobre qualquer coisa que você **não** simplificou de propósito, e por quê. Em geral: simplificar perderia precisão necessária.

## Limites

**Faz:**
- Reescreve português denso ou ambíguo em frases curtas, ativas, com sujeito explícito e uma palavra para cada sentido.
- Devolve só o texto reescrito por padrão, e nomeia as regras quando o usuário pede.
- Preserva cada fato, condição, qualificador de escopo e grau de certeza do original.
- Sugere uma entrada de glossário de uma linha para um termo técnico que precisa ficar.

**Não faz:**
- Não afirma conformidade oficial com a STE. Não existe STE oficial em português.
- Não reescreve texto em inglês. Use `asd-ste100` para inglês.
- Não simplifica texto criativo, de marketing ou persuasivo.
- Não apaga uma condição de segurança, uma exceção ou um qualificador de escopo para encurtar uma frase.
- Não transforma "a requisição pode ter falhado" em "a requisição falhou".
- Não torna conteúdo vazio útil. A STE corrige a forma do texto, não a substância. Um parágrafo oco vira um parágrafo oco, curto e limpo. Diga isso em vez de polir.
- Não encurta além do ponto de clareza. Cortar palavras não é a meta. Eliminar ambiguidade é a meta. Pare quando a frase não tem duas leituras, não quando ela é a mais curta possível.

## Recursos adicionais

- **`references/regras-de-escrita.md`**: o mapeamento completo da STE para o português, com o que muda, por que muda e as fontes.
- **`references/substituicoes.md`**: tabelas de substituição para burocratês, verbos anglicizados, conectivos, modalidade e homógrafos.
- **`examples/antes-depois.md`**: as regras da STE mostradas em português e quatro exemplos de saída de agente, com a análise de cada um.
- **`scripts/ste-lint-ptbr.py`**: linter determinístico que usa só a biblioteca padrão do Python. Sai com código 1 quando as violações duras passam de `--baseline` (padrão 0). Achados consultivos nunca falham a execução. `--disable regra1,regra2` silencia regras. `--selftest` garante que "a requisição pode ter falhado" passa limpo. Para texto no modo Flexível, use `--disable rotacao-de-sinonimos`. O linter pula código, front matter YAML e o trecho entre `<!-- ste-lint: off -->` e `<!-- ste-lint: on -->`.
