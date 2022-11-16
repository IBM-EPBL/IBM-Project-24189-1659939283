import requests

url = "https://linkedin-jobs-search.p.rapidapi.com/"

payload = {
	"search_terms": "python programmer",
	"location": "30301",
	"page": "1"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "9381357d88msha354337c2eb1e98p1348a7jsn192d84997537",
	"X-RapidAPI-Host": "linkedin-jobs-search.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)