#Calculator with History

history_file = "calc_history.txt"

def show_history():
    with open(history_file, "r") as f:
        history = f.readlines()
        if len(history) == 0:
            print("No history available.")
        else:
            print("Calculation History:")
            for entry in history:
                print(entry.strip())
        

