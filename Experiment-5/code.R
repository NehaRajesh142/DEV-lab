install.packages("dplyr")
install.packages("ggplot2")
library(dplyr)
library(ggplot2)
data("mtcars")
df <- mtcars
df$car <- rownames(mtcars)
rownames(df) <- NULL
cat("Original Data Frame (First 5 Rows):\n")
print(head(df, 5))
df_selected <- df %>% select(mpg, cyl, hp, car)
cat("\nSelected Columns (mpg, cyl, hp, car):\n")
print(head(df_selected))
df_renamed <- df_selected %>% rename(Mileage = mpg, Cylinders = cyl, HorsePower = hp)
cat("\nRenamed Columns:\n")
print(head(df_renamed))
df_mutated <- df_renamed %>% mutate(HP_per_Cyl = HorsePower / Cylinders)
cat("\nNew Variable Added (HP_per_Cyl):\n")
print(head(df_mutated))
df_dropped <- df_mutated %>% select(-HorsePower)
cat("\nDropped Column (HorsePower):\n")
print(head(df_dropped))
df_filtered <- df_dropped %>% filter(Mileage > 20)
cat("\nFiltered Rows (Mileage > 20):\n")
print(df_filtered)
df_filtered[1, "Mileage"] <- NA
df_filtered <- rbind(df_filtered, df_filtered[2, ]) 
df_no_na <- df_filtered %>% na.omit()
cat("\nRemoved NA Rows:\n")
print(df_no_na)
df_no_dup <- df_no_na %>% distinct()
cat("\nRemoved Duplicate Rows:\n")
print(df_no_dup)
ggplot(df_no_dup, aes(x = Cylinders, y = Mileage, label = car)) +
  geom_point(color = "blue", size = 3) +
  geom_text(nudge_y = 0.5, size = 3) +
  theme_minimal() +
  ggtitle("Cleaned Data: Mileage vs Cylinders")
