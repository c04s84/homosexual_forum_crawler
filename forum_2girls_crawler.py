from bs4 import BeautifulSoup
import requests
import re
import json

def trade_spider(max_page):
	page = 1
	while page <= max_page:
		url = 'http://www.2girl.net/forum-187-' + str(page) + '.html'
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text,"lxml") # all the source code from website
		
		for link in soup.findAll('a', {'class':'s xst'}):
			href =  link.get('href')
			title = link.string

			# print(title)
			# print(href)
			get_single_post_data(href)
		page += 1

'''
# go through each item one by one in order to get the content of each link 
def get_single_post_data(post_url):
		source_code = requests.get(post_url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text,"lxml") # all the source code from website

		## ----- post topic ----- ##
		for post_link in soup.findAll('span',{'id':'thread_subject'}):
			print("TOPIC:" , post_link.string)

		## ----- post content ----- ##
		for post_content in soup.findAll('div',{'class':"t_fsz"}):
			print("CONTENT:" , post_content.text)

		## ----- post author ----- ##
		for author in soup.findAll('img',{'class':'authicn'}, limit = 1):
			author_id = re.findall(r'\d+', author['id'])
			print("AUTHOR:" , author['id'])
			author_id_in_post = "authorposton" + " ".join(str(x) for x in author_id)

		## ----- post date ----- ##
			for post_date in soup.findAll('em',{'id':author_id_in_post}, limit = 1):
				author_post_date = post_date.string

				if str(author_post_date) == "None":  # Date error catch caused by post date too close
					post_date_pattern = " ".join(str(x) for x in re.findall(r'\d+\-\d+\-\d+', post_date.find('span')['title']))
					print("DATE:" , post_date_pattern)
					# print(author_post_date)
				else:
					post_date_pattern = " ".join(str(x) for x in re.findall(r'\d+\-\d+\-\d+', author_post_date))
					print("DATE:" , post_date_pattern)





trade_spider(1)

'''


# go through each item one by one in order to get the content of each link 
def get_single_post_data(post_url):
        source_code = requests.get(post_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"lxml") # all the source code from website

        ## ----- post topic ----- ##
        
        for post_link in soup.findAll('span',{'id':'thread_subject'}):
            global post_topic
            post_topic = post_link.string
            print("Processing on TOPIC:" , post_topic)

        ## ----- post content ----- ##
        for post_content in soup.findAll('div',{'class':"t_fsz"},limit = 1):
            global post_contents
            post_contents = post_content.text
#             print("CONTENT:" , post_contents)

        ## ----- post author ----- ##
        for author in soup.findAll('img',{'class':'authicn'}, limit = 1):
            global author_id
            global author_id_in_post
            author_id = re.findall(r'\d+', author['id'])
#             print("AUTHOR:" , author['id'])
            author_id_in_post = "authorposton" + " ".join(str(x) for x in author_id)

        ## ----- post date ----- ##
            for post_date in soup.findAll('em',{'id':author_id_in_post}, limit = 1):
                global author_post_date
                global post_date_pattern
                author_post_date = post_date.string
                if str(author_post_date) == "None":  # Date error catch caused by post date too close
                    post_date_pattern = " ".join(str(x) for x in re.findall(r'\d+\-\d+\-\d+', post_date.find('span')['title']))
#                     print("DATE:" , post_date_pattern)
#                     print("="*80)
                    
                else:
                    post_date_pattern = " ".join(str(x) for x in re.findall(r'\d+\-\d+\-\d+', author_post_date))
#                     print("DATE:" , post_date_pattern)
#                     print("="*80)
    
                # json data
                data = {
                    "topic": post_topic,
                    "content": post_contents,
                    "author": author['id'],
                    "date": post_date_pattern}

#                 print(data)
                with open('thesis_data/TwoGirls_json.txt', 'a') as outfile:
                    return json.dump(data, outfile, ensure_ascii = False)



                # json_data = json.dumps(data, ensure_ascii = False)s
#                 print(json_data)
                # f = open("thesis_data/TwoGirls.txt", 'a')
                # f.write(json_data +'\n')
                # f.close()

trade_spider(101)

