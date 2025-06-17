def savings(gross_pay, tax_rate, expenses):
    gross_pay, expenses = int
    tax_rate = float
    a = gross_pay*tax_rate
    emp_money = int(gross_pay - expenses - a)
    return emp_money

def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_material, num_jobs, job_consumption = int
    material_units = str
    total_consumption = int(num_jobs*job_consumption)
    leftover_mat = str(total_material - total_consumption) + str(material_units)
    return leftover_mat

def interest(principal, rate, periods):
    principal, periods = int
    rate = float
    value = principal*(rate*periods)
    final = int(principal + value)
    return final