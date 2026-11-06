# Vagas de Manutenção / PCM - EUA e Europa (com Visa Sponsorship)

App estático que lista vagas relacionadas a:
- Maintenance Planner / Analista de PCM
- Maintenance Supervisor
- Maintenance Coordinator
- Reliability Engineer
- Coordenador / Supervisor de Manutenção

Critérios aproximados:
- EUA ou Europa
- Visa sponsorship (H-1B, TN, UK sponsorship etc.)
- Salário em torno de $70k USD ou €40k+ EUR

## Como colocar no ar (gratuito)

1. Crie um repositório novo no GitHub.
2. Faça upload de todos os arquivos desta pasta.
3. Vá em **Settings → Pages**.
4. Em **Source**, escolha **Deploy from a branch**, branch `main` e pasta `/ (root)`.
5. Salve. O site ficará em `https://SEU-USUARIO.github.io/NOME-DO-REPOSITORIO/`.

## Atualização automática

O GitHub Action (`.github/workflows/update.yml`) regenera o `index.html` todo dia usando os dados curados no script Python.

Você pode forçar uma atualização em **Actions → Atualizar Vagas Manutenção → Run workflow**.

## Observações

- Vagas com visa sponsorship real para esses cargos são limitadas (muitos exigem que o cargo seja "specialty occupation" com diploma de engenharia para H-1B).
- O script usa dados curados (fallback). Para melhorar, adicione scrapers de LinkedIn/Indeed ou atualize a lista manualmente no arquivo `scripts/update_jobs.py`.
- Sempre verifique a vaga oficial e os requisitos de visto diretamente na empresa.
'''