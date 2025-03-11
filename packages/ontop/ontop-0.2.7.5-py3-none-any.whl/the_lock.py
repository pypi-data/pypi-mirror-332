from media import *
from html_helper import *
from messages import *
from string_table import *

from io import StringIO
import os
from IPython.display import HTML
from base64 import b64encode

html_close = '''
<html>
<body>
<img src="https://ontopnew.s3.il-central-1.amazonaws.com/TheLock/lock01.png" width="120" height="290">
</body>
</html>'''
html_open_1 = '''
<html>
<body>
<img src="https://ontopnew.s3.il-central-1.amazonaws.com/TheLock/lock02.png" width="188" height="290">
</body>
</html>'''
html_open_1_ar = '''
<html>
<body>
<img src="https://ontopnew.s3.il-central-1.amazonaws.com/TheLock/lock02_ara.png" width="188" height="290">
</body>
</html>'''
html_open_2 = '''
<html>
<body>
<img src="https://ontopnew.s3.il-central-1.amazonaws.com/TheLock/lock03.png" width="188" height="290">
</body>
</html>'''
html_open_2_ar = '''
<html>
<body>
<img src="https://ontopnew.s3.il-central-1.amazonaws.com/TheLock/lock03_ara.png" width="188" height="290">
</body>
</html>'''
html_fireworks = '''
<html>
<body>
<img src="https://ontopnew.s3.il-central-1.amazonaws.com/TheLock/fireworks.gif" width="587" height="263">
</body>
</html>'''


result_list = [False, False, False, False, False, False, False, False, False, False, False, False, False]
score = 0
def unlock(index, result):
  global result_list
  global score
  #print('score = ', score)
  message = ""
  if index < 1 or index > 8:
     s = get_string_from_string_table('the_lock', 'msg1')
     return s

  if index == 1:
    if score != 0:
      s = get_string_from_string_table('the_lock', 'msg2')
      print(s)#('יש לפתור את התרגילים לפי הסדר')
    else:
      if result == 67:
        if result_list[index] == False:
          score += 1
        result_list[index] = True
        s = get_string_from_string_table('the_lock', 'msg3')
        print(s)#("תשובה מדוייקת")
        correct_answer_msg(score)
        display_visual_result()
      else:
        s = get_string_from_string_table('the_lock', 'msg4')
        print(s)#("תשובה לא נכונה, נסו לתקן את הקוד")

  if index == 2:
    if score != 1:
      s = get_string_from_string_table('the_lock', 'msg2')
      print(s)#('יש לפתור את התרגילים לפי הסדר')
    else:
      if result == 340:
        if result_list[index] == False:
          score += 1
        result_list[index] = True
        s = get_string_from_string_table('the_lock', 'msg5')
        print(s)#("סחתיין תותח/ית")
        correct_answer_msg(score)
        display_visual_result()
      else:
        s = get_string_from_string_table('the_lock', 'msg4')
        print(s)#("תשובה לא נכונה, נסו לתקן את הקוד")

  if index == 3:
    if score != 2:
      s = get_string_from_string_table('the_lock', 'msg2')
      print(s)#('יש לפתור את התרגילים לפי הסדר')
    else:
      if result == 4950:
        if result_list[index] == False:
          score += 1
        result_list[index] = True
        s = get_string_from_string_table('the_lock', 'msg6')
        print(s)#("מעולה")
        correct_answer_msg(score)
        display_visual_result()
      else:
        s = get_string_from_string_table('the_lock', 'msg4')
        print(s)#("תשובה לא נכונה, נסו לתקן את הקוד")

  if index == 4:
    if score != 3:
        s = get_string_from_string_table('the_lock', 'msg2')
        print(s)#('יש לפתור את התרגילים לפי הסדר')
    else:
      if result == 118098:

        if result_list[index] == False:
          score += 1
        result_list[index] = True
        print("Hooray, Hooray ..... ")
        correct_answer_msg(score)
        display_visual_result()
      else:
        s = get_string_from_string_table('the_lock', 'msg4')  
        print(s)#("תשובה לא נכונה, נסו לתקן את הקוד")

  if index == 5:
    if score != 4:
      s = get_string_from_string_table('the_lock', 'msg2')  
      print(s)#('יש לפתור את התרגילים לפי הסדר')
    else:
      if result == 100:
        if result_list[index] == False:
          score += 1
        result_list[index] = True
        s = get_string_from_string_table('the_lock', 'msg7')
        print(s)#("בונבוניירה של פתרון")
        correct_answer_msg(score)
        display_visual_result()
      else:
        s = get_string_from_string_table('the_lock', 'msg4')
        print(s)#("תשובה לא נכונה, נסו לתקן את הקוד")

  if index == 6:
    if score != 5:
      s = get_string_from_string_table('the_lock', 'msg2')
      print(s)#('יש לפתור את התרגילים לפי הסדר')
    else:
      if result == 1683:
        if result_list[index] == False:
          score += 1
        result_list[index] = True
        s = get_string_from_string_table('the_lock', 'msg8')
        print(s)#("מי גאון/נה של אמא?")
        correct_answer_msg(score)
        display_visual_result()
      else:
        s = get_string_from_string_table('the_lock', 'msg4')
        print(s)#("תשובה לא נכונה, נסו לתקן את הקוד")

  if index == 7:
    if score != 6:
      s = get_string_from_string_table('the_lock', 'msg2')  
      print(s)#('יש לפתור את התרגילים לפי הסדר')
    else:
      if result == 7:
        if result_list[index] == False:
          score += 1
        result_list[index] = True
        s = get_string_from_string_table('the_lock', 'msg16')
        print(s)#("פתרון מדהים!")
        correct_answer_msg(score)
        display_visual_result()
      else:
        s = get_string_from_string_table('the_lock', 'msg4')
        print(s)#("תשובה לא נכונה, נסו לתקן את הקוד")   

  if index == 8:
    if score != 7:
      s = get_string_from_string_table('the_lock', 'msg2')
      print(s)#('יש לפתור את התרגילים לפי הסדר')
    else:
      if result == 225:
        if result_list[index] == False:
          score += 1
        result_list[index] = True
        correct_answer_msg(score)
        display_visual_result()
      #print("סוכריה")
      else:
        s = get_string_from_string_table('the_lock', 'msg4')
        print(s)#("תשובה לא נכונה, נסו לתקן את הקוד")
def display_visual_result():
  language = get_language()
  if score >= 8:
    #print("פתרתם נכון " + str(score)+ " תרגילים מתוך 8 תרגילים ")
    s = get_string_from_string_table('the_lock', 'msg10')
    print(s)#("זהו זה, פתרתם את כל תרגילי הריענון,")
    s = get_string_from_string_table('the_lock', 'msg11')
    print(s)#("מתחילים את שנה ב' ברגל ימין")
    display(HTML('<h1><font color="red"> בהצלחה</font></h1>'))
    if language == 'hebrew':
      display(HTML(html_open_2))
    else:
      display(HTML(html_open_2_ar))
    display(HTML(html_fireworks))
  #elif score >= 8:
    #print("פתרתם נכון " + str(score)+ " תרגילים מתוך 8 תרגילים ")
    #print("איזה תותחיות ותותחים הצלחתם לפתוח את הכספת :-)")
    #print("איזה עוד הפתעות מחכות לנו בארון?")
    #display(HTML(html_open_2))'
  elif score == 6 :
    #print("פתרתם נכון " + str(score)+ " תרגילים מתוך 8 תרגילים")
    s = get_string_from_string_table('the_lock', 'msg13')
    print(s)#("כל הכבוד, הצלחתם לפרוץ את המנעול ולפתוח את הארון.")
    s = get_string_from_string_table('the_lock', 'msg14')
    print(s)#("וואוווו ... יש בפנים כספת, מה יש בה? איך פותחים אותה?")
    if language == 'hebrew':
      display(HTML(html_open_1))
    else:
      display(HTML(html_open_1_ar))
  elif score == 7 :
    #print("פתרתם נכון " + str(score)+ " תרגילים מתוך 8 תרגילים")
    #s = get_string_from_string_table('the_lock', 'msg13')
    #print(s)#("כל הכבוד, הצלחתם לפרוץ את המנעול ולפתוח את הארון.")
    s = get_string_from_string_table('the_lock', 'msg17')
    print(s)#("וואוווו ... יש בפנים כספת, מה יש בה? איך פותחים אותה?")
    if language == 'hebrew':
      display(HTML(html_open_1))
    else:
      display(HTML(html_open_1_ar))
  else:
    #print("פתרתם נכון " + str(score)+ " תרגילים מתוך 8 תרגילים, הארון עדיין נעול")
    display(HTML(html_close))

def correct_answer_msg(score):
  s1 = get_string_from_string_table('the_lock', 'msg12')
  s2 = get_string_from_string_table('the_lock', 'msg9')  
  print(s1 + "" + str(score)+ "" +  s2 + " ")
