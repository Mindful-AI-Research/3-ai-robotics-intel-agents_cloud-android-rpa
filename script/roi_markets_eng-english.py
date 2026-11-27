import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0D1117')
ax.set_facecolor('#0D1117')

markets = [
    'Airdrop Farming & Web3',
    'Hot Niche & iGaming',
    'Growth & Mass Posting',
    'Paid Traffic & Contingency',
    'Web Scraping & BI',
    'E-Commerce & Marketplaces'
]
roi_max = [5000, 2000, 1000, 500, 400, 300]
labels = ['500% to 5,000%+', '500% to 2,000%+', '300% to 1,000%+', '100% to 500%+', '200% to 400%+', '150% to 300%']

y_pos = np.arange(len(markets))
markets, roi_max, labels = markets[::-1], roi_max[::-1], labels[::-1]
colors = ['#8B0000', '#A81C1C', '#C63838', '#E45454', '#F06868', '#FF7B7B']

bars = ax.barh(y_pos, roi_max, color=colors, height=0.55, edgecolor='#FF7B7B', linewidth=0.8)

for bar, label in zip(bars, labels):
    w = bar.get_width()
    ax.text(w + 100, bar.get_y() + bar.get_height()/2, label,
            va='center', ha='left', color='#FFFFFF', fontweight='bold', fontsize=10)

ax.set_yticks(y_pos)
ax.set_yticklabels(markets, fontsize=11, fontweight='bold', color='#E6EDF3')
ax.set_xlabel('Estimated Return on Investment (ROI %)', fontsize=11, fontweight='bold', color='#8B949E')
ax.set_title('Estimated ROI Matrix by Operational Segment', fontsize=14, fontweight='bold', color='#FF7B7B', pad=20, loc='left')
ax.set_xlim(0, 5800)
ax.xaxis.grid(True, linestyle='--', alpha=0.2, color='#8B949E')

for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)
ax.spines['left'].set_color('#30363D')
ax.spines['bottom'].set_color('#30363D')

ax.text(0, -0.15, 'Source: Virtual Environment Isolation Strategic Analysis (saida-v2.md)', 
        transform=ax.transAxes, fontsize=8, fontstyle='italic', color='#8B949E')

plt.tight_layout()
plt.savefig('/workspace/scratch/roi_markets_eng-english.png', dpi=200, bbox_inches='tight', facecolor='#0D1117')
plt.close()
