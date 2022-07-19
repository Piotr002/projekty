using Statistics
using Random
using Distributions

function Zt(p, zt, n)
    return [i > 2 * p ? 0 : (i < p ? zt : -zt) for i in (rand() for i in 1:n)]
end

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


A = [1 2; 3 4]


@time begin
for i in 1:10000
    Xt = MA1_process(1000, 0.5, 1)
    autocorr(Xt, [0, 2])
end
end

#println(var(A))
#println(rand(Normal(10, 100), 3))
#println(autocov())
#println(Zt(0.06, 0.03, 100))