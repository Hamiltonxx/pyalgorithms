s = input()
lab = s.find('AB')
rab = s.rfind('AB')
lba = s.find('BA')
rba = s.rfind('BA')

print(['NO','YES'][(abs(lab-rba)>1 or abs(rab-lba)>1) and min(lab,rab,lba,rba)>=0])
