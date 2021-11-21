# Poisonous Mushroom Predictor
</div>

  - authors: Dongxiao Li, Kyle Maj, Mahmoodur Rahman 

Data analysis project executed by Group 4.0 of 6th Cohort (2021-22)
for DSCI 522 (Data Science workflows); a course in the Master of Data 
Science program at the University of British Columbia.

## Background

Mushrooms are species of fungus, of which some can be eaten with meaty 
texture and few types are toxic [1]. Annually, a significant number of 
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

In this project, two machine-learning models, namely logistic regression 
and support vector machine (SVM), are used to predict toxic mushrooms 
considering detection of poisonous mushroom being a binary feature. We will 
see how our model performs in classifies unknown mushrooms. 
Data used in this project is from UCI machine learning repository, provided 
by Jeff Schlimmer of the Audubon Society Field Guide to North American 
Mushrooms [18](https://archive-beta.ics.uci.edu/ml/datasets/mushroom). 
The dataset has 8124 examples and 22 features with 2 possible target classes 
(edible and poisonous). The features are cap-shape, cap-surface, cap-color, 
bruises, odor, gill-spacing, gill-attachment, gill-size, gill-color, 
stalk-shape, stalk-root, stalk-surface-above-ring, stalk-surface-below-ring, 
stalk-color-above-ring, stalk-color-below-ring, veil- type, veil-color, 
ring-number, ring-type, spore-print-color, population, and habitat. 




The data set that was used in this project is of digitized breast cancer
image features created by Dr. William H. Wolberg, W. Nick Street, and
Olvi L. Mangasarian at the University of Wisconsin, Madison (Street,
Wolberg, and Mangasarian 1993). It was sourced from the UCI Machine
Learning Repository (Dua and Graff 2017) and can be found
[here](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+\(Diagnostic\)),
specifically [this
file](http://mlr.cs.umass.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data).
Each row in the data set represents summary statistics from measurements
of an image of a tumour sample, including the diagnosis (benign or
malignant) and several other measurements (e.g., nucleus texture,
perimeter, area, etc.). Diagnosis for each image was conducted by
physicians.












## Report

The final report can be found
[here](https://ttimbers.github.io/breast_cancer_predictor/doc/breast_cancer_predict_report.html).

## Usage

There are two suggested ways to run this analysis:

#### 1\. Using Docker

*note - the instructions in this section also depends on running this in
a unix shell (e.g., terminal or Git Bash)*

To replicate the analysis, install
[Docker](https://www.docker.com/get-started). Then clone this GitHub
repository and run the following command at the command line/terminal
from the root directory of this project:

    docker run --rm -v /$(pwd):/home/rstudio/breast_cancer_predictor ttimbers/bc_predictor:v4.0 make -C /home/rstudio/breast_cancer_predictor all

To reset the repo to a clean state, with no intermediate or results
files, run the following command at the command line/terminal from the
root directory of this project:

    docker run --rm -v /$(pwd):/home/rstudio/breast_cancer_predictor ttimbers/bc_predictor:v4.0 make -C /home/rstudio/breast_cancer_predictor clean

#### 2\. Without using Docker

To replicate the analysis, clone this GitHub repository, install the
[dependencies](#dependencies) listed below, and run the following
command at the command line/terminal from the root directory of this
project:

    make all

To reset the repo to a clean state, with no intermediate or results
files, run the following command at the command line/terminal from the
root directory of this project:

    make clean

## Dependencies

  - Python 3.7.4 and Python packages:
      - docopt=0.6.2
      - requests=2.22.0
      - pandas=0.25.1R
      - feather-format=0.4.0
  - R version 3.6.1 and R packages:
      - knitr=1.26
      - feather=0.3.5
      - tidyverse=1.3.0
      - caret=6.0-85
      - ggridges=0.5.2
      - ggthemes=4.2.0
  - GNU make 4.2.1

## License

The Breast Cancer Predictor materials here are licensed under the
Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If
re-using/re-mixing please provide attribution and link to this webpage.

# References

<div id="refs" class="references hanging-indent">

<div id="ref-Dua2019">

Dua, Dheeru, and Casey Graff. 2017. “UCI Machine Learning Repository.”
University of California, Irvine, School of Information; Computer
Sciences. <http://archive.ics.uci.edu/ml>.

</div>

<div id="ref-Streetetal">

Street, W. Nick, W. H. Wolberg, and O. L. Mangasarian. 1993. “Nuclear
feature extraction for breast tumor diagnosis.” In *Biomedical Image
Processing and Biomedical Visualization*, edited by Raj S. Acharya and
Dmitry B. Goldgof, 1905:861–70. International Society for Optics;
Photonics; SPIE. <https://doi.org/10.1117/12.148698>.

</div>



    
    
    
4    http://www.bccdc.ca/about/news-stories/stories/mushroom-poisonings-on-the-rise-in-british-columbia
    5 https://www.zoology.ubc.ca/~biodiv/mushroom/
    
    
  