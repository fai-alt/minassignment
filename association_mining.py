import random
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# 1. Simulate Transaction Data (3 Marks)
# Pool of at least 8 unique items
items_pool = ['Bread', 'Milk', 'Eggs', 'Cheese', 'Butter', 'Apples', 'Bananas', 'Chicken', 'Juice', 'Cereal']

# Generate at least 10 transactions, each with 2-5 items
num_transactions = 10
transactions = []
for _ in range(num_transactions):
    num_items = random.randint(2, 5)
    transaction = random.sample(items_pool, num_items)
    transactions.append(transaction)

# Display the simulated transactions
print('Simulated Transactions:')
for i, t in enumerate(transactions, 1):
    print(f'Transaction {i}: {t}')

# 2. Analyze with Apriori (4 Marks)
# Convert to one-hot encoded DataFrame
all_items = sorted(set(item for t in transactions for item in t))
one_hot = []
for t in transactions:
    row = {item: (item in t) for item in all_items}
    one_hot.append(row)
df = pd.DataFrame(one_hot)

print('\nOne-hot encoded DataFrame:')
print(df)

# Use Apriori algorithm to find frequent itemsets (min support 0.3)
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)
print('\nFrequent Itemsets (support >= 0.3):')
print(frequent_itemsets)

# 3. Generate Rules (3 Marks)
# Generate association rules with confidence >= 0.7
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.7)
print('\nAssociation Rules (confidence >= 0.7):')
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# Show at least 2 rules and explain one
if not rules.empty:
    print('\nSample Rules:')
    for idx, row in rules.head(2).iterrows():
        print(f"Rule {idx+1}: If a customer buys {set(row['antecedents'])}, they are likely to also buy {set(row['consequents'])} (confidence: {row['confidence']:.2f})")
    # Explanation for the first rule
    if len(rules) > 0:
        first_rule = rules.iloc[0]
        print('\nExplanation:')
        print(f"If a customer buys {set(first_rule['antecedents'])}, they are likely to also buy {set(first_rule['consequents'])} with a confidence of {first_rule['confidence']:.2f}. In real life, this means that these items are often bought together, so promotions or store layouts can take advantage of this pattern.")
else:
    print('No rules found with the specified confidence threshold.')

# Instructions for submission and documentation are in the README or comments above. 