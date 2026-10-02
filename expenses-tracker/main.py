import json
import datetime
from tabulate import tabulate

#-----load the file---------
def load_expenses():
    with open("expenses.json","r") as file:
        system=json.load(file)
        return system
#---------write expenses into that file---------
def save_expenses(full_system):
    with open ("expenses.json" ,"w")as file:
        json.dump(full_system,file,indent=4)





########### main flow 
class ExpensesManager:
    def __init__(self,system):
        self.full_system=system

    #validation part
    @staticmethod
    def date_validation(new_date):
        if not isinstance(new_date,str):
            return False
        try:
            datetime.datetime.strptime(new_date,"%Y-%m-%d")
            return True
        except ValueError:
            return False
    
    @staticmethod
    def category_validation(new_category):
        if not isinstance((new_category),str):
            return False
        elif not new_category.strip():
            return False
        elif len(new_category)<3:
            return False
        elif not new_category.isalpha():
            return False
        else:
            return True
    @staticmethod
    def description_validation(new_description):
        if not isinstance(new_description,str):
            return False
        elif not new_description.strip( ):
            return False
        elif len(new_description)<6:
            return False
        elif not any(ch.islower() for ch in new_description) and not any(ch.isupper() for ch in new_description):
            return False
        else:
            return True
    @staticmethod
    def amount_validation(new_amount):
        if not isinstance(new_amount,(int,float)):
            return False
        elif new_amount<=0:
            return False
        else:
            return True
        
    #----add expenses------
    def adding_expenses(self,date,category,amount,description):
        
        if not self.date_validation(date):
            print("Invalid Date Format! Please use YYYY-MM-DD.")
            return
        if not self.category_validation(category):
            print("INvalid Category! please enter a valid Category.")
            return
        if not self.amount_validation(amount):
            print("Amount is Not Acceptable! Please enter a valid Amount.")
            return
        if not self.description_validation(description):
            print("Description is not Acceptable! please Describe properly.")
            return
        next_id=self.full_system['last_used_id']+1
        self.full_system['last_used_id']=next_id
        expenses_architect={
            "ID":next_id,
            "Date":date,
            "Category":category,
            "Amount":amount,
            "Description":description
        }

        self.full_system['expenses'].append(expenses_architect)
        self.save()
        
    
    #---display expenses-----
    def view_expenses(self):
        return self.full_system['expenses']
    
    #----Search expenses----
    def search_expenses(self,keyword):
        matched_expenses=[]
        try:
            keyword=int(keyword)
        except ValueError:
            
            pass
        if isinstance(keyword,(int,float)):
            for search in self.full_system['expenses']:
                if keyword==search['Amount']:
                    matched_expenses.append(search)
                         
        elif self.date_validation(keyword):
            for search in self.full_system['expenses']:
                if keyword==search['Date']:
                    matched_expenses.append(search)
            
        else:
            for search in self.full_system['expenses']:
                if keyword.lower() in search['Category'].lower():
                    matched_expenses.append(search)
                elif keyword.lower() in search['Description'].lower():
                    matched_expenses.append(search)
                
        return matched_expenses
    ##----update expenses------
    def update_expenses(self,selected_expense,field,new_value):
            
            if field=="1":
                if not self.date_validation(new_value):
                    print("Invalid Date!")
                    return
                selected_expense['Date']=new_value
            elif field=="2":
                if not self.category_validation(new_value):
                    print("Invalid Category!")
                    return
                selected_expense['Category']=new_value
            elif field=="3":
                try:
                    new_value=int(new_value)
                except ValueError:
                    print("Amount must be number!")
                    return
                if not self.amount_validation(new_value):
                    print("Invalid Amount!")
                    return
                selected_expense['Amount']=new_value
            elif field=="4":
                if not self.description_validation(new_value):
                    print("Invalid Description!")
                    return
                selected_expense['Description']=new_value
            else:
                print("Invalid Choice!")
                return
            self.save()
            print("✅ Expense updated successfully!")
    
    #----delete expenses------
    def delete_expenses(self,delete_expense):
        self.full_system['expenses'].remove(delete_expense) 
        self.save()
    #----Report Section-----

    # Dashboard Summary
    def dashboard(self):
        total_expense=len(self.full_system['expenses'])

        total=0
        for amount in self.full_system['expenses']:
            total+=amount['Amount']
        

        average_expenses=round(total/total_expense,2)
        
        highest = self.full_system['expenses'][0]['Amount']
        
        
        for amount in self.full_system['expenses']:
            if amount['Amount']>highest:
                highest=amount['Amount']
        
        lowest=self.full_system['expenses'][0]['Amount']
        for amount in self.full_system['expenses']:
            if amount['Amount']<lowest:
                lowest=amount['Amount']
        return total_expense,total,average_expenses,highest,lowest
    
    #Highest Expense
    def highest_expense(self):
        
        high_expense = self.full_system['expenses'][0]['Amount']
        
        highest_expense_list=[]
        for expense in self.full_system['expenses']:
            if expense['Amount']>high_expense:
                high_expense=expense['Amount']
        for expense in self.full_system['expenses']:
            if high_expense==expense['Amount']:
                highest_expense_list.append(expense)
        return highest_expense_list
    
    #Lowest Expense
    def lowest_expense(self):
        low_expense=self.full_system['expenses'][0]['Amount']
        lowest_expense_list=[]
        for expense in self.full_system['expenses']:
            if expense['Amount']<low_expense:
                low_expense=expense['Amount']
        for expense in self.full_system['expenses']:
            if low_expense==expense['Amount']:
                lowest_expense_list.append(expense)
        return lowest_expense_list
    
    #---Monthly report------
    def monthly_report(self):
        monthly_expense={}
        for expense in self.full_system['expenses']:
            date_object=datetime.datetime.strptime(expense['Date'],"%Y-%m-%d")
            year_month=date_object.strftime("%Y-%m")
            if year_month not in monthly_expense:
                monthly_expense[year_month]=[]
            monthly_expense[year_month].append(expense)
        return monthly_expense
    
    #-----Category Wise Spending---------
    def categorical_total_spending(self):
        categorical_spending={}
        for spending in self.full_system['expenses']:
            category=spending['Category']
            if category not in categorical_spending:
                categorical_spending[category]=spending['Amount']
            else:
                categorical_spending[category]+=spending['Amount']
        return categorical_spending
    
    
    
    

    #--save expenses-----
    def save(self):
        save_expenses(self.full_system)

system = load_expenses()
Manager = ExpensesManager(system)
#input validation functions
#Choice Validation
def choice_validation(message="Enter your choice between (1/2/3/4/5/6/7):"):
    while True:
        choice=input(message).strip()
        if choice in ["1","2","3","4","5","6","7"]:
            return choice
        else:
            print("Invalid Choice!")

# Input validation check
def add_expense_input():
    
    while True:
        date=input("enter Date:")
        if not Manager.date_validation(date):
            print("Enter a valid Date!")
            continue
        break
    while True:
        category=input("Enter category:")
        if not Manager.category_validation(category):
            print("Enter Valid Category!")
            continue
        break
    while True:

        try:
            amount=int(input("Enter amount:"))
        except ValueError:
            print("Amount must be a number.")
            continue
        if not Manager.amount_validation(amount):
            print("Amount must be greater than 0.")
            continue
        break
    while True:
        description=input("enter description:")
        if not Manager.description_validation(description):
            print("Enter Valid Description!")
            continue
        
        break
    return date,category,amount,description

#update input validation
def update_field_validation(message="Enter update Field:"):
    print("What do you want to update?\n1. Date\n2. Category\n3. Amount\n4. Description")
    while True:
            update_field_name=input(message).strip()
            if update_field_name in ["1","2","3","4"]:
                return update_field_name
            else:
                print("Updation Field is Invalid!")

# choose valid expenses index   
def index_find_validation(search_result):
    while True:
        try:
            number=int(input("Enter ID:"))
        except ValueError:
            print("Enter a valid ID!")
            continue
        for expense in search_result:
            if expense['ID']==number:
                return expense
        print("Expense ID not found!")
    

                
#------view expences table form--------
def display_expense(expenses_list):
    table1=[]
    for exp in expenses_list:
        table1.append([exp['ID'],exp['Date'],exp['Category'],exp['Amount'],exp['Description']])

    print(tabulate(table1,headers=['ID','Date','Category','Amount','Description']))



#Report input validation function
def report_choice_validation(message="Enter your choice between (1/2/3/4/5/6):"):
    while True:
        choice=input(message).strip()
        if choice in ["1","2","3","4","5","6"]:
            return choice
        else:
            print("Invalid Choice!")


#dashboard summary report
def dashboard_summary(total_expenses,total,average,highest,lowest):
    print("="*30,end="")
    print("DASHBOARD")
    print("="*30)
    print(f"Total Expenses : {total_expenses}")
    print(f"Total Amount : {total}")
    print(f"Average Expense : {average}")
    print(f"Highest Amount : {highest}")
    print(f"Lowest Amount : {lowest}")
    print("="*60)

#monthly report
def monthly_report_view(expense_list):
    
    for year_month,expense in expense_list.items():
        monthly_total=0
        print(f"\n===== {year_month} =====")
        display_expense(expense)
        for expenditure in expense:
            monthly_total+=expenditure['Amount']
        
        print(f"Monthly Total : {monthly_total}")

#categorical Report
def category_report(expenses_list):
    table=[]
    grand_total=0
    for category,amount in expenses_list.items():
        grand_total+=amount
        table.append([category,amount])

    print(tabulate(table,headers=['Category','Amount']))
    print(f"Grand Total: {grand_total}")



#Report Menu
def report():
    while True:
        print("======================REPORT=========================")
        print("1. Dashboard Summary\n2. Highest Expense\n3. Lowest Expense\n4. Monthly Report\n5. Category-wise Spending\n6. Back")
        print("="*60)

        report_choice=report_choice_validation("Enter your choice between (1/2/3/4/5/6):")
        if report_choice=="1":
            total_expenses,total,average,highest,lowest=Manager.dashboard()
            dashboard_summary(total_expenses,total,average,highest,lowest)
        elif report_choice=="2":
            highest_expenses=Manager.highest_expense()
            if not highest_expenses:
                print("No Expenses Found!")
                continue
            print("==========HIGHEST EXPENSE(S)=============")
            display_expense(highest_expenses)
            print("=" * 60)
        elif report_choice=="3":
            lowest_expenses=Manager.lowest_expense()
            if not lowest_expenses:
                print("No Expenses Found!")
                continue
            print("==========LOWEST EXPENSE(S)=============")
            display_expense(lowest_expenses)
            print("=" * 60)
        elif report_choice=="4":
            monthly_expense=Manager.monthly_report()
            if not monthly_expense:
                print("No Expenses Found!")
                continue
            print("====================MONTHLY REPORT======================")
            monthly_report_view(monthly_expense)
            print("=" * 60)
        elif report_choice=="5":
            categorical_report=Manager.categorical_total_spending()
            if not categorical_report:
                print("No Expenses Found!")
                continue
            print("==================CATEGORYWISE SPENDING=======================")
            category_report(categorical_report)
            print("=" * 60)
        elif report_choice=="6":
            return

##-----------Main Menu--------------------
while True:
    print("="*30,end="")
    print("EXPENSE TRACKER",end="")
    print("="*30)
    print("1. Add Expense\n2. View All Expenses\n3. Search Expenses\n4. Update Expense\n5. Delete Expense\n6. Reports\n7. Exit")
    print("="*60)

    choice=choice_validation("choose your option(1/2/3/4/5/6/7):")
    if choice=="1":
        date,category,amount,description=add_expense_input()
        Manager.adding_expenses(date,category,amount,description)
        print("✅ Expense added successfully!")
        
    elif choice=="2":
        expenses_list=Manager.view_expenses()
        if len(expenses_list)==0:
            print("No Expenses Found!")
            continue
        display_expense(expenses_list)
    elif choice=="3":
        search_keyword=input("Enter What you Want to Search:")
        search_result=Manager.search_expenses(search_keyword)
        if not search_result:
            print("No matching expense found!")
            continue
        display_expense(search_result)
    elif choice=="4":
        update_keyword=input("Enter update keyword:")
        update_search_result=Manager.search_expenses(update_keyword)
        if not update_search_result:
            print("No matching expense found to update.")
            continue
        display_expense(update_search_result)
        selected_expense=index_find_validation(update_search_result)
        updated_field_choice=update_field_validation()
        new_value=input("Enter new value:")
        update_results=Manager.update_expenses(selected_expense,updated_field_choice,new_value)
    elif choice=="5":
        delete_keyword=input("Enter Delete keyword:")
        delete_search_result=Manager.search_expenses(delete_keyword)
        if not delete_search_result:
            print("No matching expense found to Delete.")
            continue
        display_expense(delete_search_result)
        delete_expense=index_find_validation(delete_search_result)
        delete_results=Manager.delete_expenses(delete_expense)
        print("✅ Expense Deleted successfully!")
    elif choice=="6":
        report_view=report()
    
    elif choice=="7":
        break




#---------------Phase-1 complete-------------------------


















 
    
    
    







    


