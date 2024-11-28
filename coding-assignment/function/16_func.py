# Question = 16 Write a function to calculate the compound interest.

def compound_interest(P, r, n, t):
    
    A = P * (1 + r/n)**(n * t)
    return A - P  

principal = 1000  
rate = 0.05       
times_per_year = 4  
time_in_years = 3   

interest = compound_interest(principal, rate, times_per_year, time_in_years)
print(f"Compound Interest: {interest:.2f}")