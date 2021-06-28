import Hospital
import DataFrame
from datetime import date, datetime, timedelta


class HospitalManage:
    processingTime = 10
    data = DataFrame.covidData()
    now = datetime.now()

    def setHospiatal(self, hoslist):
        self.hosList = hoslist

    def process(self, patient):

        time = 1
        while patient > 0:
            print(str(time) + '분 후')

            for i in range(1, len(self.hosList)):

                if time in self.hosList[i].processing.keys():
                    if patient < self.hosList[i].processing[time][0]:
                        # print(self.hosList[i].name + ': ' + str(patient))
                        self.hosList[i].total += patient
                        self.hosList[i].currPatient += patient
                        patient = 0

                    else:
                        patient -= self.hosList[i].processing[time][0]
                        # print(self.hosList[i].name+': ' + str(self.hosList[i].processing[time]))
                        # 이동시간 추가를 어떻게할 것인지?
                        self.hosList[i].currPatient += self.hosList[i].processing[time][0]
                        self.hosList[i].setprocessing(time + self.processingTime + self.hosList[i].processing[time][1],
                                                      self.hosList[i].processing[time][0],
                                                      self.hosList[i].processing[time][1])
                        self.hosList[i].setcomplete(time + self.processingTime, self.hosList[i].processing[time])
                        self.hosList[i].total += self.hosList[i].processing[time][0]

                if time in self.hosList[i].complete.keys():
                    self.hosList[i].currPatient -= self.hosList[i].complete[time][0]

                print(self.hosList[i].name + ": " + str(self.hosList[i].currPatient))

                self.data.HosName.append(self.hosList[i].name)
                self.data.date.append((self.now + timedelta(minutes=time)).strftime('%Y-%m-%dT%H:%M:%S'))
                self.data.Confirmed.append(self.hosList[i].currPatient)
                self.data.lng.append(self.hosList[i].lng)
                self.data.lat.append(self.hosList[i].lat)

            print("남은 환자 수: " + str(patient))
            print()  # 줄바꿈

            time += 1

        while True:
            a = True
            for i in range(1, len(self.hosList)):
                if self.hosList[i].currPatient != 0:
                    a = False

            if a:
                break
            print(str(time) + '분 후')
            for i in range(1, len(self.hosList)):
                if time in self.hosList[i].complete.keys():
                    self.hosList[i].currPatient -= self.hosList[i].complete[time][0]

                print(self.hosList[i].name + ": " + str(self.hosList[i].currPatient))

                self.data.HosName.append(self.hosList[i].name)
                self.data.date.append((self.now + timedelta(minutes=time)).strftime('%Y-%m-%dT%H:%M:%S'))
                self.data.Confirmed.append(self.hosList[i].currPatient)
                self.data.lng.append(self.hosList[i].lng)
                self.data.lat.append(self.hosList[i].lat)

            print("남은 환자 수: " + str(patient))
            print()  # 줄바꿈
            time += 1

        print("흐름 구성 후 걸린 시간: ", time, "분")

        return self.data
