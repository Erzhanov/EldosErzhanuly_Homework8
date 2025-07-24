# Мәтінді Өңдеуге Арналған Веб Қосымша

Бұл жоба — табиғи тілдерді өңдеуге (NLP) арналған Streamlit және Transformers кітапханалары арқылы жасалған веб-қосымша. Қосымша пайдаланушыға мәтін бойынша түрлі NLP тапсырмаларын, мысалы, атаулы нысандарды тану (NER) секілді функцияларды орындауға мүмкіндік береді.

## ЕСКЕРТУ БҰЛ МОДЕЛ ТЕК АҒЫЛШЫН ТІЛІНДЕ ЖҰМЫС ЖАСАЙДЫ! ТӨМЕНДЕ ТЕКСЕРУГЕ АРНАЛҒАН МӘТІНДЕР:
1)Benjamin Franklin (January 17, 1706 [O.S. January 6, 1705][Note 1] – April 17, 1790) was an American polymath: a writer, scientist, inventor, statesman, diplomat, printer, publisher and political philosopher.[1] Among the most influential intellectuals of his time, Franklin was one of the Founding Fathers of the United States; a drafter and signer of the Declaration of Independence; and the first postmaster general.[2]

Born in the Province of Massachusetts Bay, Franklin became a successful newspaper editor and printer in Philadelphia, the leading city in the colonies, publishing The Pennsylvania Gazette at age 23.[3] He became wealthy publishing this and Poor Richard's Almanack, which he wrote under the pseudonym "Richard Saunders".[4] After 1767, he was associated with the Pennsylvania Chronicle, a newspaper known for its revolutionary sentiments and criticisms of the policies of the British Parliament and the Crown.[5] He pioneered and was the first president of the Academy and College of Philadelphia, which opened in 1751 and later became the University of Pennsylvania. He organized and was the first secretary of the American Philosophical Society and was elected its president in 1769. He was appointed deputy postmaster-general for the British colonies in 1753,[6] which enabled him to set up the first national communications network.

2)Kazakhstan,[d] officially the Republic of Kazakhstan,[e] is a landlocked country primarily in Central Asia, with a small portion in Eastern Europe.[f] It borders Russia to the north and west, China to the east, Kyrgyzstan to the southeast, Uzbekistan to the south, and Turkmenistan to the southwest, with a coastline along the Caspian Sea. Its capital is Astana, while the largest city and leading cultural and commercial hub is Almaty.

Kazakhstan is the world's ninth-largest country by land area and the largest landlocked country. Hilly plateaus and plains account for nearly half its vast territory, with lowlands composing another third; its southern and eastern frontiers are composed of low mountainous regions. Kazakhstan has a population of 20 million and one of the lowest population densities in the world, with fewer than 6 people per square kilometre (16 people/sq mi).[15] Ethnic Kazakhs constitute a majority, while ethnic Russians form a significant minority. Officially secular, Kazakhstan is a Muslim-majority country with a sizeable Christian community.

Kazakhstan has been inhabited since the Paleolithic era. In antiquity, various nomadic Iranian peoples such as the Saka, Massagetae, and Scythians dominated the territory, with the Achaemenid Persian Empire expanding towards the south. Turkic nomads entered the region from the sixth century. In the 13th century, the area was subjugated by the Mongol Empire under Genghis Khan. Following the disintegration of the Golden Horde in the 15th century, the Kazakh Khanate was established over an area roughly corresponding with modern Kazakhstan. By the 18th century, the Kazakh Khanate had fragmented into three jüz (tribal divisions), which were gradually absorbed and conquered by the Russian Empire; by the mid-19th century, all of Kazakhstan was nominally under Russian rule.[16] Following the 1917 Russian Revolution and subsequent Russian Civil War, it became an autonomous republic of the Russian SFSR within the Soviet Union. Its status was elevated to that of a union republic in 1936. The Soviet government settled Russians and other ethnicities in the republic, which resulted in ethnic Kazakhs being a minority during the Soviet era. Kazakhstan was the last constituent republic of the Soviet Union to declare independence in 1991 during its dissolution.





## Файлдар

```
text_app/
├── app.py               # Streamlit веб-қосымшасының негізгі логикасы
├── requirements.txt     # Қажетті кітапханалар тізімі
└── README.md            # Жобаның құжаттамасы
```

## Installation

Орнату
Жобаны орнату үшін келесі қадамдарды орындаңыз:

1)Репозиторийді көшіріп алыңыз немесе жоба файлдарын жүктеп алыңыз.
2)Жоба орналасқан қалтаға өтіңіз.

3)Виртуалды орта жасаңыз (қосымша, бірақ ұсынылады):
   ```
   python -m venv venv
   ```
4. Виртуалды ортаны іске қосыңыз:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Қажетті тәуелділіктерді орнатыңыз:
   ```
   pip install -r requirements.txt
   ```

## Қосымшаны Іске Қосу

Streamlit веб-қосымшасын іске қосу үшін терминалға келесі команданы енгізіңіз:
```
streamlit run app.py
```
Егерде сізде терминалда қате деп шығарса, онда келесі қадамды көріңіз:
```
python -m streamlit run "(app.py файлы тұрған орынды көрсетіңіз.)" #Мысалы python -m streamlit run "C\Users\Eldos\OneDrive\Рабочий стол\text_app\app.py"
```

Бұл әрекет қосымшаны іске қосып, оны әдепкі браузерде ашады.



## Мүмкіндіктері

- **Атаулы Нысандарды Тану (NER)**: Қосымша енгізілген мәтіндегі адам, ұйым, орын сияқты атаулы нысандарды анықтап, ерекшелеп көрсетеді.

- **Қарапайым Интерфейс**: Қосымшада қолдануға ыңғайлы әрі түсінікті интерфейс бар. Пайдаланушы мәтін енгізіп, нәтижелерді оңай көре алады.

## Қолдану Тәртібі

1)Талдау жасағыңыз келетін мәтінді енгізу аймағына жазыңыз.
2)"Анықтау" батырмасын басыңыз.
3)Қосымша мәтінді өңдеп, табылған нысандарды ерекшелеп көрсетеді.

## Лицензия

Бұл жоба MIT лицензиясы бойынша таратылған. Толығырақ мәліметті LICENSE файлын ашып көре аласыз.
