from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.core.files import File
import math
import re
from django.template.context import RequestContext

def query_filter(que):
    qword=""
    query=[]
    stopwords=("be","is","was","are","were","can","will","do","does","did","in","the","of",)
    qwords=("when","where","what","which","why","who","how",)
    for term in que:
        if term in stopwords:
            pass
        elif term in qwords:
            qword+=term
        else:
            query.append(term)
    return (qword,query)

def reply(query,result):
    answer=""
    i=0
    while answer=="":
        myfile=File(open("/Users/Adward/Github/Info-Retrieval-Project/djcode/mysite/docs/"+result[i][0]))
        ls=re.split('[,;. \n-/]',myfile.read())
        pat=re.compile(r'[A-Z][a-z]+')
        pat2=re.compile(r'[A-Z]+')
        flag=0
        cnt=0
        for word in ls:
            if flag==0:
                if word in query:
                    flag=1
                    cnt=1
                elif pat.match(word) or pat2.match(word):
                    flag=2
                    cnt=1
                    answer+=" "+word
                else:
                    pass
            elif flag==1:
                if word.lower() in query:
                    cnt=1
                elif pat.match(word) or pat2.match(word):
                    flag=3
                    answer+=" "+word
                elif cnt>=5:
                    flag=0
                else:
                    cnt+=1
            elif flag==2:
                if word.lower() in query:
                    break
                elif pat.match(word) or pat2.match(word):
                    cnt=1
                    answer+=" "+word
                elif cnt>=5:
                    flag=0
                    answer=""
                else:
                    cnt+=1
            elif flag==3:
                if pat.match(word) or pat2.match(word):
                    answer+=" "+word
                else:
                    break
            else:
                pass
        i+=1
    return answer

def search_form(request):
    return render(
            request,
            'force.html'
            #'search_form.html'
            #template_name = '/Users/Adward/Github/Info-Retrieval-Project/djcode/mysite',
            #context_instance=RequestContext(request)
            )

def search(request):
    if 'q' in request.GET:
        qword,query = query_filter(request.GET['q'].split(' '))
        result = readIndex(query) #n needed
        message = "<p><b>"+reply(query,result)+"</b></p><br>#####<br>"+showResult(result)
    else:
        message = 'You submitted an empty query.'
    return HttpResponse(message)

#{term1:[[doc1,tf,line1,line2,...],[doc2,...]],term2:...}
def readIndex(query,n=1000):#n is the number of total docs
    dic={}
    for term in query:
        dic[term]=[]
        df=0
        myfile=File(open("/Users/Adward/Github/Info-Retrieval-Project/djcode/mysite/index/"+term))
        for line in myfile:
            dic[term].append(line.split(':'))
            df+=1
        myfile.close()
        for doc in dic[term]: #replace tf with w
            doc[1]=float((1.0+math.log10(float(doc[1])))*math.log10(n*1.0/df))
        dic[term]=sorted(dic[term],key=lambda ls:ls[1],reverse=True) #descend
        #for doc in dic[term]:#optional
        #    del doc[1]
    ###intersect
    for term in query[1:]:
        i=0
        while i < len(dic[query[0]]):
            if len(dic[query[0]][i])>3 :
            #might be the first line above the title that includes keyword                
                dic[query[0]][i][2]=dic[query[0]][i][3]
                del dic[query[0]][i][3:]
            flag=0
            for doc2 in dic[term]:
                if dic[query[0]][i][0]==doc2[0]:
                    flag=1
                    dic[query[0]][i][1]*=doc2[1]
                    if len(doc2)>3 :
                        dic[query[0]][i].append(doc2[3])
                    else:
                        dic[query[0]][i].append(doc2[2])
                    break
            if flag==0:
                del dic[query[0]][i]
            i+=1
    #sort again using the multiplied w value
    dic[query[0]]=sorted(dic[query[0]],key=lambda ls:ls[1],reverse=True)
    return dic[query[0]]            

def showResult(result):
    show=""
    for doc in result:
        myfile=File(open("/Users/Adward/Github/Info-Retrieval-Project/djcode/mysite/docs/"+doc[0]))
        l=0
        for line in myfile:
            l+=1
            if l==1: #url
                url = line
            elif l==2: #title
                show += "<p><a href="+url+">"+line+"</a></p>"
            else:
                if len(doc)<=3:
                    if (l-1)==int(doc[2]):
                        show += line+"<br>"
                else:
                    if (l-1)==int(doc[3]):
                        show += line+"<br>"
        myfile.close()
        show+="<br>"
    return show
