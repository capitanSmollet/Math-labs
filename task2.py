import numpy as np, matplotlib.pyplot as plt, seaborn as sns

np.random.seed(42)
sample = np.random.normal(loc = 0, scale = 1, size = 1000) #генерация выборки
sns.kdeplot(sample, fill=True) #реализация kde с помощью библиотеки seaborn
plt.title(f'Ядерная оценка плотности') #оформление графика
plt.xlabel('x'); plt.ylabel('$y_r^{**}$')
plt.grid(alpha=0.3); plt.show()
