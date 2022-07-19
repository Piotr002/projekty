using PyCall
using Distributions
using Random
using Statistics
using StatsFuns
using LinearAlgebra
using Plots

arma_pack = pyimport("statsmodels.tsa.arima_process")
np = pyimport("numpy")

ar4 = np.array([1, 0.33, 0.5, 0.86, 0.34])
ma4 = np.array([1, 0.9, 0.3, 0.12, 0.94])

function autocov(X, lag)
    return [1/length(X) * (sum((X[1:end - i] .- mean(X)) .* (X[i + 1:end] .- mean(X)))) for i in lag[1]:lag[2]]
end

function autocorr(X, lag)
    return [i/autocov(X, [0, 1])[1] for i in autocov(X, lag)]
end

#println(np.array([2,3,4]))
#println(arma_pack.ArmaProcess(ar4, ma4).generate_sample(nsample=100))

arma_timeseries = [arma_pack.ArmaProcess(ar4, ma4).generate_sample(nsample=100) for i in 1:1000]

Xt = arma_pack.ArmaProcess(ar4, ma4).generate_sample(nsample=100)

acorr_arma = [[autocorr(arma_pack.ArmaProcess(ar4, ma4).generate_sample(nsample=100), [0, 5])] for i in 1:100000]

theo_arma = mean(acorr_arma)
println(theo_arma[1])
println(string(@__DIR__) * "/dane/acorr_arma44_n100.txt")

text = ""
for i in theo_arma[1]
    global text = text * string(i) * "\n"
end

open(string(@__DIR__) * "/dane/acorr_arma44_n100.txt", "w") do f
    write(f, text)
end







acorr_arma = [[autocorr(arma_pack.ArmaProcess(ar4, ma4).generate_sample(nsample=1000), [0, 5])] for i in 1:100000]

theo_arma = mean(acorr_arma)

text = ""
for i in theo_arma[1]
    global text = text * string(i) * "\n"
end

open(string(@__DIR__) * "/dane/acorr_arma44_n1000.txt", "w") do f
    write(f, text)
end
