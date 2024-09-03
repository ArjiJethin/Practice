def seperator(file_name,sep_agent):
    try:
        with open(file_name, "r") as f:
            content = f.read()
            formatted_content = sep_agent.join(content)
            print(formatted_content)

    except FileNotFoundError:
        print("File not found :(")


file = "../Text.txt"
symbol = '*'
seperator(file, symbol)
