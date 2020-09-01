import argparse                         # 인자값을 쉽게 옵션으로 만들 수 있는 라이브러리
import requests                         # HTTP요청을 할 수 있는 라이브러리

def print_introduce():
    print("********************************************************")
    print("* Web_fuzzer_BoB 4조 (진영훈, 박찬솔, 석지원, 안평주)  *")
    print("********************************************************\n")

    #print("Target :", args.url)
    #print("Total requests : ", len(Payloads), "\n")

def print_item():  
    print("\n===========================================================================================================")
    print("ID         Response   Lines    Word     Chars       Payload          Target")
    print("===========================================================================================================")



def print_main():
    print("{0:04d}:{1:9}{2:11} L{3:7} W{4:8} Ch     {5}".format(ID,Response,Lines,Word,Chars,Payload), end='')
    
    #print("ID :", ID)                  
    #print("Response :", Response)      
    #print("Lines :", Lines)            
    #print("Word :", Word)              
    #print("Chars :", Chars)            
    #print("Payload : ", Payload[ID])   


# 입력받은 쿠키값 저장
bob_cookies = {}

# 입력받은 POST data값 저장
bob_data = {}

# Payload의 개수 세는 변수
ID=1

if __name__ == "__main__":

    # 인자값을 받을 수 있는 인스턴스 생성
    parser = argparse.ArgumentParser(description='사용법')

    # 입력받을 인자값 등록
    parser.add_argument('-various_seed', required=True, help='퍼징할 시드파일 경로')     # True  : 필수 입력 O
    parser.add_argument('-area_seed', required=False, help='POST방식으로 넘길 값')             

    # 입력받은 인자값을 args에 저장 (type: namespace)
    args = parser.parse_args()

    # 인자값으로 입력받은 varios시드파일에 있는 모든 시드 읽어오기
    f = open(args.various_seed, 'r')                        
    Payloads = f.readlines()                         
    f.close()
    # 인자값으로 입력받은 area시드파일에 있는 모든 시드 읽어오기
    f1 = open(args.area_seed, 'r')                        
    areas = f1.readlines()                         
    f1.close()

    # 소개 출력
    print_introduce()

    # Session 생성, with 구문 안에서 유지
    with requests.Session() as s:
        loginfo = {"login":"bee", "password":"bug", "security_level" : "0", "form" : "submit"}
        cookie = s.post("http://175.112.11.209"+"/bWAPP/login.php", data=loginfo)
        bob_cookies = s.cookies
        requests.get("http://175.112.11.209/bWAPP/sm_local_priv_esc_1.php", cookies=bob_cookies)
        phpsessid=bob_cookies['PHPSESSID']

        for area in areas:
            print_item()
            area=area.replace('ip', '175.112.11.209')   #attack area 
           
            #Get ?? POST??
            div = str(area).split("*")     # url?* data:get or url*data : post
            area=div[0]+div[1]
            print('target : ',div[0])
            if (str(div[0]).find('?')==-1):    #-1 : post, != -1 : get
                #POSt
                bob_url=div[0]
                print(bob_url)                              #div[0] = url
                div1 = div[1].split("&")                    # div[1] = postdata | "&"을 기준으로 post를 쪼갬
                Numseed = range(len(div1))
                for i in Numseed:                           # 입력받은 data만큼 반복
                    div2 = str(div1[i]).split("=")          # "="을 기준으로 data를 쪼갬
                    bob_data[div2[0]] = div2[1]             # 쪼갠 data를 dictionary형태로 저장
                    if (str(div2[1]).find("@") != -1): 
                        key_BOB = div2[0]                   # if @ exist in value, key를 저장
                    else : 
                        print("\nI don't search @")           # @문자가 안들어 있다면 프로그램 종료 
                        continue  
                for Payload in Payloads:
                    bob_data[key_BOB] = Payload.replace("\n", "")   # value가 @n인 key를 찾아서 Payload로 치환
                    req = s.post(bob_url,data=bob_data, cookies=bob_cookies, allow_redirects=False)    # 전송, allow_redirects 설정 안하면 Response 200,404 만 뜸, get도 post로 넘겨도 상관없는듯
                    bob_data = {}
                    html = req.text                                 # HTML 소스 가져오기
                    Response = req.status_code                      # HTTP Status 가져오기 (200: 정상)
                    Lines = len(html.split("\n"))-1
                    Word = len(html.split())
                    Chars = len(html)
                    print_main()                                

                    ID+=1
            else: 
                #GET
                count=1                                     #@1 ... count
                if str(div[1]).find("@") == -1 :              # @문자가 안들어 있다면 프로그램 종료 
                    print("I don't search @")
                    quit()
                div1 = div[1].split("&")                    # div[1] = postdata | "&"을 기준으로 post를 쪼갬
                Numseed = range(len(div1))
                print('NumSeed: ',Numseed)
                for i in Numseed:                           # 입력받은 data만큼 반복
                    div2 = str(div1[i]).split("=")          # "="을 기준으로 data를 쪼갬
                    if (str(div2[1]).find("@") != -1): 
                        for Payload in Payloads:            # 한줄씩 출력하여 시드파일이 끝날 때 까지 반복 
                            query='@'+str(count)
                            bob_url=area.replace(query,Payload)
                            bob_url=bob_url.replace("\n","")

                            req = s.post(bob_url,data=bob_data, cookies=bob_cookies, allow_redirects=False)    # 전송, allow_redirects 설정 안하면 Response 200,404 만 뜸, get도 post로 넘겨도 상관없는듯
                            bob_data = {}
                            html = req.text                                 # HTML 소스 가져오기
                            # 출력할 것들 파싱해주기
                            Response = req.status_code                      # HTTP Status 가져오기 (200: 정상)
                            Lines = len(html.split("\n"))-1
                            Word = len(html.split())
                            Chars = len(html)
                            print_main()                                
                            ID+=1
                        count= count+1
                    else: 
                        print("\nI don't search : @")           # @문자가 안들어 있다면 프로그램 종료 
                        count=1 
                        break
                    