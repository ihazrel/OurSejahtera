# **********************************************************************************************
# Program: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL8V
# Trimester: 2110
# Year: 2021/22 Trimester 1
# Member_1: 1211101248 | Ang Khai Pin | 1211101248@student.mmu.edu.my | 01157725120
# Member_2: 1211101260 | Samson Yoong Wen Kuang | 1211101260@student.mmu.edu.my | 0102711168
# Member_3: 1211101303 | Aiman Faris Bin Aidi Zamri | 1211101303@student.mmu.edu.my | 0136811083
# Member_4: 1211101070 | Hazrel Idlan Bin Hafizal | 1211101070@student.mmu.edu.my | 01110522347
# **********************************************************************************************
# Task Distribution
# Member_1: Flowchart, help with the code
# Member_2: Came up with 20 public users, help with the code
# Member_3: Help with the code, check errors
# Member_4: Coded most parts, came up with the codes
# **********************************************************************************************

import abc
from os import name
import sqlite3
from sqlite3.dbapi2 import connect

conn=sqlite3.connect('account.db')
c=conn.cursor()
'''
c.execute("""CREATE TABLE account
        (phone text,
        password text,
        name text,
        age text,
        postcode text,
        address text,
        risk_cat text,
        risky text,
        v_place text,
        v_date text,
        v_time text,
        confirmation text;""")'''
        
conn.close

conn2=sqlite3.connect('vacc_center.db')
c2=conn2.cursor()
'''
c2.execute("""CREATE TABLE VC
        (center text,
        CNAME TEXT,
        capacity text);""")'''
        
conn2.close


#phone_list=['user','admin']
#password_list=['user','admin']
#name_list=['user','admin']
#age_list=['user','admin']
#postcode_list=['user','admin']
#address_list=['user','admin'] 


def login():
    print('\n'+'LOGIN'+'\n')

    conn=sqlite3.connect('account.db')
    c=conn.cursor()

    phone,password=input('\n'+"Please enter your phone: "),input("Please enter your password: ")

    if phone=='admin' and password=='admin':
                ad=input('Please enter your pin number: ')

                if str(ad)=='888888':
                    admin_login()
                else:
                    print('Wrong Pin')
                    login()
    else:
        c.execute("SELECT *,oid FROM account WHERE phone ='"+phone+"'")
        records=c.fetchall()



        if len(records)==0:
            print('You are not registered yet')

            reg=input('Do you want to register (y/n)'+'\n').lower()
            if reg=='y':
                register()
            else:
                login()

        else:       
            for record in records:
                if str(phone)==str(record[0]) and str(password)==str(record[1]):
                    #p_user_login_menu(record[0])
                    x=phone
                    p_user_login_menu(x)

                else:
                    print('Your Phone / Password is incorrect')
                    login()



    conn.commit()
    conn.close()
        
    return

    #else:
    #    for x in range(len(phone_list)):
    #
    #        if str(phone) == str(phone_list[x]) and str(password) == str(password_list[x]):
    #            p_user_login_menu(x)
    #            break
    #
    #    else:
    #        print('\n'+'Bug Off')
    #         
    

def register():
    print('\n'+'REGISTRATION'+'\n')

    conn=sqlite3.connect('account.db')
    c=conn.cursor()

    print('\n'+"Please enter the information needed"+'\n')
    name, age, phone, password, postcode, address = input("Name: "),input("Age: "),input("Phone: "),input("Password: "),input("Postcode: "),input("Address: ")
    
    #phone_list.append(phone),password_list.append(password),name_list.append(name),age_list.append(age),postcode_list.append(postcode),address_list.append(address)

    c.execute("INSERT INTO account VALUES(:phone,:password,:name,:age,:postcode,:address,:risk_cat,:risky,:v_place,:v_date,:v_time,:confirmation)",
        {
            'phone':phone,
            'password':password,
            'name':name,
            'age':age,
            'postcode':postcode,
            'address':address,
            'risk_cat':'null',
            'risky':'null' ,
            'v_place':'null',
            'v_date':'null',
            'v_time':'null',
            "confirmation":'null'
        }
        )

    conn.commit()
    conn.close()
    

    a=input('\n'+'Do you want to login? y/n'+'\n').lower()
    if a == 'y':
        login()
    else:
        print('\n'+'Thanks')
        exit 
        
    return
    
def choice():
    
    ch=input('\n'+'Enter \'1\' for login in and \'2\' to register. '+ '\n')

    if ch == '1':
        login()
    elif ch == '2':
        register()
    else:
        print('Invalid Choice'+'\n')
        choice()

def p_user_login_menu(a):

    conn=sqlite3.connect('account.db')
    c=conn.cursor()

    c.execute('select name from account where phone like "'+a+'"')
    records=c.fetchone()[0]

    print('\n'+f'You successfully logged in as {str(records)} '+'\n')

    user_menu(a)

    conn.commit()
    conn.close()

    return

def user_menu(a):

    print('\n'+'MENU'+'\n')
    menu=input('1.My Profile'+'\n'+'2.Update Medical History'+'\n'+'3.Update Job Status'+'\n'+'4.Check Appointment'+'\n'+'5.Logout'+'\n')

    if menu == '1':
        profile(a)

    elif menu=='2':
        medical_history(a)

    elif menu=='3':
        occupation(a)

    elif menu=='4':
        vaccination_center(a)
    
    elif menu == '5':
        logout()

def profile(a):
    print('\n'+'MY PROFILE'+'\n')
    
    conn=sqlite3.connect('account.db')
    c=conn.cursor()

    cursor = conn.execute("SELECT * from account where phone like '"+a+"'")
    for row in cursor:

#1.Student'+'\n'+'2.Non-essetial worker'+'\n'+'3.Energy,food and transportation worker'+
# '\n'+'4.Community Services'+'\n'+'5.Health-care Workers'+'\n'+'6.Others

        job=''

        if row[6]=='1':
            job='Student'
        elif row[6]=='2':
            job='Non-essential worker'
        elif row[6]=='3':
            job='Energy, food or transportation worker'
        elif row[6]=='4':
            job='Community Services'
        elif row[6]=='5':
            job='Health-care Worker'
        elif row[6]=='6':
            job='Others'

        risk=''

        if row[7]=='y':
            risk='You are High Risk person'
        elif row[7]=='n':
            risk='You are Low Risk person '
        else: 
            risk='You are not yet update your medical history'
 
        print('\n'+'Name: '+row[2])
        print('Age: '+row[3])
        print('Phone: '+row[0])
        print('Postcode: '+row[4])
        print('Address: '+row[5])
        print('Job: '+job+'\n')
        print(risk+'\n'), "\n"
        
    conn.commit()
    conn.close()

    back=input('\n'+'Do you want to go to menu (y/n) '+'\n').lower()
    if back=='y':
        user_menu(a)
    else:
        exit()
     
    
    
    return

def medical_history(a):
    print('\n'+'MEDICAL HISTORY'+'\n')

    import sqlite3

    conn=sqlite3.connect('account.db')
    c=conn.cursor()

    one=input('\n'+'Are you exhibiting 2 or more symptoms as listed below?'+'\n'*2+'Fever'+'\n'+'Chills'+'\n'+'Shivering'+'\n'+'Body Ache'+'\n'+
    'Headache'+'\n'+'Sore Throat'+'\n'+'Nausea or Vomiting'+'\n'+'Diarrhea'+'\n'+'Fatigue'+'\n'+'Runny nose or nasal congestion'+'\n'*2+'(Y/n)'+'\n').lower()
    two=input('\n'+'Besides the above, are you exhibiting any of the symptoms listed below?'+'\n'*2+'Cough'+'\n'+'Difficulty Breathing'+'\n'+
    'Loss of Smell'+'\n'+'Loss of taste'+'\n'*2+'(Y/n)'+'\n').lower()
    three=input('\n'+'Have you attended any event / areas associated with known COVID-19?'+'\n'*2+'(Y/n)'+'\n').lower()
    four=input('\n'+'Have you travelled to any country outside Malaysia within 14 days before onset of symptoms?'+'\n'*2+'(Y/n)'+'\n').lower()
    five=input('\n'+'Have you had a close contact to confirmed or suspected case of COVID-19 within 14 days before onset of illness?'+'\n'*2+'(Y/n)'+'\n').lower()
    six=input('\n'+'Are you a MOH COVID-19 volunteer in the last 14 days?'+'\n'*2+'(Y/n)'+'\n').lower()
    risk=False

    c.execute('select age from account where phone like "'+a+'"')
    records=c.fetchone()[0]
    
    if int(records)>=60:
        risk='y'
    else:
        if one=='y' or two=='y' or three=='y' or four=='y' or five=='y' or six=='y':
            risk = 'y'

        else:
            risk='n'

    c.execute("update account set risky = '"+risk+"' where phone like '"+a+"'")

    conn.commit()
    conn.close()

    back=input('\n'+'Do you want to go to menu (y/n) '+'\n').lower()
    if back=='y':
        user_menu(a)
    else:
        exit()

    return

def occupation(a):
    print('\n'+'JOB STATUS'+'\n')

    conn=sqlite3.connect('account.db')
    c=conn.cursor()

    prio_rank=input('\n'+'Choose which are related to you?'+'\n'*2+'1.Student'+'\n'+'2.Non-essential worker'+'\n'+'3.Energy,food or transportation worker'+
        '\n'+'4.Community Services'+'\n'+'5.Health-care Workers'+'\n'+'6.Others'+'\n').lower()

    if int(prio_rank)>6 or int(prio_rank)==0:
            print('\n'+'Invalid!!'+'\n'+'Choose only between 1 to 6'+'\n')
            occupation()

    if prio_rank=='6':
        prio_rank = '0'

    c.execute("update account set risk_cat ='"+prio_rank+"' where phone = '"+a+"'",
            {
                'risk_cat':prio_rank
            })
    
    conn.commit()
    conn.close()

    back=input('\n'+'Do you want to go to menu (y/n) '+'\n').lower()
    if back=='y':
        user_menu(a)
    else:
        exit()
    
    return

    

def vaccination_center(a):
    print('\n'+'VACCINE APPOINTMENT')
    
    conn=sqlite3.connect('account.db')
    conn2=sqlite3.connect('vacc_center.db')
    c=conn.cursor()
    c2=conn2.cursor()

    c.execute("select v_place, v_date, v_time from account where phone like '"+a+"'")
    vac=c.fetchall()[0]
    
    

    if vac[0]=='null' and vac[1]=='null':
        print('\n'+'No Appointment yet. Please check next time.')

    else:
        c2.execute('select cname from vc where center ="'+vac[0]+'"')
        vname=c2.fetchall()[0]
        
        vac_place=vac[0]
        vac_date=vac[1]
        vac_time=vac[2]
        print('\n'+vac_place+' '+vname[0]+' '+vac_date+'\n' +vac_time)

        go_vac=input('Can you attend on that specific time and place? (y/n) '+'\n').lower()

        c.execute("select risky from account where phone like '"+a+"'")
        records=c.fetchone()[0]
        
        if str(records)=='n' and go_vac =='y':
            print('\n'+'Your appointment is confirmed')
            c.execute('update account set confirmation = "y" where phone like "'+a+'"')
        
        elif records=='y' and go_vac=='y':
            print('\n'+'You are a High Risk person. You will be given another appointment')
            c.execute('update account set confirmation = "n" where phone like "'+a+'"')
        
        else:
            print('\n'+'You cannot attend on the given time. You will be given another appointment')
            c.execute('update account set confirmation = "n" where phone like "'+a+'"')
    
    conn.commit()
    conn.close()

    back=input('\n'+'Do you want to go to menu (y/n) '+'\n').lower()
    if back=='y':
        user_menu(a)
    else:
        exit()
    
    return

def logout():
    exit()

  ############################################################ADMIN########################################################################

def admin_login():
    print('\n'+'You successfully logged in as ADMIN'+'\n')
    print('\n'+'ADMIN MENU'+'\n')

    a=input('1.Set Up Vaccination Center'+'\n'+'2.List User'+'\n'+'3.List Low Risk person and High Risk person'+'\n'+'4.User search'+'\n'+'5.Logout'+'\n')

    if a == '1':
        set_vacc()

    elif a=='2':
        user_list()

    elif a=='3':
        user_risk_list()

    elif a=='4':
        user_search()

    elif a=='5':
        logout()

    
    return

def set_vacc():
    print('\n'+'VACCINE CENTER')

    a=input('\n'+'1.New vaccine center'+'\n'+'2.List vaccine center'+'\n'+'3.List user that need vaccine appointment'+'\n'+'4.Assign appointment to user'+'\n')

    if a=='1':
        new_center()

    elif a=='2':
        vc_list()
    
    elif a=='3':
        vac_list()

    elif a=='4':
        assign_vacc()
        

def new_center():

    conn2=sqlite3.connect('vacc_center.db')
    c2=conn2.cursor()
    
    a=input('\n'+'Please enter new vaccine center postcode: ')
    b=input('\n'+'Please enter the vaccine center name: ')
    c=input('\n'+'Please enter the capacity per hour: ')

    c2.execute("INSERT INTO vc VALUES(:center,:cname,:capacity,:capacity_per_hour)",
        {
            'center':a,
            'cname':b,
            'capacity_per_hour':c,
            'capacity':'0'
        })

    conn2.commit()
    conn2.close()

    back=input('\n'+'Do you want to go to menu (y/n) '+'\n').lower()

    if back=='y':
        admin_login()
    else:
        exit()

def vc_list():

    conn2=sqlite3.connect('vacc_center.db')
    c2=conn2.cursor()

    c2.execute('select center, cname, capacity from vc')
    lists=c2.fetchall()

    print('\n')

    for list in lists:
        print(list[0]+' '+list[1]+' Capacity:'+list[2])

    conn2.commit()
    conn2.close()

    back=input('\n'+'Do you want to go to menu (y/n) '+'\n').lower()

    if back=='y':
        admin_login()
    else:
        exit()
    
    return

def vac_list():
    
    conn=sqlite3.connect('account.db')
    conn2=sqlite3.connect('vacc_center.db')
    c=conn.cursor()
    c2=conn2.cursor()

    c.execute('select phone, name from account where v_place like "null"')
    records=c.fetchall()

    print('\n'+'USER THAT NEEDS APPOINTMENT'+'\n')

    for record in records:
        print(record[1]+' '+record[0])

    conn.commit()
    conn2.commit()
    conn.close()
    conn2.close()

    back=input('\n'+'Do you want to go to menu (y/n) '+'\n').lower()

    if back=='y':
        admin_login()
    else:
        exit()

def assign_vacc():

    print('\n'+'ASSIGN APPOINTMENT TO USER'+'\n')

    a=input('Please enter phone number: ')

    conn=sqlite3.connect('account.db')
    conn2=sqlite3.connect('vacc_center.db')
    c=conn.cursor()
    c2=conn2.cursor()

    c.execute('select name, address, v_place from account where phone like "'+a+'"')
    records=c.fetchall()[0]

    print('\n'+records[0]+' '+records[1]+'\n')

    if records[2]=='null':

        c2.execute('select center, cname, capacity from vc')
        lists=c2.fetchall()

        for list in lists:
            print(list[0]+' '+list[1]+' Capacity:'+list[2])

        v_place=input('\n'+'Where do you want to assign the appointment. Enter the postcode: ')
        v_date=input('When do you want to assign the appointment. (In (dd/mm) format): ')
        v_time=input('When do you want to assign the appointment. (In 00:00) format): ')

        c2.execute('select capacity from vc where center like "'+v_place+'"')
        capacity=c2.fetchall()[0]
        new_cap=int(capacity[0])+1

        c2.execute('update vc set capacity ="'+str(new_cap)+'" where center like "'+v_place+'"')
        c.execute('update account set v_place = "'+v_place+'" where phone like "'+a+'"')
        c.execute('update account set v_date = "'+v_date+'" where phone like "'+a+'"')
        c.execute('update account set v_time = "'+v_time+'" where phone like "' +a+'"')

        conn.commit()
        conn2.commit()
        conn.close()
        conn2.close()
    
    else:
        print('This user already have appointment')

    back=input('\n'+'Do you want to go to menu (y/n) '+'\n').lower()

    if back=='y':
        admin_login()
    else:
        exit()
    
    return


def user_list():
    conn=sqlite3.connect('account.db')
    c=conn.cursor()

    c.execute('select name, phone from account order by name')
    records=c.fetchall()

    print('')

    for record in records:
        print(record[0]+'  '+record[1])
    

    #print('\n')
#
    #for record in records:
    #    print(record[0])

    conn.commit()
    conn.close()

    back=input('\n'+'Do you want to go to menu (y/n) '+'\n').lower()

    if back=='y':
        admin_login()
    else:
        exit()

    return

def user_risk_list():
    conn=sqlite3.connect('account.db')
    c=conn.cursor()

    print('\n'+'HIGH RISK'+'\n')
    c.execute('select name, phone from account where risky like "y" order by name')
    a=c.fetchall()

    for record in a:
        print(record[0]+'  '+record[1])

    print('\n'+'LOW RISK'+'\n')
    c.execute('select name, phone from account where risky like "n" order by name')
    a=c.fetchall()

    for record in a:
        print(record[0]+'  '+record[1])

    conn.commit()
    conn.close()

    back=input('\n'+'Do you want to go to menu (y/n) '+'\n').lower()

    if back=='y':
        admin_login()
    else:
        exit()
    

    return

    
def user_search():
    conn=sqlite3.connect('account.db')
    c=conn.cursor()

    p=input('\n'+'Please enter phone number: ')

    cursor=c.execute("select * from account where phone like '"+p+"'")
    for row in cursor:
        print('\n'+'Name: '+row[2])

        print('Age: '+row[3])

        print('Phone: '+row[0])

        print('Postcode: '+row[4])

        print('Address: '+row[5])

        print('Risk Category: '+row[6])

        if row[7]=='y':
            risk='High Risk'
        else:
            risk='Low Risk'
        print('Risk: '+risk)
        #print('Vaccination place: '+row[8])
        #print('Vaccination date: '+row[9]+'\n')


        if row[8]== None or row[8] == 'null':
            print('Vaccination place will be given later.')
        else:
            print('Vaccination place: '+row[8])

        if row[9]== None or row[9]=='null':
            print('Vaccination time will be given later.')
        else:
            print('Vaccination date: '+row[9])

        if row[10]== None or row[10]=='null':
            print('Vaccination time will be given later.')
        else:
            print('Vaccination time: '+row[10])

        if row[11]== None or row[10] == 'null':
            print('Appointment not confirmed yet.')
        elif row[11] == "y":
            print("Appointment is confirmed.")
        elif row[11] == 'n':
            print("Appointment is canceled. New appointment needed"+'\n')

    

    conn.commit()
    conn.close()
    
    back=input('\n'+'Do you want to go to menu (y/n) '+'\n').lower()

    if back=='y':
        admin_login()
    else:
        exit()
    
    return



choice()