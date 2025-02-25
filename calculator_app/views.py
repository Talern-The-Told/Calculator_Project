from django.shortcuts import render

# Create your views here.
def calculator(request):
    result = None,
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            operator = request.POST.get('operator')

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
        except (ValueError, ZeroDivisionError):
            result = "Error"

    return render(request, 'calculator_app/calculator.html', {'result': result})