from django.shortcuts import render

def index(request):
    generated_output = ""
    train_input = ""
    if request.method == 'POST':
        train_input = request.POST.get('train_input', '')
        generated_output = train_input

    return render(request, 'difm_app/index.html', {
        'train_input': train_input,
        'generated_output': generated_output
    })
