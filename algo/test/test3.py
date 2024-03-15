import a

for i in range(5):
    with open("a.py", "a+") as f:
        print(i)
        f.write(f"""\n\n
        def func_{i}({i}):
            print({i})

""")

    
    # this get the function from module "a" with name "a_i". basically work like a(i)
    getattr(a, f"func_{i}")(6)

    
  
    