def countVowels(str):
   a_count = 0
   e_count = 0
   i_count = 0
   o_count = 0
   u_count = 0
   for a in str:
      if a == 'a':
         a_count += 1
   for e in str:
      if e == 'e':
         e_count += 1
   for i in str:
      if i == 'i':
         i_count += 1
   for o in str:
      if o == 'o':
         o_count += 1
   for u in str:
      if u == 'u':
         u_count += 1
   print("a: ", a_count)
   print("e: ", e_count)
   print("i: ", i_count)
   print("o: ", o_count)
   print("u: ", u_count)

countVowels("your mom loves you")