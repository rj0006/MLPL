# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, FileResponse
from django.conf import settings
import os
from .models import Author, BookDetail, Consignment, InvoiceDetail, PartDetail

def inlinetable(request):
    if request.method == 'POST':
        # Process main form data
        author_name = request.POST.get('author_name')
        fname = request.POST.get('fname')
        age = request.POST.get('age')
        author = Author.objects.create(name=author_name, first_name=fname, age=age)
        print(author)
        
        # Process inline table data
        book_names = request.POST.getlist('book_name[]')
        publish_dates = request.POST.getlist('publish_date[]')
        prices = request.POST.getlist('price[]')
        for i in range(len(book_names)):
            BookDetail.objects.create(author=author, name=book_names[i], publish_date=publish_dates[i], price=prices[i])
            print(BookDetail)
        return redirect('/inlinetableform')
        # return JsonResponse({'success': True})
    return render(request, 'index.html')

def inlinelist(request):
    author = Author.objects.order_by('id')
    print(author)
    pdf_path = os.path.join(settings.BASE_DIR, 'inlinetableform', 'templates', 'logo.png')
    context = {
        'page' : 'Author List',
        'author' : author,
        'pdf_path' : pdf_path,
    }
    return render(request, 'list.html', context)

def update(request, authorid):
    updtAuthor = get_object_or_404(Author, id=authorid)
    updtBookdetails = BookDetail.objects.filter(author_id=authorid)
    if request.method == 'POST':
        data = request.POST
        updtAuthor.author_name = data.get('author_name')
        updtAuthor.fname = data.get('fname')
        updtAuthor.age = data.get('age')
        print(updtAuthor.age)
        updtAuthor.save()
         
        book_names = data.getlist('book_name[]')
        print(book_names)
        
        # Process inline table data
        for i, detail in enumerate(updtBookdetails):
            # Check if the form data contains information for this book detail
            if i < len(data.getlist('book_name[]')):
                detail.name = data.getlist('book_name[]')[i]
                detail.publish_date = data.getlist('publish_date[]')[i]
                detail.price = data.getlist('price[]')[i]
                detail.save()
            else:
                # If the index is out of range, delete the book detail
                detail.delete()
        # Add new book details
        new_book_names = data.getlist('new_book_name[]')
        print(new_book_names)
        new_publish_dates = data.getlist('new_publish_date[]')
        new_prices = data.getlist('new_price[]')
        for i in range(len(new_book_names)):
            BookDetail.objects.create(
                author=updtAuthor,
                name=new_book_names[i],
                publish_date=new_publish_dates[i],
                price=new_prices[i]
            )
        return JsonResponse({'success': True})
    context = {
        'page':'Update Author',
        'author':updtAuthor,
        'bookdetail': updtBookdetails,
    }
    return render(request, 'update.html', context)

def delete(request, authorid):
    author = get_object_or_404(Author, id=authorid)
    book_detail = BookDetail.objects.filter(author_id=authorid).first()
    author.delete()
    if book_detail:
        book_detail.delete()
    return redirect('/inlinetableform/inlinelist/')


def consignments(request):
    if request.method == 'POST':
        # Process main form data
        cn_no = request.POST.get('cn_no')
        cn_date = request.POST.get('cn_date')
        remark = request.POST.get('remark')
        consignment = Consignment.objects.create(cnno=cn_no, cndate=cn_date, remark=remark)
        print(Consignment)
        
        # Process inline table data
        in_no = request.POST.getlist('in_no[]')
        in_date = request.POST.getlist('in_date[]')
        in_value = request.POST.getlist('in_value[]')
        
        # partName = request.POST.getlist('part_name[]')
        
        for i in range(len(in_no)):
            invoice_detail = InvoiceDetail.objects.create(consignment=consignment, inno=in_no[i], indate=in_date[i], invalue=in_value[i])
            print(invoice_detail)
            
            # Get the list of part names for the current invoice
            part_names = request.POST.getlist('part_name[]')  # Assuming your part name lists are named as part_name_1[], part_name_2[], etc.
            
            # Iterate over the part names for the current invoice
            for part_name in part_names:
                PartDetail.objects.create(invoice_detail=invoice_detail, part_name=part_name)
                print(part_name)

        return redirect('/inlinetableform/consignments')
        # return JsonResponse({'success': True})
    return render(request, 'consignments.html')