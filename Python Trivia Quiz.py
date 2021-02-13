print('Hello, welcome to trivia')

ans = input('Are you ready to play (yes/no):')

score = 0

total_q = 5

if ans.lower() == 'yes':



  ans = input('1. Name a programming language which is used to make apps? ')
  if ans.lower() == 'python' or ans.lower() == 'ruby' or ans.lower() == 'java' or ans.lower() == 'js' or ans.lower() == 'javascript' or ans.lower() == 'c++':
      score += 1
      print('Correct')

  else:
      print('Incorrect')

  ans = input('2. What programming language is used to make webpages? ')

  if ans == 'HTML' or ans == 'html':

    score += 1

    print('Correct')

  else:

      print('Incorrect')

  ans = input('3. What is 2 + 2 + 2 + 2 - 2 / 2 * 2? ')

  if ans == '6':

    score += 1

    print('Correct')

  else:

    print('Incorrect')

  ans = input('4. What is better a 1050ti or a 1060(graphics card)? ')

  if ans.lower() == '1060':

    score += 1

    print('Correct')

  else:

    print('Incorrect')

  ans = input('5. Who won the Champions League in 2019?')

  if ans.lower() == 'liverpool' or ans.lower() == 'Liverpool f.c':

    score += 1

    print('Correct')

  else:

    print('Incorrect')
       

mark = (score/total_q) * 100
print("Thank you for playing you got", str(mark) + "%","well done!")
