from Neuron import Neuron, GraphicSimulator, LIFNeuron, MCPNeuron, Synapse

if __name__ == '__main__':
    # create graphics simulator for 120 seconds, timestep=0.1 seconds
    sim = GraphicSimulator(t=0.1, finalT=80)

    # create a single Neuron that will receive all inputs, and add it to simulator

    # create list of 10 LIF Neurons linked to inputNeuron, and list of 10 MCP
    # Neurons linked to LIF Neurons
    inputNeuronlist = []
    Alist = []
    Blist = []
    for i in range(12):
        # if or(i==0,i==3,i:
        inputNeuronlist.append(Neuron(aname="inputNeuron" + str(i)))
        Alist.append(
            LIFNeuron(athreshold=100, adecay=.5, aname="LIF Neuron " + str(i)))
        Blist.append(MCPNeuron(aname="MCP Neuron " + str(i)))
    # add Neurons to Simulator
    sim.addNeuronList(inputNeuronlist)
    sim.addNeuronList(Alist)
    sim.addNeuronList(Blist)
    # add Synapses weighted by distance between inputNeuron and Alist, and between
    # Alist and Blist, and add them to simulator
    synapseList = Synapse.connectWeightedByDistance(inputNeuronlist, Alist, 0,
                                                    80, 12)
    for i in range(len(synapseList)):
        sim.addSynapse(synapseList[i])
    synapseList = Synapse.connectWeightedByDistance(Alist, Blist, 0, 1, 0)
    for i in range(len(synapseList)):
        sim.addSynapse(synapseList[i])
    synapseList = Synapse.connectWeightedByDistance(Blist, Alist, -3, 0, 3)
    for i in range(len(synapseList)):
        sim.addSynapse(synapseList[i])

    # add input voltage to inputNeuron at 5, 20, 40, 60 and 80 seconds
    sim.appendInput(1, inputNeuronlist[0], 1)
    sim.appendInput(2, inputNeuronlist[0], 1)
    sim.appendInput(3, inputNeuronlist[0], 1)
    sim.appendInput(5, inputNeuronlist[0], 1)
    sim.appendInput(7, inputNeuronlist[0], 1)
    sim.appendInput(10, inputNeuronlist[0], 1)
    sim.appendInput(13, inputNeuronlist[3], 1)
    sim.appendInput(14, inputNeuronlist[0], 1)
    sim.appendInput(19, inputNeuronlist[0], 1)
    sim.appendInput(20, inputNeuronlist[3], 1)
    sim.appendInput(25, inputNeuronlist[0], 1)
    sim.appendInput(26, inputNeuronlist[3], 1)
    sim.appendInput(32, inputNeuronlist[0], 1)
    sim.appendInput(30, inputNeuronlist[3], 1)
    sim.appendInput(33, inputNeuronlist[3], 1)
    sim.appendInput(35, inputNeuronlist[3], 1)
    sim.appendInput(36, inputNeuronlist[3], 1)
    sim.appendInput(37, inputNeuronlist[3], 1)
    sim.appendInput(39, inputNeuronlist[3], 1)
    sim.appendInput(40, inputNeuronlist[6], 1)
    sim.appendInput(42, inputNeuronlist[3], 1)
    sim.appendInput(45, inputNeuronlist[3], 1)
    sim.appendInput(46, inputNeuronlist[6], 1)
    sim.appendInput(49, inputNeuronlist[6], 1)
    sim.appendInput(50, inputNeuronlist[3], 1)
    sim.appendInput(52, inputNeuronlist[6], 1)
    sim.appendInput(54, inputNeuronlist[6], 1)
    sim.appendInput(55, inputNeuronlist[6], 1)
    sim.appendInput(56, inputNeuronlist[6], 1)
    sim.appendInput(57, inputNeuronlist[3], 1)
    sim.appendInput(58, inputNeuronlist[11], 1)
    sim.appendInput(59, inputNeuronlist[6], 1)
    sim.appendInput(63, inputNeuronlist[6], 1)
    sim.appendInput(64, inputNeuronlist[11], 1)
    sim.appendInput(68, inputNeuronlist[6], 1)
    sim.appendInput(69, inputNeuronlist[11], 1)
    sim.appendInput(72, inputNeuronlist[11], 1)
    sim.appendInput(74, inputNeuronlist[11], 1)
    sim.appendInput(75, inputNeuronlist[6], 1)
    sim.appendInput(76, inputNeuronlist[11], 1)
    sim.appendInput(77, inputNeuronlist[11], 1)
    sim.appendInput(78, inputNeuronlist[11], 1)
    sim.appendInput(80, inputNeuronlist[11], 1)
    # sim.appendInput(80, inputNeuron, 1)

    # run simulation
    sim.main()

    # plot voltage history and spike times of each neuron in Alist
    for i in range(12):
        if i == 0 or i == 3 or i == 6 or i == 11:
            inputNeuronlist[i].plotSpikes()
        Blist[i].plotVoltage()

    # print weights of synapses from inputNeuron to Alist
    for j in range(12):
        if j == 0 or j == 3 or j == 6 or j == 11:
            for i in range(len(inputNeuronlist[j].postSynapses)):
                print("synaptic weight of neuron " + str(i) + ": " + str(
                    inputNeuronlist[j].postSynapses[i].weight))

    # print raster plots of Alist and Blist
    # sim.rasterPlot(Alist)
    sim.rasterPlot(Blist)
