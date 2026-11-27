import matplotlib.pyplot as plt
import numpy as np

# Configuração de estilo Dark Mode
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 7), facecolor='#0D1117')
ax.set_facecolor('#0D1117')

# Dados dos Mercados e ROI Máximo Estimado (%)
mercados = [
    'Airdrop Farming & Web3/Crypto',
    'Nicho Hot, Adulto & iGaming',
    'Growth & Postagens em Massa',
    'Tráfego Pago & Contingência',
    'Web Scraping & Business Intelligence',
    'E-Commerce & Marketplaces'
]

roi_max = [5000, 2000, 1000, 500, 400, 300]
roi_labels = ['500% a 5.000%+', '500% a 2.000%+', '300% a 1.000%+', '100% a 500%+', '200% a 400%+', '150% a 300%']

# Ordenar do menor para o maior para exibição horizontal
y_pos = np.arange(len(mercados))
mercados = mercados[::-1]
roi_max = roi_max[::-1]
roi_labels = roi_labels[::-1]

# Paleta em Gradiente: Vermelho Escuro (#8B0000) até Coral Vibrante (#FF7B7B)
cores_gradiente = ['#8B0000', '#A81C1C', '#C63838', '#E45454', '#F06868', '#FF7B7B']

# Criar gráfico de barras horizontais em tom Coral/Vermelho
bars = ax.barh(y_pos, roi_max, color=cores_gradiente, height=0.6, edgecolor='#FF7B7B', linewidth=0.8)

# Rótulos das barras e valores
for bar, label in zip(bars, roi_labels):
    width = bar.get_width()
    ax.text(width + 80, bar.get_y() + bar.get_height()/2, label,
            va='center', ha='left', color='#FFFFFF', fontweight='bold', fontsize=11)

# Estilização de Eixos e Títulos
ax.set_yticks(y_pos)
ax.set_yticklabels(mercados, fontsize=12, fontweight='bold', color='#E6EDF3')
ax.set_xlabel('Estimativa de Retorno sobre Investimento (ROI %)', fontsize=12, fontweight='bold', color='#8B949E', labelpad=12)
ax.set_title('Matriz de ROI Estimado por Mercado & Segmento Operacional', fontsize=15, fontweight='bold', color='#FF7B7B', pad=25, loc='left')

# Grid e Limites
ax.set_xlim(0, 5800)
ax.xaxis.grid(True, linestyle='--', alpha=0.2, color='#8B949E')
ax.yaxis.grid(False)

# Remoção de Bordas Desnecessárias (Decluttering)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#30363D')
ax.spines['bottom'].set_color('#30363D')

# Rodapé de Fonte
ax.text(0, -0.15, 'Fonte: Análise Estratégica de Isolamento de Ambientes Virtuais (saida-v2.md)', 
        transform=ax.transAxes, fontsize=9, fontstyle='italic', color='#8B949E')

plt.tight_layout()

# Salvar imagem em scratch
plt.savefig('/workspace/scratch/roi_mercados_darkmode.png', dpi=200, bbox_inches='tight', facecolor='#0D1117')
plt.close()

print("Gráfico gerado com sucesso em /workspace/scratch/roi_mercados_darkmode.png")
