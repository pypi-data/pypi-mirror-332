import arxiv
import pandas as pd
import json
import time

def fetch_arxiv_data(authors, topics, start_date, end_date, max_results=1000):
    queries = []

    if topics:
        topic_queries = ['{}'.format(topic) for topic in topics]
        queries.append(' AND '.join(topic_queries))

    full_query = ' AND '.join(queries) + f" AND submittedDate:[{start_date} TO {end_date}]"

    client = arxiv.Client()
    df = pd.DataFrame(columns=['ID', 'Title', 'Summary', 'Authors', 'Journal', 'Keywords', 'URL', 'Year', 'Month'])
    unique_ids = set()

    try:
        search = arxiv.Search(
            query=full_query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )

        for result in client.results(search):
            if result.entry_id in unique_ids:
                continue

            unique_ids.add(result.entry_id)

            title = result.title
            summary = result.summary
            authors = ', '.join([author.name for author in result.authors])
            journal = result.journal_ref if result.journal_ref else 'N/A'
            keywords = ', '.join(result.categories) if result.categories else 'N/A'
            url = result.entry_id

            pub_date = result.published
            year = pub_date.year
            month = pub_date.month

            new_row = pd.DataFrame({
                'PMID': [result.entry_id],
                'Title': [title],
                'Summary': [summary],
                'Authors': [authors],
                'Journal': [journal],
                'Keywords': [keywords],
                'URL': [url],
                'Year': [year],
                'Month': [month]
            })

            df = pd.concat([df, new_row], ignore_index=True)

    except arxiv.UnexpectedEmptyPageError:
        print("No more results found. Stopping the search.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return df

def save_to_excel(df, file_path):
    df.to_excel(file_path, index=False)
    print(f"Saved {len(df)} results to '{file_path}'.")