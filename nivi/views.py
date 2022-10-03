from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def option(request):
    return render(request,'option.html')
def contact(request):
    return render(request,'contact.html')
def add(request):
    value=request.GET['message']
    ALP = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
           'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
           'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
           '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
           '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
           '-': '-....-', '(': '-.--.', ')': '-.--.-'}

    def convert(a):
        c = ''
        for l in a:
            if l != ' ':
                c += ALP[l] + ' '
            else:
                c += ' '
        return c

    a = value
    res = convert(a.upper())
    return render(request,'single.html',{'result':res})

def contact2(request):
    return render(request,'contact2.html')
def add2(request):
    value = request.GET['message']

    ALP = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
           'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
           'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
           '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
           '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
           '-': '-....-', '(': '-.--.', ')': '-.--.-'}

    def convert(a):
        a += ' '
        b = ''
        c = ''
        for i in a:
            if i != ' ':
                j = 0
                c += i

            else:
                j += 1
                if j == 2:
                    b += ' '
                else:
                    b += list(ALP.keys())[list(ALP.values()).index(c)]
                    c = ''
        return b

    a = value
    res= convert(a)

    return render(request,'single2.html',{'result':res})

def option2(request):
    return render(request,'option2.html')
def source(request):
    return render(request,'source.html')
def audio(request):
    value = request.GET['message']

    # TEXT TO AUDIO
    ALP = {'A': '.-', 'B': '-... ', 'C': '-.-. ', 'D': '-.. ', 'E': '. ', 'F': '..-. ', 'G': '--. ', 'H': '.... ',
           'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
           'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
           '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
           '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
           '-': '-....-', '(': '-.--.', ')': '-.--.-'}

    def convert(a):
        c = ''
        for l in a:
            if l != ' ':
                c += ALP[l] + ' '
            else:
                c += ' '
        return c

    a = value
    res= convert(a.upper())


    from pygame import mixer
    import time

    for char in res:
        if char == "-":
            mixer.init()
            mixer.music.load("dah.wav")
            mixer.music.play()
            time.sleep(.6)
        elif char == ".":
            mixer.init()
            mixer.music.load("dit.wav")
            mixer.music.play()
            time.sleep(.7)
        else:
            time.sleep(.2)


    return render(request,'output.html',{'result':res})

def source2(request):
    return render(request,'source2.html')
def audio2(request):
    value = request.GET['aud']
    from morse_audio_decoder.morse import MorseCode

    morse_code = MorseCode.from_wavfile(value)
    out = morse_code.decode()


    return render(request,'output2.html',{'result':out})

def features(request):
    return render(request,'features.html')
def video(request):
    return render(request,'video.html')
def record(request):
    import cv2
    import mediapipe as mp
    import time

    res = ''

    def rescaleFrame(frame, percent=75):
        width = int(frame.shape[1] * percent / 100)
        height = int(frame.shape[0] * percent / 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    cap = cv2.VideoCapture(0)

    pTime = 0

    mp_draw = mp.solutions.drawing_utils
    mp_facemesh = mp.solutions.face_mesh
    facemesh = mp_facemesh.FaceMesh(max_num_faces=2)
    draw_spec = mp_draw.DrawingSpec(thickness=1, circle_radius=2)

    ear1prev = []
    ear2prev = []
    wordArray = []
    isLong = False
    blinkedFor = 0
    notBlinkedFor = 0
    wasBlinked = False
    letterArray = ""
    letterIs = ""

    MorseCode = {
        "SL": "A",
        "LSSS": "B",
        "LSLS": "C",
        "LSS": "D",
        "S": "E",
        "SSLS": "F",
        "LLS": "G",
        "SSSS": "H",
        "SS": "I",
        "SLLL": "J",
        "LSL": "K",
        "SLSS": "L",
        "LL": "M",
        "LS": "N",
        "LLL": "O",
        "SLLS": "P",
        "LLSL": "Q",
        "SLS": "R",
        "SSS": "S",
        "L": "T",
        "SSL": "U",
        "SSSL": "V",
        "SLL": "W",
        "LSSL": "X",
        "LSLL": "Y",
        "LLSS": "Z"
    }

    a = 0
    while True:
        a += 1
        success, img = cap.read()
        scaled = rescaleFrame(img, 150)

        imgRGB = cv2.cvtColor(scaled, cv2.COLOR_BGR2RGB)
        results = facemesh.process(imgRGB)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        count = 0
        if results.multi_face_landmarks:
            for faceLm in results.multi_face_landmarks:
                mp_draw.draw_landmarks(scaled, faceLm, mp_facemesh.FACEMESH_CONTOURS, draw_spec, draw_spec)

                ear1 = abs((faceLm.landmark[160].x - faceLm.landmark[144].x) ** 2 - (
                            faceLm.landmark[160].y - faceLm.landmark[144].y) ** 2) + abs(
                    (faceLm.landmark[158].x - faceLm.landmark[153].x) ** 2 - (
                                faceLm.landmark[158].y - faceLm.landmark[153].y) ** 2) / abs(
                    ((faceLm.landmark[33].x - faceLm.landmark[133].x) ** 2) - (
                                (faceLm.landmark[33].y - faceLm.landmark[133].y) ** 2))
                ear2 = abs((faceLm.landmark[385].x - faceLm.landmark[380].x) ** 2 - (
                            faceLm.landmark[385].y - faceLm.landmark[380].y) ** 2) + abs(
                    (faceLm.landmark[387].x - faceLm.landmark[373].x) ** 2 - (
                                faceLm.landmark[387].y - faceLm.landmark[373].y) ** 2) / abs(
                    ((faceLm.landmark[362].x - faceLm.landmark[263].x) ** 2) - (
                                (faceLm.landmark[362].y - faceLm.landmark[263].y) ** 2))

                if count > 10:
                    count = 0
                else:
                    count = count + 1

                if len(ear1prev) > 10:
                    ear1prev[count] = ear1
                    isLong = True
                else:
                    ear1prev.append(ear1)

                if len(ear2prev) > 10:
                    ear2prev[count] = ear2
                    isLong = True
                else:
                    ear2prev.append(ear2)

                if isLong:
                    if ((ear1prev[abs(count - 9)] * 0.70 > ear1) and (ear2prev[abs(count - 9)] * 0.70 > ear2)):

                        wasBlinked = True
                        blinkedFor = blinkedFor + 1
                    else:
                        if (blinkedFor > (fps * .8)):

                            letterArray = letterArray + "L"
                            blinkedFor = 0

                        elif (blinkedFor > int(fps / 8)):

                            letterArray = letterArray + "S"
                            blinkedFor = 0

                        else:

                            notBlinkedFor = notBlinkedFor + 1


                            if (notBlinkedFor > fps * 2):

                                if letterArray in MorseCode:
                                    letterIs = MorseCode[letterArray]
                                    wordArray.append(letterIs)
                                    letterArray = ""
                                letterArray = ""
                                notBlinkedFor = 0

        finalW = ''.join(wordArray)

        cv2.putText(scaled, str(finalW), (80, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)

        res = finalW
        if a == 250:
            cv2.destroyAllWindows()

            break
        cv2.imshow("Image", scaled)
        cv2.waitKey(1)



    return render(request,'ans.html',{'result':res})
































