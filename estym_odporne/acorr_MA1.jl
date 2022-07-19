using PyCall
using Distributions
using Random
using Statistics

function MA1_process(n, theta, sigma)
    Z = rand(Normal(0, sigma), n+1)
    return [Z[i+1] + theta*Z[i] for i in 1:n]
end

function autocov(X, lag)
    return [1/length(X) * (sum((X[1:end - i] .- mean(X)) .* (X[i + 1:end] .- mean(X)))) for i in lag[1]:lag[2]]
end

function autocorr(X, lag)
    return [i/autocov(X, [0, 1])[1] for i in autocov(X, lag)]
end


acorr_MA1 = [[autocorr(MA1_process(100, 0, 1), [0, 5])] for i in 1:100000]
theo_MA1 = mean(acorr_MA1)


text = ""
for i in theo_MA1[1]
    global text = text * string(i) * "\n"
end

open(string(@__DIR__) * "/dane/acorr_MA1_n100.txt", "w") do f
    write(f, text)
end


acorr_MA1 = [[autocorr(MA1_process(500, 0, 1), [0, 5])] for i in 1:100000]
theo_MA1 = mean(acorr_MA1)


text = ""
for i in theo_MA1[1]
    global text = text * string(i) * "\n"
end

open(string(@__DIR__) * "/dane/acorr_MA1_n500.txt", "w") do f
    write(f, text)
end


acorr_MA1 = [[autocorr(MA1_process(1000, 0, 1), [0, 5])] for i in 1:100000]
theo_MA1 = mean(acorr_MA1)


text = ""
for i in theo_MA1[1]
    global text = text * string(i) * "\n"
end

open(string(@__DIR__) * "/dane/acorr_MA1_n1000.txt", "w") do f
    write(f, text)
end