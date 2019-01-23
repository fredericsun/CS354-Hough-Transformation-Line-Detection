class Handoff:
    def __init__(self, robot, groupid, microid, larm_token, rarm_token, lhand_token, rhand_token, side, give_receive):
        self.robot = robot
        self.groupid = groupid
        self.microid = microid
        self.larm_token = larm_token
        self.rarm_token = rarm_token
        self.lhand_token = lhand_token
        self.rhand_token = rhand_token
        self.side = side
        self.give_receive = give_receive

    def getGroup(self):
        return self.groupid

    def getID(self):
        return self.microid

    def execute(self, last_final_state, out_list):
        wait_time = 15
        StartState = "Start_Present_Arm_Retracted"
        if self.side == None:
            self.side = "right"
        while True:
            if StartState == "Start_Present_Arm_Retracted":
                self.robot.gaze.addBehavior("Handoff", "GAZE_AT", None)
                print StartState + "\n"
                '''
                if self.side == "left":
                    self.larm_token.acquire()
                    self.robot.leftarmRetracted()
                    self.larm_token.release()
                    self.lhand_token.acquire()
                    self.robot.closeLefthand()
                    self.lhand_token.release()
                elif self.side == "right":
                    self.rarm_token.acquire()
                    self.robot.rightarmRetracted()
                    self.rarm_token.release()
                    self.rhand_token.acquire()
                    self.robot.closeRighthand()
                    self.rhand_token.release()
                '''
                newState = "Present_Extending_Arm_Extended"
                self.robot.gaze.killBehavior("Handoff", "GAZE_AT")
                print newState + "\n"

            if newState == "Present_Extending_Arm_Extended":
                if self.side == "left":
                    self.robot.gaze.addBehavior("Handoff", "GAZE_REFERENTIAL", "left")
                    self.larm_token.acquire()
                    self.robot.leftarmExtended()
                    self.larm_token.release()
                    touch = self.robot.waitUntilTouchDetected()
                    print touch
                    self.robot.gaze.killBehavior("Handoff", "GAZE_REFERENTIAL")
                elif self.side == "right":
                    self.robot.gaze.addBehavior("Handoff", "GAZE_REFERENTIAL", "right")
                    self.rarm_token.acquire()
                    self.robot.rightarmExtended()
                    self.rarm_token.release()
                    touch = self.robot.waitUntilTouchDetected()
                    print touch
                    self.robot.gaze.killBehavior("Handoff", "GAZE_REFERENTIAL")
                newState = "Releasing_Contacted_Arm_Extended"
                print newState + "\n"

            if self.give_receive == "receive":
                if newState == "Releasing_Contacted_Arm_Extended":
                    if self.side == "left":
                        self.robot.gaze.addBehavior("Handoff", "GAZE_AT", None)
                        self.lhand_token.acquire()
                        self.robot.openLefthand()
                        self.lhand_token.release()
                        self.robot.gaze.killBehavior("Handoff", "GAZE_AT")
                    elif self.side == "right":
                        self.robot.gaze.addBehavior("Handoff", "GAZE_AT", None)
                        self.rhand_token.acquire()
                        self.robot.openRighthand()
                        self.rhand_token.release()
                        self.robot.gaze.killBehavior("Handoff", "GAZE_AT")
                    newState = "Releasing_Present_Arm_Extended"
                    print newState + "\n"

                if newState == "Releasing_Present_Arm_Extended":
                    touch = self.robot.waitUntilTouchDetected()
                    print touch
                    if self.side == "left":
                        if touch[4][1] == True:
                            self.robot.gaze.addBehavior("Handoff", "GAZE_AT", None)
                            self.lhand_token.acquire()
                            self.robot.closeLefthand()
                            self.lhand_token.release()
                            time.sleep(1)
                            self.larm_token.acquire()
                            self.robot.leftarmRetracted()
                            self.larm_token.release()
                            self.robot.gaze.killBehavior("Handoff", "GAZE_AT")
                            newState = "Present_End_Arm_Retracted"
                            print newState + "\n"
                            output = "human_ready"
                            time.sleep(2)
                            break
                    elif self.side == "right":
                        if touch[1][1] == True:
                            self.robot.gaze.addBehavior("Handoff", "GAZE_AT", None)
                            self.rhand_token.acquire()
                            self.robot.closeRighthand()
                            self.rhand_token.release()
                            time.sleep(1)
                            self.rarm_token.acquire()
                            self.robot.rightarmRetracted()
                            self.rarm_token.release()
                            self.robot.gaze.killBehavior("Handoff", "GAZE_AT")
                            newState = "Present_End_Arm_Retracted"
                            print newState + "\n"
                            output = "human_ready"
                            time.sleep(2)
                            break

            if self.give_receive == "give":
                if newState == "Releasing_Contacted_Arm_Extended":
                    if self.side == "left":
                        self.robot.gaze.addBehavior("Handoff", "GAZE_AT", None)
                        self.lhand_token.acquire()
                        self.robot.openLefthand()
                        self.robot.closeLeftHand()
                        self.lhand_token.release()
                        self.robot.gaze.killBehavior("Handoff", "GAZE_AT")
                    elif self.side == "right":
                        self.robot.gaze.addBehavior("Handoff", "GAZE_AT", None)
                        self.rhand_token.acquire()
                        print "OPENING RIGHT HAND"
                        self.robot.openRighthand()
                        print "CLOSING RIGHT HAND"
                        self.robot.closeRighthand()
                        self.rhand_token.release()
                        self.robot.gaze.killBehavior("Handoff", "GAZE_AT")
                    newState = "Releasing_Present_Arm_Extended"
                    print newState + "\n"

                if newState == "Releasing_Present_Arm_Extended":
                    #time.sleep(5)
                    if self.side == "left":
                        self.robot.gaze.addBehavior("Handoff", "GAZE_AT", None)
                        print "ABOUT TO RETRACT ARM!"
                        self.larm_token.acquire()
                        self.robot.leftarmRetracted()
                        self.larm_token.release()
                        self.robot.gaze.killBehavior("Handoff", "GAZE_AT")
                    elif self.side == "right":
                        self.robot.gaze.addBehavior("Handoff", "GAZE_AT", None)
                        print "ABOUT TO RETRACT ARM!"
                        self.rarm_token.acquire()
                        self.robot.rightarmRetracted()
                        self.rarm_token.release()
                        self.robot.gaze.killBehavior("Handoff", "GAZE_AT")
                    newState = "Present_End_Arm_Retracted"
                    print newState + "\n"
                    output = "human_ready"
                    break
        out_list.append(output)
