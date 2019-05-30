import os
directory = 'D:/EBook/DP-RP1/05-30-2019/Turing'
patterns=['[图灵交互设计丛书].', '[图灵程序设计丛书].', '[图灵图书].', '[图灵新知].', '[图灵原创].', '[异步图书]', '[图灵计算机科学丛书].']
isMatched = False

for filename in os.listdir(directory):
    if filename.upper().endswith(".PDF"):
        fullFileName = directory + '/' + filename
        if os.path.isfile(fullFileName):
            for pattern in patterns:
                if filename.find(pattern) > -1:
                    isMatched = True
                    newFileName = fullFileName.replace(pattern, '')
                    print('[debug] Rename ' + fullFileName + ' to: ' + newFileName)
                    os.rename(fullFileName, newFileName)
                    break
        if not isMatched:
            print('[debug] Skip ' + fullFileName + ' since no pattern found.')
    else:
        print('Not a .pdf file')
    continue
