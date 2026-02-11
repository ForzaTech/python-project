import tkinter as tk
from tkinter import messagebox


# داده‌های سراسری برنامه

employees = []          # يست کارکنان
phonebook = []          # لیست دفترچه تلفن (name, phone)
edited = []             # ثبت نام و ويرايش هر آيتم
auth_pass = "admin123"  # قابل تغيير(محض اطلاع)
auth_success = False    # وضعیت ورود موفق


# ثبت‌نام جدید

def new_registration():
    # این تابع یک فرم باز می‌کند تا اطلاعات یک کارمند جدید ثبت شود
    def save():
        # دریافت مقدار از ورودی‌ها
        code = entry_code.get().strip()
        name = entry_name.get().strip()
        nid = entry_nid.get().strip()
        phone = entry_phone.get().strip()
        salary_text = entry_salary.get().strip()

        # اعتبار سنجي
        if code == "" or name == "" or nid == "" or phone == "" or salary_text == "":
            messagebox.showwarning("هشدار", "همه فیلدها باید پر شوند")
            return

        # تبدیل حقوق به عدد
        try:
            salary = int(salary_text)
        except:
            messagebox.showwarning("هشدار", "حقوق باید عدد صحیح باشد")
            return

        # جلوگیری از ثبت کد تکراری
        for e in employees:
            if e["code"] == code:
                messagebox.showerror("خطا", "کد پرسنلی تکراری است")
                return

        # افزودن کارمند جدید
        employees.append({"code": code, "name": name, "nid": nid, "phone": phone, "salary": salary})
        messagebox.showinfo("ثبت شد", "کارمند ذخیره شد")
        win.destroy()

    # ساخت پنجره فرم
    win = tk.Toplevel(root, bg="lightblue")
    win.geometry("320x300")
    win.title("ثبت نام جدید")

    tk.Label(win, text="کد پرسنلی", bg="lightblue").pack()
    entry_code = tk.Entry(win); entry_code.pack()

    tk.Label(win, text="نام و نام خانوادگی", bg="lightblue").pack()
    entry_name = tk.Entry(win); entry_name.pack()

    tk.Label(win, text="کد ملی", bg="lightblue").pack()
    entry_nid = tk.Entry(win); entry_nid.pack()

    tk.Label(win, text="تلفن", bg="lightblue").pack()
    entry_phone = tk.Entry(win); entry_phone.pack()

    tk.Label(win, text="حقوق پایه", bg="lightblue").pack()
    entry_salary = tk.Entry(win); entry_salary.pack()

    tk.Button(win, text="ذخیره", bg="green", fg="white", command=save).pack(pady=8)


# ویرایش ثبت‌نام (دو مرحله‌ای)

def edit_registration():
    # مرحله اول: فقط کد پرسنلی را می‌گیرد و سپس فرم ویرایش را با اطلاعات پر می‌کند
    def load_for_edit():
        code = entry_search_code.get().strip()
        if code == "":
            messagebox.showwarning("هشدار", "کد پرسنلی را وارد کنید")
            return

        # جستجوی کارمند
        for emp in employees:
            if emp["code"] == code:
                open_edit_form(emp)
                top.destroy()
                return

        messagebox.showerror("خطا", "کارمند با این کد پیدا نشد")

    top = tk.Toplevel(root, bg="lightyellow")
    top.geometry("320x140")
    top.title("ویرایش - وارد کردن کد")

    tk.Label(top, text="کد پرسنلی برای ویرایش", bg="lightyellow").pack(pady=(8, 4))
    entry_search_code = tk.Entry(top); entry_search_code.pack()
    tk.Button(top, text="Load", bg="blue", fg="white", command=load_for_edit).pack(pady=8)

def open_edit_form(emp):
    # مرحله دوم: فرم ویرایش با اطلاعات کارمند باز می‌شود
    def save_edit():
        # خواندن مقادیر جدید
        new_name = entry_name.get().strip()
        new_nid = entry_nid.get().strip()
        new_phone = entry_phone.get().strip()
        salary_text = entry_salary.get().strip()

        # اعتبارسنجی
        if new_name == "" or new_nid == "" or new_phone == "" or salary_text == "":
            messagebox.showwarning("هشدار", "همه فیلدها باید پر شوند")
            return
        try:
            new_salary = int(salary_text)
        except:
            messagebox.showwarning("هشدار", "حقوق باید عدد باشد")
            return

        # ذخیره حالت قبل از ویرایش
        before = {"code": emp["code"], "name": emp["name"], "nid": emp["nid"], "phone": emp["phone"], "salary": emp["salary"]}

        # اعمال تغییرات
        emp["name"] = new_name
        emp["nid"] = new_nid
        emp["phone"] = new_phone
        emp["salary"] = new_salary

        # ذخیره حالت بعد از ویرایش
        after = {"code": emp["code"], "name": emp["name"], "nid": emp["nid"], "phone": emp["phone"], "salary": emp["salary"]}

        # ثبت در لیست ویرایش‌ها
        edited.append({"code": emp["code"], "before": before, "after": after})

        messagebox.showinfo("بروزرسانی", "ویرایش انجام شد و در لیست ویرایش‌ها ثبت شد")
        win.destroy()
        show_edited_list()

    win = tk.Toplevel(root, bg="lightblue")
    win.geometry("320x300")
    win.title("فرم ویرایش - کد: " + emp["code"])

    tk.Label(win, text="کد پرسنلی", bg="lightblue").pack()
    tk.Label(win, text=emp["code"], bg="lightblue").pack()

    tk.Label(win, text="نام و نام خانوادگی", bg="lightblue").pack()
    entry_name = tk.Entry(win); entry_name.insert(0, emp["name"]); entry_name.pack()

    tk.Label(win, text="کد ملی", bg="lightblue").pack()
    entry_nid = tk.Entry(win); entry_nid.insert(0, emp["nid"]); entry_nid.pack()

    tk.Label(win, text="تلفن", bg="lightblue").pack()
    entry_phone = tk.Entry(win); entry_phone.insert(0, emp["phone"]); entry_phone.pack()

    tk.Label(win, text="حقوق پایه", bg="lightblue").pack()
    entry_salary = tk.Entry(win); entry_salary.insert(0, str(emp["salary"])); entry_salary.pack()

    tk.Button(win, text="ثبت تغییرات", bg="green", fg="white", command=save_edit).pack(pady=8)


# نمایش لیست ویرایش‌ها

def show_edited_list():
    # این پنجره همه ویرایش‌های ثبت‌شده را با قبل/بعد نشان می‌دهد
    win = tk.Toplevel(root, bg="white")
    win.geometry("500x380")
    win.title("لیست ویرایش‌ها")

    if len(edited) == 0:
        tk.Label(win, text="هیچ ویرایشی ثبت نشده است.", bg="white", fg="red").pack(pady=20)
        return

    txt = tk.Text(win, wrap="word")
    txt.pack(fill="both", expand=True, padx=8, pady=8)

    for idx in range(len(edited)):
        item = edited[idx]
        before = item["before"]
        after = item["after"]

        txt.insert("end", "ویرایش شماره: " + str(idx + 1) + "\n")
        txt.insert("end", "کد پرسنلی: " + item["code"] + "\n")
        txt.insert("end", "قبل: " + "نام=" + before["name"] + " | کدملی=" + before["nid"] + " | تلفن=" + before["phone"] + " | حقوق=" + str(before["salary"]) + "\n")
        txt.insert("end", "بعد: " + "نام=" + after["name"] + " | کدملی=" + after["nid"] + " | تلفن=" + after["phone"] + " | حقوق=" + str(after["salary"]) + "\n")
        txt.insert("end", "-----------------------------\n")

    txt.configure(state="disabled")


# نمایش لیست کارکنان

def show_employees():
    # این پنجره لیست کارکنان فعلی را نمایش می‌دهد
    win = tk.Toplevel(root, bg="white")
    win.geometry("420x320")
    win.title("لیست کارکنان")

    if len(employees) == 0:
        tk.Label(win, text="هیچ کارمندی ثبت نشده!", bg="white", fg="red").pack(pady=20)
        return

    txt = tk.Text(win, wrap="none")
    txt.pack(fill="both", expand=True, padx=8, pady=8)

    for emp in employees:
        line = "کد: " + emp["code"] + " | نام: " + emp["name"] + " | کدملی: " + emp["nid"] + " | تلفن: " + emp["phone"] + " | حقوق: " + str(emp["salary"]) + "\n"
        txt.insert("end", line)

    txt.configure(state="disabled")


# نمایش حقوق اولیه با کد

def show_initial_salary():
    # با گرفتن کد پرسنلی، حقوق اولیه همان فرد را نمایش می‌دهد
    def find():
        code = entry_code.get().strip()
        for emp in employees:
            if emp["code"] == code:
                messagebox.showinfo("حقوق اولیه", "کد: " + emp["code"] + "\nنام: " + emp["name"] + "\nحقوق اولیه: " + str(emp["salary"]))
                win.destroy()
                return
        messagebox.showerror("خطا", "کارمند با این کد پیدا نشد")

    win = tk.Toplevel(root, bg="lightgray")
    win.geometry("300x150")
    win.title("نمایش حقوق اولیه")

    tk.Label(win, text="کد پرسنلی", bg="lightgray").pack()
    entry_code = tk.Entry(win); entry_code.pack()
    tk.Button(win, text="نمایش حقوق", bg="black", fg="white", command=find).pack(pady=8)


# محاسبه حقوق

def payroll():
    # این پنجره ورودی‌های لازم را می‌گیرد و همه جزئیات محاسبه را نشان می‌دهد
    def calc():
        code = entry_code.get().strip()
        # تلاش برای تبدیل ورودی‌ها به عدد
        try:
            children = int(entry_children.get().strip())
            ot = int(entry_ot.get().strip())
            dec = int(entry_dec.get().strip())
        except:
            messagebox.showwarning("هشدار", "اعداد معتبر وارد کنید")
            return

        # جستجوی کارمند
        for emp in employees:
            if emp["code"] == code:
                base = emp["salary"]            # حقوق پایه
                hourly = base / 186.0           # مبلغ ساعتی = حقوق پایه / 186
                overtime = ot * 1.4 * hourly    # اضافه‌کاری = ساعت * 1.4 * مبلغ ساعتی
                deduction = dec * hourly        # کسرکار = ساعت * مبلغ ساعتی
                housing = base * 0.18           # حق مسکن 18%
                family = base * 0.12            # حق خواهر/برادر 12%
                child_bonus = children * 128560 # حق فرزند = n * 128560
                total = base + overtime - deduction + housing + family + child_bonus

                # ساخت جزييات متن
                details = (
                    "کد پرسنلی: " + emp["code"] + "\n" +
                    "نام: " + emp["name"] + "\n\n" +
                    "حقوق پایه: " + str(base) + "\n" +
                    "مبلغ ساعتی = حقوق پایه ÷ 186 = " + str(round(hourly, 2)) + "\n" +
                    "اضافه‌کاری = " + str(ot) + " × 1.4 × " + str(round(hourly, 2)) + " = " + str(round(overtime, 2)) + "\n" +
                    "کسرکار = " + str(dec) + " × " + str(round(hourly, 2)) + " = " + str(round(deduction, 2)) + "\n" +
                    "حق مسکن (18٪) = " + str(round(housing, 2)) + "\n" +
                    "حق خواهر/برادر (12٪) = " + str(round(family, 2)) + "\n" +
                    "حق فرزند = " + str(children) + " × 128560 = " + str(child_bonus) + "\n\n" +
                    "حقوق کل = " + str(int(total))
                )
                messagebox.showinfo("جزئیات حقوق", details)
                return

        messagebox.showerror("خطا", "کارمند پیدا نشد")

    win = tk.Toplevel(root, bg="lightyellow")
    win.geometry("360x300")
    win.title("محاسبه حقوق")

    tk.Label(win, text="کد پرسنلی", bg="lightyellow").pack()
    entry_code = tk.Entry(win); entry_code.pack()

    tk.Label(win, text="تعداد فرزند", bg="lightyellow").pack()
    entry_children = tk.Entry(win); entry_children.pack()

    tk.Label(win, text="ساعت اضافه کاری", bg="lightyellow").pack()
    entry_ot = tk.Entry(win); entry_ot.pack()

    tk.Label(win, text="ساعت کسرکار", bg="lightyellow").pack()
    entry_dec = tk.Entry(win); entry_dec.pack()

    tk.Button(win, text="محاسبه و نمایش جزئیات", bg="blue", fg="white", command=calc).pack(pady=8)


# دفترچه تلفن با جستجو

def phonebook_form():
    # اضافه کردن مخاطب و سرچ
    def add_contact():
        name = entry_name.get().strip()
        phone = entry_phone.get().strip()
        if name == "" and phone == "":
            messagebox.showwarning("هشدار", "نام یا تلفن باید وارد شود")
            return
        phonebook.append({"name": name, "phone": phone})
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        refresh_listbox()

    def refresh_listbox(filter_q=None):
        listbox.delete(0, tk.END)
        for p in phonebook:
            line = p["name"] + " | " + p["phone"]
            if filter_q is None:
                listbox.insert(tk.END, line)
            else:
                q = filter_q.lower()
                if q in p["name"].lower() or q in p["phone"]:
                    listbox.insert(tk.END, line)

    def search():
        q = entry_search.get().strip()
        if q == "":
            refresh_listbox(None)
        else:
            refresh_listbox(q)

    win = tk.Toplevel(root, bg="pink")
    win.geometry("420x320")
    win.title("دفترچه تلفن")

    tk.Label(win, text="نام", bg="pink").pack()
    entry_name = tk.Entry(win); entry_name.pack()

    tk.Label(win, text="تلفن", bg="pink").pack()
    entry_phone = tk.Entry(win); entry_phone.pack()

    tk.Button(win, text="افزودن", bg="red", fg="white", command=add_contact).pack(pady=6)

    tk.Label(win, text="جستجو (نام یا شماره)", bg="pink").pack(pady=(8, 0))
    entry_search = tk.Entry(win); entry_search.pack()
    tk.Button(win, text="جستجو", bg="blue", fg="white", command=search).pack(pady=4)
    tk.Button(win, text="نمایش همه", command=lambda: refresh_listbox(None)).pack(pady=(0, 6))

    frame_list = tk.Frame(win); frame_list.pack(fill="both", expand=True, padx=8, pady=8)
    scrollbar = tk.Scrollbar(frame_list); scrollbar.pack(side="right", fill="y")
    listbox = tk.Listbox(frame_list, yscrollcommand=scrollbar.set)
    listbox.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=listbox.yview)

    refresh_listbox(None)


# احراز هويت

def auth():
    def check():
        global auth_success
        phone_input = entry_phone.get().strip()
        nid_input = entry_nid.get().strip()

        # اطمینان از حداقل طول برای برش
        if len(phone_input) < 2 or len(nid_input) < 2:
            messagebox.showwarning("هشدار", "لطفاً حداقل دو رقم از شماره تلفن و دو رقم از کد ملی را وارد کنید")
            return

        # گرفتن دو رقم آخر از ورودی تلفن و دو رقم اول از ورودی کد ملی
        phone_last_input = phone_input[-2:]
        nid_first_input = nid_input[:2]

        # جستجو در بین کارکنان برای تطابق
        for emp in employees:
            emp_phone_last = emp["phone"][-2:] if len(emp["phone"]) >= 2 else emp["phone"]
            emp_nid_first = emp["nid"][:2] if len(emp["nid"]) >= 2 else emp["nid"]

            if phone_last_input == emp_phone_last and nid_first_input == emp_nid_first:
                auth_success = True
                try:
                    btn_change_salary.config(state="normal")
                except:
                    pass
                messagebox.showinfo("موفق", "انجام شد")
                win.destroy()
                return

        messagebox.showerror("خطا", "احراز هویت ناموفق است")

    win = tk.Toplevel(root, bg="lightgray")
    win.geometry("340x180")
    win.title("احراز هویت")

    tk.Label(win, text="شماره تلفن (یا دو رقم آخر)", bg="lightgray").pack(pady=6)
    entry_phone = tk.Entry(win); entry_phone.pack()
    tk.Label(win, text="کد ملی (یا دو رقم اول)", bg="lightgray").pack(pady=6)
    entry_nid = tk.Entry(win); entry_nid.pack()
    tk.Button(win, text="تایید", bg="black", fg="white", command=check).pack(pady=8)


# تغییر حقوق پایه (با سقف 20میلیون)

def change_salary():
    # فقط پس از احراز موفق قابل استفاده است (از طریق دکمه فعال‌شده)
    def save():
        code = entry_code.get().strip()
        try:
            new_salary = int(entry_salary.get().strip())
        except:
            messagebox.showwarning("هشدار", "حقوق باید عدد باشد")
            return

        if new_salary > 20000000:
            messagebox.showerror("خطا", "حداکثر حقوق پایه 20 میلیون است")
            return

        for emp in employees:
            if emp["code"] == code:
                emp["salary"] = new_salary
                messagebox.showinfo("موفق", "حقوق پایه جدید ثبت شد")
                win.destroy()
                return

        messagebox.showerror("خطا", "کارمند پیدا نشد")

    win = tk.Toplevel(root, bg="lightgreen")
    win.geometry("300x180")
    win.title("تغییر حقوق پایه")

    tk.Label(win, text="کد پرسنلی", bg="lightgreen").pack()
    entry_code = tk.Entry(win); entry_code.pack()

    tk.Label(win, text="حقوق جدید", bg="lightgreen").pack()
    entry_salary = tk.Entry(win); entry_salary.pack()

    tk.Button(win, text="ثبت", bg="blue", fg="white", command=save).pack(pady=8)


# ماشین‌حساب ساده (دو عدد + عملگر)

def calculator():
    # ماشين حساب
    def do_calc():
        # تلاش برای تبدیل ورودی به عدد
        try:
            a = float(entry_a.get().strip())
            b = float(entry_b.get().strip())
        except:
            messagebox.showwarning("هشدار", "ورودی عددی معتبر وارد کنید")
            return

        op = entry_op.get().strip()
        result = None

        # محاسبه بر اساس عملگر
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                messagebox.showerror("خطا", "تقسیم بر صفر مجاز نیست")
                return
            result = a / b
        else:
            messagebox.showwarning("هشدار", "عملگر نامعتبر است (+ - * /)")
            return

        # نمایش نتیجه در ورودی خروجی
        entry_res.delete(0, tk.END)
        entry_res.insert(0, str(result))

        # ذخیره لاگ محاسبه در فایل
        try:
            f = open("calc_log.txt", "a")
            f.write(str(a) + " " + op + " " + str(b) + " = " + str(result) + "\n")
            f.close()
        except:
            pass  # اگر ذخیره نشد، برنامه قطع نشود

    win = tk.Toplevel(root, bg="lightgreen")
    win.geometry("320x240")
    win.title("ماشین حساب")

    tk.Label(win, text="عدد A", bg="lightgreen").pack()
    entry_a = tk.Entry(win); entry_a.pack()

    tk.Label(win, text="عدد B", bg="lightgreen").pack()
    entry_b = tk.Entry(win); entry_b.pack()

    tk.Label(win, text="عملگر (+ - * /)", bg="lightgreen").pack()
    entry_op = tk.Entry(win); entry_op.pack()

    tk.Button(win, text="محاسبه", bg="darkgreen", fg="white", command=do_calc).pack(pady=8)

    tk.Label(win, text="نتیجه", bg="lightgreen").pack()
    entry_res = tk.Entry(win); entry_res.pack()


# پنجره اصلی برنامه

root = tk.Tk()
root.title("Final Project")
root.geometry("420x700")     
root.configure(bg="#2e2e2e")   # مشکی/خاکستری روشن (black light)

# دکمه‌های اصلی
tk.Button(root, text="ثبت نام جدید",    width=30, bg="blue",   fg="white", command=new_registration).pack(pady=5)
tk.Button(root, text="ویرایش ثبت‌نام",  width=30, bg="purple", fg="white", command=edit_registration).pack(pady=5)
tk.Button(root, text="لیست کارکنان",    width=30, bg="brown",  fg="white", command=show_employees).pack(pady=5)
tk.Button(root, text="نمایش حقوق اولیه", width=30, bg="teal",   fg="white", command=show_initial_salary).pack(pady=5)
tk.Button(root, text="لیست ویرایش‌ها",  width=30, bg="gray",   fg="white", command=show_edited_list).pack(pady=5)
tk.Button(root, text="محاسبه حقوق",     width=30, bg="green",  fg="white", command=payroll).pack(pady=5)
tk.Button(root, text="دفترچه تلفن",     width=30, bg="orange", fg="black", command=phonebook_form).pack(pady=5)
tk.Button(root, text="ماشین حساب",      width=30, bg="darkgreen", fg="white", command=calculator).pack(pady=5)
tk.Button(root, text="احراز هویت",      width=30, bg="purple", fg="white", command=auth).pack(pady=5)

# دکمه تغییر حقوق پس از احراز فعال می‌شود
btn_change_salary = tk.Button(root, text="تغییر حقوق پایه", width=30, bg="yellow", fg="black", state="disabled", command=change_salary)
btn_change_salary.pack(pady=5)

tk.Button(root, text="خروج",            width=30, bg="red",    fg="white", command=root.destroy).pack(pady=5)

root.mainloop() #اجراي برنامه
