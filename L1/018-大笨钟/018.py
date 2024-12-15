hh,mm=input().split(':')
int_hh=int(hh)
if (12>int_hh>=0) or (int_hh==12 and mm=='00'):
    print(f'Only {hh}:{mm}.  Too early to Dang.')
else:
    num=int_hh-12
    if mm!='00':
        num+=1
    print('Dang'*num)