import docx
import os
import schedule
import time
def lol():
    doc = docx.Document()
    parag = doc.add_paragraph('This message is automated!')
    doc.save('test.docx')
    os.system('start test.docx')

lol()
# to make it run every 10 seconds uncomment the code below by highliting it and pressing ctrl + /
# schedule.every(10).seconds.do(lol)

# while 1:
#     schedule.run_pending()
#     time.sleep(1)
    
