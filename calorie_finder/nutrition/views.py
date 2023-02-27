from django.shortcuts import render
# Create your views here.
from .forms import CalorieCalc
from .api import Api

food_items=[]
workout={}

def Home(req):
    if req.method=="POST":
        extract_food_items(req.POST);
        if(extract_workout_data(req.POST)):
            calories_burned=Calorie_Burn(workout);
        else:
            calories_burned=0;
        #giving the cleaned data to api
        total_nutritions=total_nutrition((Api(food_items)))

        return render(req,'show_report.html',{'calories_gain':total_nutritions['calories'],'calories_loss':calories_burned,'nutrition':total_nutritions})
        #total Calores burn
    else:
        pass
    form=CalorieCalc();
    return render(req,'Home.html',{'form':form})

def extract_food_items(data):
    i=1;
    while(True):
        try:
             food_items.append(data[f'food{i}'])
        except:
            break;
        i+=1;

def extract_workout_data(data):
    workName=[]
    print('In Extract_workout ')
    for i in data:
        if i[0:len(i)-1] == 'workoutn':
            workName.append(data[i])
            print('appended')
    i=1;
    if len(workName)==0:
        return -1;
    while(i<=len(workName)):
        try:
            workout[f'{workName[i-1]}']=data[f'workouth{i}']
        except:
            pass
        i+=1;
    print('safely exiting')
    return 1;

def Calorie_Burn(workout):
    chart={
'pushup':7,
'squat':8,
'lunge':6,
'situps':3,
'burpee':10,
'jumping rope':15,
'plank':3,
'running':11,
'swimming':4,
'jumping':13,
}
    calories_burned=0;
    print('Workouts', workout )
    for i in workout:
      
        if i.lower() in chart.keys():
            print('found workout')
            calories_burned+=chart[i.lower()]*int(workout[i]);
    print('calories burned',calories_burned)
    return calories_burned;

def total_nutrition(food_details):
    calories_gain=0
    fat_gain=0;
    cholestrol_gain=0;
    carbohydrates_gain=0;
    sugar=0;
    for food in food_details:
        calories_gain+=(food_details[food][0]['calories'])
        fat_gain+= food_details[food][0]['fat_total_g']
        cholestrol_gain+= food_details[food][0]['cholesterol_mg']
        carbohydrates_gain+= food_details[food][0]['carbohydrates_total_g']
        sugar+= food_details[food][0]['sugar_g']
    total_nutritions={'calories':calories_gain,'fat':fat_gain,'cholestrol':cholestrol_gain,'carbohydrates':carbohydrates_gain,'sugar':sugar}
    return total_nutritions
