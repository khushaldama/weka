import re

def count_years(input_text):

    year_pattern = r'\b\d{4}\b'
    matches = re.findall(year_pattern, input_text)


    year_counts = {}
    for year in matches:
        if year in year_counts:
            year_counts[year] += 1
        else:
            year_counts[year] = 1

    sorted_years = sorted(year_counts.items(), key=lambda x: x[0], reverse=False)
    print(sorted_years)

    for year, count in sorted_years:
        print(f"{year} appears {count} time(s)")
input1 = "In the year 2005, a technological revolution set in motion changes that would ripple through time. By 2012, the seeds of innovation planted earlier blossomed into significant breakthroughs, propelling us into a new era. Now, in 2023, we stand on the threshold of another transformation, building upon the foundations set in past and enriched by the progress of 2023. As this year unfolds, it bears the promise of reshaping industries and lives, a testament to the continuous interplay of progress across different moments in time."
count_years(input1)