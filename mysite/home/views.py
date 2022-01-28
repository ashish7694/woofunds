from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.db.models import Q

def login(request):
    if request.method == 'POST':
        login = None
        try:
            login = AngelInvester.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['email'] = request.POST['email']
            request.session['role'] = "investor"
            data = Trade.objects.filter(~Q(investor=login))
            return render(request, 'index.html', {'message': login, 'data': data})
        except:
            return render(request, 'login.html', {'message': "Not found!"})
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        try:
            user = AngelInvester.objects.get(email=request.POST['email'])
            return render(request, 'register.html', {"message":"This email already available!"})
        except:
            AngelInvester(
                name = request.POST['name'],
                email = request.POST['email'],
                password = request.POST['password'],
                banker_number = request.POST['contact'],
            ).save()
            AgentDetails(
                investor = AngelInvester.objects.get(email=request.POST['email'])
            ).save()
            message = "Yor are now a member of WOO Funds!"
            return render(request, 'register.html', {"message":message})
    else:
        return render(request, 'register.html')

def password(request):
    return render(request, 'password.html')

def profileDetails(request):
    if request.session['email']:
        test = None
    else:
        return render(request, 'login.html')
    profile = AngelInvester.objects.get(email=request.session['email'])
    try:
        agentDetails = AgentDetails.objects.get(investor=profile)
    except:
        agentDetails = profile
    return render(request, 'profile.html', {'data': agentDetails})

    # return render(request, 'profile.html')
    
def postprofiledetails(request):
    if request.session['email']:
        test = None
    else:
        return render(request, 'login.html')
    agent = AngelInvester.objects.get(pk=request.POST['agentid'])
    try:
        agentDetails = AgentDetails.objects.get(investor=agent)
        agentDetails.select_member = request.POST['member']
        agentDetails.city = request.POST['city']
        agentDetails.state = request.POST['state']
        agentDetails.postal_code = request.POST['code']
        agentDetails.Country = request.POST['country']
        agentDetails.website = request.POST['website']
        agentDetails.primary_type_of_cap_prov = request.POST['primary']
        agentDetails.expected_return_per_year = request.POST['expected']
        agentDetails.minimum_valuation_of_interest = request.POST['Minimum']
        agentDetails.maximum_valuation_of_interest = request.POST['Maximum']
        agentDetails.bussiness_reviewed_last_12month = request.POST['reviewed']
        agentDetails.investment_last_12month = request.POST['investment']
        agentDetails.total_invested_last_12month = request.POST['invested']
        agentDetails.linkedin = request.POST['linkedin']
        agentDetails.facebook = request.POST['facebook']
        agentDetails.twitter = request.POST['twitter']
        agentDetails.blog = request.POST['blog']
        agentDetails.title = request.POST['title']
        agentDetails.general_description = request.POST['comment']
        agentDetails.company_web = request.POST['website']
        agentDetails.company_name = request.POST['company_name']
        agentDetails.select_role = request.POST['role']
        agentDetails.investment_amount = request.POST['invamt']
        agentDetails.investment_round = request.POST['invrou']
        agentDetails.investment_type = request.POST['invtyp']
        agentDetails.investment_date = request.POST['investment_date']
        agentDetails.save()
    except:
        AgentDetails(
            investor = agent,
            select_member = request.POST['member'],
            city = request.POST['city'],
            state = request.POST['state'],
            postal_code = request.POST['code'],
            Country = request.POST['country'],
            website = request.POST['website'],
            primary_type_of_cap_prov = request.POST['primary'],
            expected_return_per_year = request.POST['expected'],
            minimum_valuation_of_interest = request.POST['Minimum'],
            maximum_valuation_of_interest = request.POST['Maximum'],
            bussiness_reviewed_last_12month = request.POST['reviewed'],
            investment_last_12month = request.POST['investment'],
            total_invested_last_12month = request.POST['invested'],
            linkedin = request.POST['linkedin'],
            facebook = request.POST['facebook'],
            twitter = request.POST['twitter'],
            blog = request.POST['blog'],
            title = request.POST['title'],
            general_description = request.POST['comment'],
            company_web = request.POST['website'],
            company_name = request.POST['company_name'],
            select_role = request.POST['role'],
            investment_amount = request.POST['invamt'],
            investment_round = request.POST['invrou'],
            investment_type = request.POST['invtyp'],
            investment_date = request.POST['investment_date'],
        ).save()
    agent.name = request.POST['name']
    agent.email = request.POST['email']
    agent.banker_number = request.POST['phone']
    agent.profile = request.POST['logo']
    agent.save()
    profile = AngelInvester.objects.get(email=request.session['email'])
    agentDetails = AgentDetails.objects.get(investor=profile)
    return render(request, 'profile.html', {"message" : "Agent Updated Successfully!", 'data': agentDetails})

def home(request):
    data = None
    try:
        login = AngelInvester.objects.get(email=request.session['email'])
        data = SellPurchase.objects.filter(~Q(created_by=login.email), action_type='sell')
    except:
        return render(request, 'login.html')
    return render(request, 'index.html', {'data': data})

def startup(request):
    try:
        email = request.session['email']
        test = None
    except:
        return render(request, 'login.html')
    data = Company.objects.filter(type='Startup')
    return render(request, 'startup.html', {'data': data})

def ipos(request):
    try:
        email = request.session['email']
        test = None
    except:
        return render(request, 'login.html')
    data = Company.objects.filter(type='Ipos')
    return render(request, 'ipos.html', {'data': data})

def profile(request):
    try:
        email = request.session['email']
    except:
        return render(request, 'login.html')
    profile = AngelInvester.objects.get(email=request.session['email'])
    return render(request, 'ipos.html', {'data': profile})

def unlisted(request):
    try:
        email = request.session['email']
    except:
        return render(request, 'login.html')
    data = Company.objects.filter(type='Unlisted Company')
    return render(request, 'unlisted.html', {'data': data})

def trade(request):
    try:
        email = request.session['email']
    except:
        return render(request, 'login.html')
    data = SellPurchase.objects.filter(created_by=request.session['email'], action_type="purchase")
    return render(request, 'trade.html', {'data': data})

def sell(request):
    try:
        email = request.session['email']
    except:
        return render(request, 'login.html')
    data = Trade.objects.filter()
    return render(request, 'trade.html', {'data': data})

def sellrequest(request):
    try:
        email = request.session['email']
    except:
        return render(request, 'login.html')
    data = Company.objects.filter().all()
    return render(request, 'sellrequest.html', {'company': data})

def postsell(request):
    try:
        email = request.session['email']
    except:
        return render(request, 'login.html')
    SellPurchase(
        company = request.POST['company'],
        shares = request.POST['share'],
        amount = request.POST['price'],
        alot = request.POST['alot'],
        action_type = "sell",
        status = "pending",
        created_by = request.session['email']
    ).save()
    sell = SellPurchase.objects.filter(created_by=request.session['email'])
    return render(request, 'sellrequest.html', {"message" : "Sell request created!"})

def index(request):
    data = Company.objects.filter()
    return render(request, 'frontend/index.html', {'data': data})

def ipo(request):
    data = Company.objects.filter(type='Ipos')
    return render(request, 'frontend/ipos.html', {'data': data})

def share(request):
    data = Company.objects.filter(type='Unlisted Company')
    return render(request, 'frontend/share.html', {'data': data})

def equity(request):
    return render(request, 'frontend/equity.html')

def company(request):
    return render(request, 'frontend/company.html')

def bankers(request):
    return render(request, 'frontend/bankers.html')

def blog(request):
    return render(request, 'frontend/blog1.html')

def blog_post(request):
    return render(request, 'frontend/blog-single.html')

def contact(request):
    return render(request, 'frontend/contact1.html')

def term(request):
    return render(request, 'frontend/term.html')

def risk(request):
    return render(request, 'frontend/risk.html')

def privacy(request):
    return render(request, 'frontend/privacy.html')

def rating(request):
    return render(request, 'frontend/rating.html')

def about(request):
    return render(request, 'frontend/about1.html')

def counselor(request):
    return render(request, 'frontend/counselor1.html')

def services(request):
    return render(request, 'frontend/services1.html')

def pricing(request):
    return render(request, 'frontend/pricing1.html')

def disclaimer(request):
    return render(request, 'frontend/disclaimer.html')

def company_details(request, id):
    data = Company.objects.get(pk=id)
    review = Reviews.objects.filter(created_for=data)
    faq = FAQ.objects.filter(created_by=data)
    news = News.objects.filter(created_by=data)
    board = BoaedMembers.objects.filter(created_for=data, valid=1)
    return render(request, 'frontend/company_details.html', {'data': data, 'boards': board, 'reviews': review, 'faqs': faq, 'news': news})

def sellList(request):
    try:
        email = request.session['email']
    except:
        return render(request, 'login.html')
    agent = AngelInvester.objects.get(email=request.session['email'])
    data = SellPurchase.objects.filter(created_by=agent.email, action_type="sell")
    return render(request, 'sell_list.html', {'data': data})

def sellDelete(request, id):
    try:
        email = request.session['email']
    except:
        return render(request, 'login.html')
    SellPurchase.objects.filter(pk=id).delete()
    messages.success(request, 'Sell deleted successfully!')
    return redirect(request.META.get('HTTP_REFERER'))

def purchase(request, id):
    try:
        email = request.session['email']
    except:
        return render(request, 'login.html')
    data = SellPurchase.objects.get(pk=id)
    SellPurchase(
        company = data.company,
        shares = data.shares,
        amount = data.amount,
        alot = data.alot,
        action_type = "purchase",
        status = "pending",
        created_by = request.session['email']
    ).save()
    messages.success(request, 'Purchase request sent to admin')
    return redirect(request.META.get('HTTP_REFERER'))

def notification(request):
    try:
        email = request.session['email']
    except:
        return render(request, 'login.html')
    return render(request, 'frontend/notification.html')

def message(request):
    try:
        email = request.session['email']
    except:
        return render(request, 'login.html')
    agent = AngelInvester.objects.get(email=request.session['email'])
    message = Message.objects.filter(created_by=agent)
    return render(request, 'frontend/message.html', {'data' : message})

def postMessage(request):
    try:
        email = request.session['email']
    except:
        return render(request, 'login.html')
    if request.method == 'POST':
        Message(
            subject = request.POST['subject'],
            message = request.POST['message'],
            created_by = AngelInvester.objects.get(email=request.session['email'])
        ).save()
        messages.success(request, 'Message send successfully!')
    else:
        pass
    return render(request, 'post_message.html')

def companyDes(request, name):
    data = None
    try:
        email = request.session['email']
    except:
        return render(request, 'login.html')
    try:
        data = Company.objects.get(name=name)
    except:
        data = None
    return render(request, 'companydetails.html', {'data': data})
