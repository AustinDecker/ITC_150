def analyze_file(file_name):
    metrics = {"upper_case": 0, "lower_case": 0, "numeric": 0, "white_space": 0, "characters": 0, "word_count": 0}
    try:

        with open(file_name, "r") as file:
            for line in file:
                word_count = len(line.split());
                characters = len(line);

                metrics["characters"] = metrics["characters"] + characters;
                metrics["word_count"] = metrics["word_count"] + word_count;

                for char in line:
                    if char.isalpha() and char.isupper():
                        metrics["upper_case"] = metrics["upper_case"] + 1;
                    elif char.isalpha() and char.islower():
                        metrics["lower_case"] = metrics["lower_case"] + 1;
                    elif char.isdigit():
                        metrics["numeric"] = metrics["numeric"] + 1;
                    elif char.isspace():
                        metrics["white_space"] = metrics["white_space"] + 1;

            
    except FileNotFoundError:
        print(f'file {file_name} could not be found.');
    except OSError:
        print(f'could not access {file_name} for some reason.');
    
    return metrics;

def main():
    file_name = "./test.txt"
    metrics = analyze_file(file_name);
    print(metrics);


if __name__ == "__main__":
    main();