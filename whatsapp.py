#############
#remliegrand#
#############

# TODO #
# Check plotly docs for amazing stuff

#All the imports you need and maybe even more !
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
from PIL import Image
from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop
import plotly.express as px
import re
import os
import requests
from bs4 import BeautifulSoup
from random import randint as rd

#I use it to center everything
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.title('Who am I ?') #Rémi, why are you Rémi and not Maximilien ?
    st.image('https://i.ibb.co/3FtLbQ3/28-EEB9-C5-129-E-4127-AEC7-D95044119-D8-B.jpg', width = 400)
    st.write('https://github.com/remliegrand')
    st.write('---')

with col3:
    st.write("")


#Gives a list of images from google with the word capital
def get_random_img(capital):
    urlcapital = 'https://www.google.com/search?q=' + capital + '&source=lnms&tbm=isch'
    pagecapital = requests.get(urlcapital)
    soupcapital = BeautifulSoup(pagecapital.text, 'html.parser')
    list_img = [x["src"] for x in soupcapital.find_all('img')][1:]
    r = rd(0, len(list_img)-1)
    return list_img[r]

#Did not take time to use scrapping for that part
listcapitals = ['Abu Dhabi',
 'Abuja',
 'Accra',
 'Adamstown',
 'Addis Ababa',
 'Algiers',
 'Alofi',
 'Amman',
 'Amsterdam',
 'Andorra la Vella',
 'Ankara',
 'Antananarivo',
 'Apia',
 'Ashgabat',
 'Asmara',
 'Astana',
 'Asunción',
 'Athens',
 'Avarua',
 'Baghdad',
 'Baku',
 'Bamako',
 'Bandar Seri Begawan',
 'Bangkok',
 'Bangui',
 'Banjul',
 'Basseterre',
 'Beijing',
 'Beirut',
 'Belgrade',
 'Belmopan',
 'Berlin',
 'Bern',
 'Bishkek',
 'Bissau',
 'Bogotá',
 'Brasília',
 'Bratislava',
 'Brazzaville',
 'Bridgetown',
 'Brussels',
 'Bucharest',
 'Budapest',
 'Buenos Aires',
 'Bujumbura',
 'Cairo',
 'Canberra',
 'Caracas',
 'Castries',
 'Cayenne',
 'Charlotte Amalie',
 'Chisinau',
 'Cockburn Town',
 'Conakry',
 'Copenhagen',
 'Dakar',
 'Damascus',
 'Dhaka',
 'Dili',
 'Djibouti',
 'Dodoma',
 'Doha',
 'Douglas',
 'Dublin',
 'Dushanbe',
 'Edinburgh of the Seven Seas',
 'El Aaiún',
 'Episkopi Cantonment',
 'Flying Fish Cove',
 'Freetown',
 'Funafuti',
 'Gaborone',
 'George Town',
 'Georgetown',
 'Georgetown',
 'Gibraltar',
 'Grytviken',
 'Guatemala City',
 'Gustavia',
 'Hagåtña',
 'Hamilton',
 'Hanga Roa',
 'Hanoi',
 'Harare',
 'Hargeisa',
 'Havana',
 'Helsinki',
 'Honiara',
 'Islamabad',
 'Jakarta',
 'Jamestown',
 'Jerusalem',
 'Ramallah and Gaza',
 'Juba',
 'Kabul',
 'Kampala',
 'Kathmandu',
 'Khartoum',
 'Kiev',
 'Kigali',
 'Kingston',
 'Kingston',
 'Kingstown',
 'Kinshasa',
 'Kuala Lumpur',
 'Kuwait City',
 'Libreville',
 'Lilongwe',
 'Lima',
 'Lisbon',
 'Ljubljana',
 'Lomé',
 'London',
 'Luanda',
 'Lusaka',
 'Luxembourg',
 'Madrid',
 'Majuro',
 'Malabo',
 'Malé',
 'Managua',
 'Manama',
 'Manila',
 'Maputo',
 'Marigot',
 'Maseru',
 'Mata-Utu',
 'Mbabane',
 'Melekeok',
 'Mexico City',
 'Minsk',
 'Mogadishu',
 'Monaco',
 'Monrovia',
 'Montevideo',
 'Moroni',
 'Moscow',
 'Muscat',
 'Nairobi',
 'Nassau',
 'Naypyidaw',
 "N'Djamena",
 'New Delhi',
 'Niamey',
 'Nicosia',
 'Nicosia',
 'Nouakchott',
 'Nouméa',
 'Nukuʻalofa',
 'Nuuk',
 'Oranjestad',
 'Oslo',
 'Ottawa',
 'Ouagadougou',
 'Pago Pago',
 'Palikir',
 'Panama City',
 'Papeete',
 'Paramaribo',
 'Paris',
 'Philipsburg',
 'Phnom Penh',
 'Plymouth',
 'Podgorica',
 'Port Louis',
 'Port Moresby',
 'Port Vila',
 'Port-au-Prince',
 'Port of Spain',
 'Porto-Novo',
 'Prague',
 'Praia',
 'Cape Town',
 'Pristina',
 'Pyongyang',
 'Quito',
 'Rabat',
 'Reykjavík',
 'Riga',
 'Riyadh',
 'Road Town',
 'Rome',
 'Roseau',
 'Saipan',
 'San José',
 'San Juan',
 'San Marino',
 'San Salvador',
 "Sana'a",
 'Santiago',
 'Santo Domingo',
 'São Tomé',
 'Sarajevo',
 'Seoul',
 'Singapore',
 'Skopje',
 'Sri Jayawardenepura Kotte',
 "St. George's",
 'St. Helier',
 "St. John's",
 'St. Peter Port',
 'St. Pierre',
 'Stanley',
 'Stepanakert',
 'Stockholm',
 'La Paz',
 'Sukhumi',
 'Suva',
 'Taipei',
 'Tallinn',
 'Tarawa',
 'Tashkent',
 'Tbilisi',
 'Tegucigalpa',
 'Tehran',
 'Thimphu',
 'Tirana',
 'Tiraspol',
 'Tokyo',
 'Tórshavn',
 'Tripoli',
 'Tskhinvali',
 'Tunis',
 'Ulan Bator',
 'Vaduz',
 'Valletta',
 'The Valley',
 'Vatican City',
 'Victoria',
 'Vienna',
 'Vientiane',
 'Vilnius',
 'Warsaw',
 'Washington',
 'Wellington',
 'West Island',
 'Willemstad',
 'Windhoek',
 'Abidjan',
 'Yaoundé',
 'Yaren',
 'Yerevan',
 'Zagreb']

#Bonus scrapping for coronavirus
url = 'https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
covid = str(soup.select("div[class='maincounter-number']"))

st.title('''Rediscovering your....''')
if(st.button("Click here for a funny program")): 

    st.image('https://logos-marques.com/wp-content/uploads/2020/09/WhatsApp-logo.png') #Are we on whatsapp or what ?
    st.write("Here is how everything works (btw I hope you have an iPhone):")
    st.write("Firstly, you need to download a whatsapp conversation on your phone, and export the conversation without medias.")
    st.write("Once it's done, you can unzip the file and put the file chat.txt on the sidebar !")
    st.write("Check out this youtube tutorial !")
    st.video('https://youtu.be/dTzxw1YQHk0') #The tutoria I did

#Allows to upload the .txt on the straemlit
uploaded_file = st.sidebar.file_uploader(label = "HERE HERE HERE !!!!! THIS IS THE PLACE I'M TALKING ABOUT", type=["txt"])
if uploaded_file:
    st.image('https://logos-marques.com/wp-content/uploads/2020/09/WhatsApp-logo.png')
    content = str(uploaded_file.read(),"utf-8")

    #We use the whatsapp format to split the messages between them : [16/02/2021 16:12:37] MIREN: Bonjour
    l = re.split(r"(\[\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}\])", content)
    l2 = []
    for string in l:
        newString = mod_string = re.sub(r"\u200e$", '', string )
        l2.append(newString)
    l2 = l2[3:]

    texts = []
    for i in range(0, len(l2), 2):
        texts.append(l2[i] + l2[i + 1])

    # Transforming the list in a Dataframe because I did not learn to use pandas for no reason.
    df = pd.DataFrame (texts,columns=['texts'])

    st.write('---')
    #Part where I find all capitals talked about in the conversation
    capitals = []
    def findcapitals(word_list, a_string):
        return set(word_list).intersection(a_string.split())

    for word in findcapitals(listcapitals, str(texts)):
        capitals.append(word)
    #I remove Paris if others are here because as a parisian it is highly probable that Paris is in the conversation commonly
    if len(capitals) > 0:
        if (len(capitals) > 1) and ('Paris' in capitals):
            capitals.remove('Paris')
        capital = random.choice(capitals)
        st.image(get_random_img(capital), width = 500)
        st.write('Before anything, feel free to take a little look back to your old trip in', capital,'here: https://fr.wikipedia.org/wiki/' + capital)

    st.write('You can find here all the texts presented to you in a very "brupt" form')
    st.dataframe(df.style.highlight_max(axis=0))


    # I simply removes the first character '\u200e' if it is in the message so it does not bother me afterwards for dates and so on.
    def cut_if_image(row):
        if row[0] == '\u200e':
            return row[1:]
        return row
    df.texts = df.texts.map(cut_if_image)


    # Getting the date in a new column and converting it in a pandas date format
    df.loc[df['texts'].notnull(), 'Text Time'] = df['texts'].str[1:20]
    df["Text Time"]= df["Text Time"].map(pd.to_datetime)

    # Same for the content of the text
    df.loc[df['texts'].notnull(), 'Message'] = df['texts'].str[21:]

    # As each line with a picture starts with '\u200e', I chefor each line which is a picture.
    # df['is_image'] = re.match('\u200e', df['Message'])
    df['is_image'] = df.texts.str.contains('\u200e', flags=re.IGNORECASE, regex=True, na=False)

    # Taking the name in the texts column, as there is ':' in the hour and after the name, we split and take the [1] elements which is all the time the name of the person.
    text = []
    name = ''
    lName = []
    for index, row in df.iterrows():
        text = row.Message.split(':')
        name = text[0]
        text = text[1:]
        df.loc[index, 'Message'] = ":".join(text)
        lName.append(name)
    df['Name'] = lName

    # Various functions that speak for themselves and that will be used later on for date and time analysis.

    def get_dom(dt):
        return dt.day
    def get_weekday(dt): 
        return dt.weekday() 
    def get_hour(dt):
        return dt.hour
    def get_date(dt):
        return dt.date()
    def count_rows(rows):
        return len(rows)


    # Creating new columns thanks to the conversion in pandas date that will be used for analysis
    df['Day'] = df['Text Time'].map(get_dom)
    df['Weekday']= df['Text Time'].map(get_weekday)
    df['Hour'] = df['Text Time'].map(get_hour)
    df['Date'] = df['Text Time'].map(get_date)
    st.write('---')

    # The DataFrame is ready now !
    overalltime = (df["Date"][-1:] - df["Date"][0]).dt.days
    st.write('And here they are in a way more "ordered" way, with all informations you can neeed for any kind of analysis of your conversation over ', int(overalltime), ' days !')
    st.dataframe(df.style.highlight_max(axis=0))
    st.write('---')

    # Gives the number of texts by giving the number of rows in the df
    number_of_text = count_rows(df)
    st.write('In this conversation, there are ', number_of_text, ' texts')
    st.write('---')

    # Gives the number of images by giving the number of 1 in the column made thanks to the line [[ df['is_image'] = df.texts.str[0] == '\u200e' ]]
    number_of_images = df['is_image'].values.sum()
    st.write('In this conversation, there are ', number_of_images, ' images')
    df3 = df[['Name','is_image']].groupby(['Name']).apply(lambda x : x['is_image'].map(lambda y: y).sum())
    st.write(df3)

    st.write('---')
    st.write('''Now, let's play a little game that you might enjoy.\n Below are 5 texts that are picked randomly in the conversation and that are displayed below.''')

    # I think the line above speaks for itself, but we take 5 random number between 0 and the size of the df and prints them
    x = st.slider('Number of texts you want to see', min_value = 1, max_value = 50, value = 5)  
    for i in range(x):
        texts[random.randint(0, len(df))]

    st.write('---')

    st.write('You can find below a bar graph representing which days of the month we used to text the most with the number of texts sent')

    # Simple hist described above
    fig = px.histogram(df[["Day"]], nbins = 31, title ='Number of texts per day of the month').update_layout(bargap = .2);
    st.write(fig)

    # Counts and orders the more frequent days of the month
    day_count = df['Day'].value_counts()
    day_count

    st.write('---')

    st.write('You can find below a bar graph representing which days of the week we used to text the most with the number of texts sent')

    # Simple hist described above
    fig = px.histogram(df[["Weekday"]], nbins = 31, title ='Number of texts per weekday');
    fig.update_xaxes(tickmode = 'array',
                     tickvals = [i for i in range(7)],
                     ticktext=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    st.write(fig)

    # Counts and orders the more frequent days of the month
    day_count = df['Weekday'].value_counts()
    day_count

    st.write('---')

    st.write('You can find below a bar graph representing which hour of the day we used to text the most with the number of texts sent')

    # Simple hist described above
    fig = px.histogram(df[["Hour"]], nbins = 24, title ='Number of texts per hour of the day').update_layout(bargap = .2);
    st.write(fig)

    # Counts and orders the more frequent hours
    hour_count = df['Hour'].value_counts()
    hour_count

    st.write('---')

    st.write('You can find below a bar graph representing which week we used to text the most with the number of texts sent')
    df["Date"] = df["Date"].astype("datetime64")

    # Simple hist described above
    fig = px.histogram(df[["Date"]], title ='Number of texts per week').update_layout(bargap = .2);
    st.write(fig)

    # Counts and orders the more frequent days where texts got sent
    date_count = df['Date'].value_counts()
    date_count

    st.write('---')

    st.write('You can find below a bar graph representing which emojies we used to used to sent')
    emojies = []

    # Functions only used here (so far) to find the more used characters in a list. 
    def most_frequent(List):
        return max(set(List), key = List.count)

    # Going through the list and adding an emoji to the list emojies if it is found, ord(j) > 9999 because ASCII says so
    for i in df['Message']:
        for j in i:
            if ord(j) > 9999:
                emojies.append(j)

    # Simple hist for emojies
    fig = px.histogram(emojies, title ='Number of emojies in all the texts');
    st.write(fig)


    most_freq_emojies = most_frequent(emojies)
    st.write('And more specifically, the most frequently used emoji in the texts is:', most_freq_emojies)

    st.write('---')

    # Wordcloud made from the messages and with all french stopwords removed
    st.write('And else you have here a little wordcloud of all the most used words in the conv.')
    stop_whatsapp = ['c', 'jpg', 'pièce jointe','jointe' ,'image absente', 'image', 'absente', 'vidéo absente', 'audios omis', 'j', 'vidéo', 'l', 'audio', 'omis', 'GIF retiré', 't','d', 'PHOTO', 'pièce', 'https', 'www', 'GIF', 'retiré']
    fr_stop.update(stop_whatsapp)
    wordcloud1 = WordCloud(background_color = 'black', stopwords = fr_stop, width = 1920, height = 1080)
    wc1 = wordcloud1.generate_from_text(' '.join(df['Message'].to_list()))
    st.image(wc1.to_array())
    
    st.write('---')

    #Wordcloud per person
    option = st.selectbox('Select someone you want to check his or her wordcloud', np.unique(df.Name))
    st.write('Below is a wordcloud made from the words used the most by', option)
    wordcloud = WordCloud(background_color = 'black', stopwords = fr_stop, width = 1920, height = 1080)
    wc = wordcloud.generate_from_text(' '.join(df.loc[df.Name == option,'Message'].to_list()))

    # Wordcloud converted to an array so st.image can be applied on it
    st.image(wc.to_array())
    st.write('---')

    # Here I am working on the list, this is why there is the - 29 that looks like going out of nowhere
    st.write('''Who sends more texts ? Let's find out !!!''')

    df1 = df.groupby(['Name']).count()
    df1['Name'] = df1.index
    fig = px.pie(df1, values='Message', names='Name')
    st.write(fig)
    df2 = df[['Name','Message']].groupby(['Name']).apply(lambda x : st.write(x))
    st.write(df2)


    st.write('---')
    st.write('''But the more texts does not mean the more things to say, what if texts are longer ?''')
    df1 = df[['Name','Message']].groupby(['Name']).apply(lambda x : x['Message'].map(lambda y: len(y)).mean())
    st.write(df1)

if(st.button("Click here for a little web scrapping about your favorite subject later on")):
    
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")

    with col2:
        st.title("Just in case you forgot about the pandemic, here are today's statistics :")
        st.image("https://global.unitednations.entermediadb.net/assets/mediadb/services/module/asset/downloads/preset/Libraries/Production+Library/09-11-2020-NIAID-SARS-COV-2-virus-particles.jpg/image1170x530cropped.jpg")
        st.title("At this day, there are :")
        st.write(covid[59:70])
        st.write('people who caught covid')
        st.title('AND')
        # st.write(covid[126:135])
        # st.write('people who died from covid')
        # st.write('---')
        st.write(covid[213:224])
        st.write('people who recovered from covid')

    with col3:
        st.write("")


    #############
    #remliegrand#
    #############