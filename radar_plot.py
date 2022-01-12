import plotly.express as px
import pandas as pd
df = pd.DataFrame(dict(
    r=[10, 32, 42, 47, 48, 59, 60, 71, 78, 92],
    theta=['Cristiano Ronaldo','Justin Bieber','Selena Gomez',
           'Taylor Swift', 'Rihanna', 'Katy Perry', 'Neymar', 'Shakira', 'Real Madrid CF', 'Jennifer Lopez']))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.show()
