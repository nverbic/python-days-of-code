'''
    Day 56
    Create a function to extract all URLs from a given text using regular expressions.

    Output:
    https://www.rtvslo.si/sarajevo-1984/video-tocno-40-let-od-jureta-bureka-in-nepozabne-sarajevske-srebrne-medalje/698111
    file://localhost:4040/zip_file
    http://tutorialspoint.com
    https://www.tutorialspoint.com/market/index.asp
'''

import re

TEXT_EXAMPLE = "Olimpijada u Sarajevu: \
        https://www.rtvslo.si/sarajevo-1984/video-tocno-40-let-od-jureta-bureka-in-nepozabne-sarajevske-srebrne-medalje/698111 \
        File location: file://localhost:4040/zip_file \
        <p>Hello World: </p><a href=http://tutorialspoint.com>More Courses</a> \
        <a href=https://www.tutorialspoint.com/market/index.asp>Even More Courses</a>'"

if __name__ == "__main__":
    # Extract URLs from a text
    # \w matches[a-zA-Z0-9_]
    # + is repeating metachar. and requires at list one occurence of the repeating characters
    # [] define a set of char. that we want to match
    url_list = re.findall(r'\w+://[\w\-\.\:\/]+', TEXT_EXAMPLE)

    for url in url_list:
        print(url)
