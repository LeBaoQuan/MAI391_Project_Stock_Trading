# Is it possible to earn abnormal return in an inefficient market?

# An approach based on ML in stock trading

1. Abstract:

  This study focuses on:

  - VN Index and VN30 portfolio
  - buy and sell within a day
  - using Logistic Regression and SVM (support vector machine)
  - aim for short-term investors

2. Introduction:

  - 3 types of efficient market: weak, semi-strong and strong
  > [Summary of EMH Efficient Market Hypothesis ( EMH)](https://www.investopedia.com/ask/answers/032615/what-are-differences-between-weak-strong-and-semistrong-versions-efficient-market-hypothesis.asp)

  - **EMH**: Market __cannot be beaten__ based on publicly available data and the __use of technical analysis doesn't give investors any competitive advantages__ and trading price is always fair

  - in the **weak** form --> stock price fully reflects its history data
  - in **semi-strong** form --> stock price is effected by history data and public information, however inside information may help investors to gain advantages
  - in **strong form** --> both public and insider information reflect the current stock price, and none of these info may give investors advantages

 ### this study aims to test the weak-form efficiency of the Ho Chi Minh stock market###

3. Literature review / Summary of pre-requisite knowledge:

> Logistic Regression:

- Maximum likelihood estimation (MLE)

> Support Vector Machine (SVM):

4. Research method:

### Tesing the Weak-form Efficient Market###

* examine the randomness (in the changes of VN-index and VN30 index), weather they're independent (stock price is effected by its own past price, not by other stocks or the overall market)

* using Logistic Regression to examine how factors (close, HL, LO, var, etc) effect a stock price (increase or decrease)

### Predict stock price movement

* use a _rolling window_ of 1year (365 days) as observation period
* identifying the optimal parameters for the first 365 days --> predict the price of day 366th --> continue with the next _rolling window_ (day 2th to day 366th, to predit day 367th), so on and so forth

![rolling window](https://github.com/LeBaoQuan/MAI391_Project_Stock_Trading/blob/master/rolling_window.png)


5. Results:
