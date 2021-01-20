# Fitbit Time Series Project

## About the Project
### Goals
- Clean the current data set. Document the code that take the original source to the workable data.
- Draw conclusions on the individual who wore the fitness tracker
- Make predictions on the two weeks of missing data
### Background
Scenario:
>A man wearing a lab coat and a worried expression bursts into your office.
>
>"I need help!" he says. "I mixed up the labels and have one extra!"
>
>Before you can ask what he has an extra of, he throws a USB thumb drive in your direction. As you wonder who still uses thumb drives, the man in the lab coat rushes back out the door.
>
>"Oh, and I need to know what the missing next 2 weeks will look like too" he says on his way out.
>
>Before you can think of a question to ask, he's out of sight.
>
>You open up the files on the drive and find the data.
>
>Even though you just started a week ago, as a data scientist for Big Research Co., you know several things:
>
>- Your company is running multiple different experiments: drug trials, testing different fitness equipment, and some "very ethical" human experimentation.
>- Everyone in every experiment wears a fitbit.
>- No one seems to have time for smalltalk.
>- Everyone on staff has a fitbit.
>
>It's a pretty good guess that this data comes from somebody's fitbit, but you don't know who it belongs to, it could be from someone participating in a research experiment, or a staff member just going about their days.


### Deliverables
- A notebook containing my analysis
- Predictions for the missing two weeks worth of data in a separate csv file.
- The above information distilled into two slides that can be shared with a general audience. Include at least one visualization, and make sure that the visualization is clearly labeled.

### Acknowledgments
- Data
- Codeup Curriculum

## Data Dictionary

## Initial Thoughts & Hypotheses
### Thoughts
- The data is mostly the activity of the individual including: date, calories burned, steps, distance, floors, minutes, sedentary, minutes lightly active, minutes fairly active, minutes very active, activity calories.
- These will be the features worth exploring
- Data is from April of 2018 to the end of the year
- Food log, and calories in sections are inconsistent and should be omitted since the majority are null values.
- May need to change some of the features to match the data
- Going to look into the calories burned over time.
- What part of the year does this individual burn the most calories?
- Does this individual burn more calories on the weekends?
- Based on activity level can we determine how fit this individual is?

### Hypotheses
- The steps and calories burned have a direct correlation.
- This individual burns more calories in the summertime.
- Floors and calories burned have a direct correlation.

## Project Steps
### Acquire
1. Import necessary modules
  - pandas
  - numpy
  - matplotlib
  - seaborn
2. Clean up the data in an spreadsheet for easier reading into a Pandas DataFrame
  - Food log and Calories in sections are mostly null so they were eliminated
  - Saved to a CSV in local repository
3. Peeked into and summarized data (columns, rows, data types, nulls, etc.)
 
### Prepare
1. Data Cleaning (*prepare.py*)
  - Dropped last 22 days/rows since we will be predicting them (they were null).
  - Lowercase the features, use a '_' to replace whitespace (best practice convention).
  - Change `date` column --> 'datetime' type
  - Change the index --> `date`, sorted index by date
  - Drop remaining `date` column
  - Change the commas in `calories_burned`, `steps`, `minutes_sedentary`, `activity_calories` --> '_'
  - Change columns to 'int' type
2. Summarized the preppared data
3. Plotted the Distribution of each variable

### Explore
### Model
### Conclusions

## How to Reproduce
### Steps
### Tools & Requirements

## License

## Creators

