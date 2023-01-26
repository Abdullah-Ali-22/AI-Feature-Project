#load the model
#/Users/abdullahali/Desktop/Work-Folder/Intern_project
import pickle
lodeed_pickle_mode=pickle.load(open("/Users/abdullahali/Desktop/Work-Folder/Intern_project/AI_feature_model.pkl","rb"))
import pandas as pd
weather_d = {
"Cloudy":  [1, 0, 0, 0, 0, 0 ],
"Foggy":  [0, 1, 0, 0, 0, 0 ],
"Rainy":  [0, 0, 1, 0, 0, 0 ],
"Sunny":  [0, 0, 0, 1, 0, 0 ],
"Windy":[0, 0, 0, 0, 1, 0 ],
"Snowing": [0, 0, 0, 0, 0, 1 ],
}
Event_d = {
"No":  [1,0],
"Yes":  [0,1]
}
Day_week_d = {
"Friday":    [1, 0, 0, 0, 0],
"Monday":  [0, 1, 0, 0, 0],
"Thursday":   [0, 0, 1, 0, 0],
"Tuesday": [0, 0, 0, 1, 0],
"Wednesday":    [0, 0, 0, 0, 1]
}
#Day_week_Monday	Day_week_Saturday	Day_week_Sunday	Day_week_Thursday	Day_week_Tuesday	Day_week_Wednesday
#Weather_Foggy	Weather_Rainy	Weather_Sunny	Weather_Windy	Weather_snowing
#Sunny','Cloudy','Windy','Rainy','Foggy','snowing'

Places_free = int(input("Please Enter the number Places_free "))
weather = input("Please enter the weather on that day (i.e. Foggy, Rainy, Sunny, Windy, Snowing) ")
Event = input("Will be an Event on that day? (i.e. Yes, No)")
Day_week = input("Please enter the the Day you want to book (i.e. Monday, Tuesday, Thursday, Wednesday, Friday) ")

l = [Places_free] +  weather_d[weather] + Event_d[Event]  + Day_week_d[Day_week] 
data_predict = {
        'Places_free':   [l[0]],
        'Weather_Cloudy':[l[1]],
        'Weather_Foggy': [l[2]],
        'Weather_Rainy': [l[3]],
        'Weather_Sunny': [l[4]],
        'Weather_Windy': [l[5]],
        'Weather_snowing': [l[6]],
        'Event_No': [l[7]],
        'Event_Yes':[l[8]],
    
        'Day_week_Friday':  [l[9]],
        'Day_week_Monday':  [l[10]],
        'Day_week_Thursday':[l[11]],                     
        'Day_week_Tuesday': [l[12]],
        'Day_week_Wendesday': [l[13]]


}
#print(l)
# Create DataFrame
df_test = pd.DataFrame(data_predict)
#print(df_test)
predicted_days=lodeed_pickle_mode.predict(df_test)
if predicted_days==0:
    print("our AI Feature recommended you to book your workplace today as we expected")
else:
    print("\n If you are not sure to book now our AI Feature predict that you will be still able to find a place if you book in the next {} Days".format(predicted_days))