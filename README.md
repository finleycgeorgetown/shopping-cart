# Shopping-Ccart
Cullen Finley Shopping Cart Project OPIM 243
10-10-20

# Introduction
This application is a product of the following business prompt.

## Prompt
Your local corner grocery store has hired you as a technology consultant to help modernize their checkout system.

Currently, when managing inventory, store employees affix a price tag sticker on each grocery item in stock. And when a customer visits the checkout counter with their selected items, a checkout clerk uses a calculator to add product prices, calculate tax, and calculate the total amount due.

Instead, the store owner describes a desired checkout process which involves the checkout clerk scanning each product's barcode to automatically lookup prices, perform tax and total calculations, and print a customer receipt. To facilitate this process, the store owner has authorized the purchase of a few inexpensive barcode scanners, as well as checkout computers capable of running Python applications.

The store owner says it would be "acceptable but not preferable" to manage the inventory of products via the application's source code, that it would be "better" to manage the inventory of products via a local CSV file stored on the checkout computer, and that it would be "ideal" to be able to manage the inventory of products via a centralized Google Sheet spreadsheet document.

The store owner also says it would be "nice to have" a feature which prompts the checkout clerk or the customer to input the customer's email address in order to send them a receipt via email.

# Setup
## Repository Setup
Use the GitHub.com online interface to clone a new remote project repository "shopping-cart". 

Use the GitHub desktop software to clone your repository onto your desktop. After cloning there, use the GitHub option to open the directory into GitBash.



## Enviornment Setup
Create and activate a new Anaconda virtual environment:
```
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```

From within the virtual environment, demonstrate your ability to run the Python script from the command-line:
```
python shopping_cart.py
```
This will run the program.
# Output
By entering the product ids that are listed in the attatched products.txt, the application will store your inputs and then create a final receipt of your purchase.