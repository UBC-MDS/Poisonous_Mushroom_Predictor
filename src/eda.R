# author: Group 4
# date: 2020-11-26


"This script produces an EDA plot and saves it to the data folder as eda_plot.png
Usage: src/eda.r --train=<train> --out_dir=<out_dir>
  
Options:
--train=<train>     Path (including filename) to train data
--out_dir=<out_dir> Path to directory where the plots should be saved
" -> doc

# Example
# Rscript src/eda.r --train='data/processed/train_df.csv' --out_dir='results/eda_plot.png'


library(tidyverse)
library(readr)
library(docopt)
library(dplyr)
library(ggplot2)
library(gridExtra)

opt <- docopt(doc)


main <- function(train, out_dir){
  mushrooms <- read_csv(train)
  
  mushrooms$class <- as.character(mushrooms$class)
  
  features <- c("class",
                "cap_shape",
                "cap_surface",
                "cap_color",
                "bruises",
                "odor",
                "gill_attachment",
                "gill_spacing",
                "gill_size",
                "gill_color",
                "stalk_shape",
                "stalk_root",
                "stalk_surface_above_ring",
                "stalk_surface_below_ring",
                "stalk_color_above_ring",
                "stalk_color_below_ring",
                "veil_type",
                "veil_color",
                "ring_number",
                "ring_type",
                "spore_print_color",
                "population",
                "habitat")
  colnames(mushrooms) <- features
  
  mush_features <- colnames(mushrooms)[-1]
  
  gp <- map(mush_features, function(x) {
    ggplot(data=mushrooms,
           aes(x = eval(parse(text=x)), fill = class)) +
      geom_bar() +
      xlab(x) +
      scale_fill_manual("target",
                        values = c("0" = "salmon",
                                   "1" = "purple")) +
      ggtitle("") + theme_bw()})
  
  
  options(repr.plot.width = 15, repr.plot.height = 30)
  plot_all <- do.call("grid.arrange", c(gp, ncol = 3))
  
  ggsave(filename = out_dir, plot_all, device = "png", width=10, height=20)
  
}

main(opt[["--train"]], opt[["--out_dir"]])



