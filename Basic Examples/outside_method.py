# create a funciton
def close_rate_bucket(row):
    if row['Close Rate'] >0 and  row['Close Rate'] < .05:
        val = 'Poor'
    elif row['Close Rate'] >= .05 and row['Close Rate'] < .1:
        val = 'Okay'
    elif row['Close Rate'] >= .1  and row['Close Rate'] < .15:
        val = 'Average'
    elif row['Close Rate'] >= .15  and row['Close Rate'] < .2:
        val = 'Good'
    elif row['Close Rate'] >= .2  and row['Close Rate'] < .25:
        val = "Great"
    else:
        val = "Other"
    return val
