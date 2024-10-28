def add_record(records):
    while True:
        department = input("請輸入部門: ")
        name = input("請輸入姓名: ")
        age = input("請輸入年齡: ")
        phone = input("請輸入手機號碼: ")
        record = {
            "department": department,
            "name": name,
            "age": age,
            "phone": phone
        }
        records.append(record)
        print("資料已新增！")
        cont = input("是否繼續新增資料? (y/n): ")
        if cont.lower() != 'y':
            break


def query_record(records):
    name = input("請輸入要查詢的姓名: ")
    found = False
    print("\n--- 查詢結果 ---")
    print("{:<10} {:<10} {:<10} {:<15}".format("部門", "姓名", "年齡", "手機"))
    print("----------------------------------------")
    for record in records:
        if record["name"] == name:
            print_record(record)
            found = True
    if not found:
        print("查無此人")


def update_record(records):
    name = input("請輸入要修改的姓名: ")
    for record in records:
        if record["name"] == name:
            print("\n當前資料:")
            print("{:<10} {:<10} {:<10} {:<15}".format("部門", "姓名", "年齡", "手機"))
            print("----------------------------------------")
            print_record(record)
            while True:
                print("\n請選擇要修改的欄位:")
                print("1. 修改部門")
                print("2. 修改姓名")
                print("3. 修改年齡")
                print("4. 修改手機")
                print("5. 完成修改")
                field_choice = input("請輸入選項 (1-5): ")
                if field_choice == '1':
                    record["department"] = input("請輸入新的部門: ")
                elif field_choice == '2':
                    record["name"] = input("請輸入新的姓名: ")
                elif field_choice == '3':
                    record["age"] = input("請輸入新的年齡: ")
                elif field_choice == '4':
                    record["phone"] = input("請輸入新的手機號碼: ")
                elif field_choice == '5':
                    print("資料已更新！")
                    print("\n更新後資料:")
                    print("{:<10} {:<10} {:<10} {:<15}".format("部門", "姓名", "年齡", "手機"))
                    print("----------------------------------------")
                    print_record(record)
                    break
                else:
                    print("無效的選項，請重新選擇")
            return
    print("查無此人")


def delete_record(records):
    name = input("請輸入要刪除的姓名: ")
    for i, record in enumerate(records):
        if record["name"] == name:
            print("\n找到以下資料:")
            print("{:<10} {:<10} {:<10} {:<15}".format("部門", "姓名", "年齡", "手機"))
            print("----------------------------------------")
            print_record(record)
            confirm = input("是否確定刪除？(y/n): ")
            if confirm.lower() == 'y':
                records.pop(i)
                print("資料已刪除！")
            else:
                print("取消刪除")
            display_all_records(records)
            return
    print("查無此人")


def display_all_records(records):
    if not records:
        print("目前沒有任何資料")
    else:
        print("{:<10} {:<10} {:<10} {:<15}".format("部門", "姓名", "年齡", "手機"))
        print("----------------------------------------")
        for record in records:
            print("{:<10} {:<10} {:<10} {:<15}".format(
                record["department"], record["name"], record["age"], record["phone"]
            ))


def print_record(record):
    print("{:<10} {:<10} {:<10} {:<15}".format(
        record["department"], record["name"], record["age"], record["phone"]
    ))



if __name__ == "__main__":
    records = []
    while True:
        print("\n--- 人事資料管理系統 ---")
        print("1. 新增資料")
        print("2. 查詢資料")
        print("3. 修改資料")
        print("4. 刪除資料")
        print("5. 顯示所有資料")
        print("6. 退出系統")
        print("------------------------")

        choice = input("請選擇功能: ")

        if choice == '1':
            add_record(records)
        elif choice == '2':
            query_record(records)
        elif choice == '3':
            update_record(records)
        elif choice == '4':
            delete_record(records)
        elif choice == '5':
            display_all_records(records)
        elif choice == '6':
            print("系統已退出")
            break
        else:
            print("無效的選項，請重新選擇")