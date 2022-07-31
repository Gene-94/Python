import yfinance
import pandas
import streamlit
from datetime import date

streamlit.write("""
# Aplicação para seguir o preço de ações

Abaixo estão vários gráficos com o histórico de ações de cada empresa.

""")
#define ticker symbol
tickerSymbol = 'GOOGL'
streamlit.write("-"*50)
streamlit.write("#**GOOGLE**")
#get data based on the defined ticker
tickerData = yfinance.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d',  start='2020-1-1', end=date.today())
# Open High     Low Close   Volume  Dividends   Stock Slits

streamlit.write("\n-Gráfico baseado no preço de fecho")
streamlit.line_chart(tickerDf.Close)
streamlit.write("\n\n-Gráfico baseado no volume")
streamlit.line_chart(tickerDf.Volume)

tickerSymbol2 = 'FB'
streamlit.write("-"*50)
streamlit.write("#**FACEBOOK**")
#get data based on the defined ticker
tickerData2 = yfinance.Ticker(tickerSymbol2)
#get the historical prices for this ticker
tickerDf2 = tickerData2.history(period='1d',  start='2020-1-1', end=date.today())
# Open High     Low Close   Volume  Dividends   Stock Slits

streamlit.write("\n-Gráfico baseado no preço de fecho")
streamlit.line_chart(tickerDf2.Close)
streamlit.write("\n\n-Gráfico baseado no volume")
streamlit.bar_chart(tickerDf2.Volume)
