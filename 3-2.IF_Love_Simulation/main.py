print('''
*******************************************************************************
               ________                           ________
         _,=**************,_                 _,**************=,_
      _,*********************,_           _,*********************,_
    ,***************************,       ,***************************,
  ,*******************************,   ,*******************************,
 ,*********************************, ,*********************************,
,************************ ,;ssssssss;. *********************************,
******************** ____sSSSSSSSSSSSSs, ********************************
******************* / __()SSSSSSSSSSSSSSs            ********************
****************** / ___()SSSSSSSSSSSSSSS _-TTTTTT--_  ******************
***************** / ___()SSSSSSSSS'     |///|||\\\\\\\\ *****************
**************** ( __()SSSSSS(@)S' ====/=_ '||||\\\\\\\\ ****************
***************** \SSSSSSSSSS()     ~=|_  ~  ||||\\\\\\\\ ***************
**************** {SSSSSSSSSS'         |       ||||||||||| ***************
 *************** {SSSSSSS'         _/~'       ||||||||||| **************
 *************** {SSSSS'   \      (x)         ||||||||||| **************'
 `*************  /          ~-_   /~          ||||||||||| *************'
  `************ |            / ~~~\______--~  ||||||||||| ************'
   `*********** |           | \ ****** /      ||||||||||| ***********'
    `********* |   _-----__ |  \ **** /       ||||||||||| **********'
      ~******* |           ~~-__`----/ __----_||||||||||| ********~
        ~***** |                ~~-_/ /       |||||||\\\\\ *****~
          ~** |                     ~~--__     \\\\\\\\\\\\ **~
            ~**                           ~~----\\\\\\\\\\**~
              ~**                                \\\\\\\**~
                ~** --__                          \\\\**~
                  ~**,. ~~--__                    ||**~
                    ~****;,.. ~~~---____         .**~
                      ~************;,.. ~~~~~~~.**~
                        ~***********************~
                          ~*******************~
                            ~***************~
                              ~***JS'88***~
                                ~*******~
                                  ~***~
                                   `*'
*******************************************************************************
''')
print("City of Romance: 사랑과 모험")
print("도시의 불빛 아래, 당신의 사랑 이야기가 시작됩니다. 심장이 뛰는 만남으로 초대합니다!")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choise1 = input(
    '\n\n1단계: 뜻밖의 맛남\n당신은 친구들과 함께 세련된 도시의 팝업 이벤트에 참석했습니다. 이곳에서 독특한 스타일로 눈에 띄는 인물이 당신의 시선을 사로잡습니다. 친구가 이 인물과 학교 선후배 사이라며 수빈이를 소개를 합니다.\n질문: "당신은 이 기회를 활용해 그 인물에게 다가갈 용기가 있습니까? (y/n)\n답:'
).lower()

if choise1 == "y":
    choise2 = input(
        '\n\n2단계: 불꽃 튀는 데이트\n 수영장에서의 첫 만남은 성공적이었고, 두 사람 사이의 호기심이 커지면서 본격적인 데이트를 계획하게 됩니다. 당신은 두 가지 다른 타입의 데이트를 제안합니다.\n 질문: "당신은 역동적인 암벽 등반을 하러 갈 것입니까, 아니면 문화적인 박물관 투어를 할 것입니까?\n(y: 박물관 투어/n: 암벽 등반)\n답:'
    ).lower()
    if choise2 == "n":
        choise3 = input(
            '\n\n3단계: 고백의 순간\n 암벽등반 당시 정말 위험한 상황에서 수빈을 구출한 당신! 그 후 여러 차례의 데이트를 거치며 서로에 대해 많은 것을 알게 되었습니다. 더 깊은 감정을 확인하기 위하여 분위기 좋은 이자카야에 방문합니다. 수빈은 이미 사케 1병과 소주 2병을 마신 상태입니다. 자신의 취약한 모습을 보이며 당신에게 질문합니다.\n "오빠~, 이제 어디가?"\n질문: "이 상황, 당신은 어떤 대답을 하시겠습니까? (y: 근처에서 쉬었다갈까?/n: 너무 늦었다. 오빠가 집에 데려다 줄게)\n답:'
        ).lower()
        if choise3 == "y":
            print('''                    
   ***     ***                   ***     ***                   ***     ***
 **   ** **   **               **   ** **   **               **   ** **   **
*       *       *             *       *       *             *       *       *
*               *             *               *             *               *
 *     LOVE    *               *     LOVE    *               *     LOVE    *
  **         **   ***     ***   **         **   ***     ***   **         **
    **     **   **   ** **   **   **     **   **   ** **   **   **     **
      ** **    *       *       *    ** **    *       *       *    ** **
        *      *               *      *      *               *      *
                *     LOVE    *               *     LOVE    *
   ***     ***   **         **   ***     ***   **         **   ***     ***
 **   ** **   **   **     **   **   ** **   **   **     **   **   ** **   **
*       *       *    ** **    *       *       *    ** **    *       *       *
*               *      *      *               *      *      *               *
 *     LOVE    *               *     LOVE    *               *     LOVE    *
  **         **   ***     ***   **         **   ***     ***   **         **
    **     **   **   ** **   **   **     **   **   ** **   **   **     **
      ** **    *       *       *    ** **    *       *       *    ** **
        *      *               *      *      *               *      *
                *     LOVE    *               *     LOVE    *
                 **         **                 **         **
                   **     **                     **     **
                     ** **                         ** **
                       *                             *
            ''')
            choise4 = input(
                '\n\n4단계: 결정적 순간\n사랑에 빠진 당신은 이제 마음을 고백할 준비가 되었습니다. 당신은 세 가지 중 한 가지 방법을 선택해 수빈이에게 미뤄뒀던 마음을 전달할 계획입니다. 질문:\n"바닷가에서 별빛 아래 고백할 것입니까?" (1번)\n"친구들이 보는 앞에서 파티에서 고백할 것입니까?" (2번)\n"좋아하는 음악 콘서트가 끝난 후 무대 위에서 고백할 것입니까?" (3번)\n답:'
            )
            if choise4 == "1":
                print("나는 뜨거운 태양이 좋아~ 잘가~")
            elif choise4 == "2":
                print('''
                             -   "?"  " """  %=.
                         .  -^^    -  -- .    =\ .
                        '    " =.  "          %  "?
                       :   ^       -.       ^   ^ .^               .,,_
                       -   -  -         . Jb -   z$r           , ; ,, ."z..
                          r = ^         . d$e..e$$$P         zr4dF"`",.^^";.- ,.
                    ce$  -               z$$$$$$$$P":n.    ,J;' ,db 4e$de;/F?bc"$e
                   $$$$b ^. -     r  . .d$$$$PF",$..4MM J,d$C ,$$??% ?$cF?$?$b-3."$-e
                  $$$$$b^ /..      .^"$$$$P"  .,$$$c "M dd$; z"$b????c `$."e^?$;?$.%"
                 d$$$$$$ . ^/      eed$$$$$$$$$$$"$$b 4 "$F  zd$$.,,cd$  "$r?c^?.$Fd%d
                `F$$"?$$ /      %.J$$$$$$$$$$$$$$ee   M "? '("$$$$$$$$$$."-"?b;^L4c"\"-
                 %"$  3F    ... ."""$$$$$$$$$$$$".   /  eF `??$$$$$$$$$$$b-  :`;^c?=c;`;.
                 ( $ : % .  J$$$$$$c "$$$$$$$$$$$Lz   .$"z ,.,z$$$$$$$$P.""" .,;;'$.;%;)..
                  ``b`!; 4h.`?$$$$$"    `"""""??""    $";" d$$$$$$$P?',e$$..;;-;e"^-;^"""
                ' ! " !!; MMhx. """.nhd -h          /4F;".  `""???:''`.,zcJC";e$$F'   =ede

                .!! !!!!!!>   nM>             ~  ,4$r4$b";;e$P?ECeedP",n"Cr=?",$$"$$$$$ '.
                `'!;.  '`'!>  MM      '     ~  ,dL$$$$;;;zELe$""', ,udMMn,n= z$"$$"u$3" "
                 '!!!! .;!!!. Mf  \'  d  >   ,^z$$"$";;.$$$F',uMMM;MMMMMMM ,P",$F $$)f.
                   '!  \    od;d$F;";;zP$)F',cMMMM;dMMMMMP d" zP"'4$.J,M
                 !!!;`!!!!!!!> Mh. '     .r";d";4;=%J";cF ,MMMMMF;MMMMMMMn-.d",f P'" MM
                :!!!!>`'!!!!!! "MM      z";d$;;4";;rr;z$; MMMMM>;:MMMMMMMMn,,Mf "  xn3M
                !!!!!!> `
                !!!!!!!   `  )    4F;$"F4F4;;F;?-;?; :MMMMMM;MMMMMMMMMMMMMMMMM;4MMMf
                !!!'!!!     `'!      e$;3Ce^;;;L;^;^.;4 .MMMMMM>;MMMMMMMMMMMMMMMMMM;MMMP
                ''')
                print("수빈이가 내게 입을 맞췄고 우리는 연인이 되었다~ Happy Ending~")
            elif choise4 == "3":
                print("모르는 사람도 가득한 곳에서 나를 이렇게 망신을 줘? 다신 연락하지마! Game Over.")
        else:
            print("오빠는 참 좋은 사람이네... 잘가~ Game Over.")
    else:
        print("저는 오빠가 역동적인 사람이라 좋았어요. 잘가~ Game Over.")
else:
    print("네, 잠이나 자세요. Game Over.")