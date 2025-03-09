import os
import sys
import importlib
import typer
from rich import print
from InquirerPy import inquirer
from spice.analyze import analyze_file


# initialize typer
app = typer.Typer()

# add the current directory (cli) to the sys.path
sys.path.append('cli')

# get current directory, this is needed for it to work on other peoples computers via pip
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# select a file to save the current selected langague (if saved to memory it wont persist between commands)
LANG_FILE = os.path.join(CURRENT_DIR, "lang.txt")

# this will load the translations
def get_translation():
    
    # read the lang file to see what langague was set by user
    if os.path.exists(LANG_FILE):

        # open the lang file
        with open(LANG_FILE, "r") as file:
                
                # read the lang file
                lang = file.read().strip()

              
                if not lang:
                    lang = 'en' # if file is empty, default to english
        
    else:
        lang = 'en'  # default to English if there is not file but there will always be a file this is just in case ALSO THIS IS SO @icrcode DOESNT COMPLAIN ABOUT MY CODE NOT BEING CLEAN AND WHATEVER

    # this is actually import the translations
    try:
        return importlib.import_module(f"cli.translations.{lang}").messages
    except ModuleNotFoundError:
        return importlib.import_module("cli.translations.en").messages  # default to English if any errors

    


# SPICE SET_LANG COMMAND
@app.command()
def translate():
    """
    Set the language for CLI messages.
    """

    # LIST OF ALL AVAILIBLE LANGAUGES ADD NEW TRANSLATIONS HERE PLEASE !!!!!!!!!!!!!!!!!!!!!!!!
    LANGUAGES = {
    "en": {"name": "English"},
    "pt-br": {"name": "Portuguese"},
    "fremen": {"name": "Fremen"},
    # Add more languages as needed
    }

    # this just makes the list above actually work (i wanted to add emojis but flag emojies dont work on pc 😭)
    choices = [
        f"{info['name']} ({lang})" for lang, info in LANGUAGES.items()
    ]

    # intereacitive menu
    selected_choice = inquirer.select(
        message="Choose a language:",
        choices=choices,
        pointer="> ",
        default="English"
    ).execute()

    # will read the dicionary to see what langauggue is which does that make sense? its like the reverse of before
    selected_lang = next(
        lang for lang, info in LANGUAGES.items() if f"{info['name']} ({lang})" == selected_choice
    )

    # will write the new language to the langague file (to save it to HD instead of memory) (so its persistant between commands)
    with open(LANG_FILE, "w") as file:
        file.write(selected_lang)

    print(f"[green]Language set to:[/] {selected_lang}")



# SPICE HELLO COMMAND
@app.command()
def hello():
    """
    Welcome message.
    """

    # load translations
    messages = get_translation()

    # print the hello message
    print(messages["welcome"])
    print(messages["description"])


# SPICE ANALYZE COMMAND
@app.command()
def analyze(file: str):
    """
    Analyze the given file.
    """
    
    # load translations
    messages = get_translation()

    # Define available stats
    available_stats = [
        "line_count",
        "function_count", 
        "comment_line_count"
    ]

    # Create human-readable labels for the stats
    stats_labels = {
        "line_count": messages.get("line_count_option", "Line Count"),
        "function_count": messages.get("function_count_option", "Function Count"),
        "comment_line_count": messages.get("comment_line_count_option", "Comment Line Count")
    }
    
    # Present a checkbox menu to select which stats to show
    selected_stats = inquirer.checkbox(
        message=messages.get("select_stats", "Select stats to display:"),
        choices=[stats_labels[stat] for stat in available_stats],
        pointer="> ",
        default=[stats_labels[stat] for stat in available_stats],  # All selected by default
        instruction=messages.get("checkbox_hint", "(Use space to select, enter to confirm)")
    ).execute()

    # If no stats were selected, return early
    if not selected_stats:
        print(messages.get("no_stats_selected", "No stats selected. Analysis cancelled."))
        return

    # Create a mapping from displayed labels back to stat keys
    reverse_mapping = {v: k for k, v in stats_labels.items()}
    
    # Convert selected labels back to stat keys
    selected_stat_keys = [reverse_mapping[label] for label in selected_stats]

    # try to analyze and if error then print the error
    try:
        # Show analyzing message
        print(f"{messages['analyzing_file']}: {file}")
        
        # get analysis results from analyze_file
        results = analyze_file(file)
        
        # Only print the selected stats
        for stat in selected_stat_keys:
            if stat in results:
                print(messages[stat].format(count=results[stat]))
        
    except Exception as e:
        print(f"[red]{messages['error']}[/] {e}")


def main():
    app()  # run typer

# whatever the fuck this is python makes no sense
if __name__ == "__main__":
    main()
