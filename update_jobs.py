#!/usr/bin/env python3
"""
Script para buscar vagas de Manutenção / PCM / Reliability no EUA e Europa
com visa sponsorship e salário aproximado de $70k USD ou €40k EUR.
Gera index.html atualizado.
"""

import json
from datetime import datetime

def get_fallback_data():
    """Dados curados com base em vagas reais recentes (atualize periodicamente)"""
    return [
        {
            "titulo": "Maintenance Planner",
            "empresa": "Tesla",
            "local": "United States (various sites)",
            "salario": 116000,
            "moeda": "USD",
            "visa": "H-1B sponsorship available (historical filings)",
            "tipo": "Maintenance Planner / Reliability",
            "status": "open",
            "statusLabel": "Vagas abertas (verificar site da empresa)",
            "descricao": "Planejamento de manutenção em plantas de manufatura. Experiência com CMMS desejável.",
            "link": "https://www.tesla.com/careers",
            "fonte": "visa-bulletin.us / Tesla careers"
        },
        {
            "titulo": "Reliability Engineer",
            "empresa": "Bosch Group",
            "local": "Lincolnton, NC, USA",
            "salario": 95000,
            "moeda": "USD",
            "visa": "H-1B sponsorship available",
            "tipo": "Reliability Engineer",
            "status": "open",
            "statusLabel": "Sponsorship confirmado em listagens recentes",
            "descricao": "Melhoria de confiabilidade de equipamentos, RCM, análise de dados, redução de downtime.",
            "link": "https://h1bvisajobs.com/jobs/reliability-engineer-lincolnton-us",
            "fonte": "H1BVisaJobs"
        },
        {
            "titulo": "Mgr, Maintenance I / CMMS Process Owner",
            "empresa": "Amgen",
            "local": "Holly Springs, NC, USA",
            "salario": 127000,
            "moeda": "USD",
            "visa": "H-1B sponsorship available",
            "tipo": "Maintenance Manager / CMMS",
            "status": "open",
            "statusLabel": "Sponsorship para nível Principal+",
            "descricao": "Gestão de planejamento de manutenção e CMMS em planta farmacêutica.",
            "link": "https://h1bvisajobs.com/jobs/mgr-maintenance-i-us-north-carolina-holly-springs-us",
            "fonte": "H1BVisaJobs"
        },
        {
            "titulo": "Maintenance Supervisor (TN Visa Sponsorship)",
            "empresa": "Mauser Packaging Solutions",
            "local": "Homerville, GA, USA",
            "salario": 87500,
            "moeda": "USD",
            "visa": "TN Visa Sponsorship available",
            "tipo": "Maintenance Supervisor",
            "status": "open",
            "statusLabel": "TN sponsorship + relocation",
            "descricao": "Supervisor de manutenção em manufatura. Suporte a candidatos TN.",
            "link": "https://mx.indeed.com/viewjob?jk=d607aedefb573e5e",
            "fonte": "Indeed"
        },
        {
            "titulo": "Senior Reliability, Maintenance and Engineering (RME) Planner",
            "empresa": "Amazon",
            "local": "Lewisberry, PA / Global",
            "salario": 102000,
            "moeda": "USD",
            "visa": "H-1B sponsorship available (Amazon is elite sponsor)",
            "tipo": "Maintenance Planner / Reliability",
            "status": "open",
            "statusLabel": "Amazon sponsorship forte",
            "descricao": "Planejamento de manutenção e confiabilidade em operações de fulfillment/transporte.",
            "link": "https://www.amazon.jobs/",
            "fonte": "Amazon Jobs / H1BConnect"
        },
        {
            "titulo": "Reliability Engineer",
            "empresa": "Warburtons",
            "local": "Enfield, UK / Europe",
            "salario": 50000,
            "moeda": "GBP",
            "visa": "UK visa sponsorship possible",
            "tipo": "Reliability Engineer",
            "status": "open",
            "statusLabel": "Sponsorship a discutir no processo",
            "descricao": "Melhoria de confiabilidade de ativos em planta de alimentos.",
            "link": "https://uk.indeed.com/",
            "fonte": "Indeed UK"
        },
        {
            "titulo": "Maintenance Supervisor",
            "empresa": "Smithfield Foods",
            "local": "St Charles, USA",
            "salario": 83750,
            "moeda": "USD",
            "visa": "Verificar com a empresa (relocation disponível)",
            "tipo": "Maintenance Supervisor",
            "status": "open",
            "statusLabel": "Salário $70k-$97.5k",
            "descricao": "Supervisor de manutenção de planta. Relocação oferecida.",
            "link": "https://jobera.com/job/smithfieldfoods-plant-maintenance-supervisor-relocation-fbd464da/",
            "fonte": "Jobera"
        }
    ]

def generate_html(vagas):
    data_js = json.dumps(vagas, ensure_ascii=False, indent=2)
    today = datetime.now().strftime('%d/%m/%Y')
    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vagas Manutenção / PCM - EUA & Europa | Visa Sponsorship</title>
<style>
  :root {{ --bg:#0f1419; --card:#1a2332; --accent:#3b82f6; --accent2:#10b981; --text:#e2e8f0; --muted:#94a3b8; --border:#334155; }}
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ font-family:system-ui,-apple-system,sans-serif; background:var(--bg); color:var(--text); line-height:1.5; padding:1rem; }}
  header {{ text-align:center; padding:2rem 1rem; background:linear-gradient(135deg,#1e3a8a,#1e40af); border-radius:16px; margin-bottom:1.5rem; }}
  h1 {{ font-size:1.7rem; margin-bottom:0.5rem; }}
  .subtitle {{ color:#bfdbfe; font-size:0.95rem; }}
  .filters {{ display:flex; flex-wrap:wrap; gap:0.75rem; margin-bottom:1.5rem; justify-content:center; }}
  input,select,button {{ padding:0.6rem 1rem; border-radius:8px; border:1px solid var(--border); background:var(--card); color:var(--text); font-size:0.9rem; }}
  button {{ background:var(--accent); border:none; cursor:pointer; font-weight:600; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(360px,1fr)); gap:1.25rem; }}
  .card {{ background:var(--card); border:1px solid var(--border); border-radius:12px; padding:1.25rem; transition:transform 0.2s,box-shadow 0.2s; }}
  .card:hover {{ transform:translateY(-4px); box-shadow:0 10px 25px rgba(0,0,0,0.4); }}
  .badge {{ display:inline-block; padding:0.25rem 0.6rem; border-radius:999px; font-size:0.75rem; font-weight:600; margin-bottom:0.5rem; background:#065f46; color:#6ee7b7; }}
  .card h2 {{ font-size:1.2rem; margin:0.4rem 0; }}
  .meta {{ color:var(--muted); font-size:0.85rem; margin-bottom:0.5rem; }}
  .stats {{ display:flex; justify-content:space-between; margin:0.75rem 0; font-weight:600; }}
  .stat-value {{ color:var(--accent2); }}
  .links a {{ color:var(--accent); text-decoration:none; font-size:0.9rem; margin-right:1rem; }}
  footer {{ text-align:center; margin-top:2rem; color:var(--muted); font-size:0.8rem; }}
  .empty {{ text-align:center; padding:3rem; color:var(--muted); }}
</style>
</head>
<body>
<header>
  <h1>Localizador de Vagas de Manutenção / PCM</h1>
  <p class="subtitle">EUA e Europa • Visa Sponsorship • Salário aproximado $70k USD ou €40k+ EUR</p>
  <p style="margin-top:0.5rem; font-size:0.85rem; opacity:0.9;">Dados atualizados em {today} • Sempre confira a vaga oficial</p>
</header>
<div class="filters">
  <input type="text" id="search" placeholder="Buscar cargo, empresa ou local..." oninput="filterCards()">
  <select id="tipoFilter" onchange="filterCards()">
    <option value="">Todos os tipos</option>
    <option value="Planner">Maintenance Planner / PCM</option>
    <option value="Supervisor">Supervisor</option>
    <option value="Reliability">Reliability Engineer</option>
    <option value="Manager">Manager / Coordenador</option>
  </select>
  <button onclick="filterCards()">Filtrar</button>
</div>
<div class="grid" id="cards"></div>
<div class="empty" id="empty" style="display:none;">Nenhuma vaga encontrada com os filtros.</div>
<footer>
  <p>App gerado automaticamente. Não substitui pesquisa direta nos sites oficiais (LinkedIn, Indeed, company careers).</p>
  <p>Fontes: H1BVisaJobs, visa-bulletin.us, Indeed, company sites.</p>
</footer>
<script>
const vagas = {data_js};
function formatMoney(v, moeda) {{
  if (moeda === 'USD') return '$' + v.toLocaleString('en-US');
  if (moeda === 'EUR') return '€' + v.toLocaleString('de-DE');
  if (moeda === 'GBP') return '£' + v.toLocaleString('en-GB');
  return v.toLocaleString();
}}
function render(list) {{
  const container = document.getElementById('cards');
  const empty = document.getElementById('empty');
  container.innerHTML = '';
  if (list.length === 0) {{ empty.style.display = 'block'; return; }}
  empty.style.display = 'none';
  list.forEach(v => {{
    const div = document.createElement('div');
    div.className = 'card';
    div.innerHTML = `
      <span class="badge">${{v.statusLabel}}</span>
      <h2>${{v.titulo}}</h2>
      <div class="meta"><strong>${{v.empresa}}</strong> • ${{v.local}}</div>
      <div class="stats">
        <div><span class="stat-value">${{formatMoney(v.salario, v.moeda)}}</span>/ano</div>
        <div>${{v.tipo}}</div>
      </div>
      <div class="meta"><strong>Visa:</strong> ${{v.visa}}<br>${{v.descricao}}</div>
      <div class="links">
        <a href="${{v.link}}" target="_blank">Ver vaga / Aplicar</a>
      </div>
    `;
    container.appendChild(div);
  }});
}}
function filterCards() {{
  const q = document.getElementById('search').value.toLowerCase();
  const tipo = document.getElementById('tipoFilter').value;
  const filtered = vagas.filter(v => {{
    const matchText = (v.titulo + v.empresa + v.local + v.tipo).toLowerCase().includes(q);
    const matchTipo = !tipo || v.tipo.includes(tipo);
    return matchText && matchTipo;
  }});
  filtered.sort((a,b) => b.salario - a.salario);
  render(filtered);
}}
filterCards();
</script>
</body>
</html>'''
    return html

def main():
    print('Gerando lista de vagas...')
    vagas = get_fallback_data()
    # Filtro básico de salário aproximado
    filtered = [v for v in vagas if (v['moeda'] == 'USD' and v['salario'] >= 65000) or (v['moeda'] in ['EUR','GBP'] and v['salario'] >= 38000)]
    if not filtered:
        filtered = vagas
    html = generate_html(filtered)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'index.html gerado com {len(filtered)} vagas.')

if __name__ == '__main__':
    main()
