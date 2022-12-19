gross_income=float(input("Enter gross income"))
dependents=int(input("Enter number of dependents"))
standard_ded=10000
dependent_ded=3000
tax_rate=0.2
taxable_income=gross_income-standard_ded-(dependent_ded*dependents)
tax=taxable_income*tax_rate
print("Tax=",tax)