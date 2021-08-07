# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：字母图形
@时间：2020/3/4  
"""

"""
main()
{
    int n,m,j,k;
    scanf("%d %d",&n,&m);
    if(n>=1&&m<=26)
    for(j=0;j<n;j++)
    {
        for(k=0;k<m;k++)
        printf("%c",65+abs(j-k)); //j-k实现倒序
        printf("\n");
    }
    return 0;
}

"""
#d=a为浅复制，直接复制引用。d=a[:]或import copy  d=copy.deepcopy(a)为深复制或d = a.copy()
j = 65
k = 0
number = input().split()
row, col = number
a = []
d = []
for i in range(26):
    a = a + [chr(j)]
    j = j + 1
d =a[:]
for i in range(int(row)):
    b = ''.join(d)
    b = b[:int(col)]
    print(b)
    if k+1 == 26:
        k = -1
    d.insert(0,a[k+1])
    d.pop()
    k = k+1






