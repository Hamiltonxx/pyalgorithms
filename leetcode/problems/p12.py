def intToRoman(num):
    g = ['','I','II','III','IV','V','VI','VII','VIII','IX'],
    s = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
    b = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
    q = ['','M','MM','MMM']
    
    return q[num//1000] + b[num%1000//100] + s[num%100//10] + g[num%10]
    