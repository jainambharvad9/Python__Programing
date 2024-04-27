papeol = {1:{'name': 'Jainam', 'age' : '24', 'Gender' : 'Male' },
          2:{'name': 'Meet', 'age' : '25', 'Gender' : 'Male' },
          3:{'name': 'Nandan', 'age' : '22', 'Gender' : 'Male' },
          4:{'name': 'Kavan', 'age' : '32', 'Gender' : 'Male' }}

print(papeol)

print(papeol.items())

for p_id,p_info in papeol.items():
    print("\nPerson ID : ",p_id)
    
    for key in p_info:
        print(key , " : ",p_info[key])