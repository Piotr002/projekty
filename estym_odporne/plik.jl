ans = "Hello World"
 
open("./geek.txt", "r") do file
    println(joinpath(root, file))
end