# Tabelas de substituição

Consulte este arquivo quando uma frase marcada precisar de uma palavra mais simples e você quiser a troca padrão. As tabelas cobrem burocratês, verbos anglicizados, conectivos, enchimento, modalidade e homógrafos. Elas são orientação, não dicionário aprovado: a STE em português não tem um.

## Sumário

1. Burocratês e juridiquês
2. Verbos-suporte (nominalização)
3. Verbos anglicizados e gíria de TI
4. Conectivos e condições
5. Enchimento e ressalvas vazias
6. Modalidade
7. Homógrafos e palavras de dupla leitura
8. Abreviações

## 1. Burocratês e juridiquês

| Evite | Use |
|---|---|
| a fim de, com vistas a, no sentido de, de modo a, de forma a, visando | para |
| no que tange a, no tocante a, no que diz respeito a, relativamente a | sobre |
| em virtude de, em razão de, em face de, face a, haja vista, tendo em vista | por causa de, porque |
| por conseguinte, destarte, dessa forma, sendo assim, isto posto, ante o exposto | por isso |
| outrossim, ademais | também |
| através de (como meio) | por, com, pelo |
| mediante | com, por meio de |
| junto a, junto ao (como destino) | a, ao, no |
| por parte de | de, pelo |
| a nível de, em nível de | em, no |
| no âmbito de | em, dentro de |
| na medida em que | porque |
| sob pena de | se não, caso contrário (ou diga a consequência) |
| supracitado, supramencionado, retromencionado, referido, em questão, em tela, em epígrafe, dito | repita o substantivo |
| o mesmo, a mesma (como pronome) | repita o substantivo |
| trata-se de | é |
| faz-se necessário | é necessário (em descrição) / imperativo (em instrução) |
| levar a efeito, levar a cabo | fazer, concluir |
| possui, dispõe de | tem |
| encontra-se | está |
| visa, objetiva, tem como objetivo | serve para, faz |
| ora | (apague) |

## 2. Verbos-suporte (nominalização)

O verbo-suporte não carrega sentido. Use o verbo da ação.

| Evite | Use |
|---|---|
| realizar / efetuar / fazer a verificação de | verificar |
| realizar / efetuar a instalação de | instalar |
| proceder à análise de | analisar |
| efetuar a configuração de | configurar |
| realizar a atualização de | atualizar |
| efetuar o envio de | enviar |
| realizar a leitura de | ler |
| fazer a gravação de | gravar |
| efetuar a remoção / exclusão de | apagar (ou excluir, um só) |
| realizar o teste de | testar |
| dar início a | iniciar |
| dar continuidade / andamento / prosseguimento a | continuar |
| dar entrada em | registrar |
| dar baixa em | baixar, cancelar (diga qual) |
| dar suporte a | atender, ajudar |
| fazer uso de | usar |
| efetuar o pagamento | pagar |
| realizar a cópia de | copiar |
| fazer a limpeza de | limpar |
| fazer a montagem de | montar |
| realizar a inspeção de | inspecionar |
| fazer a substituição de | substituir |
| ter como objetivo | servir para |

Quando o substantivo não tem verbo em português (`fazer login`, `fazer backup`, `fazer o deploy`), mantenha a locução e registre o termo no glossário, ou use o verbo português se o time o aceita (`entrar`, `copiar`, `implantar`).

## 3. Verbos anglicizados e gíria de TI

| Evite | Use |
|---|---|
| deployar, fazer o deploy, subir (o serviço, a versão) | implantar, publicar |
| derrubar (o servidor) | desligar, parar (diga qual) |
| setar | definir, configurar |
| logar, fazer login | entrar, autenticar-se |
| deslogar | sair |
| comitar, fazer commit | registrar (ou mantenha `commit` como substantivo no glossário) |
| mergear, fazer merge | mesclar |
| debugar | depurar |
| bugar, bugou, deu pau, deu ruim, crashou | falhar, parar |
| printar, tirar print | capturar a tela, imprimir (diga qual) |
| startar, bootar | iniciar |
| restartar, resetar | reiniciar, redefinir (diga qual) |
| upar, fazer upload | enviar |
| baixar, fazer download | baixar (um só) |
| mockar | simular |
| buildar, fazer o build | compilar, gerar |
| linkar | vincular, ligar |
| dropar | descartar, apagar |
| forkar | bifurcar, copiar o repositório |
| pushar, pullar | enviar, trazer |
| flagar | marcar |
| zipar | compactar |
| performar | executar, ter desempenho |
| attachar | anexar |
| rodar | executar (em texto estrito) |
| estourar (memória, limite) | exceder, ultrapassar |
| dar um jeito, quebrar o galho | corrigir, resolver |
| ficar de olho | monitorar |
| correr atrás | obter, buscar (um só) |
| no automático, na mão | de forma automática, de forma manual |

Anglicismos consolidados que ficam como substantivo, com glossário: `deploy`, `commit`, `merge`, `build`, `backup`, `login`, `log`, `cache`, `token`, `bug`, `rollback`, `upload`, `download`, `pull request`, `branch`.

## 4. Conectivos e condições

| Evite | Use | Por quê |
|---|---|---|
| caso, em caso de, na hipótese de, desde que, contanto que | se | Uma palavra para condição no documento todo. |
| a menos que, a não ser que, salvo se, exceto se | Inverta: "Se X, não faça Y." | Condição negativa lida de trás para a frente. |
| ao + infinitivo (ao clicar, ao receber) | quando, depois de, assim que | "Ao" não diz se é "no momento em que", "depois que" ou "por meio de", e não diz quem age. |
| então, logo (ambíguos) | depois (sequência) / por isso (consequência) | As duas leituras cabem com frequência. |
| até (quantidade) | no máximo | "Aguarde até 30 segundos" vs "até o serviço iniciar". |
| até (tempo) | até que | Mesma razão. |
| enquanto | durante (tempo) / já (contraste) | "Enquanto o serviço processa" vs "enquanto o outro falha". |
| uma vez que | porque (causa) / depois que (tempo) | Duas leituras. |
| após, posteriormente | depois de, depois | Uma palavra para sequência. |
| anteriormente, previamente | antes, antes de | Mesma razão. |
| bem como, assim como | e | Enchimento. |
| ou seja, isto é | (apague, ou diga o conteúdo direto) | Se precisou de "ou seja", a primeira versão não serviu. |
| e/ou | "X, Y ou os dois" | Diga as três possibilidades. |
| respectivamente | repita os pares | O leitor precisa refazer a conta. |

## 5. Enchimento e ressalvas vazias

Saem inteiros. Se a frase que sobra não diz nada, a frase inteira sai.

- vale ressaltar que, vale destacar que, vale lembrar que, vale frisar que
- é importante ressaltar / destacar / notar / mencionar / salientar que
- cabe salientar / ressaltar / destacar / mencionar que
- cumpre informar / salientar / ressaltar que
- ressalte-se, registre-se, frise-se, insta salientar
- convém notar, observe-se que
- de certa forma, de certo modo, em certa medida, meio que, tipo assim
- basicamente, essencialmente, simplesmente, literalmente
- eventualmente (no sentido de "talvez": use `talvez`; no sentido de "ocasionalmente": use `às vezes`)
- a princípio (no sentido de "em princípio" ou "por enquanto": diga qual)

Ressalvas que **ficam**, porque são conteúdo: `pode`, `talvez`, `provavelmente`, `possivelmente`, `é possível que`, `às vezes`, `em alguns casos`, `tenta`, `vai tentar`, `estimado`, `aproximadamente` com número.

## 6. Modalidade

| Sentido na fonte | Escreva |
|---|---|
| Obrigação, requisito | deve, é obrigatório (em descrição) / imperativo (em instrução) |
| Proibição | não deve, é proibido / "Não" + imperativo |
| Recomendação | convém que, recomenda-se (não transforme em obrigação) |
| Permissão | pode (quando o contexto exclui possibilidade e capacidade), tem permissão para (só se a dupla leitura persistir) |
| Capacidade | consegue, é capaz de |
| Possibilidade | pode + infinitivo (a forma natural: pode falhar, pode ter falhado), talvez, é possível que |
| Probabilidade alta | provavelmente |
| Suposição ("deve estar") | provavelmente está |
| Tentativa sem garantia | tenta, vai tentar |

## 7. Homógrafos e palavras de dupla leitura

| Palavra | Leituras | Saída |
|---|---|---|
| para | preposição / verbo parar (3ª pessoa) | interrompe, encerra; ou imperativo `Pare` |
| se | se (condição) / se (pronome) | condição: mantenha. Pronome passivo: diga quem age. |
| como | de que modo / assim como / porque | "de que modo", "igual a", "porque" |
| ainda | até agora / mesmo assim / além disso | "até agora", "mesmo assim", "também" |
| até | limite de tempo / limite de quantidade / inclusive | "até que", "no máximo", "inclusive" |
| então, logo | depois / por isso | "depois", "por isso" |
| pode, deve | veja a seção 6 | |
| só, apenas, somente | depende da posição | `apenas` colado à palavra que limita |
| seu, sua | de você / dele / dela / deles | repita o dono, ou "de você" |
| este, esse, aquele, o mesmo, o referido | antecedente incerto | repita o substantivo |
| certo | correto / determinado | "correto", "um" |
| atual | de agora / real (anglicismo) | "de agora" |
| eventual | que talvez aconteça / ocasional | "possível", "ocasional" |
| assumir | tomar para si / supor (anglicismo) | "assumir" só no primeiro sentido; "supor" no segundo |
| suportar | aguentar / dar suporte (anglicismo) | "aguentar" / "oferecer", "aceitar", "funcionar com" |
| realizar | fazer / perceber (anglicismo) | "fazer" (ou o verbo da ação) / "perceber" |
| aplicação | ato de aplicar / programa | "aplicativo", "programa", "sistema" (um só) |
| atender | responder / cumprir | "responder a", "cumprir" |
| passar | transmitir / decorrer / aplicar | "enviar", "decorrer", "aplicar" |

## 8. Abreviações

| Evite | Use |
|---|---|
| ex.:, p. ex., e.g. | por exemplo |
| i.e. | isto é (ou reescreva) |
| etc., e outros, e afins | liste os itens, ou "e outros N itens" |
| obs.:, obs: | observação: |
| p/, c/, s/ | para, com, sem |
| tb, tbm | também |
| vc, vcs | você, vocês |
| pq | porque, por que (diga qual) |
| qdo, qq, qqr | quando, qualquer |
| msg | mensagem |
| cfg, conf | configuração |
| aprox. | cerca de |
| nº, n°, num. | número |
| V.Sa., V.Exa. | você |
| Sr., Sra., Dr. | (apague em texto técnico) |
| art., inc., par., fls. | artigo, inciso, parágrafo, folhas |

Siglas consolidadas ficam (`API`, `URL`, `HTTP`, `CPF`, `CNPJ`, `ABNT`). Defina uma vez a sigla que não é de conhecimento geral do leitor.
