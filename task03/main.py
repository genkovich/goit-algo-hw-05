from rabin_karp import rabin_karp_search
from kmp import kmp_search
from boyer_moore import boyer_moore_search
from pathlib import Path
from prettytable import PrettyTable
import timeit


def main():
    article1 = Path('article_1.txt').read_text()
    article2 = Path('article_2.txt').read_text()

    #benchmarking

    search_patterns = ["алгоритм", "asdsdsadasdas"]

    for search_pattern in search_patterns:
        table = PrettyTable()
        table.field_names = ["Algorithm", "Pattern", "Article", "Time (seconds)"]

        start_time = timeit.default_timer()
        rabin_karp_search(article1, search_pattern)
        elapsed_time = timeit.default_timer() - start_time
        table.add_row(["Rabin-Karp", search_pattern, "Article 1", elapsed_time])

        start_time = timeit.default_timer()
        rabin_karp_search(article2, search_pattern)
        elapsed_time = timeit.default_timer() - start_time
        table.add_row(["Rabin-Karp", search_pattern, "Article 2", elapsed_time])

        # KMP search
        start_time = timeit.default_timer()
        kmp_search(article1, search_pattern)
        elapsed_time = timeit.default_timer() - start_time
        table.add_row(["KMP", search_pattern, "Article 1", elapsed_time])

        start_time = timeit.default_timer()
        kmp_search(article2, search_pattern)
        elapsed_time = timeit.default_timer() - start_time
        table.add_row(["KMP", search_pattern, "Article 2", elapsed_time])

        # Boyer-Moore search
        start_time = timeit.default_timer()
        boyer_moore_search(article1, search_pattern)
        elapsed_time = timeit.default_timer() - start_time
        table.add_row(["Boyer-Moore", search_pattern, "Article 1", elapsed_time])

        start_time = timeit.default_timer()
        boyer_moore_search(article2, search_pattern)
        elapsed_time = timeit.default_timer() - start_time
        table.add_row(["Boyer-Moore", search_pattern, "Article 2", elapsed_time])

        print(table)

if __name__ == "__main__":
    main()
