#Install packages
install.packages(c('RPostgres',"DBI","RODBC","odbc","dplyr","dbplyr","plotrix","knitr","ggplotpie"))

#Load packages
library (RPostgres)
library (DBI)
library (RODBC)
library (odbc)
library (dplyr)
library (dbplyr)
library(ggplot2)
library(ggplotpie)
library(knitr)

#Database connection (!!! Type in your data !!!)
con1 <- dbConnect (RPostgres::Postgres(),
                     dbname = "postgres" ,
                     host = "127.0.0.1" , 
                     port = 5432,
                     user = "postgres", 
                     password = "timon1998" 
)
con1

#Load all datasets

#All athletes (Umbenennung der Spalte in gleiche ID zum mergen)
athletes_df <- dbGetQuery(con1, "SELECT * FROM athlete")
colnames(athletes_df)[6] <- "athleten_ID"
View(athletes_df)

#Alle Trainingsdaten (Umbenennung der Spalte in gleiche ID zum mergen)
training_data_df <- dbGetQuery(con1, "SELECT * FROM training_data")
colnames(training_data_df)[1] <- "athleten_ID"
colnames(training_data_df)[6] <- "trainings_ID"
View(training_data_df)

#Alle Trainings (Umbenennung der Spalte in gleiche ID zum mergen)
training_df <- dbGetQuery(con1, "SELECT * FROM training")
colnames(training_df)[3] <- "trainings_ID"
View(training_df)

#Mergen von ID´s der Trainings_ID und dem Trainingsnamen im Trainingssatz und dem Trainingsdatensatz
merged_data_df1 <- merge(training_df, training_data_df, by = "trainings_ID")
View(merged_data_df1)

#Mergen von ID´s der Athleten und der Namen im Athletendatensatz und dem Trainingsdatensatz
merged_data_df <- merge(athletes_df, training_data_df, by = "athleten_ID")
View(merged_data_df)

#Mergen aller Datensätze
merged_data_df2 <- merge(training_df, merged_data_df, by = "trainings_ID")
View(merged_data_df2)





#---------------------------------------
#Aufgaben:
#All workouts of a specific athlete
kable(athletes_df)
eingabe_ahtlete_ID <- as.numeric(readline("Bitte geben Sie die Athleten ID ein: "))
trainingdata_Person_df <-merged_data_df2[merged_data_df2$athleten_ID == eingabe_ahtlete_ID,]
View(trainingdata_Person_df)


#Average over training duration of a certain athlete over all trainings (ID Eingeben der Person)
kable(athletes_df)
eingabe_ahtlete_ID <- as.numeric(readline("Bitte geben Sie die Athleten ID ein: "))
trainingdata_Person_average <- merged_data_df2[merged_data_df2$athleten_ID == eingabe_ahtlete_ID,]
#Anzeigen der gefilterten Daten
View(trainingdata_Person_average)
trainingdata_Person_average %>%
  summarize(duration = mean(duration, na.rm = TRUE))



#Average of the training duration of a specific training of an athlete (ID Eingeben der Person & ID des Trainings)
kable(athletes_df)
eingabe_ahtlete_ID <- as.numeric(readline("Bitte geben Sie die Athleten ID ein: "))
trainingsdescription_ID <- unique((merged_data_df1[1:3]))
kable(trainingsdescription_ID)
eingabe_training_ID <- as.numeric(readline("Bitte geben Sie die Trainings ID ein: "))
trainingdata_Training_athelete_average <- merged_data_df2[merged_data_df2$athleten_ID == eingabe_ahtlete_ID & merged_data_df2$trainings_ID == eingabe_training_ID,]
#Anzeigen der gefilterten Daten
View(trainingdata_Training_athelete_average)
trainingdata_Training_athelete_average %>%
  summarize(duration = mean(duration, na.rm = TRUE))



#Average of the training duration of a certain training over all athletes
kable(trainingsdescription_ID)
eingabe_training_ID <- as.numeric(readline("Bitte geben Sie die Trainings ID ein: "))
trainingdata_Training_average <- merged_data_df2[merged_data_df2$trainings_ID == eingabe_training_ID,]
#Anzeigen der gefilterten Daten
View(trainingdata_Training_average)
trainingdata_Training_average %>%
  summarize(duration = mean(duration, na.rm = TRUE))



#Median of the training duration of a certain training over all athletes
kable(trainingsdescription_ID)
eingabe_training_ID <- as.numeric(readline("Bitte geben Sie die Trainings ID ein: "))
trainingdata_Training_median <- merged_data_df2[merged_data_df2$trainings_ID == eingabe_training_ID,]
#Anzeigen der gefilterten Daten
View(trainingdata_Training_median)
trainingdata_Training_median %>%
  summarize(median = median(duration, na.rm = TRUE))



#Standard deviation of the training duration of a certain training over all athletes
kable(trainingsdescription_ID)
eingabe_training_ID <- as.numeric(readline("Bitte geben Sie die Trainings ID ein: "))
trainingdata_Training_sd <- merged_data_df2[merged_data_df2$trainings_ID == eingabe_training_ID,]
#Anzeigen der gefilterten Daten
View(trainingdata_Training_sd)
trainingdata_Training_sd %>%
  summarize(standard_deviation = sd(duration, na.rm = TRUE))



#All training duration values of a specific training in  (Anzeige der einzelnen Duration einer Trainingseinheit)
ggplot(merged_data_df1, aes(x = text_course_description , y = duration)) +
  geom_bar(stat = "identity",fill = "lightblue", color = "black")+ 
  ggtitle("Duration of each Training over time")+
  ylab("Duration")+
  xlab("Training")+
  scale_x_discrete(limits = unique(merged_data_df1$text_course_description))+
  geom_text(aes(label = duration), position = position_stack(vjust = 0.5))




#All training duration values of a specific training in ggplot (Anzeige der Gesamtlänge eines Trainings)
merged_data_df5 <- merged_data_df2 %>% group_by(text_course_description) %>% 
  summarize(duration = round(sum(duration), 2))
ggplot(merged_data_df5, aes(x = text_course_description , y = duration)) +
  geom_bar(stat = "identity",fill = "lightblue", color = "black")+ 
  ggtitle("Duration of each Training over time")+
  ylab("Duration")+
  xlab("Training")+
  scale_x_discrete(limits = unique(merged_data_df1$text_course_description))+
  geom_text(aes(label = duration), position = position_stack(vjust = 0.5))


#Boxplot of all trainings
ggplot(merged_data_df2, aes(x=as.character(text_course_description), y=duration)) +
  geom_boxplot(fill="steelblue") +
  labs(title="Boxplot of all trainings",x ="Training", y="Duration")



#Average of the training duration over all athletes (i.e. per athlete average of the training duration over all trainings)
aggregated_data <- merged_data_df2 %>%
  group_by(text_athlete_name ) %>%
  summarize(average_duration = round(mean(duration),2))
ggplot(aggregated_data, aes(x = text_athlete_name, y = average_duration)) +
  geom_bar(stat = "identity",fill = "lightblue", color = "black")+
  ggtitle("Average duration of each Athlete over all trainings")+
  ylab("Duration in h")+
  xlab("Athlete")+
  scale_x_discrete(limits = unique(merged_data_df2$text_athlete_name))+
  geom_text(aes(label = average_duration), vjust = -0.5, size = 4)


#-------------------------------------
#Features
#Recognize target group age of all trainings
merged_data_df$age <- merged_data_df$age%%10000
age_counts <- table(merged_data_df[,"age"])
pie(age_counts)
pie(age_counts, labels = paste(names(age_counts),"\n", round((age_counts/sum(age_counts))*100, 2),"%"), col = rainbow(length(age_counts)), main = "Target group age of all trainings")

#Identify target group age of a particular training
merged_data_df$age <- merged_data_df$age%%10000
kable(trainingsdescription_ID)
eingabe_training_ID <- as.numeric(readline("Bitte geben Sie die Trainings ID ein: "))
df_filtered <- merged_data_df %>% filter(trainings_ID == eingabe_training_ID)
age_counts <- table(df_filtered[,"age"])
pie(age_counts)
pie(age_counts, labels = paste(names(age_counts),"\n", round((age_counts/sum(age_counts))*100, 2),"%"), col = rainbow(length(age_counts)), main = "Target group age of 'Rückentraining'")

#Gender distribution for all trainings
gender_counts <- table(merged_data_df[,"gender_variable"])
pie(gender_counts)
pie(gender_counts, labels = paste(names(gender_counts),"\n", round((gender_counts/sum(gender_counts))*100, 2),"%"), col = rainbow(length(gender_counts)), main = "Gender distribution of all trainings")


#Gender distribution in a particular training
gender_counts <- table(merged_data_df[,"gender_variable"])
kable(trainingsdescription_ID)
eingabe_training_ID <- as.numeric(readline("Bitte geben Sie die Trainings ID ein: "))
df_filtered <- merged_data_df %>% filter(trainings_ID == eingabe_training_ID)
gender_counts <- table(df_filtered[,"gender_variable"])
pie(gender_counts)
pie(gender_counts, labels = paste(names(gender_counts),"\n", round((gender_counts/sum(gender_counts))*100, 2),"%"), col = rainbow(length(gender_counts)), main = "Gender distribution of 'Rückentraining'")

#Bar-chart with number of athletes for each training and the age distribution
merged_data_df2$age <- merged_data_df2$age%%10000
merged_data_df2 %>% 
  group_by(text_course_description, age) %>%
  summarise(count = n()) %>%
  ggplot(aes(x=text_course_description, y=count, fill=age)) +
  geom_bar(stat='identity', position='dodge') +
  ggtitle("Participants count by Training ID and Age") +
  xlab("Trainings course") + ylab("Count")
  scale_color_gradient(low = "blue", high = "red")
  scale_fill_gradientn(colors = c("#87CEFA", "#00008B"))


sessionInfo()
  