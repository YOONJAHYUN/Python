def solution(m, musicinfos):
    dic = {"C#": "H", "D#": "I", "F#": "J", "G#": "K", "A#": "L"}
    change = ["C#", "D#", "F#", "G#", "A#"]

    for char in change:
        if char in m:
            m = m.replace(char, dic[char])

    candi = []
    idx = 1
    # for 문을 돌려서 음악정보를 정리한다.
    for music in musicinfos:
        start, end, title, melody = music.split(',')

        time = 0
        time += int(end[:2]) * 60 + int(end[3:])
        time -= int(start[:2]) * 60 + int(start[3:])
        full_melody = ''

        for char in change:
            if char in melody:
                melody = melody.replace(char, dic[char])

        for i in range(time):
            full_melody += melody[i % len(melody)]
        # print(full_melody)

        # 악보를 순회하면서 m이 있는지 체크한다.
        if m in full_melody:
            candi.append([idx, title, time])
        idx += 1

    # 체크를 중지하지말고 다 반환.
    # 재생시간이 가장 긴 것부터.
    # 같을 경우 먼저 입력된 제목
    candi.sort(key=lambda x: (-x[2], x[0]))
    if candi:
        answer = candi[0][1]


    else:
        answer = "(None)"
    return answer
