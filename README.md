# Projeto DIO — Simulação e Análise de Malware (Ransomware & Keylogger) — Abordagem Segura

> Atenção: Este repositório documenta um projeto **didático** sobre funcionamento e defesa contra malwares. Não contém código malicioso. Todas as simulações descritas foram realizadas (ou descritas) em **ambiente controlado** e com fins educativos. Nunca execute ou distribua códigos capazes de comprometer sistemas alheios.

## Sumário
1. Objetivo  
2. Declaração Ética e de Segurança  
3. Ambiente de Teste
4. Descrição das Simulações 
   - Ransomware 
   - Keylogger 
5. Experimentos realizados / Documentação  
6. Resultados observados  
7. Medidas de Detecção e Mitigação  
8. Entregáveis
9. Como reproduzir
10. Atividades para aprofundamento

---

## 1. Objetivo
Compreender, de forma segura e ética, os mecanismos básicos por trás de dois tipos de ameaça: ransomware e keylogger; aprender a identificar indicadores de comprometimento; e documentar estratégias práticas de defesa, prevenção e resposta.

## 2. Declaração Ética e de Segurança
- Todo o trabalho foi realizado em ambiente de laboratório isolado (Host-Only / NAT / redes virtuais) e com arquivos de teste criados especificamente para o exercício.  
- Não há, em hipótese alguma, scripts que possam ser executados para causar dano fora do ambiente controlado.  
- Este repositório tem finalidade educacional e de conscientização.

## 3. Ambiente de Teste (recomendado)
- Host: máquina física com snapshot (Windows/Linux)  
- VMs: Kali Linux (analisador), uma VM alvo isolada (ex.: Windows ou Linux com arquivos de teste)  
- Rede: Host-Only / Internal Network (isolada, sem acesso à internet)  
- Ferramentas: Wireshark, Sysmon (Windows), Process Monitor (ProcMon), antivírus com quarentena, ferramentas de análise (strings, VirusTotal para hashes), IDE para documentar experimentos

> **IMPORTANTE:** Sempre trabalhar com snapshots e backups. Se algo sair do controle, restaure a VM.

## 4. Descrição das Simulações (conceitual)
> Abaixo a descrição do comportamento que foi estudado/documentado — **não** há código executável aqui.

### 4.1 Ransomware (simulação controlada)
- **Objetivo didático:** entender fluxo: busca de arquivos, criptografia do conteúdo, geração de nota de resgate, e técnicas de persistência (conceito).  
- **Comportamento descrito:**  
  - identificação de arquivos-alvo por extensão (.txt, .docx, .xlsx — neste experimento apenas arquivos dummy);  
  - criação de backup seguro e/ou armazenamento de chaves local para estudo (apenas conceitual aqui);  
  - geração de mensagem de resgate em arquivo texto.  
- **Observação:** Em vez de criptografar arquivos reais do sistema, as práticas recomendadas no laboratório limitaram operações a **uma pasta de teste** com arquivos gerados especificamente.

### 4.2 Keylogger (simulação controlada)
- **Objetivo didático:** entender como entrada de teclado pode ser capturada, como logs são armazenados e métodos de exfiltração (conceito).  
- **Comportamento descrito:**  
  - captura de eventos de entrada de teclado armazenados localmente em arquivo de teste;  
  - técnicas de camuflagem de arquivo (apenas conceitual);  
  - envio (simulado) por e-mail ou upload a servidor de testes (nunca para servidores reais).  
- **Observação:** Não está presente nenhum logger funcional neste repositório. Para demonstrar pipeline de detecção, foram gerados logs sintéticos (ex.: `logs/test-typing.log`) que simulam tráfego.

## 5. Experimentos realizados / Documentação
- Lista de passos executados (aplicados apenas em ambiente isolado):  
  1. Preparação do ambiente e criação de pasta `laboratorio/arquivos_teste` com 50 arquivos dummy.  
  2. Execução de análise de baseline (snapshot de sistema, processos e logs).  
  3. Registro das mudanças de arquivo e do comportamento do antivírus/IDS ao operar sobre a pasta de testes.  
  4. Coleta de evidências: prints, logs ProcMon/Sysmon, capturas Wireshark, hashes dos arquivos originais e “criptografados” (simulados).  
- Todos os comandos e outputs estão documentados em `/docs/experiment_log.md`.

## 6. Resultados observados
- Indicadores típicos observados (exemplos documentados):  
  - criação massiva de arquivos em curto espaço de tempo;  
  - alterações de hashes de arquivos;  
  - criação de processos filhos não usuais;  
  - conexões de rede incomuns (simuladas).  
- Esses indicadores estão correlacionados com técnicas de detecção descritas na seção 7.

## 7. Medidas de Detecção e Mitigação
- Backup versionado e offline;  
- Aplicar princípio de menor privilégio (roles e permissões);  
- Política de whitelist de aplicações;  
- Soluções EDR/AV com regras de comportamento (alertas em mass file write);  
- Monitoramento de processos (Sysmon/ProcMon), integrando logs ao SIEM;  
- Educação do usuário (phishing, anexos desconhecidos);  
- Isolamento de VMs e uso de sandboxing para análise.

## 8. Entregáveis (no repositório)
- `/README.md` — este documento  
- `/docs/experiment_log.md` — passo a passo das simulações e saídas do laboratório (sem código malicioso)  
- `/images/` — screenshots e evidências (outputs, capturas de ferramentas)  
- `/laboratorio/` — **APENAS** arquivos de teste (dummy) e logs sintéticos que representam capturas, sem conter código malicioso

## 9. Como reproduzir (modo seguro)
1. Crie duas VMs em rede isolada.  
2. Carregue os arquivos de teste na pasta dedicada.  
3. Siga os passos do `/docs/experiment_log.md` para gerar evidências.  
4. Não execute scripts obtidos na internet sem avaliação; restaure snapshot se necessário.

## 10. Atividades para aprofundamento (sugestões)
- Configurar Sysmon em Windows e escrever regras básicas para detecção de criação massiva de arquivos.  
- Usar Wireshark para detectar padrões de exfiltração simulada.  
- Criar regras YARA para identificar strings comuns em ransom notes (apenas para detecção e pesquisa).  
- Desenvolver um pequeno dashboard que recebe logs e indica anomalias (Python + ELK/Graylog).

---

## Conclusão
Este projeto foca em **aprender e documentar** — não em distribuir ou executar código perigoso. A experiência permitiu identificar indicadores práticos e estratégias de defesa acionáveis. Recomenda-se seguir as atividades de aprofundamento para transformar conhecimento teórico em prática segura.

