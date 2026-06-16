class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        numlog=[]
        letlog=[]
        for i in logs:
            t=i.split(" ",1)
            if t[1][0].isdigit():
                numlog.append(i)
            else:
                letlog.append(t)
        letlog.sort(key=lambda x: (x[1],x[0]))
        re=[]
        for i in letlog:
            re.append(i[0]+" "+i[1])
        for i in numlog:
            re.append(i)
        return re