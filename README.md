# Titanic - Machine Learning from Disaster

This is my submission for the [Titanic challenge](https://www.kaggle.com/c/titanic/overview) from Kaggle. The main notebook of interest is `main.ipynb`

My current best score is at 78%, which I may look to improve. That places me at about the 80th percentile of scores. I used a random forest classifier with randomized hyperparameter searching for my solution. I might consider seeing if logistic regression or gradboosting end up improving my scores, or getting more in the weeds with hyperparameter tuning by using something like Bayesian optimization to see if that helps. Could also consider try other stuff at the data cleaning stage, looking separating age into groups or combining SipSp and Parch.