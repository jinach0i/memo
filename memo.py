
import sys
#ㄴ sys라는 lib module을 load
option=sys.argv[1]
#ㄴ 이제부터 option은 '프로그램 실행 옵션 값'(+argv[2]=memo 내용)
if option=='-a':
#ㄴ option이가 -a로 입력되면,
    memo=sys.argv[2]
    #ㄴ 이제부터 memo라는 애는 입력한 memo 내용이다
    with open('memo.txt','a') as f:
    #ㄴ 다음 file 안에 a방식(append)식으로 내용을 붙여가고 다 붙이면 알아서 close한다(with문으로 인해)
        f.write(memo)
        #ㄴ f 에 괄호 안(memo에 해당하는 값=입력한 memo의) 내용을 덧붙인다
        f.write('\n')
        #ㄴ f 에 괄호 안(memo에 해당하는 값:/n:한줄 띈 상태)라는 내용을 덧붙인다
elif option=='-v':
#ㄴ =else if:option을 -v라고 하면:python memo.py -v라고 입력하면
    with open('memo.txt') as f:
    #ㄴ 
        memo=f.read()
        #ㄴ read method: f로 선언된 file(memo.txt)의 내용을 읽고 memo로 저장 선언
        print(memo)
        #ㄴ memo값 을 출력