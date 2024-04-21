import streamlit as st

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def main():
    st.title("Find the Largest Number")

    num1 = st.number_input("Enter the first number:", value=0)
    num2 = st.number_input("Enter the second number:", value=0)
    num3 = st.number_input("Enter the third number:", value=0)

    if st.button("Find Largest"):
        largest_num = find_largest(num1, num2, num3)
        st.write(f"The largest number among {num1}, {num2}, and {num3} is: {largest_num}")

if __name__ == "__main__":
    main()
