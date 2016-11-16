import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

statement=pd.read_csv("../finances/stmt.csv")
#print(statement)
#pd.to_numeric(statement['Date'])
statement.plot(x='Date',y='Running Bal.')
plt.show()
