def func():
    qu = "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    ans = input(qu)
    return ans.lower().strip() in ["42", "forty-two", "forty two"]


print("Yes" if func() else "No")
