import matplotlib.pyplot as plt
import numpy as np

# Configuração global Dark Mode (#0D1117 - GitHub Dark)
plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(9, 5.5), facecolor='#0D1117')
ax.set_facecolor('#0D1117')

categorias = ['Aporte Inicial (CapEx)', 'Manutenção / Recarga', 'Risco de Banimento (Perda)']
fisico = [35000, 2500, 15000]
nuvem = [0, 676, 500]

x = np.arange(len(categorias))
width = 0.35

rects1 = ax.bar(x - width/2, fisico, width, label='Hardware Físico (30-50 aparelhos)', color='#8B0000', edgecolor='#FF4D4D')
rects2 = ax.bar(x + width/2, nuvem, width, label='Cloud Phones (DuoPlus/PhoneGrid)', color='#FF7B7B', edgecolor='#FFFFFF')

ax.set_ylabel('Custo Estimado (R$)', fontsize=11, fontweight='bold', color='#8B949E')
ax.set_title('Comparativo Financeiro: Hardware Físico vs. Cloud Phones', fontsize=13, fontweight='bold', color='#FF7B7B', pad=20, loc='left')
ax.set_xticks(x)
ax.set_xticklabels(categorias, fontsize=10, fontweight='bold', color='#E6EDF3')
ax.legend(facecolor='#161B22', edgecolor='#30363D', labelcolor='#E6EDF3')
ax.yaxis.grid(True, linestyle='--', alpha=0.2, color='#8B949E')

for bar in rects1:
    h = bar.get_height()
    ax.annotate(f'R$ {h:,.0f}', xy=(bar.get_x() + bar.get_width()/2, h),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, color='#FF8080')

for bar in rects2:
    h = bar.get_height()
    ax.annotate(f'R$ {h:,.0f}', xy=(bar.get_x() + bar.get_width()/2, h),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=9, color='#FFFFFF')

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#30363D')
ax.spines['bottom'].set_color('#30363D')

plt.tight_layout()
plt.savefig('capex_vs_opex_darkmode.png', dpi=200, bbox_inches='tight', facecolor='#0D1117')
plt.close()
print("gerar_grafico_capex_opex.py executado com sucesso!")
