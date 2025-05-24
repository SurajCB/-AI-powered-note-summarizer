from transformers import pipeline
import os

def find_text_files(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".txt")]

def read_files(file_paths):
    content = ""
    for path in file_paths:
        with open(path, 'r', encoding='utf-8') as file:
            content += file.read() + "\n"
    return content

def summarize_text(text):
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    summaries = [summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text'] for chunk in chunks]
    return " ".join(summaries)

def save_summary(summary):
    with open("notes.txt", "w", encoding="utf-8") as f:
        f.write("📘 Summary Notes\n\n")
        f.write("Hey there! Here's a quick and clear summary of the material you provided:\n\n")
        f.write(summary + "\n\n")
        f.write("Hope this helps with your studies. Feel free to add more notes anytime!\n")

if __name__ == "__main__":
    folder = "notes"
    if not os.path.exists(folder):
        print("Oops! I couldn't find the 'notes' folder. Please make sure your text files are there.")
    else:
        files = find_text_files(folder)
        if not files:
            print("Looks like the folder is empty. Please add some text files for me to summarize.")
        else:
            print("Got the files. Working on your summary, hang tight...")
            content = read_files(files)
            summary = summarize_text(content)
            save_summary(summary)
            print("Done! Your summary is saved in 'notes.txt'. Good luck with your learning!")
