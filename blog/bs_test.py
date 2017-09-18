



from bs4 import BeautifulSoup

valid_label_list=["p","div"]


s='<div class="c1"><div class="c2">div2</div></div><script>alert(111)</script>'



BS=BeautifulSoup(s,"html.parser")

# print(BS)
# print(type(BS))


# ret=BS.find(name="div")
# ret=BS.find_all(name="div")
#
# ret=BS.find_all(attrs={"class":"c1"})


for label in BS.find_all():

    print(label.name)

    if label.name not in valid_label_list:

        label.decompose()

print(BS)










