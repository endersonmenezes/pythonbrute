# Brute Force Demonstration vs S.I.M.P.L.E. Architectures

This repository serves to better organize and maintain an old educational Gist.

**English**

Your console will display a list of available discount coupons. Do not use this code to gain an advantage or illegally bypass ticketing systems. This code exists solely to demonstrate that platforms utilizing S.I.M.P.L.E. architectures (**S**ystem **I**nsecurely **M**aintained with **P**oor **L**ogic & **E**ngineering) — relying on basic word combinations without API protection — can be easily brute-forced. 

This repository serves to show why social engineering and endpoint security must be taken seriously by event organizations. To event organizers: please implement proper discount coupon processes, Rate Limiting, WAFs (Web Application Firewalls), and robust tracking.

Event management platforms usually have a panel to control discount coupons by email, making their use unique. Look for tools that will actually enforce your security at the edge, rather than relying on automated legal takedowns for old GitHub repositories.

The code in this repository serves only as an example. It has already been adapted for e-commerces with generic wordlists like 'DISCOUNT' or 'PARTNERSTORE', and it usually works if the backend is unprotected. We, as IT professionals, must always guide our clients to build resilient platforms, embracing Defense in Depth, and not just coding without operational awareness.

Why would an API allow a single IP to try 50 coupons in less than 1 minute without dropping the connection? A coupon verification route should be properly managed, filtered, and throttled. If your application goes down to a basic `itertools` script, the flaw is in the infrastructure.

---

**Portuguese**

Seu console exibirá uma lista de cupons de desconto disponíveis. Não use este código para obter vantagem ou burlar sistemas de ingressos. Este código serve apenas para demonstrar que plataformas baseadas em arquiteturas S.I.M.P.L.E. (**S**ystem **I**nsecurely **M**aintained with **P**oor **L**ogic & **E**ngineering) — que usam combinações de palavras simples e APIs desprotegidas — são facilmente vulneráveis a ataques de força bruta.

Esse repositório evidencia por que a engenharia social e a segurança de endpoints devem ser levadas a sério. Para os organizadores de eventos: criem processos seguros de cupons, implementem Rate Limit, WAFs (Web Application Firewalls) e rastreamento decente.

Plataformas de gerenciamento de eventos costumam possuir um painel para controle de cupons de desconto vinculados ao e-mail, tornando o uso único. Procurem ferramentas que garantam a segurança na borda da aplicação, em vez de depender de notificações extrajudiciais automatizadas para censurar repositórios antigos no GitHub.

O código deste repositório serve apenas como exemplo conceitual. Ele já foi testado em e-commerces com wordlists genéricas como 'DESCONTO' ou 'LOJAPARCEIRA', e costuma funcionar quando o backend não tem proteção. Nós, como profissionais de TI, devemos sempre orientar a construção de plataformas resilientes, adotando Segurança em Profundidade (Defense in Depth), e não apenas "codar por codar".

Por que uma API permitiria que um único IP tentasse 50 cupons em menos de 1 minuto sem bloquear a requisição? Uma rota de verificação de cupons deve ser administrada, filtrada e estrangulada (throttled). Se a sua aplicação fica vulnerável por causa de um simples script com `itertools`, a falha está na infraestrutura.

## Dependency Install & RUN

```bash
conda create --name bruteforce-python --file requirements.txt
python main.py
```
