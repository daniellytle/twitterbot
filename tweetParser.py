# tweetParser.py #
# Alex Quinlan (quinlal) #

import sys, json, os
from pprint import pprint

if len(sys.argv) != 2:
	print 'wrong number of arguments. proper usage: python tweetParser.py <file-containing tweets>\nExample: python live.py tweets.json'
	sys.exit(0)

tweetFile = sys.argv[1]

tweets = open(tweetFile, 'r')

states = {
		'AK': 1,'AL': 2,'AR': 3,'AZ': 4,'CA': 5,'CO': 6,'CT': 7,'DE': 8,'FL': 9,'GA': 10,'HI': 11,'IA': 12,'ID': 13,'IL': 14,'IN': 15,
        'KS': 16,'KY': 17,'LA': 18,'MA': 19,'MD': 20,'ME': 21,'MI': 22,'MN': 23,'MO': 24,
        'MS': 25,
        'MT': 26,
        'NC': 27,
        'ND': 28,
        'NE': 29,
        'NH': 30,
        'NJ': 31,
        'NM': 32,
        'NV': 33,
        'NY': 34,
        'OH': 35,
        'OK': 36,
        'OR': 37,
        'PA': 38,
        'RI': 39,
        'SC': 40,
        'SD': 41,
        'TN': 42,
        'TX': 43,
        'UT': 44,
        'VA': 45,
        'VT': 46,
        'WA': 47,
        'WI': 48,
        'WV': 49,
        'WY': 50,
        'Alaska': 1,
        'Alabama': 2,
        'Arkansas': 3,
        'Arizona': 4,
        'California': 5,
        'Colorado': 6,
        'Connecticut': 7,
        'Delaware': 8,
        'Florida': 9,
        'Georgia': 10,
        'Hawaii': 11,
        'Iowa': 12,
        'Idaho':13,
        'Illinois':14,
        'Indiana':15,
        'Kansas':16,
        'Kentucky':17,
        'Louisiana':18,
        'Massachusetts':19,
        'Maryland':20,
        'Maine':21,
        'Michigan':22,
        'Minnesota':23,
        'Missouri':24,
        'Mississippi':25,
        'Montana':26,
        'North Carolina':27,
        'North Dakota':28,
        'Nebraska':29,
        'New Hampshire':30,
        'New Jersey':31,
        'New Mexico':32,
        'Nevada':33,
        'New York':34,
        'Ohio':35,
        'Oklahoma':36,
        'Oregon':37,
        'Pennsylvania':38,
        'Rhode Island':39,
        'South Carolina':40,
        'South Dakota':41,
        'Tennessee':42,
        'Texas':43,
        'Utah':44,
        'Virginia':45,
        'Vermont':46,
        'Washington':47,
        'Wisconsin':48,
        'West Virginia':49,
        'Wyoming':50
}

idToState = {
25 :"Mississippi",
36 :"Oklahoma",
8 :"Delaware",
23 :"Minnesota",
14 :"Illinois",
3 :"Arkansas",
32 :"New Mexico",
15 :"Indiana",
18 :"Louisiana",
43 :"Texas",
48 :"Wisconsin",
16 :"Kansas",
7 :"Connecticut",
5 :"California",
49 :"West Virginia",
10 :"Georgia",
28 :"North Dakota",
38 :"Pennsylvania",
1 :"Alaska",
24 :"Missouri"
,41 :"South Dakota"
,6 :"Colorado"
,31 :"New Jersey"
,47 :"Washington"
,34 :"New York"
,33 :"Nevada"
,20 :"Maryland"
,13 :"Idaho"
,50 :"Wyoming"
,4 :"Arizona"
,12 :"Iowa"
,22 :"Michigan"
,44 :"Utah"
,45 :"Virginia"
,37 :"Oregon"
,26 :"Montana"
,30 :"New Hampshire"
,19 :"Massachusetts"
,40 :"South Carolina"
,46 :"Vermont"
,9 :"Florida"
,11 :"Hawaii"
,17 :"Kentucky"
,39 :"Rhode Island"
,29 :"Nebraska"
,35 :"Ohio"
,2 :"Alabama"
,27 :"North Carolina"
,42 :"Tennessee"
,21 :"Maine"
}

stateIds = {
1 : {}, 
2 : {}, 
3 : {}, 
4 : {}, 
5 : {}, 
6 : {}, 
7 : {}, 
8 : {}, 
9 : {}, 
10 : {}, 
11 : {}, 
12 : {}, 
13 : {}, 
14 : {}, 
15 : {}, 
16 : {}, 
17 : {}, 
18 : {}, 
19 : {}, 
20 : {}, 
21 : {}, 
22 : {}, 
23 : {}, 
24 : {}, 
25 : {}, 
26 : {}, 
27 : {}, 
28 : {}, 
29 : {}, 
30 : {}, 
31 : {}, 
32 : {}, 
33 : {}, 
34 : {}, 
35 : {}, 
36 : {}, 
37 : {}, 
38 : {}, 
39 : {}, 
40 : {}, 
41 : {}, 
42 : {}, 
43 : {}, 
44 : {}, 
45 : {}, 
46 : {}, 
47 : {}, 
48 : {}, 
49 : {}, 
50 : {}, 
}


for tweet in tweets:

	tweet = tweet.strip()

	if tweet is not '':
		t = json.loads(tweet)
		place = ''
		text = ''
		id = -1

		if t.get('id'):
			id = t['id']

		if t.get('text'):
			text = t['text'].encode('ascii', 'ignore')

		if t.get('place'):

			if t['place']['country_code'].encode('ascii', 'ignore') == 'US':
				place = t['place']['full_name'].encode('ascii', 'ignore')
				space = place.rfind(' ') + 1
				locCode = place[space:]
				if len(locCode) == 3:
					locCode = place[:space-2]
				if locCode in states:
					location = states[locCode]
				if location in stateIds:
					stateIds[location][id] = text
		else:
			continue

for x in stateIds:
	print "STATE: ", idToState[x], ' ID: ', x, "\nTweets: ", stateIds[x]