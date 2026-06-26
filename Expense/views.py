from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from .forms import ExpenseForm , UserForm ,LoginForm
from .models import Category,Expense,User
# Create your views here.
def get_current_user(request):

    if "user_id" in request.session:
        try:
            return User.objects.get(
                id=request.session["user_id"]
            )
        except User.DoesNotExist:
            return None
    return None
def home(request):
    if "user_id" not in request.session:
     return redirect("login")
    current_user = get_current_user(request)
    if request.method == "POST":

        form = ExpenseForm(request.POST)

        if form.is_valid():

            expense = form.save(commit=False)

            expense.user = current_user

            expense.save()

            return redirect("expense")

    else:

        form = ExpenseForm()

    return render(request,"Expense/home.html",{
        "expense": form,
        "current_user": current_user}
        )
    
def expense(request):
    if "user_id" not in request.session:
     return redirect("login")

    current_user = get_current_user(request)

    expenses = Expense.objects.filter(
        user=current_user
    ).order_by("date")

    return render(
        request,
        "Expense/expense.html",
        {
            "expense": expenses,
            "current_user": current_user
        }
    )   
from django.shortcuts import redirect

def delete_expense(request, id):
    current_user = get_current_user(request)
    expense = Expense.objects.get(
        id=id,
        user=current_user
    )
    expense.delete()
    return redirect("expense")
def edit_expense(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == "POST":
        form = ExpenseForm(
            request.POST,
            instance=expense
        )
        if form.is_valid():
            form.save()
            return redirect("expense")
    else:
        form = ExpenseForm(instance=expense)
    return render(
        request,
        "Expense/edit.html",
        {
            "expense": form
        }
    )
from django.shortcuts import render
from django.db.models import Sum, Max, Avg
from .models import Expense, Category
def report(request):

    if "user_id" not in request.session:
        return redirect("login")

    current_user = User.objects.get(
        id=request.session["user_id"]
    )

    user_expenses = Expense.objects.filter(
        user=current_user
    )

    total = user_expenses.aggregate(
        total=Sum("amount")
    )

    highest = user_expenses.aggregate(
        highest=Max("amount")
    )

    average = user_expenses.aggregate(
        average=Avg("amount")
    )

    total_expenses = user_expenses.count()

    total_categories = Category.objects.count()

    return render(
        request,
        "Expense/report.html",
        {
            "current_user": current_user,

            "total": total["total"] or 0,

            "highest": highest["highest"] or 0,

            "average": average["average"] or 0,

            "total_expenses": total_expenses,

            "total_categories": total_categories,
        }
    )

def register_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            confirm = form.cleaned_data["confirm_password"]
            # username already exists
            if User.objects.filter(username=username).exists():
                form.add_error(
                    "username",
                    "Username already exists"
                )
            # password mismatch
            elif password != confirm:
                form.add_error(
                    "confirm_password",
                    "Passwords do not match"
                )
            else:
                form.save()
                return redirect("home")
    else:
        form = UserForm()
    return render(
        request,
        "Expense/register.html",
        {
            "user": form
        }
    )

def login_user(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                user = User.objects.get(
                    username=username
                )
                if user.password == password:
                    request.session["user_id"] = user.id

                    return redirect("home")
                else:

                    form.add_error(
                        "password",
                        "Invalid Password"
                    )
            except User.DoesNotExist:
                form.add_error(
                    "username",
                    "User does not exist"
                )
    else:
        form = LoginForm()
    return render(
        request,
        "Expense/login.html",
        {
            "form": form
        }
    )
def logout_user(request):
    request.session.flush()
    return redirect("login")