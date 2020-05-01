import numpy as np

def IzhiKevich(stimulate_level):
    
    # time values
    totalTime = 50 #total time
    startTime = 0 #time to start injecting current
    stopTime = 50 #time to stope injecting current
    dt = 0.1 #steps of time
    timeArray = np.arange(0, totalTime+dt, dt)

    current = 18 + 2 * stimulate_level
    
    firingRate = 0
    
    spikingNum = 0

    v_rest = -60 #resting membrane potential [mV]
    v_th = -40 #threshold potential [mV]
    v_spike = 30 #spike value for membrane potential [mV]

    #parameters
    a = 0.02
    b = 0.2
    c = -65
    d = 2
   
    v_m = np.zeros(len(timeArray)) + v_rest # membrane potential array
    u = np.zeros(len(timeArray)) #membrane recovery variable
    refractoryTime = startTime

    for T, time in enumerate(timeArray):
        if time > refractoryTime and time < stopTime:
            v_m[T] = dt * (0.04 * v_m[T-1]**2 + 5 * v_m[T-1] + 140 - u[T-1] + current) + v_m[T-1]
            u[T] = dt * (a * (b * v_m[T-1]) - u[T-1]) + u[T-1]

            if v_m[T] > v_th:
                v_m[T] = v_spike
                spikingNum += 1
                refractoryTime =  2 * time - timeArray[T-1]
        elif time > startTime and time < stopTime:
            v_m[T] = c
            u[T] = u[T-1] + d
        elif time >= stopTime:
            v_m[T] = c

    firingRate = spikingNum/((stopTime - startTime)/1000)

    return firingRate, spikingNum


class RGC_onCell:

    def __init__(self, center_size, surround_size):
        self.cell = np.ones([surround_size,surround_size])
        self.cell *= -1
        center = surround_size // 2
        self.left_edge = center - center_size // 2
        self.right_edge = center + center_size // 2
        self.cell[self.left_edge:self.right_edge+1,self.left_edge:self.right_edge+1] = 1

    def run(self, input_field):
        stimulate_mat = self.cell * input_field
        # option 1: -1,0,1,2
        is_stimulated = 0
        is_inhibited = 0
        # print(stimulate_mat[self.left_edge:self.right_edge+1,self.left_edge:self.right_edge+1])
        if 1 in stimulate_mat[self.left_edge:self.right_edge+1,self.left_edge:self.right_edge+1]:
            is_stimulated = 1
        stimulate_mat[self.left_edge:self.right_edge+1,self.left_edge:self.right_edge+1] = 0
        if -1 in stimulate_mat:
            is_inhibited = 1
        level = 0
        if is_stimulated == 0 and is_inhibited == 1:
            level = 0
        if is_stimulated == 0 and is_inhibited == 0:
            level = 1
        if is_stimulated == 1 and is_inhibited == 1:
            level = 2
        if is_stimulated == 1 and is_inhibited == 0:
            level = 3
        # print(level)
        firingRate, spikingNum = IzhiKevich(level)
        print("firingRate is " + str(firingRate))
        print("spikingNum is " + str(spikingNum))
        # option 2: 0,1,2
        
        return firingRate
        

class RGC_offCell:

    def __init__(self, center_size, surround_size):
        self.cell = np.ones([surround_size,surround_size])
        center = surround_size // 2
        self.left_edge = center - center_size // 2
        self.right_edge = center + center_size // 2
        self.cell[self.left_edge:self.right_edge+1,self.left_edge:self.right_edge+1] = -1
        
    def run(self, input_field):
        stimulate_mat = self.cell * input_field
        # option 1: -1,0,1,2
        is_stimulated = 0
        is_inhibited = 0
        # print(stimulate_mat[self.left_edge:self.right_edge+1,self.left_edge:self.right_edge+1])
        if -1 in stimulate_mat[self.left_edge:self.right_edge+1,self.left_edge:self.right_edge+1]:
            is_inhibited = 1
        stimulate_mat[self.left_edge:self.right_edge+1,self.left_edge:self.right_edge+1] = 0
        if 1 in stimulate_mat:
            is_stimulated = 1
        level = 0
        if is_stimulated == 0 and is_inhibited == 1:
            level = 0
        if is_stimulated == 0 and is_inhibited == 0:
            level = 1
        if is_stimulated == 1 and is_inhibited == 1:
            level = 2
        if is_stimulated == 1 and is_inhibited == 0:
            level = 3
        # print(level)
        firingRate, spikingNum = IzhiKevich(level)
        print("firingRate is " + str(firingRate))
        print("spikingNum is " + str(spikingNum))
        # option 2: 0,1,2
        
        return firingRate