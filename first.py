from urllib import request
import re


class InstDWIMG:

    def __init__(self, opop):
        self.g = opop
        pass

    def dw(self):
        try:
            myUrl = "https://www.instagram.com/p/" + self.g + "/?__a=1"
            otvet = request.urlopen(myUrl)

            text = otvet.readlines()
            text2 = text[0]
            text2 = text2.decode('utf-8')
            text3 = re.split(",|:", text2)
            k = len(text3)

            q = 0

            for q in range(0, k, 1):
                res = re.search("http", text3[q])
                if res is None:
                    q += 1
                else:
                    break

                pass

            myUrl2 = text3[q] + ":" + text3[q+1]

            myUrl2 = myUrl2[:-1]
            myUrl2 = myUrl2[1:]

            logo = request.urlopen(myUrl2).read()
            try:
                nadpis = "Download img:"+self.g
                print(nadpis)

                logo = request.urlopen(myUrl2).read()
                nameop = self.g+".jpg"
                f = open(nameop, "wb")
                f.write(logo)
                f.close()
            except:
                print("Bad URL")

            print("Download complete")

        except:
            print("Error")
        pass

    pass
