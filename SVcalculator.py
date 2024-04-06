import matplotlib.pyplot as plt


def move(inS, inB, mp):
    i=0
    while inS > 0 and (False in inB):
        if inB[i] == False:
            inB[i] = True
            inS -= 1
            mp[i] = 0
        i += 1
    return inS, inB, mp


def SVcalculator(totalDays, growing_peroid, making_period, harvest_max, bucket, lands, price):
    
    gp, hm, d = 0,0,0
    inS = 0
    
    #有可能桶多地少的情况，所以要用list分开计算每一批的成熟时间
    mp = [-1]*bucket
    inB = [False]*bucket

    money = [0]*(totalDays+1)
    while d < totalDays:
        d+=1 #日子开始过
        gp += 1 #作物开始生长
        if gp >=growing_peroid: #达到生长周期开始收获
            inS += lands #收获
            hm += 1#收获次数+1
            inS, inB, mp = move(inS, inB, mp) #从库存转移到制造机器
            
            if hm >= harvest_max: #超过最大收割次数了
                gp = 0 #重新播撒种子，开始计时
                hm = 0 #收割次数也要从零开始计算
            else: #并没有超过最大收割次数
                hm+=1
        for i in range(bucket): #所有有材料的桶开始酿造
            if mp[i] != -1:
                mp[i] +=1 
        else:
            pass
        
        if inS == 0 and inB.count(True) == 0: #不在酿造，并且没有库存
            money[d] =   money[d-1]
            
        else:
            if True in inB: #已经有桶开始酿造
                count = 0
                for i in range(bucket):
                    if mp[i] >= making_period:#有桶里的成熟了
                        count += 1
                        mp[i] -= making_period
                        inB[i] = False #清空桶
                    else:
                        pass
                M = price*count #计算价钱
                money[d] = money[d-1] + M
            else: #没有桶生产完成
                money[d] = money[d-1]
    return money



if __name__ == "__main__":
    x=SVcalculator(45, 13, 7, 1, 41, 80, 2250)
    y = SVcalculator(45, 11, 1.5, 999, 41, 80, 200)
    days = [i for i in range(46)]
    title = "The comparision between StarFruit Beer and Beer Profit in 45 days"
    plt.title(title)
    plt.plot(days, x, label = "StarFruit Beer") 
    plt.plot(days, y, label = "Beer") 
    plt.legend() 
    plt.show()
                
                        
                    




