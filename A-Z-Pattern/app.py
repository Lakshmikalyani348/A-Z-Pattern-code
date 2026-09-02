
import streamlit as st

st.set_page_config(
    page_title="A-Z Pattern Generator",
    page_icon="🔤",
    layout="centered"
)

st.title("🔤 A-Z Pattern Generator")
st.write("Enter your name and generate its alphabet pattern.")

word = st.text_input("Enter your name").upper()

if word:

    output = []

    for i in range(5):

        row = ""

        for ch in word:

            if ch == "A":
                for j in range(5):
                    if (
                        (i == 0 and j in [1, 2, 3])
                        or (i == 1 and j in [0, 4])
                        or i == 2
                        or (i in [3, 4] and j in [0, 4])
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "B":
                for j in range(5):
                    if (
                        j == 0
                        or (i in [0, 2, 4] and j < 4)
                        or (j == 4 and i in [1, 3])
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "C":
                for j in range(5):
                    if (
                        (i in [0, 4] and j > 0)
                        or (j == 0 and i in [1, 2, 3])
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "D":
                for j in range(5):
                    if (
                        j == 0
                        or (i in [0, 4] and j < 4)
                        or (j == 4 and i in [1, 2, 3])
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "E":
                for j in range(5):
                    if j == 0 or i in [0, 2, 4]:
                        row += "* "
                    else:
                        row += "  "

            elif ch == "F":
                for j in range(5):
                    if j == 0 or i in [0, 2]:
                        row += "* "
                    else:
                        row += "  "

            elif ch == "G":
                for j in range(5):
                    if (
                        (i == 0 and j > 0)
                        or (i == 4 and j > 0)
                        or (j == 0 and i in [1, 2, 3])
                        or (i == 2 and j >= 2)
                        or (i == 3 and j == 4)
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "H":
                for j in range(5):
                    if j == 0 or j == 4 or i == 2:
                        row += "* "
                    else:
                        row += "  "

            elif ch == "I":
                for j in range(5):
                    if i == 0 or i == 4 or j == 2:
                        row += "* "
                    else:
                        row += "  "

            elif ch == "J":
                for j in range(5):
                    if (
                        i == 0
                        or j == 2
                        or (i == 4 and j < 3)
                        or (i == 3 and j == 0)
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "K":
                for j in range(5):
                    if (
                        j == 0
                        or (i == 0 and j == 4)
                        or (i == 1 and j == 3)
                        or (i == 2 and j == 2)
                        or (i == 3 and j == 3)
                        or (i == 4 and j == 4)
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "L":
                for j in range(5):
                    if j == 0 or i == 4:
                        row += "* "
                    else:
                        row += "  "

            elif ch == "M":
                for j in range(5):
                    if (
                        j == 0
                        or j == 4
                        or (i == 1 and j in [1, 3])
                        or (i == 2 and j == 2)
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "N":
                for j in range(5):
                    if j == 0 or j == 4 or i == j:
                        row += "* "
                    else:
                        row += "  "

            elif ch == "O":
                for j in range(5):
                    if (
                        (i in [0, 4] and j in [1, 2, 3])
                        or (j in [0, 4] and i in [1, 2, 3])
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "P":
                for j in range(5):
                    if (
                        j == 0
                        or (i == 0 and j < 4)
                        or (i == 2 and j < 4)
                        or (i == 1 and j == 4)
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "Q":
                for j in range(5):
                    if (
                        (i == 0 and j in [1, 2, 3])
                        or (i == 4 and j in [1, 2, 3])
                        or (j == 0 and i in [1, 2, 3])
                        or (j == 4 and i in [1, 2, 3])
                        or (i == 3 and j == 3)
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "R":
                for j in range(5):
                    if (
                        j == 0
                        or (i == 0 and j < 4)
                        or (i == 2 and j < 4)
                        or (i == 1 and j == 4)
                        or (i == 3 and j == 3)
                        or (i == 4 and j == 4)
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "S":
                for j in range(5):
                    if (
                        (i == 0 and j > 0)
                        or (i == 2 and j > 0 and j < 4)
                        or (i == 4 and j < 4)
                        or (i == 1 and j == 0)
                        or (i == 3 and j == 4)
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "T":
                for j in range(5):
                    if i == 0 or j == 2:
                        row += "* "
                    else:
                        row += "  "

            elif ch == "U":
                for j in range(5):
                    if (
                        (j == 0 and i < 4)
                        or (j == 4 and i < 4)
                        or (i == 4 and j in [1, 2, 3])
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "V":
                for j in range(5):
                    if (
                        (i == j and i < 3)
                        or (i + j == 4 and i < 3)
                        or (i == 4 and j == 2)
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "W":
                for j in range(5):
                    if (
                        j == 0
                        or j == 4
                        or (i == 3 and j in [1, 3])
                        or (i == 4 and j == 2)
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "X":
                for j in range(5):
                    if i == j or i + j == 4:
                        row += "* "
                    else:
                        row += "  "

            elif ch == "Y":
                for j in range(5):
                    if (
                        (i == 0 and j in [0, 4])
                        or (i == 1 and j in [1, 3])
                        or (j == 2 and i >= 2)
                    ):
                        row += "* "
                    else:
                        row += "  "

            elif ch == "Z":
                for j in range(5):
                    if i == 0 or i == 4 or i + j == 4:
                        row += "* "
                    else:
                        row += "  "

            else:
                for j in range(5):
                    row += "  "

            row += "   "

        output.append(row)

    st.subheader("✨ Your Pattern")

    st.code("\n".join(output), language="text")

