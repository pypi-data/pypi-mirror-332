import pandas as pd
import re

def find_matching_sentences(abstract, terms):
    sentences = re.split(r'(?<=[.!?]) +', abstract)
    matching_sentences = []
    for sentence in sentences:
        if any(re.search(r'\b' + re.escape(term) + r'\b', sentence, re.IGNORECASE) for term in terms):
            matching_sentences.append(sentence)
    return matching_sentences

def search_terms_in_abstracts(terms_file_path, excel_file_path, output_file_path):
    with open(terms_file_path, 'r') as file:
        search_terms = [line.strip() for line in file.readlines()]

    df = pd.read_excel(excel_file_path)
    total_articles = len(df)
    term_percentages = {}

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for term in search_terms:
            articles_with_keyword = 0

            for index, row in df.iterrows():
                abstract = row['Summary']
                if pd.isna(abstract):
                    continue

                matching_sentences = find_matching_sentences(abstract, [term])
                if matching_sentences:
                    articles_with_keyword += 1

            percentage = (articles_with_keyword / total_articles) * 100
            term_percentages[term] = percentage

        sorted_terms = sorted(term_percentages.keys(), key=lambda x: term_percentages[x], reverse=True)

        for term in sorted_terms:
            output_file.write(f"Search Term: {term}\n")
            output_file.write("=" * 50 + "\n")

            for index, row in df.iterrows():
                abstract = row['Summary']
                if pd.isna(abstract):
                    continue

                matching_sentences = find_matching_sentences(abstract, [term])
                if matching_sentences:
                    output_file.write(f"Title: {row['Title']}\n")
                    output_file.write(f"URL: {row['URL']}\n")
                    output_file.write("Matching Sentences:\n")
                    for sentence in matching_sentences:
                        output_file.write(f" - {sentence}\n")
                    output_file.write("-" * 50 + "\n")

            output_file.write(f"\nPercentage of articles containing '{term}': {term_percentages[term]:.2f}%\n")
            output_file.write("\n\n")

    print(f"Results have been saved to: {output_file_path}")