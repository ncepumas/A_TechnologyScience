#install.packages("units")
setwd("D:A_TechnologyScience/R/lm/code")
library(spdep)
data(boston)
BostonData <- boston.c
colnames(BostonData)
lm_model <- lm(MEDV~.-TOWN-TOWNNO-TRACT-LON-CMEDV,data = BostonData)
summary(lm_model)

step_lm_model <- step(lm_model,trace = 0)
summary(step_lm_model)

par(mfrow=c(2,2))
plot(step_lm_model)

re<-rstudent(step_lm_model)
shapiro.test(re)
#取对数
#正则项