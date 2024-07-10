'''
1. pip install openpyxl
'''
 
from openpyxl import Workbook

wb = Workbook() # 새 워크북 생성
ws = wb.active # 현재 활성화된 sheet 가져옴

ws.title = 'Test' # sheet의 이름을 변경

wb.save('sample.xlsx') # 저장('저장이름.확장자')
wb.close()