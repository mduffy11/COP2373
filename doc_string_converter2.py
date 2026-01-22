import inspect
import Duffy_ProgrammingExercise_1

with open("Duffy_ProgrammingExercise_1_design_doc.txt", "w") as doc:

        doc.write(f"# Technical Design Document: {Duffy_ProgrammingExercise_1.__name__}\n\n")

    doc.write("# Name: Duffy, Michael\n")
    doc.write("# Date: January 22, 2026\n")
    doc.write("# Program Description: An application to pre-sell a limited number of cinema tickets.\n\n")

    for name, func in inspect.getmembers(Duffy_ProgrammingExercise_1, inspect.isfunction):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")

    doc.write("# Link to your repository: https://github.com/mduffy11/COP2373/\n")

print("Complete")
