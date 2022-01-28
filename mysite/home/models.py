from django.db import models
from django.db.models.deletion import CASCADE


class Company(models.Model):
    name = models.CharField(max_length=2000,null=True)
    gst_no = models.CharField(max_length=20, null=True)
    registered_date = models.DateField(null=True)
    sector = models.CharField(max_length=100,null=True)
    total_shares = models.IntegerField(null=True)
    revenue_number = models.IntegerField(null=True)
    purchase_price = models.IntegerField(null=True)
    current_price = models.IntegerField(null=True)
    isin = models.CharField(max_length=2000, null=True)
    pan_no = models.CharField(max_length=2000, null=True)
    email = models.CharField(max_length=2000)
    password = models.CharField(max_length=100, null=True)
    gain_loss = models.FloatField( max_length=10,null=True)
    face_value = models.IntegerField(null=True)
    lot_size = models.IntegerField(null=True)
    logo = models.ImageField(upload_to ='uploads/', null=True)
    about = models.TextField()
    is_verify = models.CharField(max_length=10, null=True)
    is_active = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SalaryExpense(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    commission_expense = models.CharField(max_length=2000, null=True)
    third_party_expense = models.CharField(max_length=2000, null=True)
    office_expense = models.CharField(max_length=2000, null=True)
    assets_expense = models.CharField(max_length=2000, null=True)
    marketing_expense = models.CharField(max_length=2000, null=True)
    online_payments = models.CharField(max_length=2000, null=True)
    audit_fees = models.CharField(max_length=2000, null=True)
    consulting_fees = models.CharField(max_length=2000, null=True)
    miscellaneous_payments = models.CharField(max_length=2000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commission_expense

class AngelInvester(models.Model):
    name = models.CharField(max_length=2000)
    email = models.CharField(max_length=2000)
    password = models.CharField(max_length=100, null=True)
    myprofile = models.CharField(max_length=2000, null=True)
    banker_name = models.CharField(max_length=2000, null=True)
    banker_number = models.CharField(max_length=2000, null=True)
    dob = models.CharField(max_length=2000, null=True)
    pan = models.CharField(max_length=2000, null=True)
    aadhar = models.CharField(max_length=2000, null=True)
    profile = models.ImageField(upload_to ='uploads/')
    address = models.TextField()
    is_verify = models.CharField(max_length=10, null=True)
    is_active = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class InvestmentEquity(models.Model):
    investor = models.ForeignKey(AngelInvester,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=2000, null=True)
    investment_amount = models.CharField(max_length=2000, null=True)
    shares_hold = models.CharField(max_length=2000, null=True)
    face_value = models.CharField(max_length=2000, null=True)
    divident_received = models.CharField(max_length=2000, null=True)
    request_for_exit = models.CharField(max_length=2000, null=True)
    condition =models.TextField()
    commitment =models.TextField()
    status = models.CharField(max_length=2000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

class InvestmentPreference(models.Model):
    investor = models.ForeignKey(AngelInvester,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=2000, null=True)
    investment_amount = models.CharField(max_length=2000, null=True)
    shares_hold = models.CharField(max_length=2000, null=True)
    face_value = models.CharField(max_length=2000, null=True)
    divident_received = models.CharField(max_length=2000, null=True)
    request_for_exit = models.CharField(max_length=2000, null=True)
    condition =models.TextField()
    commitment =models.TextField()
    convertable_nonconvertable = models.CharField(max_length=2000, null=True)
    status = models.CharField(max_length=2000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

# class Startups(models.Model):
#     verified_ipos = models.CharField(max_length=2000)
#     startup = models.CharField(max_length=2000, null=True)
#     coming = models.CharField(max_length=2000, null=True)

class Trade(models.Model):
    investor = models.ForeignKey(AngelInvester,on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE, null=True)
    shares = models.CharField(max_length=2000, null=True)
    amount = models.CharField(max_length=2000, null=True)
    trade_type = models.CharField(max_length=2000, null=True)
    status = models.CharField(max_length=2000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.trade_type

class SellPurchase(models.Model):
    company = models.CharField(max_length=2000, null=True)
    shares = models.CharField(max_length=2000, null=True)
    amount = models.CharField(max_length=2000, null=True)
    alot = models.CharField(max_length=2000, null=True)
    action_type = models.CharField(max_length=2000, null=True)
    status = models.CharField(max_length=2000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.created_by

class AgentDetails(models.Model):
    investor = models.ForeignKey(AngelInvester, on_delete=models.CASCADE)
    select_member = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    postal_code = models.CharField(max_length=200, null=True)
    Country = models.CharField( max_length=200, null=True)
    email = models.EmailField( max_length=200, null=True)
    website = models.CharField( max_length=200, null=True)
    primary_type_of_cap_prov = models.CharField(max_length=200, null=True)
    expected_return_per_year = models.CharField(max_length=200, null=True)
    minimum_valuation_of_interest = models.CharField(max_length=200, null=True)
    maximum_valuation_of_interest = models.CharField(max_length=200, null=True)
    bussiness_reviewed_last_12month = models.CharField(max_length=200, null=True)
    investment_last_12month = models.CharField(max_length=200, null=True)
    total_invested_last_12month = models.CharField(max_length=200, null=True)
    linkedin = models.URLField(max_length=200, null=True)
    facebook = models.URLField(max_length=200, null=True)
    twitter = models.URLField(max_length=200, null=True)
    blog = models.URLField(max_length=200, null=True)
    title = models.CharField(max_length=200, null=True)
    general_description = models.TextField(max_length=2000, null=True)
    company_web = models.CharField(max_length=200, null=True)
    company_name = models.CharField(max_length=200, null=True)
    select_role = models.CharField(max_length=200, null=True)
    investment_amount = models.CharField(max_length=200, null=True)
    investment_round = models.CharField(max_length=200, null=True)
    investment_type = models.CharField(max_length=200, null=True)
    investment_date = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    subject = models.CharField(max_length=2000)
    message = models.TextField()
    created_by = models.ForeignKey(AngelInvester, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_by = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class News(models.Model):
    title = models.TextField()
    subject = models.TextField()
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    paragraph3 = models.TextField()
    paragraph4 = models.TextField()
    paragraph5 = models.TextField()
    created_by = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Reviews(models.Model):
    name = models.CharField(max_length=200)
    reviews = models.TextField()
    start = models.CharField(max_length=10, null=True)
    created_for = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class BoaedMembers(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    valid = models.CharField(max_length=10, null=True)
    created_for = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name+ ':' + self.designation
