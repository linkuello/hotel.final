import shutil
import os
from datetime import date, timedelta
from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request, "index.html")

def Room(request):
    if request.method == "POST":
        dt = list_days(request.POST.get("check_in"), request.POST.get("check_out"))
        available_rooms = []
        rooms_path = os.path.join("rooms")  # Указываем путь к папке с комнатами
        for room in os.listdir(rooms_path):
            room_path = os.path.join(rooms_path, room)
            status = open(os.path.join(room_path, "status.txt"), "r").read()
            if status == "clear":
                available_rooms.append(room)
            else:
                dates = open(os.path.join(room_path, "date.txt"), "r").read().split("\n")
                if all(date not in dates for date in dt):
                    available_rooms.append(room)
        return render(request, "rooms.html", {"r": available_rooms, "message": "none", "in_d": request.POST.get("check_in"), "out_d": request.POST.get("check_out")})
    else:
        return HttpResponse("<a href='/'><button>back</button></a>")

def Book(request, room, in_d, out_d, details):
    room_path = os.path.join("rooms", room)
    tr = "\n".join(list_days(in_d, out_d))
    with open(os.path.join(room_path, "date.txt"), "a") as file:
        file.write(tr + "\n")
    open(os.path.join(room_path, "status.txt"), "w").write("booked")
    open(os.path.join(room_path, "detail.txt"), "a").write(f"{details} {in_d},{out_d}\n")
    return HttpResponse("Booked")

def list_days(start_date, end_date):
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    delta = (end - start).days + 1  # Включаем конечную дату
    return [str(start + timedelta(days=i)) for i in range(delta)]

def list_booked(request):
    booked_rooms = []
    rooms_path = os.path.join("rooms")
    for room in os.listdir(rooms_path):
        room_path = os.path.join(rooms_path, room)
        status = open(os.path.join(room_path, "status.txt"), "r").read()
        if status == "booked":
            dates = open(os.path.join(room_path, "date.txt"), "r").read().replace("\n", "<br>")
            booked_rooms.append({"number": room, "dates": dates})
    return render(request, "pr.html", {"room": booked_rooms})

def deBook(request, room):
    room_path = os.path.join("rooms", room)
    shutil.rmtree(room_path)
    os.makedirs(room_path)
    open(os.path.join(room_path, "status.txt"), "a").write("clear")
    open(os.path.join(room_path, "detail.txt"), "a").write("")
    open(os.path.join(room_path, "date.txt"), "a").write("")
    return HttpResponse("Debooked")

def index(request):
    return render(request, 'index.html')
