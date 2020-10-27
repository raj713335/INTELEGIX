import os

listx=[]

for dirname, _, filenames in os.walk('OUTPUT/REC/CLASS_ENVIRONMENT/IMAGES'):
    for filename in filenames:
        print('OUTPUT/REC/CLASS_ENVIRONMENT/IMAGES'+'/'+filename)
        listx.append(str('OUTPUT/REC/CLASS_ENVIRONMENT/IMAGES'+'/'+filename))

