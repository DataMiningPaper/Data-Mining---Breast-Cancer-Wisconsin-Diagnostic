import matplotlib.pyplot as plt

def parse_percent_block(text):
    values = []
    for token in text.replace('%', ' ').split():
        token = token.replace(',', '.')
        if not token:
            continue
        v = float(token)
        values.append(v)
    return values


# inserted percentage data for recall

rf_recall_text = """
95,28%
96,23%
96,70%
96,23%
97,17%
97,17%
97,64%
98,11%
98,11%
97,64%
97,64%
97,64%
97,64%
98,11%
98,11%
98,11%
98,11%
98,58%
97,64%
97,64%
98,11%
98,11%
98,58%
98,11%
98,58%
98,11%
98,11%
98,11%
98,11%
99,06%
99,06%
98,58%
99,06%
99,06%
99,53%
100,00%
"""

# J48 – recall
j48_recall_text = """
92,92%
93,87%
92,45%
93,87%
95,75%
95,28%
95,28%
94,81%
96,23%
97,17%
97,17%
97,17%
97,17%
96,70%
96,70%
97,17%
96,23%
97,17%
96,70%
96,70%
96,70%
97,17%
97,17%
98,11%
98,58%
98,11%
98,58%
98,58%
98,58%
99,53%
100,00%
"""

# Naive Bayes – recall
naive_recall_text = """
89,62%
90,09%
90,09%
90,09%
90,09%
90,09%
90,09%
90,09%
90,09%
90,09%
90,57%
91,04%
91,04%
91,04%
91,51%
91,98%
92,45%
92,92%
92,92%
92,92%
93,40%
93,40%
93,40%
93,40%
93,40%
93,40%
93,40%
93,40%
93,40%
93,40%
93,40%
93,40%
93,87%
93,87%
93,87%
93,87%
"""

# Bayes Net – recall
bayesnet_recall_text = """
93,40%
94,34%
93,87%
93,87%
94,81%
94,81%
94,34%
94,81%
93,87%
94,34%
94,34%
94,34%
94,34%
93,87%
94,34%

99,06%
99,06%
99,06%
100,00%
100,00%
100,00%
"""

# OneR – recall
oner_recall_text = """
86,79%
87,74%
90,09%
92,92%
93,40%
94,81%
95,75%
96,23%
94,81%
94,81%
95,75%
96,70%
97,17%
96,70%
96,70%
97,64%
98,11%
99,53%
99,53%
99,53%
99,53%
100,00%
100,00%
"""

# Functions Logistic – recall
function_recall_text = """
94,81%
97,17%
97,17%
97,64%
97,17%
97,17%
97,64%
97,17%
98,11%
98,11%
98,11%
98,58%
99,06%
99,53%
99,53%
98,58%

99,53%
99,53%
99,53%
99,53%
99,53%
99,53%
100,00%
100,00%
100,00%
100,00%
100,00%
"""


# changed to lists
rf_recall        = parse_percent_block(rf_recall_text)
j48_recall       = parse_percent_block(j48_recall_text)
naive_recall     = parse_percent_block(naive_recall_text)
bayesnet_recall  = parse_percent_block(bayesnet_recall_text)
oner_recall      = parse_percent_block(oner_recall_text)
function_recall  = parse_percent_block(function_recall_text)

# insert false negative data
rf_fn = [
    15,10,8,7,8,6,6,5,4,4,5,5,5,5,4,4,4,4,
    3,5,5,4,4,3,4,3,4,4,4,4,2,2,3,2,2,1,0
]

j48_fn = [
    15, 13, 16, 13, 9, 10, 10, 11, 8, 6, 6, 6, 6, 7, 7, 6, 8,
    6, 7, 7, 7, 6, 6, 4, 3, 4, 3, 3, 3, 1, 0
]

naive_fn = [
    22, 21, 21, 21, 21, 21, 21, 21, 21, 21,
    20, 19, 19, 19, 18, 17, 16, 15, 15, 15,
    14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
    14, 14, 13, 13, 13, 13
]

bayesnet_fn = [
    14, 12, 13, 13, 11, 11, 12, 11, 13, 12,
    12, 12, 12, 13, 12, 2, 2, 2, 0, 0, 0
]

oner_fn = [
    28, 26, 21, 15, 14, 11, 9, 8, 11, 11,
    9, 7, 6, 7, 7, 5, 4, 1, 1, 1, 1, 0, 0
]

function_fn = [
    11, 6, 6, 5, 6, 6, 5, 6, 4, 4, 4, 3, 2, 1, 1, 3,
    1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0
]

# inserted into directory

algorithms_recall = {
    "Random Forest": {
        "fn": rf_fn,
        "rec": rf_recall,
    },
    "J48": {
        "fn": j48_fn,
        "rec": j48_recall,
    },
    "Naive Bayes": {
        "fn": naive_fn,
        "rec": naive_recall,
    },
    "Bayes Net": {
        "fn": bayesnet_fn,
        "rec": bayesnet_recall,
    },
    "OneR": {
        "fn": oner_fn,
        "rec": oner_recall,
    },
    "Functions Logistic": {
        "fn": function_fn,
        "rec": function_recall,
    },
}
# plotted recall vs false negatives

plt.figure(figsize=(8, 5))

markers    = ['o', '^', 's', 'D', 'x', '+']
linestyles = ['-', '--', '-.', ':', '-', '--']

for i, (name, data) in enumerate(algorithms_recall.items()):
    fn   = data["fn"]
    rec  = data["rec"]

    # changed length to a similar one
    n = min(len(fn), len(rec))
    x = fn[:n]
    y = rec[:n]

    plt.plot(
        x, y,
        marker=markers[i % len(markers)],
        linestyle=linestyles[i % len(linestyles)],
        label=name
    )

plt.xlabel("False Negatives")
plt.ylabel("recall (%)")
plt.title("recall vs. False Negatives für alle Algorithmen")
plt.ylim(80, 100)   # if necessary changed to 80/100
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
