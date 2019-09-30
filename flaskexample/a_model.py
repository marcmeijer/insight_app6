def ModelIt(fromUser  = 'Default', drugs = []):
 in_month = len(drugs)
 result = in_month
 if fromUser != 'Default':
   return result
 else:
   return 'check your input'
