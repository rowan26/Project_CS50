import streamlit as st

def print_menu():
    options = [
        "Minutes to TV show episodes 🍿",
        "Kilograms to cats 🐈",
        "Meters to football fields 🏟️",
        "Liters to soda cans 🥤"
    ]
    choice = st.selectbox("Choose your conversion", options, key="conversion_select")
    return choice

def get_input():
    value = st.number_input("Enter the value to convert:", min_value=0, step=1, format="%d", key="value_input")
    return int(value)

def convert(choice, value):
    if choice == "Minutes to TV show episodes 🍿":
        return value / 45
    elif choice == "Kilograms to cats 🐈":
        return value / 4
    elif choice == "Meters to football fields 🏟️":
        return value / 100
    elif choice == "Liters to soda cans 🥤":
        return value / 0.33
    else:
        raise ValueError("Invalid conversion choice.")


def print_result(choice, value, result):
    if choice == "Minutes to TV show episodes 🍿":
        st.success(f"{value} minutes = {result:.2f} TV episodes 🍿")
    elif choice == "Kilograms to cats 🐈":
        st.success(f"{value} kilograms = {result:.2f} cats 🐱")
    elif choice == "Meters to football fields 🏟️":
        st.success(f"{value} meters = {result:.2f} football fields 🏟️")
    elif choice == "Liters to soda cans 🥤":
        st.success(f"{value} liters = {result:.2f} soda cans 🥤")
    else:
        st.error("Unknown conversion.")

def main():
    st.title("Comic Converter 🤪")

    choice = print_menu()
    value = get_input()

    if st.button("Convert", key="convert_btn"):
        result = convert(choice, value)
        print_result(choice, value, result)

        if st.button("Convert again", key="replay_btn"):
            st.experimental_rerun() 


if __name__ == "__main__":
    main()
