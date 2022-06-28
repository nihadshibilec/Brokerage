def charges(buy,sell,qty):
    turnover = (buy*qty)+(sell*qty)
    t=turnover*0.0003
    if(t<20):
        brokerage = t*2
    else:
        brokerage = 40



    STT = sell*qty*0.00025
    transaction_charges = turnover*.0000345
    gst =(brokerage+transaction_charges)*0.18
    sebi_charges = sell*qty*0.000001*2
    stamp_duty = buy*qty*0.00003

    total_charges = brokerage + STT + transaction_charges + gst + sebi_charges+stamp_duty



    return(total_charges)
    


print(charges(2200,2207,1000))
    


    

