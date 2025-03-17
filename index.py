with open("large_script.py", "w") as f:
    for i in range(10000): 
        f.write(f"def function_{i}():\n    pass\n\n")
