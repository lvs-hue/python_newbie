import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('Streamlit 超入門')

st.write('DataFrame')
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.write(df)
st.dataframe(df.style.highlight_max(axis=0), width = 300, height = 500)
# axis=0 列、axis=1 行

st.table(df.style.highlight_max(axis=0))
#詳しくは　https://docs.streamlit.io/develop/api-reference/data

"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig