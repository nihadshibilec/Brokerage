# capital = float(input("Enter your trading capital:"))
# # #recomend a risk % of 2 
# risk_pct = float(input("Enter your risk % (Recomended : 2%)"))
# risk = capital * risk_pct
# trades_per_day = input("Enter the no of trades per day (Recomended = 2)")

performance = input("Enter your expected performance:(From 1 to 3):")
rr_ratio = input("Select the average RR ratio :(1,1.5,2,2.5,3)")

winrate = 0.1

if (performance == "1"):
    if(rr_ratio == "1"):
        winrate = 0.55
    elif(rr_ratio =="1.5"):
        winrate = .45
    elif(rr_ratio =="2"):
        winrate = .4
    elif(rr_ratio =="2.5"):
        winrate = .35
    elif(rr_ratio =="3"):
        winrate = .3


if (performance == "2"):
    if(rr_ratio == "1"):
        winrate = 0.6
    elif(rr_ratio =="1.5"):
        winrate = .5
    elif(rr_ratio =="2"):
        winrate = .45
    elif(rr_ratio =="2.5"):
        winrate = .4
    elif(rr_ratio =="3"):
        winrate = .35

if (performance == "3"):
    if(rr_ratio == "1"):
        winrate = 0.65
    elif(rr_ratio =="1.5"):
        winrate = .55
    elif(rr_ratio =="2"):
        winrate = .5
    elif(rr_ratio =="2.5"):
        winrate = .45
    elif(rr_ratio =="3"):
        winrate = .4

print(winrate)

# month1 = (trades_per_day * 20 *(1-winrate)* risk)

# print(month1)