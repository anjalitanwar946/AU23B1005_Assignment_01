def ROI():
    annualprofit=int(input("Amnual Site profit: "))
    ccr=float(input("Current Conversion Rate: "))
    icr=float(input("Improved Conversion RAte: "))
    ic=int(input("Improvement Cost: "))
    epl=float(input("Expected Project life (in years): "))
    i=0.05
    # fgp= Future Gain From Improvement
    fgi= annualprofit * (icr/ccr) - annualprofit * (((1+i) ** epl) - 1) / i-ic * ((1+i) ** epl)

    # tgi=Total Gain from Improvement
    tgi=fgi/(1+i)**epl

    # agi = Annual gain From Improvement
    agi=tgi/epl

    annual_roi=agi/ic
    total_roi=tgi/ic

    print("Annual ROI: ", annual_roi)
    print("Total ROI : ", total_roi)

ROI()