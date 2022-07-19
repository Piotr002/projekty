from statsmodels.tsa.arima_process import ArmaProcess
import numpy as np

ar4 = np.array([1, 0.33, 0.5, 0.86, 0.34])
ma4 = np.array([1, 0.9, 0.3, 0.12, 0.94])
Y = ArmaProcess(ar4, ma4).generate_sample(nsample=100)

for i in Y:
    print(i)