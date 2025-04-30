state_capitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Karnataka': 'Bangalore',
    'Tamil Nadu': 'Chennai',
    'Kerala': 'Thiruvananthapuram',
    'Rajasthan': 'Jaipur',
    'Uttar Pradesh': 'Lucknow',
    'Madhya Pradesh': 'Bhopal',
    'Punjab': 'Chandigarh',
    'Haryana': 'Chandigarh',
    'Himachal Pradesh': 'Shimla',
    'Bihar': 'Patna',
    'Jharkhand': 'Ranchi',
    'Odisha': 'Bhubaneswar',
    'West Bengal': 'Kolkata',
    'Andhra Pradesh': 'Hyderabad',
    'Telangana': 'Hyderabad',
    'Chhattisgarh': 'Raipur',
    'Assam': 'Dispur',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Tripura': 'Agartala',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Arunachal Pradesh': 'Itanagar',
    'Goa': 'Panaji'}
print(state_capitals)
#print(*state_capitals.values())
#print(*state_capitals.keys())

for state, capital in state_capitals.items():
    print(f"The capital of {state} is {capital}")
print('---------------------')
for state, capital in sorted(state_capitals.items()):
    print(f"The capital of {state} is {capital}")
print('---------------------')
# for state, capital in sorted(state_capitals.items()):
#     common_letters = set(state) & set(capital)
#     if len (common_letters) > 2: