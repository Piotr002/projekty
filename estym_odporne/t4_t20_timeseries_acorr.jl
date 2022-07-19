using Distributions
using Random
using Statistics
using StatsFuns

function MA1_process_t_distribution(n, theta, freedom_degrees)
    Z = rand(TDist(freedom_degrees), n+1)
    return [Z[i+1] + theta*Z[i] for i in 1:n]
end

function autocov(X, lag)
    return [1/length(X) * (sum((X[1:end - i] .- mean(X)) .* (X[i + 1:end] .- mean(X)))) for i in lag[1]:lag[2]]
end

function autocorr(X, lag)
    return [i/autocov(X, [0, 1])[1] for i in autocov(X, lag)]
end

acorr_t4 = [[autocorr(MA1_process_t_distribution(100, 0.5, 4), [0, 5])] for i in 1:100000]
theo_t4 = mean(acorr_t4)


text = ""
for i in theo_t4[1]
    global text = text * string(i) * "\n"
end

open(string(@__DIR__) * "/dane/acorr_t4_n100.txt", "w") do f
    write(f, text)
end

acorr_t4 = [[autocorr(MA1_process_t_distribution(500, 0.5, 4), [0, 5])] for i in 1:100000]
theo_t4 = mean(acorr_t4)

text = ""
for i in theo_t4[1]
    global text = text * string(i) * "\n"
end

open(string(@__DIR__) * "/dane/acorr_t4_n500.txt", "w") do f
    write(f, text)
end


acorr_t4 = [[autocorr(MA1_process_t_distribution(1000, 0.5, 4), [0, 5])] for i in 1:100000]
theo_t4 = mean(acorr_t4)

text = ""
for i in theo_t4[1]
    global text = text * string(i) * "\n"
end

open(string(@__DIR__) * "/dane/acorr_t4_n1000.txt", "w") do f
    write(f, text)
end






acorr_t20 = [[autocorr(MA1_process_t_distribution(100, 0.5, 20), [0, 5])] for i in 1:100000]
theo_t20 = mean(acorr_t20)


text = ""
for i in theo_t20[1]
    global text = text * string(i) * "\n"
end

open(string(@__DIR__) * "/dane/acorr_t20_n100.txt", "w") do f
    write(f, text)
end

acorr_t20 = [[autocorr(MA1_process_t_distribution(500, 0.5, 20), [0, 5])] for i in 1:100000]
theo_t20 = mean(acorr_t20)

text = ""
for i in theo_t20[1]
    global text = text * string(i) * "\n"
end

open(string(@__DIR__) * "/dane/acorr_t20_n500.txt", "w") do f
    write(f, text)
end


acorr_t20 = [[autocorr(MA1_process_t_distribution(1000, 0.5, 20), [0, 5])] for i in 1:100000]
theo_t20 = mean(acorr_t20)

text = ""
for i in theo_t20[1]
    global text = text * string(i) * "\n"
end

open(string(@__DIR__) * "/dane/acorr_t20_n1000.txt", "w") do f
    write(f, text)
end