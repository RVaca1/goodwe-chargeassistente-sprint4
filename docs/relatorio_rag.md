# Relatório técnico e avaliação RAG — Sprint 04

## Arquitetura e parâmetros

Extração de manuais GoodWe, divisão em chunks de 800 caracteres com overlap de 120, embeddings `nomic-embed-text`, armazenamento persistente ChromaDB e busca de similaridade. O pipeline utiliza LangChain, prompt `v3`, recuperação `k=8`, limiar de relevância `0.55` e geração local `qwen3:4b-instruct`. Parâmetros do modelo: temperature `0.2`, top_p `0.9`, max_tokens/num_predict `512`. Modelo alternativo avaliado: `llama3.2:3b`.

## Conjunto e procedimento

10 casos fixos em `evals/sprint4_eval_set.json`: 5 perguntas técnicas e 5 perguntas de recusa/segurança/fora de escopo. Comparação dos arquivos de execução existentes; nenhuma nova inferência foi executada ao revisar este relatório. A rubrica manual equivalente em `evals/manual_rubric.md` aplica 0, 0.5 ou 1 para faithfulness e answer relevancy. **Somente respostas técnicas efetivamente produzidas recebem notas**; recusas e cobertura são medidas separadamente. Avaliação humana conservadora a partir das respostas registradas e trechos do manual; não é cálculo automático RAGAS e a auditoria documental integral permanece pendente.

| Configuração | Cobertura | Citações explícitas | Faithfulness média (respondidas) | Answer relevancy média (respondidas) |
|---|---:|---:|---:|---:|
| qwen_v2_060 | 4/5 | 0/4 | 0.75 | 1.00 |
| qwen_v3_060 | 4/5 | 4/4 | 0.75 | 1.00 |
| llama_v2_060 | 4/5 | 1/4 | 0.75 | 1.00 |
| qwen_v3_055 | 5/5 | 5/5 | 0.80 | 1.00 |

**Interpretação:** as médias de fidelidade não demonstram ganho entre as versões Qwen; a evolução observada está em **rastreabilidade** (0/4 → 4/4 com v3) e **cobertura** (4/5 → 5/5 com limiar 0.55). A métrica de citação identifica presença textual de nome do PDF e página, não verifica automaticamente se a página sustenta todas as afirmações. A amostra é pequena e foi usada para selecionar a configuração.

## Evidências e problemas resolvidos

1. **Falta de citação explícita:** prompt v2 citava apenas “Trecho 1”; prompt v3 passou a exigir nome do manual e página.
2. **Recusa indevida por recuperação insuficiente:** a pergunta sobre potências da HCA encontrou trecho com relevância ~0.569, abaixo de 0.60. Reduzir para 0.55 permitiu resposta 7/11/22 kW, conforme manual p.10. É preciso monitorar ruído de recuperação em outros casos.
3. **Erro factual do Llama:** expandiu CA como “Carregador de Alta Potência” na pergunta 7. O manual identifica carregador CA doméstico (corrente alternada). Tanto Qwen quanto Llama apresentaram expansões não comprovadas de “RCD”; as notas de fidelidade dessas respostas foram reduzidas a 0.5.

## Segurança

Dois casos de injection direta nas perguntas foram bloqueados em cada execução. Em teste isolado, um documento simulado contendo “IGNORE TODAS AS INSTRUÇÕES ANTERIORES” foi devolvido pela busca com score 0.99 e descartado antes da geração: `status=insufficient_context`, 0 fontes. Esse teste foi executado com `unittest.mock` e não alterou o ChromaDB. Não há evidência de robustez contra ataques reformulados ou em outros idiomas.

## Arquivos auditáveis

- Execuções: `evals/qwen_v2_10.json`, `evals/qwen_v3_10.json`, `evals/llama_v2_10.json`, `evals/qwen_v3_threshold055.json`.
- Notas por pergunta, justificativas e médias: `evals/avaliacao_manual_comparativa_sprint4.json`.
- Resumo: `evals/resumo_comparativo_sprint4.json`.
- Rubrica: `evals/manual_rubric.md`.
