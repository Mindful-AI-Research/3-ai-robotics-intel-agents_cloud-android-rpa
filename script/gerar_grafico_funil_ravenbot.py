import matplotlib.pyplot as plt

# Configuração global Dark Mode (#0D1117 - GitHub Dark)
plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(9, 5.5), facecolor='#0D1117')
ax.set_facecolor('#0D1117')

etapas = ['Faturamento Bruto', 'Receita Gerada (Pix)', 'Receita Liquidada', 'Investimento Mídia']
valores = [84135.34, 66915.00, 51000.00, 13783.78]
cores = ['#FF7B7B', '#E45454', '#C63838', '#8B0000']

bars = ax.bar(etapas, valores, color=cores, width=0.5, edgecolor='#FFFFFF', linewidth=0.5)

ax.set_ylabel('Valor Acumulado (R$)', fontsize=11, fontweight='bold', color='#8B949E')
ax.set_title('Desempenho de Conversão e Liquidação Pix (RavenBot - 47 Dias)', fontsize=13, fontweight='bold', color='#FF7B7B', pad=20, loc='left')
ax.yaxis.grid(True, linestyle='--', alpha=0.2, color='#8B949E')

for bar in bars:
    h = bar.get_height()
    ax.annotate(f'R$ {h:,.2f}', xy=(bar.get_x() + bar.get_width()/2, h),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold', color='#FFFFFF')

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#30363D')
ax.spines['bottom'].set_color('#30363D')

ax.text(0, -0.15, 'Métricas Reais: Taxa de Conversão Pix = 77,5% | ROI de Mídia = 3.7x', 
        transform=ax.transAxes, fontsize=9, fontstyle='italic', color='#FF7B7B')

plt.tight_layout()
plt.savefig('funil_ravenbot_darkmode.png', dpi=200, bbox_inches='tight', facecolor='#0D1117')
plt.close()
print("gerar_grafico_funil_ravenbot.py executado com sucesso!")
