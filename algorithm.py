from distance import getDistance
from tmap import timeSet


def createMat(index):
    global c
    c = [[0 for i in range(index)] for i in range(index)]
    global f
    f = [[0 for i in range(index)] for i in range(index)]
    global d
    d = [[0 for i in range(index)] for i in range(index)]
    global w
    w = [[0 for i in range(index)] for i in range(index)]
    global time
    time = [[1 for i in range(index)] for i in range(index)]


def mcmf(hosList, vec, start, end, index):
    max_flow = 0
    que = []
    pathList = []
    qwe = 1
    while True:
        processingTime = 0
        setWeight(vec, start, end, index)  # 가중치설정
        path = [-1] * index  # 경로저장
        inQue = [False] * index
        dist = [10000000] * index
        que.append(start)
        path[start] = start
        inQue[start] = True
        dist[start] = 0
        while que:
            curr = que.pop(0)
            if curr == end:
                break
            inQue[curr] = False

            for next in vec[curr]:
                if (c[curr][next] - f[curr][next] > 0) and (dist[next] > dist[curr] + w[curr][next]):
                    path[next] = curr
                    dist[next] = dist[curr] + w[curr][next]
                    if not inQue[next]:
                        inQue[next] = True
                        que.append(next)
                        # print("que push num:",next)

        if path[end] == -1:
            break
        flow = 1000000
        # 보낼 수 있는 유량 중 최소값 탐색
        hosArray = [end]
        s = end
        while s != start:
            flow = min(flow, c[path[s]][s] - f[path[s]][s])
            s = path[s]
            hosArray.append(s)

        hosArray.reverse()

        for i in range((len(hosArray)-1)):
            processingTime += time[hosArray[i]][hosArray[i + 1]]
            hosList[hosArray[i + 1]].setprocessing(processingTime, flow, processingTime)  # key, patient, movetime

        print("경로" + str(qwe) + ":", end="")
        qwe += 1
        for i in hosArray:
            print(hosList[i].name, "->", end="")
            pathList.append(hosList[i])
        print("flow: ", flow)
        # 최소값으로 보낼 유량을 더해줌
        s = end
        while s != start:
            f[path[s]][s] += flow
            s = path[s]

        max_flow += flow

    print("max_flow = ", max_flow)


def setMat(hosList, vec, index):
    for curr in range(index):
        for next in range(index):
            if curr == next: continue
            d[curr][next] = getDistance(hosList[curr].lat, hosList[curr].lng, hosList[next].lat, hosList[next].lng)

    maxvalue = 0
    endIndex = 0

    for i in range(1, index):
        if maxvalue < d[0][i]:
            maxvalue = d[0][i]
            endIndex = i

    for curr in range(index):
        for next in vec[curr]:
            # print("hosList lat:"+str(hosList[curr].lat))
            # print("hosList lng:" + str(hosList[curr].lng))
            t = timeSet(hosList[curr].lat, hosList[curr].lng, hosList[next].lat, hosList[next].lng)
            if curr == 0:
                c[curr][next] = hosList[next].capacity
                # time[curr][next] = t

            else:
                c[curr][next] = hosList[next].capacity
                time[curr][next] = t
                c[next][curr] = hosList[curr].capacity
                time[next][curr] = t

    return endIndex


def setWeight(vec, start, end, index):
    que = [start]

    while que:
        curr = que.pop(0)

        for next in vec[curr]:
            if c[curr][next] - f[curr][next] == 0:
                w[curr][next] = 1000000
            else:
                w[curr][next] = time[curr][next] / (c[curr][next] - f[curr][next])
                que.append(next)
            if next == end:
                break
        if next == end:
            break
