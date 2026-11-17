# Exemplos antes / depois

## Parte 1 — Regras da STE, mostradas em português

A ASD-STE100 define apenas o inglês. Estas linhas mostram como cada regra passa para o português. São ilustrações, não citações da norma.

<!-- ste-lint: off -->

| Regra | Antes | Depois | Por quê |
|---|---|---|---|
| Uma palavra, um sentido | "Verifique o sistema." / "Cheque as conexões." / "Confira o recibo." | "Verifique o sistema. Verifique as conexões. Verifique o recibo." | Três quase-sinônimos fazem o leitor adivinhar se são uma ação ou três. |
| Uma classe gramatical por palavra | "O comando para o serviço." | "O comando interrompe o serviço." | Depois do Acordo de 1990, `para` (verbo) é igual a `para` (preposição). |
| Verbo, não substantivo (Regra 3.7) | "Realize a verificação do filtro." | "Verifique o filtro." | `Realizar` não carrega sentido. A ação está escondida no substantivo. |
| Sem gíria nem anglicismo conjugado (substitui a Regra 9.3) | "Suba o serviço e depois deploya a nova versão." | "Inicie o serviço. Depois implante a nova versão." | O sentido de `subir` e `deployar` não vem das palavras, e a grafia não é fixa. |
| Voz ativa | "O arquivo é apagado." / "Apaga-se o arquivo." | "O agente apaga o arquivo." | As duas formas escondem quem age. |
| Uma forma de instrução | "Abra o arquivo. Deve-se ler a linha 3. Favor verificar a saída." | "Abra o arquivo. Leia a linha 3. Verifique a saída." | Uma forma, o imperativo na forma `você`, que é neutro em gênero. |
| Só tempos simples | "Temos recebido os relatórios técnicos da matriz." | "Recebemos os relatórios técnicos da matriz." | O pretérito composto diz "repetidamente". Se a fonte quis dizer um fato concluído, o simples é o certo. |
| Sem gerundismo | "O sistema vai estar enviando o relatório às 8h." | "O sistema vai enviar o relatório às 8h." | O `estar + -ndo` não acrescenta nada. |
| Sem gerúndio encadeando | "Clicando em Salvar, o sistema fecha a janela." | "Quando você clica em **Salvar**, o sistema fecha a janela." | O gerúndio não diz quem clica nem qual é a relação entre as ações. |
| Sem palavras omitidas | "Apagar arquivo temporário." | "Apague o arquivo temporário." | Sem o artigo, não se sabe se é um arquivo específico ou qualquer um. |
| Pronome com um só dono | "O agente envia o arquivo ao usuário e apaga sua cópia." | "O agente envia o arquivo ao usuário e apaga a cópia do agente." | `Sua` cabe para o agente e para o usuário. |
| Condição antes da instrução | "Não abra o painel se o LED estiver vermelho." | "Se o LED estiver vermelho, não abra o painel." | O leitor que age frase a frase precisa da condição primeiro. |
| `Apenas` ao lado do que limita | "O administrador só pode apagar o arquivo." | "Apenas o administrador apaga o arquivo." (ou: "O administrador apaga apenas o arquivo.") | Três leituras na frase original. |
| Sem abreviações | "Salve o arquivo (ex.: `relatorio.pdf`) p/ a pasta de saída, tb o log etc." | "Salve o arquivo, por exemplo `relatorio.pdf`, na pasta de saída. Salve também o log." | Uma abreviação pode valer por mais de uma expressão, e `etc.` esconde itens. |
| Sem `(a)` e `(s)` | "Apague o(s) arquivo(s) selecionado(s)." | "Apague os arquivos selecionados." | Quatro leituras viram uma. |
| Cadeia de "de" | "Verifique o conjunto da válvula de entrada da bomba de combustível de alta pressão." | "Verifique a válvula de entrada da bomba de combustível. Essa bomba é de alta pressão." | Com quatro `de`, não se sabe o que é de alta pressão. |

<!-- ste-lint: on -->

## Parte 2 — Aplicado a saída de agente

Estes são exemplos originais para o caso de uso desta skill: reescrever saída de agente de IA para que outro agente, uma camada de tradução ou um leitor com pouco domínio da língua interprete sem ambiguidade. As contagens de palavras são de tokens separados por espaço.

### Exemplo A — Descrição de ferramenta (Estrito)

<!-- ste-lint: off -->

**Antes:**

> Esta ferramenta irá tentar realizar a sincronização do estado entre os diversos backends que tenham sido configurados, e caso seja detectado algum conflito, o mesmo poderá ser resolvido automaticamente conforme a estratégia que tiver sido definida; do contrário, o conflito será apresentado para revisão manual.

**Violações marcadas:**
- Nominalização: "realizar a sincronização".
- Passivas e sujeito escondido: "seja detectado", "poderá ser resolvido", "será apresentado", "tenham sido configurados", "tiver sido definida".
- "O mesmo" como pronome.
- "Caso" em vez de "se". Ponto e vírgula. 44 palavras em uma frase.

Não marcado: "irá tentar" e "poderá ser resolvido". São ressalvas. A ferramenta não promete sucesso, e a reescrita também não pode prometer.

<!-- ste-lint: on -->

**Depois:**

> A ferramenta tenta sincronizar o estado entre os backends configurados. Se a ferramenta encontra um conflito, ela lê a estratégia configurada. Se a estratégia permite resolução automática, a ferramenta pode resolver o conflito sem um usuário. Se a ferramenta não resolve o conflito, ela apresenta o conflito para revisão manual.

"Que tenham sido configurados" virou o adjetivo "configurados". A STE permite particípio usado como adjetivo. A fonte não diz quem configurou os backends, então a reescrita não inventa um agente. "Do contrário" virou uma condição explícita, sobre o conflito não resolvido, e não sobre o que a estratégia permite.

### Exemplo B — Mensagem de erro (Estrito)

<!-- ste-lint: off -->

**Antes:**

> Pode ter ocorrido um erro durante o processamento da sua requisição em virtude de uma possível incompatibilidade no formato dos dados esperado, a qual pode ter sido ocasionada por uma versão desatualizada do cliente.

**Violações marcadas:**
- Uma frase com três afirmações (um erro, uma incompatibilidade de formato, uma versão de cliente).
- Burocratês: "em virtude de", "ocasionada", "a qual".
- Nominalização: "o processamento da sua requisição".
- 36 palavras.

Não marcado: "pode ter ocorrido" e "pode ter sido ocasionada". A mensagem vem de um sistema que não sabe o que deu errado. As duas ressalvas relatam essa ignorância com honestidade.

<!-- ste-lint: on -->

**Depois:**

> Sua requisição pode ter falhado. A causa pode ser um formato de dados diferente do que o servidor espera. Uma versão desatualizada do cliente pode causar essa diferença. Verifique a versão do seu cliente.

**Este exemplo é a razão de existir da regra de modalidade.** Uma versão anterior deste arquivo reescreveu a primeira frase como "A requisição falhou", e a terceira como "a causa mais comum é uma versão desatualizada do cliente". As duas leem melhor. As duas estão erradas: a primeira afirma uma falha que o sistema só suspeita, e a segunda inventa uma frequência que não aparece na fonte.

Note também que "pode ter falhado" mantém um tempo composto que a regra dos tempos simples apagaria. **Quando a regra de tempo e a regra de modalidade entram em conflito, a modalidade vence.** Tirar o auxiliar aqui apagaria a dúvida junto com o tempo.

"Sua requisição" e "seu cliente" ficaram: na mensagem de erro, só existe um dono possível, o leitor.

### Exemplo C — Instrução entre agentes (Estrito)

<!-- ste-lint: off -->

**Antes:**

> Uma vez que o job upstream tenha sido concluído e assumindo que nenhum erro tenha sido levantado, o agente downstream deverá proceder ao consumo do artefato de saída, sendo importante ressaltar que artefatos parciais são por vezes gerados em condições de timeout.

**Violações marcadas:**
- Tempos compostos e passivas: "tenha sido concluído", "tenha sido levantado", "são gerados".
- Gerúndios encadeando: "assumindo que", "sendo importante ressaltar que".
- "Uma vez que" (causa ou tempo?). "Deverá". "Proceder ao consumo". "Por vezes". "Assumindo" no sentido inglês de "supondo".
- Uma frase, três fatos (condição de conclusão, próxima ação, aviso de caso-limite). 42 palavras.

<!-- ste-lint: on -->

**Depois:**

> Espere o job upstream terminar sem erros. Depois leia o artefato de saída. Atenção: um timeout pode gerar um artefato parcial. Verifique se o artefato está completo antes de usá-lo.

Duas decisões que vale declarar em vez de esconder:
- "Deverá proceder ao consumo" virou o imperativo "leia". A STE permite isso em instruções: uma recomendação dirigida ao agente que executa é um comando. Não faça o mesmo em texto descritivo.
- A última frase é **nova**. A fonte avisava sobre artefatos parciais sem dizer o que fazer. Acrescentar a verificação torna o aviso acionável, mas é conteúdo acrescentado, por isso está declarado aqui e não disfarçado de reescrita. Se o silêncio da fonte foi proposital, apague a frase.

"Job", "upstream", "downstream" e "timeout" ficaram como substantivos: são os termos que o time usa, e trocá-los criaria um nome novo para a mesma coisa. Uma entrada de glossário resolve: "timeout: tempo máximo de espera, depois do qual a operação é cancelada".

### Exemplo D — Prosa de README (Flexível)

<!-- ste-lint: off -->

**Antes:**

> Nossa camada de cache foi projetada para se integrar de forma fluida à sua stack existente, com o mínimo de atrito e sem lock-in de fornecedor; ela se vale de similaridade semântica para reduzir drasticamente os cache misses que tradicionalmente assolam cargas de trabalho de LLM.

**Violações marcadas:**
- Palavras de marketing e afirmações sem medida: "de forma fluida", "mínimo de atrito", "drasticamente".
- Ponto e vírgula unindo duas ideias.
- "Se vale de", "assolam": vocabulário raro onde o comum serve.
- 44 palavras.

<!-- ste-lint: on -->

**Depois:**

> Projetamos nossa camada de cache para funcionar com a sua stack atual, sem lock-in de fornecedor. Ela usa similaridade semântica para reduzir os cache misses, um problema antigo em cargas de trabalho de LLM.

O modo Flexível não forçou um termo fixo por conceito. Mesmo assim, cortou as palavras de marketing, o ponto e vírgula e o tamanho. Manteve "projetamos para", porque a fonte declara uma meta de projeto, não um resultado.

Uma versão anterior deste arquivo acrescentou dois fatos: que um cache comum compara requisições por texto exato, e que este cache não guarda dados fora da stack. A fonte não diz nenhum dos dois. Uma reescrita que acrescenta um fato deixou de ser reescrita.

### Exemplo E — Procedimento de manutenção (Estrito)

<!-- ste-lint: off -->

**Antes:**

> Antes de dar início à manutenção, deve-se desligar o equipamento, sendo que o técnico não deverá abrir o painel caso o LED indicador esteja vermelho, pois o mesmo indica que o capacitor ainda pode estar carregado; favor aguardar aprox. 5 min. e realizar nova verificação do(s) LED(s).

**Violações marcadas:**
- Quatro formas de instrução: "deve-se", "não deverá", "favor aguardar", "realizar".
- Condição de segurança ("caso o LED esteja vermelho") depois da ação que ela proíbe.
- "O mesmo" como pronome, "sendo que", "dar início a", "realizar nova verificação", "aprox.", "min.", "do(s) LED(s)".
- Ponto e vírgula. 49 palavras.

Não marcado: "ainda pode estar carregado". É uma ressalva sobre o estado do capacitor, e o texto reescrito a mantém.

<!-- ste-lint: on -->

**Depois:**

> 1. Desligue o equipamento.
> 2. Olhe o LED indicador.
> 3. Se o LED estiver vermelho, não abra o painel. O LED vermelho indica que o capacitor ainda pode estar carregado. Espere cerca de 5 minutos. Depois volte ao passo 2.
> 4. Se o LED estiver apagado, abra o painel.
>
> Mantido como está: "cerca de 5 minutos". A fonte diz "aprox. 5 min.", e um tempo exato seria um fato novo.

A lista numerada substitui a sequência escondida na frase. A condição de segurança vem antes do verbo que ela proíbe. "Do(s) LED(s)" virou "o LED": o texto fala de um LED indicador. Se o equipamento tem vários, a fonte precisa dizer quantos.

## Como ler estes exemplos

A Parte 1 mostra as regras em que esta skill se baseia. A Parte 2 mostra a transferência: a mesma disciplina, um sentido por palavra, voz ativa, tempo simples, uma instrução por frase, condição explícita antes da ação, torna texto de máquina para máquina e texto para leitor com pouco domínio da língua mais seguro de interpretar, não só manuais de aeronave.
