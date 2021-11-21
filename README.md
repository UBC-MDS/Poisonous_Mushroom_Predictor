# Poisonous Mushroom Predictor
</div>
Group 4.0
  - Dongxiao Li
  - Kyle Maj
  - Mahmoodur Rahman 

Data analysis project executed by Group 4.0 of 6th Cohort (2021-22)
for DSCI 522 (Data Science workflows); a course in the Master of Data 
Science program at the University of British Columbia.

## Background

Mushrooms are species of fungus, of which some can be eaten with meaty 
texture and few types are toxic [^1]. Annually, a significant number of 
people die from eating poisonous mushroom [2, 3]. The BC Centre for 
Disease Control (BCCDC) received 200 calls relating to mushroom poisoning 
in 2018 [?4]. Thus, It is critical to recognize a mushroom of poisonous 
species by observing it's appearance. By appearance, primarily it refers 
to certain physical traits. A model recognizing mushroom toxicity by 
taking these physical traits into account can be effective at preventing 
mushroom toxicity [4]. Recent methods on classifying mushroom falls into 
three groups, chemical determination, animal experimentation, fungal 
classification and folk experience [5]. These methods are not perfect 
and there is room for improvement [7]. Mankind has been identifying toxic 
mushrooms by observing morphology, smell and distinct features[12]. These 
intuitive-based methods are less reliable, and often lead to fatal 
incidents. However, relying on these experiences and intuitions, 
machine-learning models can be tried and tested. In this era of fourth 
Industrial revolution, artificial intelligence is playing a major role 
through deployment of machine-learning and deep learning model [13]. This 
also made it's way to detecting poisonous muashroom also. Chaoqun and 
colleagues developed an android-based application, which detects toxic 
mushrooms through machine-learning models [14]. To further improve 
classification, decision fusion method has been used, by stacking 
algorythms [16]. Shuaichang and colleagues used image-based models for 
poisonous mushroom detection [17].

## Proposed method

In this project, after performing tabular and visual exploratory data
analysis, we intend to obtain baseline predictions from fitting Dummy
classifiers on training data. Then we run three classifier, namely 
Logistic Regression, Support Vector Model, and Random Forest on training 
data. We will interpret certain evaluation matrices such as Confusion 
matrix with cross-validation, Precision, recall, f1 score, Classification 
report, and Precision-recall curve and ROC curve. Eventually, after 
hyperparameter optimization, we will reach a decisionon the best model 
with the best hyperparameters. We may need to address class imbalance,
or manipulate threadsholds for target detection before applying on test 
data. 
Data used in this project is from UCI machine learning repository, provided 
by Jeff Schlimmer of the Audubon Society Field Guide to North American 
Mushrooms [18](https://archive-beta.ics.uci.edu/ml/datasets/mushroom). 
The dataset has 8124 examples and 22 features with 2 possible target classes 
(edible and poisonous). The features are cap-shape, cap-surface, cap-color, 
bruises, odor, gill-spacing, gill-attachment, gill-size, gill-color, 
stalk-shape, stalk-root, stalk-surface-above-ring, stalk-surface-below-ring, 
stalk-color-above-ring, stalk-color-below-ring, veil- type, veil-color, 
ring-number, ring-type, spore-print-color, population, and habitat. 

## Reference

[^1] Here 










    
4    http://www.bccdc.ca/about/news-stories/stories/mushroom-poisonings-on-the-rise-in-british-columbia
    5 https://www.zoology.ubc.ca/~biodiv/mushroom/
    
    
  