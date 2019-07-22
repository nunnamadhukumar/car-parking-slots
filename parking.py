#!/usr/bin/env python
car_main_data = []


def create_car_data(park_slot_no):
    dup_data = []
    for slot in range(1, (int(park_slot_no) + 1)):
        slot_data = raw_input("enter the car data:")
        slot_data1 = slot_data
        if slot_data1 in dup_data:
            print("Already enter the data")
            break;
        car_data = {}
        slot_data = slot_data.split()
        car_data['slot_no'] = slot
        car_data['Registraion_no'] = slot_data[1]
        car_data['colour'] = slot_data[2]
        car_main_data.append(car_data)
        dup_data.append(slot_data1)
        print(("Allocated slot number:" + str(slot)))
    return car_main_data


def leave_data(leave_position, df, slot_no):
    leave = leave_position.split()
    leave1 = int(leave[1]) - 1
    if (leave1 >= slot_no):
        print("Enter the leave data less than equal to slot no")
    else:
        df[leave1] = ''
        print(("Slot number" + leave[1] + " is free"))
        return df


def table(df, status):
    if status == "status":
        print("Slot No.\tRegistration No\tColour")
        for i in df:
            if i == '':
                print(("{}\t{}\t{}\t".format('', '', '')))
            else:
                print(("{}\t\t{}\t\t{}\t\t".format(i['slot_no'], i['Registraion_no'], i['colour'])))
    else:
        print("enter the correct word status")


def inserting(insert_data, df):
    car_data = {}
    insert_data = insert_data.split()
    if '' not in df:
        data = "Sorry, parking lot is full"
        return data

    else:
        for position in range(len(df)):
            if df[position] == '':
                car_data['slot_no'] = position + 1
                car_data['Registraion_no'] = insert_data[1]
                car_data['colour'] = insert_data[2]
                df[position] = car_data
                print("Allocated slot number:" + str(position + 1))
                return df


def reg_found(colour_query):
    if (colour_query == ''):
        print("Not Found")
    else:
        print(colour_query)


def reg_colour_data(df, reg_col):
    reg_col = reg_col.split()
    final_data = []
    if reg_col[0] == 'registration_numbers_for_cars_with_colour':
        k = list([df for df in df if df['colour'] == reg_col[1]])
        for j in k:
            final_data.append(j.get('Registraion_no'))
        final_data = (' , '.join(final_data))
        return final_data

    elif reg_col[0] == 'slot_numbers_for_cars_with_colour':
        k = list([df for df in df if df['colour'] == reg_col[1]])
        for j in k:
            final_data.append(j.get('slot_no'))
        final_data = ",".join(str(n) for n in final_data)
        return final_data

    else:
        if reg_col[0] == 'slot_number_for_registration_number':
            k = list([df for df in df if df['Registraion_no'] == reg_col[1]])
            for j in k:
                final_data.append(j.get('slot_no'))
            if final_data != '':
                final_data = ",".join(str(n) for n in final_data)
            return final_data


def main():
    park_slot_no = raw_input("create_parking_lot")
    print(("Created a parking lot with" + " " + str(park_slot_no) + " " + "slots"))
    df = create_car_data(park_slot_no)
    leave_position = raw_input("enter the leave position")
    df = leave_data(leave_position, df, int(park_slot_no))
    status = raw_input("enter the status")
    status_data = table(df, status)
    insert_data = raw_input("enter the car details")
    df = inserting(insert_data, df)
    insert_data = raw_input("enter the car details")
    df1 = df
    df = inserting(insert_data, df)
    print(df)
    df = df1
    reg_col = raw_input("registration_numbers_for_cars_with_colour")
    colour_query = reg_colour_data(df, reg_col)
    print(colour_query)
    reg_col = raw_input("slot_numbers_for_cars_with_colour with colour")
    colour_query = reg_colour_data(df, reg_col)
    print(str(colour_query))
    reg_col = raw_input("slot_number_for_registration_number")
    colour_query = reg_colour_data(df, reg_col)
    final_req = reg_found(colour_query)
    reg_col = raw_input("slot_number_for_registration_number")
    colour_query = reg_colour_data(df, reg_col)
    final_req = reg_found(colour_query)


if __name__ == '__main__':
    main()