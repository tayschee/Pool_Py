import pandas as pd

class FileLoader():
    
    def load(self, path):
        df = pd.read_csv(path)
        print("Loading dataset of dimensions", df.shape[0], "x", df.shape[1])
        return (df)
    def display(self, df, n):
        print(df[0:n]) if n > 0 else print(df[n - 1:-1])
        pass
