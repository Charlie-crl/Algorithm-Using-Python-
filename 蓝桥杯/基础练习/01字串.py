# -*- encoding:utf-8 -*-
"""
@作者：踏着七色云彩
@问题名：01字串
@时间：2020/3/4  
"""
"""
main()
{
    int a,b,c,d,e;
    
    for(e=0;e<=1;e++)
    for(d=0;d<=1;d++)
    for(c=0;c<=1;c++)
    for(b=0;b<=1;b++)
    for(a=0;a<=1;a++)
    printf("%d%d%d%d%d\n",e,d,c,b,a);
    
    return 0;
}

"""
#print(int('10',base=2))将其他进制的数转为10进制；如print则输出2
#bin()将其他进制转为二进制
for i in range(32):
    b = bin(i).replace("0b", "")
    if len(b) < 5:
        b = '0' * (5-len(b)) + b
    print(b)

