import os

def get_domain_from_url(url):
    if url in (None, "", " ", "\n") or len(url) == 0:
        results_domain.write("Error: row is empty" + '\n')
    else:
        start1 = "http://"
        start2 = "https://"
        a = url.find(start1)
        if a >= 0:
            start = len(start1)
        else:
            a = url.find(start2)
            if a >= 0:
                start = len(start2)
            else:
                start = 0
        url_no_http = url[start:]
        end = url_no_http.find("/")
        if end == -1:
            domain = url_no_http
        else:
            domain = url_no_http[:end]
        if "." in domain:
            results_domain.write(domain + '\n')
        else:
            results_domain.write("Error: not a domain" + '\n')

#clear previous results
def clean_old_files():
    try:
        os.remove("domain.txt")
        print('Old file domain.txt removed')
    except:
        print('File domain.txt not found')

# create file for results
clean_old_files()
results_domain = open('domain.txt', 'x')

# working with list of urls
file = open("url.csv", "r")
num_lines = sum(1 for line in open('url.csv'))

current_line = 1
for line in file:
    #if __name__ == '__main__':
    #    print("line " + str(current_line) + " from " + str(num_lines) + " lines")
    #    current_line += 1
    get_domain_from_url(line)

file.close()
results_domain.close()

print("Done!")