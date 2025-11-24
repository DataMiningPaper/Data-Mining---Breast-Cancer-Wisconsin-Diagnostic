import matplotlib.pyplot as plt

#helpfunctions for percentage data preparations
def parse_percent_block(text):
    values = []
    for token in text.replace('%', ' ').split():
        token = token.replace(',', '.')
        if not token:
            continue
        v = float(token)
       
        if v > 1000:
            v = v / 100.0
        values.append(v)
    return values


#data which was created in weka for the single algorithms

# Random Forest – Accuracy
rf_acc_text = """
95,7821%
9666,0800%
95,9578%
95,7821%
95,0791%
94,5518%
93,6731%
93,3216%
93,1459%
92,4429%
92,4429%
91,9156%
91,2127%
91,7399%
91,3884%
91,2127%
90,8612%
91,0369%
91,3884%
90,5097%
89,6309%
89,1037%
89,8067%
89,6309%
89,2794%
89,2794%
88,0492%
88,4007%
88,5764%
87,6977%
88,2250%
87,1705%
87,5220%
86,9947%
86,4675%
75,7469%
53,4271%
"""

# Random Forest – Precision
rf_prec_text = """
95,63%
95,73%
93,15%
96,70%
91,07%
89,18%
87,29%
86,25%
85,60%
84,21%
84,49%
83,47%
82,14%
83,13%
82,21%
81,89%
81,25%
81,57%
81,96%
80,86%
79,31%
78,20%
79,39%
78,87%
78,49%
78,28%
76,47%
77,04%
77,32%
75,91%
76,36%
74,73%
75,45%
74,47%
73,68%
60,63%
44,44%
"""

# J48 – Accuracy
j48_acc_text = """
93,3216%
94,5518%
93,6731%
93,6731%
94,0246%
94,0246%
92,6186%
92,4429%
92,6186%
92,6186%
91,9156%
91,7399%
91,3884%
91,0369%
91,3884%
91,3884%
90,8612%
89,6309%
88,7522%
88,9279%
87,6977%
82,4253%
83,3040%
80,6678%
79,4376%
80,3163%
71,8805%
45,8699%
45,87%
41,65%
37,26%
"""

# J48 – Precision
j48_prec_text = """
89,55%
91,71%
90,74%
93,87%
89,04%
89,38%
86,32%
86,27%
85,71%
85,12%
83,74%
83,40%
82,73%
82,33%
83,00%
82,73%
82,26%
79,54%
78,24%
78,54%
76,49%
68,67%
69,83%
66,24%
64,71%
65,82%
57,10%
40,66%
40,66%
38,93%
37,26%
"""

# Bayes Net – Accuracy
bayesnet_acc_text = """
95,08%
94,90%
94,73%
94,90%
94,90%
95,08%
94,55%
94,55%
94,38%
94,55%
94,55%
94,02%
94,02%
93,15%
93,15%
41,48%
41,48%
41,48%
37,26%
37,26%
37,26%
"""

# Bayes Net – Precision
bayesnet_prec_text = """
93,40%
92,17%
92,13%
92,56%
91,78%
92,20%
91,32%
90,95%
91,28%
91,32%
91,32%
90,09%
90,09%
88,44%
88,11%
38,82%
38,82%
38,82%
37,26%
37,26%
37,26%
"""

# OneR – Accuracy
oner_acc_text = """
90,16%
88,58%
89,10%
86,82%
85,76%
86,12%
83,66%
82,95%
82,43%
82,43%
77,68%
74,34%
70,47%
68,89%
62,21%
63,80%
58,52%
49,91%
49,91%
49,91%
49,91%
46,05%
46,05%
"""

# OneR – Precision
oner_prec_text = """
86,79%
82,67%
82,33%
76,65%
74,72%
74,72%
70,73%
69,62%
69,31%
69,31%
63,24%
59,59%
55,98%
54,67%
54,67%
50,74%
47,27%
42,63%
42,63%
42,63%
42,63%
40,85%
40,85%
"""

# Functions Logistic – Accuracy
function_acc_text = """
97,1880%
97,1880%
96,3093%
95,4306%
94,5518%
93,8489%
93,3216%
93,8489%
94,2004%
93,3216%
92,9701%
92,2671%
92,4429%
91,7399%
90,6854%
90,5097%
70,2988%
70,4745%
67,6626%
69,9473%
69,9473%
69,5958%
66,4323%
66,4323%
66,0808%
65,9051%
65,7293%
"""

# Functions Logistic – Precision
function_prec_text = """
97,57%
95,37%
93,21%
90,79%
89,18%
87,66%
86,25%
87,66%
87,76%
85,95%
85,25%
83,60%
83,67%
82,10%
80,23%
80,38%

55,67%
55,82%
53,55%
55,38%
55,38%
55,09%
52,61%
52,61%
52,35%
52,22%
52,09%
"""

# Naive Bayes – Accuracy
naivebyas_acc_text = """
92,97%
92,97%
92,97%
92,97%
92,97%
92,97%
92,97%
92,97%
92,97%
92,97%
93,15%
92,79%
92,79%
92,97%
93,15%
93,32%
93,50%
93,50%
93,32%
93,50%
93,50%
93,50%
93,32%
93,32%
93,32%
93,32%
93,32%
93,32%
93,32%
93,32%
93,32%
93,32%
93,32%
93,32%
93,32%
"""

# Naive Bayes – Precision
naivebyas_prec_text = """
91,35%
90,95%
90,95%
90,95%
90,95%
90,95%
90,95%
90,95%
90,95%
90,95%
90,57%
90,61%
89,77%
89,77%
89,81%
89,86%
89,91%
89,95%
89,95%
89,55%
89,59%
89,59%
89,59%
89,19%
89,19%
89,19%
89,19%
89,19%
89,19%
89,19%
89,19%
89,19%
88,84%
88,84%
88,84%
88,84%
"""


#create the python lists
rf_accuracy   = parse_percent_block(rf_acc_text)
rf_precision  = parse_percent_block(rf_prec_text)

j48_accuracy  = parse_percent_block(j48_acc_text)
j48_precision = parse_percent_block(j48_prec_text)

bayesnet_accuracy  = parse_percent_block(bayesnet_acc_text)
bayesnet_precision = parse_percent_block(bayesnet_prec_text)

oner_accuracy = parse_percent_block(oner_acc_text)
oner_precision = parse_percent_block(oner_prec_text)

function_accuracy = parse_percent_block(function_acc_text)
function_precision = parse_percent_block(function_prec_text)

naivebyas_accuracy = parse_percent_block(naivebyas_acc_text)
naivebyas_precision = parse_percent_block(naivebyas_prec_text)


#methods for the index-plots
methods = {
    "Random Forest": {
        "acc": rf_accuracy,
        "prec": rf_precision,
        "marker": "o",
        "linestyle": "-"
    },
    "J48": {
        "acc": j48_accuracy,
        "prec": j48_precision,
        "marker": "^",
        "linestyle": "--"
    },
    "Bayes Net": {
        "acc": bayesnet_accuracy,
        "prec": bayesnet_precision,
        "marker": "s",
        "linestyle": "-."
    },
    "OneR": {
        "acc": oner_accuracy,
        "prec": oner_precision,
        "marker": "+",
        "linestyle": "-"
    },
    "Functions Logistic": {
        "acc": function_accuracy,
        "prec": function_precision,
        "marker": "o",
        "linestyle": "--"
    },
    "Naive Bayes": {
        "acc": naivebyas_accuracy,
        "prec": naivebyas_precision,
        "marker": "^",
        "linestyle": "-."
    },
}



#false-negative data for each algorithmen

rf_false_negatives = [
    15, 10, 8, 7, 8, 6, 6, 5, 4, 4, 5, 5, 5, 5, 4, 4, 4, 4,
    3, 5, 5, 4, 4, 3, 4, 3, 4, 4, 4, 4, 2, 2, 3, 2, 2, 1, 0
]

j48_false_negatives = [
    15, 13, 16, 13, 9, 10, 10, 11, 8, 6, 6, 6, 6, 7, 7, 6, 8,
    6, 7, 7, 7, 6, 6, 4, 3, 4, 3, 3, 3, 1, 0
]

naive_false_negatives_raw = [
    22, 21, 21, 21, 21, 21, 21, 21, 21, 21,
    20, 19, 19, 19, 18, 17, 16, 15, 15, 15,
    14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
    14, 14, 13, 13, 13, 13
]

naive_false_negatives = naive_false_negatives_raw[:35]

bayesnet_false_negatives = [
    14, 12, 13, 13, 11, 11, 12, 11, 13, 12,
    12, 12, 12, 13, 12, 2, 2, 2, 0, 0, 0
]

oner_false_negatives = [
    28, 26, 21, 15, 14, 11, 9, 8, 11, 11,
    9, 7, 6, 7, 7, 5, 4, 1, 1, 1, 1, 0, 0
]

function_false_negatives = [
    11, 6, 6, 5, 6, 6, 5, 6, 4, 4, 4, 3, 2, 1, 1, 3,
    1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0
]

#check for security
print("RF  :", len(rf_false_negatives),       len(rf_accuracy))
print("J48 :", len(j48_false_negatives),      len(j48_accuracy))
print("NB  :", len(naive_false_negatives),    len(naivebyas_accuracy))
print("BNet:", len(bayesnet_false_negatives), len(bayesnet_accuracy))
print("OneR:", len(oner_false_negatives),     len(oner_accuracy))
print("Func:", len(function_false_negatives), len(function_accuracy))


#plot the graph: accuracy vs false-negatives for all algorithms

algorithms_fn = {
    "Random Forest": {
        "fn": rf_false_negatives,
        "acc": rf_accuracy,
    },
    "J48": {
        "fn": j48_false_negatives,
        "acc": j48_accuracy,
    },
    "Naive Bayes": {
        "fn": naive_false_negatives,
        "acc": naivebyas_accuracy,
    },
    "Bayes Net": {
        "fn": bayesnet_false_negatives,
        "acc": bayesnet_accuracy,
    },
    "OneR": {
        "fn": oner_false_negatives,
        "acc": oner_accuracy,
    },
    "Functions Logistic": {
        "fn": function_false_negatives,
        "acc": function_accuracy,
    },
}

plt.figure(figsize=(8, 5))

markers = ['o', '^', 's', 'D', 'x', '+']
linestyles = ['-', '--', '-.', ':', '-', '--']

for i, (name, data) in enumerate(algorithms_fn.items()):
    fn  = data["fn"]
    acc = data["acc"]

    if len(fn) != len(acc):
        print(f"Attention: Lengths are wrong for {name} (FN={len(fn)}, ACC={len(acc)})")
        continue

    plt.plot(
        fn,
        acc,
        marker=markers[i % len(markers)],
        linestyle=linestyles[i % len(linestyles)],
        label=name
    )

plt.xlabel("False Negatives")
plt.ylabel("Accuracy in %")
plt.title("Accuracy vs. False Negatives for all algorithms")
plt.ylim(0, 100)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
