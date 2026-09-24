import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 1. Выборка
np.random.seed(42)
sample = np.random.normal(loc=0, scale=1, size=10000)

# 2. Заданная вероятность
p = 0.9

# 3. ЭФР через statsmodels — получаем значения, рисуем сами
ecdf = sm.distributions.ECDF(sample)
x = np.linspace(sample.min(), sample.max(), 1000)
y = ecdf(x)

# 4. Оценка выборочной квантили
q = np.quantile(sample, p)

# 5. Визуализация
plt.step(x, y, where='post', label='ЭФР $F_n(x)$')
plt.axhline(p, color='red',   linestyle='--', label=f'$p = {p}$')
plt.axvline(q, color='green', linestyle='--', label=f'$q = {q:.3f}$')
plt.scatter([q], [p], color='black', zorder=5)

plt.xlabel('x'); plt.ylabel('$F_n(x)$')
plt.title(f'Выборочная функция распределения и квантиль уровня {p}')
plt.legend(); plt.grid(alpha=0.3)
plt.show()

print(f"Выборочная квантиль уровня {p} = {q:.4f}")
