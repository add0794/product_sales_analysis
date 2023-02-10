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

## How Do Customers Differ in Their Shopping Behavior?

Over the past 6 weeks, I analyzed data on Pens and Partners' customers. I looked at:

- how many customers use each sales method.
- what the breakdown of customers using each sales method was according to where the order was being shipped to (i.e. "state") and how long the customer has used Pens and Partners' services (i.e. "years as customer").
- how much revenue was earned by groups of customers (e.g. number of customers that spent between $32 and $52), in addition to how much revenue was earned by each sales method and the breakdown of sales method by "years as customer."
- how revenue changed over time for each sales method.

Based on this analysis, I recommended how Pens and Partners should measure success (i.e. success criteria) and recommended which sales method is preferable. 

### Customer Use of Each Sales Method

Email is preferred: ~50% of customers use email exclusively, though it should be mentioned that ~34% prefer to get phone calls exclusively, too. A considerable percentage prefer email and phone calls: ~16%. **This gives insight that, perhaps, email is the preferred method of communication.**

[INSERT PIE CHART]

Regardless of sales method, customers for each group of sales method have used the company's services for a relatively short period of time or have come from a relatively select number of states. Each group has used the services for 1 year, and, thereafter, the proportion of customers having used the services for more than 1 years decreases in a linear fashion. Notable states are California, Illinois, Pennsylvania, and New York, where each group's customers made up a proportion of greater than 4% of the total group's customers. 

Otherwise, knowing how sales method is influenced by "state" or "years as customer" does not say much else. **There was no specific value for both "years as customer" or "state" that indicated one sales method is preferred over another.**

### Revenue Analysis

Revenue was right-skewed. Most customers spent between $32 and $53, which likely corresponds to 1-2 purchases. However, there's a considerable count of customers paying between $73 and $115.

[INSERT HISTOGRAM]

Overall, email has the highest revenue, with almost twice the revenue of email and calls. WIthin each method, most of the revenue came from customers who had been with the company between 0 and 8 years (highlighted by blue): $524988.89 (78.1%), $175138.14 (77.0%), and $330944.03 (81.1%) for email, call, and email and call, respectively. A considerable percentage came from customers between 8 and 16 years, too, with each showing percentages between 15% and 18% (highlighted by orange). The rest is from customers beyond 16 years.

**Email already is used the most; now, it has the highest revenue. This may lead us to believe that email is the preferred sales method.** 

[INSERT BAR CHART]

Ironically, weekly revenue for sales showed an inverse relationship. As the weeks went on, revenue decreased. For call, weekly revenue was usually below $50000, though for week 5, it hit $53518.11. Revenue by email and call increased over this time period.

[INSERT LINE CHART]

This begs the question: Is email the realized sales method?

I returned to review how much email was used by customers and came across a critical finding. Email was the majority because it was mostly used for the first week. However, as the weeks went on, email and call exclusively began to trend downward, with email being used 181 times as a sales method by week 6. On the other hand, email and call trended upwards.

But that isn't really what Pens and Partners need to know. Instead, it is that the number of sales decreased since week 1, from 3497 in week 1 to 1096 in week 6, regardless of which sales method is being monitored. Revenue decreased, too, from $272810.06 in week 1 to $163111.74 in week 6.

[INSERT BAR CHART]
[INSERT TABLE]

## Recommendations

Since our goal is to increase sales as efficiently as possible, I recommend that we measure (1) revenue changes over time as (2) each sales method's use changes while (3) accounting for changes in sales. It's critical, however, that we invest in **how we do email and call** because, although email and call's revenue has increased over time, sales have decreased: from $272810.06 in week 1 to $163111.74 in week 6. That's a 40% decrease in revenue, and sales have seen a similar decrease: 69%.

Moving forward, I recommend the following:

- Improve the data analysis pipeline to create an efficient and seamless way to implement the key performance metrics (KPMs) laid out here.
- Implement the KPMs as soon as possible to measure if Pens and Partners is decreasing in profitability and cash flow and at risk of bankruptcy.
- Redesign email and call to maintain existing customers as well as bring in new customers.
- Benchmark against peers to understand what tools work best and reconstruct existing sales methods.
- Change what data is collected, considering that much of the data used in this analysis did not provide useful, conclusive results for increasing sales and revenue. 
