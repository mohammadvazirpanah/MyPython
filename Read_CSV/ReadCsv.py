import pandas as pd
df = pd.read_excel("Book1.xlsx")

def read_csv():
        list_p = list (df["P"].dropna())
        list_i_prime = list (df["i"].dropna())
        n = int (df["n"].dropna())
        t = int (df["t"].dropna())
        s = int (df["s"].dropna())
        list_i = []
        p = 0
        for i in range (s):
                list_help = [] 
                for j in range (n):
                        list_help.append(list_i_prime[j+p])
                p = p + n 
                list_i.append (list_help)

        return (list_p,list_i,n,t,s)


        





