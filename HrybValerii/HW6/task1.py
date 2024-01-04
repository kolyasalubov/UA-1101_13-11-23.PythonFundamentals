even = []
odd_divis_by3 = []
not_divis_by2_3 = []

for num in range(1, 11):
    if num%2 == 0:
        even.append(num)
    if num%2 and not num%3 :
        odd_divis_by3.append(num)
    if num%2 and num%3:
        not_divis_by2_3.append(num)

print("Numbers divisible by 2:", ', '.join(map(str, even)))    
print("Odd numbers divisible by 3:", ', '.join(map(str, odd_divis_by3))) 
print("Numbers not divisible by both 2 and 3:", ', '.join(map(str, not_divis_by2_3))) 