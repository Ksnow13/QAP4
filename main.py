# Preparing a menu program that allows the user to enter new insurance policies and saves them to a file.
# The program also has a detailed and exception report.
# Authors: Kyle Snow
# Start Date: July 29 2022
# Completion Date: August 1 2022


import FormatValues as FV
import datetime
from time import sleep
CurrentDate = datetime.datetime.now()


# Function to enter the new policies

def NewPolicy():

    # Reads the values from the defaults file

    DefaultsData = open("OSICDef.dat", "r")

    PolicyNum = int(DefaultsData.readline())
    BasicPremium_Amt = float(DefaultsData.readline())
    AddCarDiscount_Rate = float(DefaultsData.readline())
    ExtraLiability_Amt = float(DefaultsData.readline())
    GlassCoverage_Amt = float(DefaultsData.readline())
    LoanerCoverage_Amt = float(DefaultsData.readline())
    HST_RATE = float(DefaultsData.readline())
    ProcessingFee_Amt = float(DefaultsData.readline())

    DefaultsData.close()

    # Gathering user inputs.

    while True:
        print()
        while True:

            Allowed_Characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'")

            CustFirstName = input("Enter the customers first name (END to return to menu): ")

            if CustFirstName == "":
                print(" Error - Cannot be blank ")
            elif set(CustFirstName).issubset(Allowed_Characters) == False:
                print(" Error - Invalid characters ")
            else:
                break
        if CustFirstName.upper() == "END":
            break

        while True:

            CustLastName = input("Enter the customers last name: ")

            if CustLastName == "":
                print(" Error - Cannot be blank ")
            elif set(CustLastName).issubset(Allowed_Characters) == False:
                print(" Error - Invalid characters ")
            else:
                break

        while True:

            Address = input("Enter the customers address: ")

            if Address == "":
                print(" Error - Cannot be blank ")
            else:
                break

        while True:

            City = input("Enter the city: ")

            if City == "":
                print(" Error - Cannot be blank ")
            else:
                break

        while True:

            Province = input("Enter the province: ")

            if Province == "":
                print(" Error - Cannot be blank ")
            elif set(Province).issubset(Allowed_Characters) == False:
                print(" Error - Invalid characters ")
            else:
                break

        while True:

            PostalCode = input("Enter the postal code: ")

            if PostalCode == "":
                print(" Error - Cannot be blank ")
            else:
                break

        while True:

            PhonenNum = input("Enter the customers phone number: (10 digits): ")

            if (PhonenNum).isdigit() == False:
                print(" Error - Must be digits ")
            elif len(PhonenNum) != 10:
                print(" Error - Must be 10 digits ")
            else:
                break

        while True:

            try:
                NumCarsInsured = input("Enter the number of cars being insured: ")
                NumCarsInsured = int(NumCarsInsured)
            except:
                print(" Error - Must be a digit ")
            else:
                if NumCarsInsured < 1:
                    print(" Error - Must be at least 1 car ")
                else:
                    break

        while True:

            ExtraLiabilityChoice = input("Would you like extra liability (Y/N): ")

            if ExtraLiabilityChoice.upper() != "Y" and ExtraLiabilityChoice.upper() != "N":
                print(" Error - Must be Y or N ")
            else:
                break

        while True:

            GlassCoverageChoice = input("Would you like glass coverage (Y/N): ")

            if GlassCoverageChoice.upper() != "Y" and GlassCoverageChoice.upper() != "N":
                print(" Error - Must be Y or N ")
            else:
                break

        while True:

            LoanerCarChoice = input("Would you like a loaner car (Y/N): ")

            if LoanerCarChoice.upper() != "Y" and LoanerCarChoice.upper() != "N":
                print(" Error - Must be Y or N ")
            else:
                break

        while True:

            PaymentOption = input("Pay in full or monthly (F/M): ")

            if PaymentOption.upper() != "F" and PaymentOption.upper() != "M":
                print(" Error - Must be F or M ")
            else:
                break

        # My Calculations.

        if NumCarsInsured == 1:
            InsurancePremiumCost = BasicPremium_Amt
        else:
            InsurancePremiumCost = ((NumCarsInsured - 1) * (BasicPremium_Amt - (BasicPremium_Amt * AddCarDiscount_Rate))) + BasicPremium_Amt


        if ExtraLiabilityChoice.upper() == "Y":
            ExtraLiabilityCost = ExtraLiability_Amt * NumCarsInsured
        else:
            ExtraLiabilityCost = 0


        if GlassCoverageChoice.upper() == "Y":
            GlassCoverageCost = GlassCoverage_Amt * NumCarsInsured
        else:
            GlassCoverageCost = 0


        if LoanerCarChoice.upper() == "Y":
            LoanerCarCost = LoanerCoverage_Amt * NumCarsInsured
        else:
            LoanerCarCost = 0


        TotalExtraCost = ExtraLiabilityCost + GlassCoverageCost + LoanerCarCost
        TotalInsurePremiumCost = InsurancePremiumCost + TotalExtraCost
        HST = TotalInsurePremiumCost * HST_RATE
        GrandTotal = TotalInsurePremiumCost + HST


        if PaymentOption.upper() == "M":
            MonthlyPayment = (GrandTotal + ProcessingFee_Amt) / 12
        else:
            MonthlyPayment = 0

        # Stating dates and getting the next payment date.

        PolicyDate = CurrentDate
        CurrentDateYear = CurrentDate.year
        CurrentDateMonth = CurrentDate.month
        CurrentDateDay = CurrentDate.day

        if CurrentDateDay > 25:
            PaymentDate = datetime.date(CurrentDateYear, (CurrentDateMonth + 2), day=1)
        else:
            PaymentDate = datetime.date(CurrentDateYear, (CurrentDateMonth + 1), day=1)


        # printing all user inputs and calculations to the screen.

        print()
        print("-----------------------------------")
        print(" Policy Date: {:>10s} ".format(FV.FDateMedium(PolicyDate)))
        print(" Customers name: {} {} ".format(CustFirstName.title(), CustLastName.title()))
        print(" Phone Number: {}-{}-{} ".format(PhonenNum[0:3], PhonenNum[3:6], PhonenNum[6:10]))
        print(" Address: ")
        print("        {} ".format(Address))
        print("        {}, {}, {} ".format(City.title(), Province.title(), PostalCode.upper()))
        print("------------------------------------")
        print(" Cars being insured:   {}".format(NumCarsInsured))
        print(" Insurance premium:        {:>9s}".format(FV.FDollar2(InsurancePremiumCost)))
        print(" Extra liability:     ({:<1s})    {:>7s}".format(ExtraLiabilityChoice.upper(),FV.FDollar2(ExtraLiabilityCost)))
        print(" Glass Coverage:      ({:<1s})    {:>7s}".format(GlassCoverageChoice.upper(), FV.FDollar2(GlassCoverageCost)))
        print(" Loaner car:          ({:<1s})    {:>7s}".format(LoanerCarChoice.upper(), FV.FDollar2(LoanerCarCost)))
        print("------------------------------------")
        print(" Total extra costs:          {:>7s}".format(FV.FDollar2(TotalExtraCost)))
        print(" Total insurance premium:  {:>9s}".format(FV.FDollar2(TotalInsurePremiumCost)))
        print(" HST:                        {:>7s}".format(FV.FDollar2(HST)))
        print("                           ---------")
        print(" Grand Total:              {:>9s}".format(FV.FDollar2(GrandTotal)))
        print("------------------------------------")
        if PaymentOption.upper() == "F":
            print(" Payment option:                FULL")
        else:
            print(" Payment option:             Monthly")
            print(" Monthly payment:            {:>7s}".format(FV.FDollar2(MonthlyPayment)))
            print(" Payment date:            {:>10s}".format(FV.FDateMedium(PaymentDate)))

        # Saving required information to a file.

        DataFile = open("Policies.dat", "a")

        DataFile.write("{}-{}{}, ".format(str(PolicyNum), CustFirstName.upper()[0], CustLastName.upper()[0]))
        DataFile.write("{}, ".format(FV.FDateMedium(PolicyDate)))
        DataFile.write("{}, ".format(CustFirstName.title()))
        DataFile.write("{}, ".format(CustLastName.title()))
        DataFile.write("{}, ".format(Address.title()))
        DataFile.write("{}, ".format(City.title()))
        DataFile.write("{}, ".format(Province.upper()))
        DataFile.write("{}, ".format(PostalCode.upper()))
        DataFile.write("{}-{}-{}, ".format(PhonenNum[0:3], PhonenNum[3:6], PhonenNum[6:10]))
        DataFile.write("{}, ".format(str(NumCarsInsured)))
        DataFile.write("{}, ".format(ExtraLiabilityChoice.upper()))
        DataFile.write("{}, ".format(GlassCoverageChoice.upper()))
        DataFile.write("{}, ".format(LoanerCarChoice.upper()))
        DataFile.write("{}, ".format(PaymentOption.upper()))
        DataFile.write("{}\n".format(str(FV.FNumber2(GrandTotal))))

        DataFile.close()

        print()
        print("Saving....")

        sleep(2)
        print()
        print(" Information successfully saved. ")
        print()

        PolicyNum += 1

        # Writing back the values to the defaults file.

        DefaultsData = open("OSICDef.dat", "w")

        DefaultsData.write("{}\n".format(str(PolicyNum)))
        DefaultsData.write("{}\n".format(str(BasicPremium_Amt)))
        DefaultsData.write("{}\n".format(str(AddCarDiscount_Rate)))
        DefaultsData.write("{}\n".format(str(ExtraLiability_Amt)))
        DefaultsData.write("{}\n".format(str(GlassCoverage_Amt)))
        DefaultsData.write("{}\n".format(str(LoanerCoverage_Amt)))
        DefaultsData.write("{}\n".format(str(HST_RATE)))
        DefaultsData.write("{}\n".format(str(ProcessingFee_Amt)))

        DefaultsData.close()

        while True:

            Another = input(" Would you like to Enter other Customer? (Y/N): ")

            if Another == "":
                print(" Error - Cannot be blank ")
            elif Another.upper() != "Y" and Another.upper() != "N":
                print(" Error - Must be Y or N ")
            elif Another.upper() == "Y" or Another.upper() == "N":
                break
        if Another.upper() == "N":
            break


# Function for the Detail Report.

def Detailreport():

    # Reading the values from the defaults table so the constants can be used for calculations

    DefaultsData = open("OSICDef.dat", "r")

    PolicyNum = int(DefaultsData.readline())
    BasicPremium_Amt = float(DefaultsData.readline())
    AddCarDiscount_Rate = float(DefaultsData.readline())
    ExtraLiability_Amt = float(DefaultsData.readline())
    GlassCoverage_Amt = float(DefaultsData.readline())
    LoanerCoverage_Amt = float(DefaultsData.readline())
    HST_RATE = float(DefaultsData.readline())
    ProcessingFee_Amt = float(DefaultsData.readline())

    DefaultsData.close()

    print()
    print("ONE STOP INSURANCE COMPANY ")
    print("POLICY LISTING AS OF {}".format(FV.FDateLong(CurrentDate)))
    print()
    print("POLICY     CUSTOMERS             INSURANCE        EXTRA          TOTAL")
    print("NUMBER     NAME                   PREMIUM         COSTS         PREMIUM")
    print("=======================================================================")

    PolicyCtr = 0
    InsurPremAcc = 0
    ExtraCostAcc = 0
    TotalInsureAcc = 0

    # opening the file so I can gather my values.

    f = open("Policies.dat", "r")

    for CustomerRecord in f:

        CustomerLine = CustomerRecord.split(",")

        PolicyNum = CustomerLine[0].strip()
        CustFirstName = CustomerLine[2].strip()
        CustLastName = CustomerLine[3].strip()
        CustFullName = (CustFirstName +  " " + CustLastName)
        CustNumCars = int(CustomerLine[9].strip())
        ExtraLiability = CustomerLine[10].strip()
        GlassCover = CustomerLine[11].strip()
        LoanerCar = CustomerLine[12].strip()

        # my calculations

        if CustNumCars == 1:
            InsurancePremiumCost = BasicPremium_Amt
        else:
            InsurancePremiumCost = ((CustNumCars - 1) * (BasicPremium_Amt - (BasicPremium_Amt * AddCarDiscount_Rate)))

        if ExtraLiability.upper() == "Y":
            ExtraLiabilityCost = ExtraLiability_Amt * CustNumCars
        else:
            ExtraLiabilityCost = 0

        if GlassCover.upper() == "Y":
            GlassCoverageCost = GlassCoverage_Amt * CustNumCars
        else:
            GlassCoverageCost = 0

        if LoanerCar.upper() == "Y":
            LoanerCarCost = LoanerCoverage_Amt * CustNumCars
        else:
            LoanerCarCost = 0

        TotalExtraCost = ExtraLiabilityCost + GlassCoverageCost + LoanerCarCost
        TotalInsurePremiumCost = InsurancePremiumCost + TotalExtraCost


        PolicyCtr += 1
        InsurPremAcc += InsurancePremiumCost
        ExtraCostAcc += TotalExtraCost
        TotalInsureAcc += TotalInsurePremiumCost

        # Printing values for the listing.

        print(" {:<6s}   {:<20s} {:>9s}      {:>9s}      {:>9s}".format(PolicyNum, CustFullName.upper(), FV.FDollar2(InsurancePremiumCost), FV.FDollar2(TotalExtraCost),FV.FDollar2(TotalInsurePremiumCost)))
    print("=======================================================================")
    print("Total policies: {:<3d}            {:>10s}     {:>10s}     {:>10s}".format(PolicyCtr, FV.FDollar2(InsurPremAcc), FV.FDollar2(ExtraCostAcc), FV.FDollar2(TotalInsureAcc)))

    f.close()

    print()
    while True:
        BackToMenu = input(" Press enter to return to menu. ")
        break


# function for the Exception Report.

def Exceptionreport():

    # Reading the values from the defaults table so the constants can be used for calculations

    DefaultsData = open("OSICDef.dat", "r")

    PolicyNum = int(DefaultsData.readline())
    BasicPremium_Amt = float(DefaultsData.readline())
    AddCarDiscount_Rate = float(DefaultsData.readline())
    ExtraLiability_Amt = float(DefaultsData.readline())
    GlassCoverage_Amt = float(DefaultsData.readline())
    LoanerCoverage_Amt = float(DefaultsData.readline())
    HST_RATE = float(DefaultsData.readline())
    ProcessingFee_Amt = float(DefaultsData.readline())

    DefaultsData.close()

    print()
    print("ONE STOP INSURANCE COMPANY ")
    print("MONTHLY PAYMENT LISTING AS OF {}".format(FV.FDateLong(CurrentDate)))
    print()
    print("POLICY     CUSTOMERS             TOTAL                        TOTAL        MONTHLY")
    print("NUMBER     NAME                 PREMIUM         HST           COST         PAYMENT")
    print("==================================================================================")

    MonthlyPayCtr = 0
    TotalPreAcc = 0
    HSTAcc = 0
    TotalCostAcc = 0
    PaymentAcc = 0

    # opening the file so I can gather my values.

    f = open("Policies.dat", "r")

    for CustomerRecord in f:

        CustomerLine = CustomerRecord.split(",")

        PayMethod = CustomerLine[13].strip()

        PolicyNum = CustomerLine[0].strip()
        PolicyDate = CustomerLine[1].strip()
        CustPolicyDate = datetime.datetime.strptime(PolicyDate, "%Y-%m-%d")
        CustFirstName = CustomerLine[2].strip()
        CustLastName = CustomerLine[3].strip()
        CustFullName = (CustFirstName + " " + CustLastName)
        CustAddress = CustomerLine[4].strip()
        CustCity = CustomerLine[5].strip()
        CustProvince = CustomerLine[6].strip()
        CustPostal = CustomerLine[7].strip()
        CustPhone = CustomerLine[8].strip()
        CustNumCars = int(CustomerLine[9].strip())
        ExtraLiability = CustomerLine[10].strip()
        GlassCover = CustomerLine[11].strip()
        LoanerCar = CustomerLine[12].strip()
        CustGrandTotal = float(CustomerLine[14].strip())

        # statement to find customers who are doing payments.

        if PayMethod.upper() == "M":

            # Calculations to find costs.

            if CustNumCars == 1:
                InsurancePremiumCost = BasicPremium_Amt
            else:
                InsurancePremiumCost = (
                            (CustNumCars - 1) * (BasicPremium_Amt - (BasicPremium_Amt * AddCarDiscount_Rate)))

            if ExtraLiability.upper() == "Y":
                ExtraLiabilityCost = ExtraLiability_Amt * CustNumCars
            else:
                ExtraLiabilityCost = 0

            if GlassCover.upper() == "Y":
                GlassCoverageCost = GlassCoverage_Amt * CustNumCars
            else:
                GlassCoverageCost = 0

            if LoanerCar.upper() == "Y":
                LoanerCarCost = LoanerCoverage_Amt * CustNumCars
            else:
                LoanerCarCost = 0

            TotalExtraCost = ExtraLiabilityCost + GlassCoverageCost + LoanerCarCost
            TotalInsurePremiumCost = InsurancePremiumCost + TotalExtraCost

            HST = TotalInsurePremiumCost * HST_RATE
            TotalCost = HST + TotalInsurePremiumCost

            MonthlyPayment = (TotalCost + ProcessingFee_Amt) / 12


            MonthlyPayCtr += 1
            TotalPreAcc += TotalInsurePremiumCost
            HSTAcc += HST
            TotalCostAcc += TotalCost
            PaymentAcc += MonthlyPayment

            # Printing information for people doing payments only.

            print("{:<6s}   {:<20s} {:>9s}      {:>7s}      {:>9s}     {:>9s}".format(PolicyNum, CustFullName.upper(), FV.FDollar2(TotalInsurePremiumCost), FV.FDollar2(HST), FV.FDollar2(TotalCost), FV.FDollar2(MonthlyPayment)))
    print("==================================================================================")
    print("Total policies: {:<3d}           {:>10s}    {:>9s}     {:>10s}    {:>10s}".format(MonthlyPayCtr, FV.FDollar2(TotalPreAcc), FV.FDollar2(HSTAcc), FV.FDollar2(TotalCostAcc), FV.FDollar2(PaymentAcc)))

    f.close()

    print()
    while True:
        BackToMenu = input(" Press enter to return to menu. ")
        break




# Main menu program

while True:

    print()
    print("    One Stop insurance Company    ")
    print("             Main Menu            ")
    print()
    print(" 1. Enter new insurance policy. ")
    print(" 2. Show all policy listings. ")
    print(" 3. Show policy listing for monthly payments. ")
    print(" 4. Quit.")
    print()

    while True:

        try:
            Selection = input(" Enter choice (1-4): ")
            Selection = int(Selection)
        except:
            print(" Error - Invalid Input")
        else:
            if Selection < 1 or Selection > 4:
                print(" Error - Must be 1 to 4 ")
            else:
                break

    print()

    if Selection == 1:
        NewPolicy()
    if Selection == 2:
        Detailreport()
    if Selection == 3:
        Exceptionreport()
    if Selection == 4:
        print("Thanks for using this program. ")
        break
