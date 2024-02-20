import pandas as pd

df = pd.read_csv("adult.data.csv")

def calculate_demographic_data(print_data=True):
    # Read data from fileq
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men = df[df['sex'] == 'Male']
    average_age = men['age'].mean()
    average_age_men = round(average_age,1)

    # What is the percentage of people who have a Bachelor's degree?
    count_Bachelor = df["education"].value_counts().get("Bachelors", 0)
    total_rows = df.shape[0]
    per_bachelor = (count_Bachelor / total_rows) * 100
    percentage_bachelors = round(per_bachelor, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    high_earners_df = higher_education[higher_education['salary'].isin(['>50K'])]
    higher_education_advanced = higher_education.shape[0]
    high_earning_advanced = high_earners_df.shape[0]
    h_e_r = (high_earning_advanced / higher_education_advanced) * 100
    higher_education_rich = round(h_e_r, 1)
    
    lower_earners_df = lower_education[lower_education['salary'].isin(['>50K'])]
    lower_education_advanced = lower_education.shape[0]
    lower_earning_advanced = lower_earners_df.shape[0]
    l_e_r = (lower_earning_advanced / lower_education_advanced) * 100
    lower_education_rich = round(l_e_r, 1)
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df['hours-per-week'].isin([1]).sum()
    all_min_workers = df[df['hours-per-week'].isin([1])]
    min_rich_workers = all_min_workers[all_min_workers['salary'].isin(['>50K'])]
    rich_percentage = (min_rich_workers.shape[0] / all_min_workers.shape[0] * 100)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts()/ df['native-country'].value_counts() * 100).sort_values(ascending=False).fillna(0).idxmax()
    highest_earning_country_percentage = round(len(df[(df['native-country'] == highest_earning_country) & (df['salary'] == '>50K')]) / len(df[(df['native-country'] == highest_earning_country)])*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['salary'] == ">50K") & (df['native-country'] == "India")]["occupation"].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
