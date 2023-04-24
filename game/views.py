from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm
# Create your views here.
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee.html', {'form': form})