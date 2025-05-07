class Neuron():
    #@PARAMS:
    # name: string - describes neuron
    # output: list - list of output neurons
    # bias: float - bias that affect neuron response
    def __init__(self, name, bias, output=None):
        self.name = name
        if output == None:
            self.output = None
        else:
            newOutput = []
            for o in output:
                assert(isinstance(o, Neuron))
                newOutput.append([o, .5])#TODO add randomized weight values
            self.output = newOutput
        assert(isinstance(bias, float))
        self.bias = bias

    def __str__(self):
        if self.output == None:
            output = None
        else:
            output = [f"{o[0].name} - weight {o[1]:.2f}" for o in self.output]
        return f"Neuron {self.name}: bias {self.bias}, outputs to {output}"
    
if __name__ == '__main__':
    print(Neuron('a1', .5, [Neuron('b1', .6, None)]))