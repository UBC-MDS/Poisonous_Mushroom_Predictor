# author: Kyle Maj
# date: 2020-11-26

"This script produces an EDA plot and saves it to the data folder as eda_plot.png
Usage: eda.R
" -> doc


library(tidyverse)
library(readr)
library(dplyr)
library(ggplot2)
library(gridExtra)

mushrooms <- read_csv("../data/processed/train_df.csv")

mushrooms$`stalk_root` <- na_if(mushrooms$`stalk_root`, "?")

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


filename <- "../results/eda_plot.png"
ggsave(filename = filename, plot_all, device = "png", width=10, height=20)