# Summary

As mushrooms have disntinctive characteristics which help in identifying
whether thgey are poisous or edible, we attempt to build a
classification model using logistic regression algorithm which can use
several morphological charateristics of mushrooms to predict whether the
particularmushroom is toxic or non-toxic. Our final classifier performed
fairly well on an unseen test data set, with a 99% recall. On the 762
test data of toxic mushrooms, it correctly predicted 761. However it
incorrectly predicted 1 toxic mushroom as edible, and hence this was an
instance of false negatives. Such error can lead to consumption of a
poisonous mushroom, which can have fatal consequences. Therefore, more
models should be tested to achieve optimum accuracy before deploying.

# Introduction

Mushrooms are species of fungus, of which some can be eaten with meaty
texture and few types are toxic (Tegzes and Puschner 2002). Annually, a
significant number of people die from ingesting poisonous mushrooms
White et al. (2019). The BC Centre for Disease Control (BCCDC) received
200 calls relating to mushroom poisoning in 2018 (BC Centre for Disease
Control 2019 \[Online\]). Thus, It is critical to recognize a mushroom
of poisonous species by observing it’s appearance. By appearance,
primarily it refers to certain physical traits. A model recognizing
mushroom toxicity by taking these physical traits into account can be
effective at preventing mushroom toxicity (Diaz 2005). Recent methods on
classifying mushroom falls into three groups, chemical determination,
animal experimentation, fungal classification and folk experience
(Fukuwatari et al. 2001). These methods are not perfect and there is
room for improvement (Min, Yu, et al. 2006). Mankind has been
identifying toxic mushrooms by observing morphology, smell and distinct
features (Tanaka, Miyasaka, and Inoue 1996). These intuitive-based
methods are less reliable, and often lead to fatal incidents. However,
relying on these experiences and intuitions, machine-learning models can
be tried and tested. In this era of fourth Industrial revolution,
artificial intelligence is playing a major role through deployment of
machine-learning and deep learning model (Reynolds and Lowe 1965). This
also made it’s way to detecting poisonous mushroom also. Chaoqun and
colleagues developed an android-based application, which detects toxic
mushrooms through machine-learning models (Chaoqun 2019). To further
improve classification, decision fusion method has been used, by
stacking algorithms (Zhifeng 2019). Shuaichang and colleagues used
image-based models for poisonous mushroom detection (Shuaichang,
Xiaomei, and Jian 2020).

# Methods

## Data

For this project we will are using the “Mushroom” dataset from UC
Irvine’s Machine learning repository. The data set was originally
donated on April 27, 1987 and has since been cited 76 times. The data
set contains hypothetical samples of 23 species of mushrooms classified
in the Agaricus and Lepiota Families. There were originally three
classes in our target feature: poisonous, edible, and unknown. For
simplicity, all ‘unknown’ mushrooms are assumed to be poisonous. The
original data set can be found
[here](https://archive-beta.ics.uci.edu/ml/datasets/mushroom). The data
was processed through the tidyverse package (Wickham et al. 2019);
Exploratory data analysis was plotted using ggplot2 (Wickham 2016). This
report was compiled using an R (R Core Team 2021) and Python (Van Rossum
and Drake Jr 1995) and R markdown (Allaire et al. 2020) with knitr (Xie
2020) package document file with scripts running via the docopt (de
Jonge 2020) package.

## Analysis

### Exploration

In this project, we first randomly split the raw data file into a train
dataset(80%) and a test dataset(20%), after performing tabular and
visual exploratory analysis on the train dataset. By doing exploratory
analysis, we identified features might be more useful to predict the
subscription target. We looked at the distribution of toxic and
non-toxic mushroom acroos the categorrical features in the training
dataset.

<img src="../results/eda_plot.png" alt="Figure 1.Distribution of Target feature (Target = 1: Toxic, and Target = 0: Edible) in the training set" width="100%" />
<p class="caption">
Figure 1.Distribution of Target feature (Target = 1: Toxic, and Target =
0: Edible) in the training set
</p>

From exploratory data analysis we can see that edible mushrooms are
likely to have have sunken(denoted as s) cap-shapem, green(r) or
purple(u) cap-color, red(e) or orange(o) gill color, and brown(n) and
orange(o) veil color. They also have rooted stalk root(r), areof flaring
ring type(f), and black(b), orange(o), purple(u) or yellow(y) spore
print color. Another characteristics of edible mushroom is they are
abundant(a) or numerous(n) in population, and dwells in waste(w) type
habitat.

<img src="../results/img/cap_shape.png" alt="Figure 2.Different mushroom cap shape" width="50%" />
<p class="caption">
Figure 2.Different mushroom cap shape
</p>

### Prediction

The Sklearn LogisticRegression (Pedregosa et al. 2011) algorithm is used
to create a classification model to predict whether a mushroom was
poisonus or edible (found in the `class` column of the data set). As the
first step towards building the model to answer the predictive question
posed above we split the data into train and test data set at 80% and
20% level. We performed our exploratory data analysis on the training
data frame.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>
Table 1. Table of cross-validation score results for models used
</caption>
<thead>
<tr>
<th style="text-align:left;">
</th>
<th style="text-align:left;">
Baseline (DummyClassifier)
</th>
<th style="text-align:left;">
LogisticRegression
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
fit\_time
</td>
<td style="text-align:left;">
0.026 (+/- 0.002)
</td>
<td style="text-align:left;">
0.067 (+/- 0.002)
</td>
</tr>
<tr>
<td style="text-align:left;">
score\_time
</td>
<td style="text-align:left;">
0.018 (+/- 0.001)
</td>
<td style="text-align:left;">
0.018 (+/- 0.001)
</td>
</tr>
<tr>
<td style="text-align:left;">
test\_accuracy
</td>
<td style="text-align:left;">
0.515 (+/- 0.000)
</td>
<td style="text-align:left;">
1.000 (+/- 0.000)
</td>
</tr>
<tr>
<td style="text-align:left;">
test\_precision
</td>
<td style="text-align:left;">
0.000 (+/- 0.000)
</td>
<td style="text-align:left;">
1.000 (+/- 0.000)
</td>
</tr>
<tr>
<td style="text-align:left;">
test\_recall
</td>
<td style="text-align:left;">
0.000 (+/- 0.000)
</td>
<td style="text-align:left;">
0.999 (+/- 0.001)
</td>
</tr>
<tr>
<td style="text-align:left;">
test\_f1
</td>
<td style="text-align:left;">
0.000 (+/- 0.000)
</td>
<td style="text-align:left;">
1.000 (+/- 0.000)
</td>
</tr>
<tr>
<td style="text-align:left;">
test\_roc\_auc
</td>
<td style="text-align:left;">
0.500 (+/- 0.000)
</td>
<td style="text-align:left;">
1.000 (+/- 0.000)
</td>
</tr>
<tr>
<td style="text-align:left;">
test\_average\_precision
</td>
<td style="text-align:left;">
0.485 (+/- 0.000)
</td>
<td style="text-align:left;">
1.000 (+/- 0.000)
</td>
</tr>
</tbody>
</table>

We decided to use LogisticRregression classifier from the scikit-learn
pacakge (Pedregosa et al. 2011). To better understand the performance of
our selected models, we use the scoring metrics of accuracy, precision,
recall, f1, roc\_auc and average precision when doing cross validation.
The cross-validation scores for each model is summarized in the Table 1.
Besides the LogisticRegression classifier, we only built a
DummyClassifier as a baseline. We discovered that LogisticRegression
returned an extremely high cross-validation scores on all scoring
metrics we used. Except for recall, the other metrics are 1 which is the
highest score a model can reach.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>
Table 2. Confusion Matrix of Prediction Given by cross\_val\_predict
</caption>
<thead>
<tr>
<th style="text-align:left;">
</th>
<th style="text-align:right;">
Edible / Non-toxic
</th>
<th style="text-align:right;">
Poisonous / Toxic
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
edible
</td>
<td style="text-align:right;">
3345
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
poisonous
</td>
<td style="text-align:right;">
2
</td>
<td style="text-align:right;">
3152
</td>
</tr>
</tbody>
</table>

Hence, we would like to see the confusion matrix of prediction in cross
validation (Table 2). We can see that the TP(True Positive) is 3345 such
that for mushrooms that are edible, our Logistic Regression Classifier
identified all of them correctly as ‘edible.’ FP(False Positive) here is
0 given all the edible mushrooms are being correctly identified. TN(True
Negative) is 3125, for 3154 poisonous mushrooms in our train data set,
3152 of them are correctly identified as ‘poisonous’ while FN(False
Negative) is 2 since only 2 of them are being identified as ‘edible’
even though they are actually poisonous.

Given the formula of `recall`, we can see how the 0.99 recall score in
the Table 1 is calculated:

$$ recall = \\frac{TP}{TP+FN} = \\frac{3345}{3345+2} \\approx 0.99 $$

Given that our model is performing extremely better than we expected. We
did not do hyper-parameter optimization and directly applied it to the
test data set to evaluate our model. The confusion matrix of prediction
on the test data is given below (Table 3).

Test result is quite similar to the cross validation results. We can see
that the TP(True Positive) is 863 such that for mushrooms that are
edible, our Logistic Regression Classifier identified all of them
correctly as ‘edible.’ FP(False Positive) here is 0 given all the edible
mushrooms are being correctly identified. TN(True Negative) is 761, for
the total 762 poisonous mushrooms in our train data set, 761 of them are
correctly identified as ‘poisonous’ while FN(False Negative) is 1 since
only 1 of them are being identified as ‘edible’ even though it is
actually poisonous.

<table class="table" style="width: auto !important; margin-left: auto; margin-right: auto;">
<caption>
Table 3. Confusion Matrix of Prediction on Test Data
</caption>
<thead>
<tr>
<th style="text-align:left;">
</th>
<th style="text-align:right;">
Edible / Non-toxic
</th>
<th style="text-align:right;">
Poisonous / Toxic
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:left;">
edible
</td>
<td style="text-align:right;">
863
</td>
<td style="text-align:right;">
0
</td>
</tr>
<tr>
<td style="text-align:left;">
poisonous
</td>
<td style="text-align:right;">
1
</td>
<td style="text-align:right;">
761
</td>
</tr>
</tbody>
</table>

# Limitations & Assumptions

So, the recall score will be 0.99 while the rest scoring metrics will be
1 as well. The LogicsticRegression classifier is performing quite well
in predicting whether a mushroom is poisonous or edible. Given the
unexpected performance and high accuracy of our model, we decided to do
sanity checks from expert’s advice. First, we checked if there is the
class imbalance issue in our dataset. It turns out that we have no class
imbalance as the train data set contains 3334 edible mushrooms and 3154
poisonous mushrooms which are quite equally distributed. Also in the
test data set, there are 863 edible mushrooms and 762 poisonous
mushrooms which are not hugely imbalanced.Additionally, we checked if
our data set is too small that makes the accuracy of the model to be so
high. Given suggestion, the train data set contains 6499 observations
which are sufficient enough for model training and fitting.

In conclusion, the results of our model reliable. But there are still
some potential improvements we can made which will be discussed in the
next section.

# Looking Forward

In the future there are two key areas we would like to explore. Firstly,
we would like to conduct an analysis of feature importance to gain
insight into which features were most critical in predicting mushroom
toxicity. This could also potentially allow us to drop several features
while preserving model performance. With less features the model will
not only be less expensive computationally, but the potential costs of
gathering more data could also be drastically reduced. Secondly, we
would like to test our model on a real data set. While our model
performs remarkably well on the hypothetical samples of UC Irvine’s
Mushroom data set we cannot be fully confident until it has been tested
on real-world data. Ideally we will be able to find other data sets with
similar features. If not, it may be necessary to conduct our own
sampling in the field.

# References

Allaire, JJ, Yihui Xie, Jonathan McPherson, Javier Luraschi, Kevin
Ushey, Aron Atkins, Hadley Wickham, Joe Cheng, Winston Chang, and
Richard Iannone. 2020. *Rmarkdown: Dynamic Documents for r*.
<https://github.com/rstudio/rmarkdown>.

BC Centre for Disease Control. 2019 \[Online\]. “Mushroom Poisonings on
the Rise in British Columbia.”
<http://www.bccdc.ca/about/news-stories/stories/mushroom-poisonings-on-the-rise-in-british-columbia>.

Chaoqun, Zheng. 2019. “Recognition and Research of Poisonous Mushroom
Based on Machine Learning.” *Taigu: Shanxi Agricultural University,
Jinzhong, China*.

de Jonge, Edwin. 2020. *Docopt: Command-Line Interface Specification
Language*. <https://CRAN.R-project.org/package=docopt>.

Diaz, James H. 2005. “Evolving Global Epidemiology, Syndromic
Classification, General Management, and Prevention of Unknown Mushroom
Poisonings.” *Critical Care Medicine* 33 (2): 419–26.

Fukuwatari, Tsutomu, Etsuro Sugimoto, Kazumasa Yokoyama, and Katsumi
Shibata. 2001. “Establishment of Animal Model for Elucidating the
Mechanism of Intoxication by the Poisonous Mushroom Clitocybe
Acromelalga.” *Shokuhin Eiseigaku Zasshi. Journal of the Food Hygienic
Society of Japan* 42 (3): 185–89.

Lei, Chen, W Tangkanakul, L Lu, XQ Liu, C Jiraphongsa, and S Jetanasen.
2016. “Mushroom Poisoning Surveillance Analysis, Yunnan Province, China,
2001-2006.” *OSIR Journal* 1 (1): 8–11.

Min, LU, LI Yu, et al. 2006. “Present Status and Future Prospects of the
Mushroom Industry in China.” *Acta Edulis Fungi* 13 (01): 9.

Pedregosa, Fabian, Gaël Varoquaux, Alexandre Gramfort, Vincent Michel,
Bertrand Thirion, Olivier Grisel, Mathieu Blondel, et al. 2011.
“Scikit-Learn: Machine Learning in Python.” *Journal of Machine Learning
Research* 12 (Oct): 2825–30.

R Core Team. 2021. *R: A Language and Environment for Statistical
Computing*. Vienna, Austria: R Foundation for Statistical Computing.
<https://www.R-project.org/>.

Reynolds, WA, and FH Lowe. 1965. “Mushrooms and a Toxic Reaction to
Alcohol: Report of Four Cases.” *New England Journal of Medicine* 272
(12): 630–31.

Shuaichang, F, Y Xiaomei, and L Jian. 2020. “Toadstool Image Recognition
Based on Deep Residual Network and Transfer Learning.” *Journal of
Transduction Technology* 33: 74–83.

Tanaka, K, S Miyasaka, and T Inoue. 1996. “Histopathological Effects of
Illudin s, a Toxic Substance of Poisonous Mushroom, in Rat.” *Human &
Experimental Toxicology* 15 (4): 289–93.

Tegzes, John H, and Birgit Puschner. 2002. “Toxic Mushrooms.”
*Veterinary Clinics of North America: Small Animal Practice* 32 (2):
397–407.
https://doi.org/<https://doi.org/10.1016/S0195-5616(01)00012-2>.

Van Rossum, Guido, and Fred L Drake Jr. 1995. *Python Reference Manual*.
Centrum voor Wiskunde en Informatica Amsterdam.

White, Julian, Scott A Weinstein, Luc De Haro, Regis Bédry, Andreas
Schaper, Barry H Rumack, and Thomas Zilker. 2019. “Mushroom Poisoning: A
Proposed New Clinical Classification.” *Toxicon* 157: 53–65.

Wickham, Hadley. 2016. *Ggplot2: Elegant Graphics for Data Analysis*.
Springer-Verlag New York. <https://ggplot2.tidyverse.org>.

Wickham, Hadley, Mara Averick, Jennifer Bryan, Winston Chang, Lucy
D’Agostino McGowan, Romain François, Garrett Grolemund, et al. 2019.
“Welcome to the <span class="nocase">tidyverse</span>.” *Journal of Open
Source Software* 4 (43): 1686. <https://doi.org/10.21105/joss.01686>.

Xie, Yihui. 2020. *Knitr: A General-Purpose Package for Dynamic Report
Generation in r*. <https://yihui.org/knitr/>.

Zhifeng, Yang. 2019. “Application of Multi-Classifier Fusion Based on
Stacking Algorithm in Identification of Poisonous Mushrooms.” *Taigu:
Shanxi Agricultural University, Jinzhong, China*.
