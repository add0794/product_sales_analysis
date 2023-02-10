# Product Sales Analysis

Pens and Printers was founded in 1984 and provides high quality office products to large organizations. We are a trusted provider of everything from pens and notebooks to desk chairs and monitors. We don’t produce our own products but sell those made by other companies.

We have built long lasting relationships with our customers and they trust us to provide them with the best products for them. As the way in which consumers buy products is changing, our sales tactics have to change too. Launching a new product line is expensive and we need to make sure we are using the best techniques to sell the new product effectively. The best approach may vary for each new product, so we need to learn quickly what works and what doesn’t.

We need to know:

- How many customers were there for each approach?
- What does the spread of the revenue look like overall? And for each method?
- Was there any difference in revenue over time for each of the methods?
- Based on the data, which method would you recommend we continue to use? Some of these methods take more time from the team so they may not be the best for us to use if the results are similar.

**Email**: Customers in this group received an email when the product line was launched, and a further email three weeks later. This required very little work for the team.

**Call**: Customers in this group were called by a member of the sales team. On average members of the team were on the phone for around thirty minutes per customer.

**Email and call**: Customers in this group were first sent the product information email, then called a week later by the sales team to talk about their needs and how this new product may support their work. The email required little work from the team, the call was around ten minutes per customer.

## Data Validation

The dataset contains 15000 rows and 8 columns before cleaning and validataion. I have validated all the columns against the criteria in the dataset table:

1. week: There are 6 unique values, represented as integers, indicating which week since product launch. There are no missing values, so no cleaning is necessary. 
2. sales_method: There are 5 unique values, represented as strings, indicating the sales method used to sell the car. There are no missing values, so no cleaning is necessary. Because we should expect 3 sales method, rows with two unique values had their values changed. For example, "em + call" was changed to "Email + Call." 
3. customer_id: Each customer has their own unique ID, represented as strings. There are no missing values, so no cleaning is necessary.
4. nb_sold: There are 10 unique values, represented as integers, indicating the number of new products sold. Values range as low as 7 to as high as 16. There are no missing values, so no cleaning is necessary. 
5. revenue: This column reflects revenue from sales garnered by each customer, represented as a float. There were 1074 missing values. We cannot assume missing values are zeroes. (Perhaps a sales rep accidentally input the data incorrectly or there was an issue with the server.) Therefore, these rows were removed.
6. years_as_customer: There are 42 unique values, represented as integers, indicating the number of years a customer has been with Pens and Printers. Values ranged as low as 0 (i.e. new customer) to as high as 63. There are no missing values, so no cleaning is necessary.
7. nb_site_visits: There are 27 unique values, represented as integers, indicating the number of years a customer has visited Pens and Printers website in the past year. Values ranged as low as 12 to as high as 41. There are no missing values, so no cleaning is necessary. 
8. state: There are 50 unique values, represented as strings, indicating the states where a customer has their order shipped to. In other words, customers represent all of the contiguous USA. DC and Puerto Rico are not included. There are no missing values, so no cleaning is necessary.

Now that data validation is complete, the dataset has 13926 rows and 8 columns.
