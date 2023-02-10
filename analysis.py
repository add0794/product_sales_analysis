import helper as hf
import importlib
import inspect
import numpy as np
import pandas as pd


importlib.reload(hf)


funcs = []
def list_functions(): 
    members = inspect.getmembers(hf)
    functions = [m for m in members if inspect.isfunction(m[1])]
    for name, obj in functions:
        funcs.append(name)
    print(funcs)
list_functions()


data = pd.read_csv("product_sales.csv")
hf.get_basic_info(data)


data = hf.rename(data, 'sales_method', 'email', 'Email')
data = hf.rename(data, 'sales_method', 'em + call', 'Email + Call')
data = hf.remove(data)


hf.show_pie_chart(data, hf.my_fmt, 'sales_method', 'customer_id')


email_years = hf.count_proportions(data, 'sales_method', 'Email', 'years_as_customer', 'customer_id')
call_years = hf.count_proportions(data, 'sales_method', 'Call', 'years_as_customer', 'customer_id')
email_and_call_years = hf.count_proportions(data, 'sales_method', 'Email + Call', 'years_as_customer', 'customer_id')
years_as_customer = pd.DataFrame({'years_as_customer': data['years_as_customer'].unique(), 'email': email_years, 'call': call_years, 'email_and_call': email_and_call_years})
years_as_customer['max'] = np.argmax((years_as_customer[['email', 'call', 'email_and_call']]).to_numpy(), axis=1)
print(years_as_customer.sort_values(by = 'years_as_customer'))


email_state = hf.count_proportions(data, 'sales_method', 'Email', 'state', 'customer_id')
call_state = hf.count_proportions(data, 'sales_method', 'Call', 'state', 'customer_id')
email_and_call_state = hf.count_proportions(data, 'sales_method', 'Email + Call', 'state', 'customer_id')
state = pd.DataFrame({'state': data['state'].unique(), 'email': email_state, 'call': call_state, 'email_and_call': email_and_call_state})
state['max'] = np.argmax((state[['email', 'call', 'email_and_call']]).to_numpy(), axis=1)
print(print(state.sort_values(by = 'state')))


hf.hist(data, 'revenue', data['revenue'].min(), data['revenue'].max())
hf.bar_chart(data, 'sales_method', 'revenue')
hf.line_chart(data, 'sales_method', ['Email', 'Email + Call', 'Call'], 'week', 'revenue')
hf.bar_chart_comparison(data, 'sales_method', 'week', 'customer_id')


hf.sales_summary(data, 'sales_method', 'week', 'customer_id', 'revenue')
