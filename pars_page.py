from urllib import request
import re


class Profile:

    def __init__(self,key):
        self.key = key
        pass

    def Pars(self):
        try:
            myUrl = "https://www.instagram.com/" + self.key + "/"
            otvet = request.urlopen(myUrl)
            text = otvet.readlines()
            k = len(text)
            text2 = []
            for q in range(0, k, 1):
                dec = text[q]
                dec = dec.decode('utf-8')
                text[q] = dec

                res = re.search("shortcode", text[q])

                if res is None:
                    q += 1
                else:
                    text2.append(text[q])
                    q += 1
                    pass
                pass
            pass

            text2 = re.split(":|,", text2[0])
            k = len(text2)

            key_for_dw = []
            for q in range(0, (k-1), 1):
                res = re.search("shortcode", text2[q])
                if res is None:
                    q += 1
                else:
                    key_for_dw.append(text2[q+1])
                    q += 1
                pass
            return key_for_dw
        except:
            print("Error pars_page")



pass

