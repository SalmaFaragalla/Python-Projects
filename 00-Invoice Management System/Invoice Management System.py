import datetime

class Invoice:
    def __init__(self):
        self.currDate = None
        self.rcDay = None
        self.gracePeriod = None
        self.billIssueOffset = None

        self.rcStartDate = None
        self.createInvoiceDate = None
        self.gpStartDate = None
        self.gpEndDate = None
        self.expirationDate = None
        self.invoiceStatus = None
        self.weekdays = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
                         "Friday": 4, "Saturday": 5, "Sunday": 6}
        return

    def ReadInput(self):
        print("\n")
        print("Enter current date (DD-MM-YYYY): ",end = "")
        self.currDate = input()

        print("Enter start of the recurring cycle day: ",end = "")
        self.rcDay = input()

        print("Enter the grace period: ",end = "")
        self.gracePeriod = int(input())

        print("Enter the bill issue offset: ",end = "")
        self.billIssueOffset = int(input())
        return

    def CalcCreateInvoiceDate(self):
        
        currDateDay , currDateMonth , currDateYear = map (int,self.currDate.split(sep= '-'))
        self.currDate = datetime.date(currDateYear,currDateMonth,currDateDay)

        self.rcDay = self.weekdays[self.rcDay.title()]
        print()

        if (self.rcDay - self.billIssueOffset >= 0):
            createInvoiceDay = self.rcDay - self.billIssueOffset
        else:
            createInvoiceDay = 7-abs(self.rcDay - self.billIssueOffset)

        daysDelta = self.currDate.weekday() - createInvoiceDay


        if (daysDelta) >= 0 :
            self.createInvoiceDate = self.currDate - datetime.timedelta(days = daysDelta)
        else:
            self.createInvoiceDate = self.currDate - datetime.timedelta(days = 7-abs(daysDelta))
        return
    
    def CalcRcStartDate(self):
        self.rcStartDate = self.createInvoiceDate + datetime.timedelta(days = self.billIssueOffset)
        return
    
    def CalcGracePeriodDates(self):
        if (self.gracePeriod>0):
            self.gpStartDate = self.rcStartDate + datetime.timedelta(days = 1)
            self.gpEndDate = self.rcStartDate + datetime.timedelta(days = self.gracePeriod)
            self.expirationDate = self.gpEndDate + datetime.timedelta(days = 1)
        elif (self.gracePeriod == 0):
            self.gpStartDate = self.gpEndDate = self.expirationDate = self.rcStartDate
        return

    def EvalInvoiceStatus(self):
        if (self.createInvoiceDate <= self.currDate <=self.rcStartDate):
            self.invoiceStatus = "Due"
        elif (self.gpStartDate <= self.currDate <= self.gpEndDate):
            self.invoiceStatus = "Overdue"
        elif (self.currDate > self.gpEndDate):
            self.invoiceStatus = "Expired"
        return
    
    def PrintTimeline(self):
        self.CalcCreateInvoiceDate()
        self.CalcRcStartDate()
        self.CalcGracePeriodDates()
        self.EvalInvoiceStatus()

        weedaysWidth = 10
        print("--------------------- Invoice Timeline ---------------------")
        print("Invoice Creation Date:      " , self.createInvoiceDate.strftime('%A').ljust(weedaysWidth, ' '), self.createInvoiceDate , end= "  ")
        print("Due")
        print("Recurring Cycle Start Date: " , self.rcStartDate.strftime('%A').ljust(weedaysWidth, ' ') ,self.rcStartDate , end= "  ")
        print("Due")
        print("Grace Period Start Date:    " , self.gpStartDate.strftime('%A').ljust(weedaysWidth, ' '), self.gpStartDate, end= "  ")
        print("Overdue")
        print("Grace Period End Date:      " , self.gpEndDate.strftime('%A').ljust(weedaysWidth, ' '),  self.gpEndDate, end= "  ")
        print("Overdue")
        print("Expiration Date:            " , self.expirationDate.strftime('%A').ljust(weedaysWidth, ' '),  self.expirationDate, end= "  ")
        print("Expired")
        print("-------------------------------------------------------------")
        print("Invoice Status:    " + self.invoiceStatus)

        return

if __name__ == "__main__":
    newInvoice = Invoice()
    newInvoice.ReadInput()
    newInvoice.PrintTimeline()
