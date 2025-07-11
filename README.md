# Association Rule Mining Mini Assignment

## Overview
This project simulates transaction data, applies the Apriori algorithm to find frequent itemsets, and generates association rules using Python, pandas, and mlxtend.

## Code Explanation

### 1. Simulate Transaction Data
- The script defines a pool of 10 unique items (e.g., Bread, Milk, Eggs, etc.).
- It generates 10 fake transactions. Each transaction randomly contains 2–5 items from the pool, ensuring variety and overlap between transactions.
- Example output:
  ```
  Transaction 1: ['Butter', 'Bread']
  Transaction 2: ['Juice', 'Bananas', 'Butter', 'Cheese', 'Eggs']
  ...
  ```

### 2. One-Hot Encoding
- The transactions are converted into a one-hot encoded pandas DataFrame. Each row represents a transaction, and each column represents an item. A value of `True` means the item is present in that transaction.
- Example output:
  ```
     Apples  Bananas  Bread  Butter  Cereal  Cheese  Chicken   Eggs  Juice   Milk
  0   False    False   True    True   False   False    False  False  False  False
  1   False     True  False    True   False    True    False   True   True  False
  ...
  ```

### 3. Apriori Algorithm
- The script uses the `apriori` function from mlxtend to find frequent itemsets with a minimum support of 0.3 (i.e., the itemset appears in at least 30% of transactions).
- Example output:
  ```
     support                 itemsets
  0     0.3                 (Apples)
  1     0.4                (Bananas)
  2     0.3                  (Bread)
  ...
  ```

### 4. Association Rule Generation
- The script generates association rules from the frequent itemsets using the `association_rules` function, with the metric set to confidence and a minimum threshold of 0.7.
- The rules are displayed with their support, confidence, and lift values.
- Example output:
  ```
            antecedents        consequents  support  confidence   lift
  0           (Bananas)           (Butter)      0.3        0.75  1.250
  1           (Bananas)           (Cheese)      0.3        0.75  1.875
  ...
  ```

### 5. Rule Explanation
- The script prints at least two rules and provides a technical explanation for one.
- Example:
  ```
  Rule 1: If a customer buys {'Bananas'}, they are likely to also buy {'Butter'} (confidence: 0.75)
  Rule 2: If a customer buys {'Bananas'}, they are likely to also buy {'Cheese'} (confidence: 0.75)
  Explanation:
  If a customer buys {'Bananas'}, they are likely to also buy {'Butter'} with a confidence of 0.75. In real life, this means that these items are often bought together, so promotions or store layouts can take advantage of this pattern.
  ```

## Output Explanation
- **Simulated Transactions:** Shows the randomly generated transactions.
- **One-hot encoded DataFrame:** Shows the binary matrix used for mining.
- **Frequent Itemsets:** Lists itemsets that appear in at least 30% of transactions.
- **Association Rules:** Lists rules with confidence ≥ 0.7, showing which items are likely to be bought together.
- **Sample Rules and Explanation:** Demonstrates how to interpret the rules in a business context.

## How to Run
1. Ensure you have Python 3, pandas, and mlxtend installed.
2. Run the script:
   ```
   python association_mining.py
   ```
3. The results will be printed to the console and can be saved to a file as needed.

## Files
- `association_mining.py`: Main script for data simulation, analysis, and rule generation.
- `results.txt`: Example output from running the script.
- `todo.md`: Assignment checklist.

---
Replace `yourname` in the repo name as required for submission. 