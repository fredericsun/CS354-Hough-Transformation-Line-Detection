class Comment:
    def __init__(self, robot, groupid, microid, speech, gesture, speech_token):
        self.robot = robot
        self.groupid = groupid
        self.microid = microid
        self.speech = speech
        self.gesture = gesture
        self.speech_token = speech_token
        print "GESTURE IS {}".format(self.gesture)

    def getGroup(self):
        return self.groupid

    def getID(self):
        return self.microid

    def execute(self, last_final_state, out_list):
        startState_Ignored = "Start_Silent_Ignored"
        startState_Present = "Start_Silent_Present"
        startState_Busy = "Start_Silent_Busy"
        while True:
            if last_final_state == "human_ready":

                self.robot.gaze.addBehavior("Comment", "GAZE_AT", None)
                print startState_Present + "\n"
                newState = "Speaking_Present_Asking"
                print newState + "\n"
                self.robot.gaze.killBehavior("Comment", "GAZE_AT")

                if newState == "Speaking_Present_Asking":

                    self.robot.gaze.addBehavior("Comment", "GAZE_INTIMACY", None)
                    if self.gesture:
                        self.robot.gesture.addBehavior("Comment", "GESTURE_BEAT")
                    else:
                        self.robot.gesture.addBehavior("Comment", "GESTURE_NONE")
                    self.speech_token.acquire()
                    self.robot.comment(self.speech)
                    self.speech_token.release()
                    self.robot.gaze.killBehavior("Comment", "GAZE_INTIMACY")
                    if self.gesture:
                        self.robot.gesture.killBehavior("Comment", "GESTURE_BEAT")
                    else:
                        self.robot.gesture.killBehavior("Comment", "GESTURE_NONE")

                    self.robot.gaze.addBehavior("Comment", "GAZE_AT", None)
                    self.robot.gesture.addBehavior("Comment", "GESTURE_NONE")
                    newState = "Silent_Present_End"
                    self.robot.gaze.killBehavior("Comment", "GAZE_AT")
                    self.robot.gesture.killBehavior("Comment", "GESTURE_NONE")
                    print newState + "\n"
                    output = "human_ready"
                    break

            elif last_final_state == "human_busy":

                self.robot.gaze.addBehavior("Comment", "GAZE_AT", None)
                print startState_Busy + "\n"
                newState = "Speaking_Busy_Asking"
                print newState + "\n"
                self.robot.gaze.killBehavior("Comment", "GAZE_AT")

                if newState == "Speaking_Busy_Asking":

                    self.robot.gaze.addBehavior("Comment", "GAZE_INTIMACY", None)
                    if self.gesture:
                        self.robot.gesture.addBehavior("Comment", "GESTURE_BEAT")
                    else:
                        self.robot.gesture.addBehavior("Comment", "GESTURE_NONE")
                    self.speech_token.acquire()
                    self.robot.comment(self.speech)
                    self.speech_token.release()
                    self.robot.gaze.killBehavior("Comment", "GAZE_INTIMACY")
                    if self.gesture:
                        self.robot.gesture.killBehavior("Comment", "GESTURE_BEAT")
                    else:
                        self.robot.gesture.killBehavior("Comment", "GESTURE_NONE")

                    self.robot.gaze.addBehavior("Comment", "GAZE_AT", None)
                    self.robot.gesture.addBehavior("Comment", "GESTURE_NONE")
                    newState = "Silent_End_Busy"
                    print newState + "\n"
                    output = "human_busy"
                    self.robot.gaze.killBehavior("Comment", "GAZE_AT")
                    self.robot.gesture.killBehavior("Comment", "GESTURE_NONE")
                    break

            elif last_final_state is None or last_final_state == "human_ignore":

                self.robot.gaze.addBehavior("Comment", "GAZE_AT", None)
                print startState_Ignored + "\n"
                newState = "Speaking_Ignored_Asking"
                print newState + "\n"
                self.robot.gaze.killBehavior("Comment", "GAZE_AT")

                if newState == "Speaking_Ignored_Asking":

                    self.robot.gaze.addBehavior("Comment", "GAZE_INTIMACY", None)
                    if self.gesture:
                        self.robot.gesture.addBehavior("Comment", "GESTURE_BEAT")
                    else:
                        self.robot.gesture.addBehavior("Comment", "GESTURE_NONE")
                    self.speech_token.acquire()
                    self.robot.comment(self.speech)
                    self.speech_token.release()
                    self.robot.gaze.killBehavior("Comment", "GAZE_INTIMACY")
                    if self.gesture:
                        self.robot.gesture.killBehavior("Comment", "GESTURE_BEAT")
                    else:
                        self.robot.gesture.killBehavior("Comment", "GESTURE_NONE")

                    self.robot.gaze.addBehavior("Comment", "GAZE_AT", None)
                    self.robot.gesture.addBehavior("Comment", "GESTURE_NONE")
                    newState = "Silent_Ignored_End"
                    print newState + "\n"
                    output = "human_ignore"
                    self.robot.gaze.killBehavior("Comment", "GAZE_AT")
                    self.robot.gesture.killBehavior("Comment", "GESTURE_NONE")
                    break
        out_list.append(output)
