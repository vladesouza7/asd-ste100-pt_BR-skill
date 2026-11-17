---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Estou escrevendo as descrições das ferramentas de um agente em português e o pessoal reclamou que a do sincronizador ficou confusa. Simplifica essa descrição pra mim, do jeito que eu possa colar direto no JSON da ferramenta:

"Esta ferramenta irá tentar realizar a sincronização do estado entre os diversos backends que tenham sido previamente configurados pelo usuário, e, caso venha a ser detectado algum tipo de conflito, o mesmo poderá eventualmente ser resolvido de forma automática conforme a estratégia que tiver sido definida nas configurações; do contrário, o referido conflito será apresentado ao usuário para que o mesmo proceda à sua revisão manual, sendo importante ressaltar que, em condições de timeout, artefatos parciais podem vir a ser gerados."
