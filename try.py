class Question:
    def __init__(self, robot, groupid, microid, speech_token, AnswerList):
        self.groupid = groupid
        self.microid = microid
        self.robot = robot
        self.speech_token = speech_token
        self.AnswerList = AnswerList

    def getGroup(self):
        return self.groupid

    def getID(self):
        return self.microid

    def execute(self, last_final_state, out_list):
        StartState = "Start_Silent_Present_H_Silent"
        wait_time = 5

        while True:
            if StartState == "Start_Silent_Present_H_Silent":
                self.robot.gaze.addBehavior("Ask", "GAZE_AT")
                print StartState + "\n"
                newState = "Speaking_Present_H_Silent_Asking"
                print newState + "\n"
                self.robot.gaze.killBehavior("Ask", "GAZE_AT")

            if newState == "Speaking_Present_H_Silent_Asking":
                self.robot.gaze.addBehavior("Ask", "GAZE_AT")
                self.robot.gesture.addBehavior("Ask", "GESTURE_BEAT")
                self.speech_token.acquire()
                self.robot.question()
                self.speech_token.release()
                newState = "Silent_Present_Listening_H_Silent"
                self.robot.gaze.killBehavior("Ask", "GAZE_AT")
                self.robot.gesture.killBehavior("Ask", "GESTURE_BEAT")

            while True:
                if newState == "Silent_Present_Listening_H_Silent":
                    self.robot.gaze.addBehavior("Ask", "GAZE_AT")
                    self.robot.gesture.addBehavior("Ask", "GESTURE_NONE")
                    print newState + "\n"
                    val = self.robot.speechRecognition(wait_time)
                    if val is None or val == "":
                        newState = "Silent_Ignored_H_Silent_End"
                        print newState + "\n"
                        self.robot.gaze.killBehavior("Ask", "GAZE_AT")
                        self.robot.gesture.killBehavior("Ask", "GESTURE_NONE")
                        break
                    else:
                        newState = "Silent_Listening_H_Speaking_Answering"
                        self.robot.gaze.killBehavior("Ask", "GAZE_AT")
                        #self.robot.gesture.killBehavior("Ask", "GESTURE_NONE")
                        print newState + "\n"

                    if newState == "Silent_Listening_H_Speaking_Answering":
                        self.robot.gaze.addBehavior("Ask", "GAZE_AT")
                        #self.robot.gesture.addBehavior("Ask", "GESTURE_NONE")
                        if val in self.AnswerList:
                            newState = "Silent_Present_Listening_H_Silent"
                            print newState + "\n"
                            newState = "Silent_Present_H_Silent_End"
                            print newState + "\n"
                            self.robot.gaze.killBehavior("Ask", "GAZE_AT")
                            #self.robot.gesture.killBehavior("Ask", "GESTURE_NONE")
                            break
                        elif val not in self.AnswerList:
                            newState = "Silent_Present_Listening_H_Silent"
                            self.robot.gaze.killBehavior("Ask", "GAZE_AT")
                            #self.robot.gesture.killBehavior("Ask", "GESTURE_NONE")
                            print newState + "\n"
                            newState = "Speaking_RepeatAsk_Present_H_Silent"
                            print newState + "\n"
                            self.robot.gaze.addBehavior("Ask", "GAZE_AT")
                            self.robot.gesture.addBehavior("Ask", "GESTURE_BEAT")
                            self.robot.repeatAnswer()
                            newState = "Silent_Present_Listening_H_Silent"
                            self.robot.gaze.killBehavior("Ask", "GAZE_AT")
                            self.robot.gesture.killBehavior("Ask", "GESTURE_BEAT")

            if newState == "Silent_Ignored_H_Silent_End":
                output = "human_ignore"
                break

            if newState == "Silent_Present_H_Silent_End":
                idx = AnswerList.index(val)
                link = linkList[idx]
                if (link == "human_ready" or link == ""):
                    output = "human_ready"
                else:
                    output = "human_ignore"
                break
        out_list.append(output)
