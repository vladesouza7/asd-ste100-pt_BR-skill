---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Esse é o prompt de sistema de um agente que faz triagem de chamados e repassa pra outro agente que executa. Já tivemos dois incidentes porque o agente executor entendeu errado. Reescreve em português técnico simplificado, sem mudar nenhuma regra de negócio, pra eu colar direto no prompt:

"Quando o solicitante abrir um chamado para o analista, o agente registra seu e-mail e encaminha o chamado para a fila. O analista só pode encerrar o chamado depois de validar a solução com o solicitante. Se o comando de rollback para o serviço, o agente notifica o gestor e ele decide se reinicia. O solicitante pode anexar até 5 arquivos, e o agente deve estar com a fila vazia antes de iniciar uma nova triagem, caso contrário a mesma será descartada."
