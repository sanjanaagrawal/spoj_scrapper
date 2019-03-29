from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests as re
import requests
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup
import os
import shutil
from .models import Project_ings
from datetime import date

def index(request):
    list=Project_ings.objects.all()
    my_list={'abc':list}
    return render(request,'my_app/index.html',context=my_list)

def scrape(requests):
    today_date=date.today()
    content=re.get('https://www.spoj.com/ranks/users/114940/').content
    soup=BeautifulSoup(content,"html.parser")
    #details of students of first page
    div_tag=soup.find('div',class_='col-lg-9 col-md-8')
    table = div_tag.find('table',class_='table table-condensed')
    tr_tags=table.find_all('tr')
    for tr in table.find_all('tr'):
        for td in tr.find_all('td'):
            for a_tag in td.find_all('a'):
                url='https://www.spoj.com'+a_tag['href']
                user=a_tag.text
                user_link=url
                content=re.get(url,verify=False).content
                soup=BeautifulSoup(content,"html.parser")
                #history of submissions of each coder-->status
                div_tag=soup.find('div',class_='submenu')
                a_tag=div_tag.find('a')
                #print 'https://www.spoj.com'+ a_tag['href']
                url='https://www.spoj.com'+ a_tag['href']
                content=re.get(url,verify=False).content
                soup=BeautifulSoup(content,"html.parser")
                #questions on first page
                div_tag=soup.find('div',class_='col-lg-10 col-md-9')
                tbody_tag=div_tag.find('tbody')
                tr_tags=tbody_tag.find_all('tr')
                for tr in tr_tags:
                    stat_tag=tr.find('td',class_='statustext text-center')
                    st=stat_tag.text
                    id_no=int(st)
                    date_tag=tr.find('td',class_='status_sm')
                    span_tag=date_tag.find('span')
                    full_string=span_tag.text
                    date_string=full_string[0:10]
                    time_string=full_string[11:19]
                    res_tag=tr.find('td',class_='statusres text-center')
                    slang_tag=tr.find('td',class_='slang text-center')
                    lang_tag=slang_tag.find('span')
                    if date_string == str(today_date):
                        a_tag=tr.find('a')
                        new_link=Project_ings()
                        new_link.username=user
                        new_link.link_username=user_link
                        new_link.problem_name=a_tag.text
                        new_link.problem_link= 'https://www.spoj.com'+a_tag['href']
                        new_link.time_string=time_string
                        new_link.result= res_tag.text
                        new_link.language= lang_tag.text
                        new_link.id_no= id_no
                        id_no=new_link.id_no
                        if not Project_ings.objects.filter(id_no=id_no):
                            new_link.save()

    content=re.get('https://www.spoj.com/ranks/users/114940/').content
    soup=BeautifulSoup(content,"html.parser")
    div_tag=soup.find('div',class_='text-center')
    li_tags=div_tag.find_all('li',class_='')
    for li in li_tags:
        a_tag=li.find('a')
        url='https://www.spoj.com/ranks/users/114940/'+ a_tag['href']
        content=re.get(url,verify=False).content
        soup=BeautifulSoup(content,"html.parser")

        div_tag=soup.find('div',class_='col-lg-9 col-md-8')
        table = div_tag.find('table',class_='table table-condensed')
        tr_tags=table.find_all('tr')
        for tr in table.find_all('tr'):
            for td in tr.find_all('td'):
                for a_tag in td.find_all('a'):
                    url='https://www.spoj.com'+a_tag['href']
                    user=a_tag.text
                    user_link=url
                    content=re.get(url,verify=False).content
                    soup=BeautifulSoup(content,"html.parser")
                    #history of submissions of each coder-->status
                    div_tag=soup.find('div',class_='submenu')
                    a_tag=div_tag.find('a')
                    #print 'https://www.spoj.com'+ a_tag['href']
                    url='https://www.spoj.com'+ a_tag['href']
                    content=re.get(url,verify=False).content
                    soup=BeautifulSoup(content,"html.parser")
                    #questions on first page
                    div_tag=soup.find('div',class_='col-lg-10 col-md-9')
                    tbody_tag=div_tag.find('tbody')
                    tr_tags=tbody_tag.find_all('tr')
                    for tr in tr_tags:
                        stat_tag=tr.find('td',class_='statustext text-center')
                        st=stat_tag.text
                        id_no=int(st)
                        date_tag=tr.find('td',class_='status_sm')
                        span_tag=date_tag.find('span')
                        full_string=span_tag.text
                        date_string=full_string[0:10]
                        time_string=full_string[11:19]
                        res_tag=tr.find('td',class_='statusres text-center')
                        slang_tag=tr.find('td',class_='slang text-center')
                        lang_tag=slang_tag.find('span')
                        if date_string == str(today_date):
                            a_tag=tr.find('a')
                            new_link=Project_ings()
                            new_link.username=user
                            new_link.link_username=user_link
                            new_link.problem_name=a_tag.text
                            new_link.problem_link= 'https://www.spoj.com'+a_tag['href']
                            new_link.time_string=time_string[12:20]
                            new_link.result= res_tag.text
                            new_link.language= lang_tag.text
                            id_no=new_link.id_no
                            if not Project_ings.objects.filter(id_no=id_no):
                                new_link.save()

    return redirect('/index/')
