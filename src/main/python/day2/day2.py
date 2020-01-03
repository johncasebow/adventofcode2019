
class IntcodeComputer:

    OP_ADD  = 1
    OP_MULT = 2
    OP_STOP = 99

    def __init__(self, program=[]):
        self.program = program

    def run_program(self):
        currPos=0;

        operation = self.program[currPos]
        while operation != IntcodeComputer.OP_STOP:
            inputPos1 = self.program[currPos+1]
            inputPos2 = self.program[currPos+2]
            outputPos = self.program[currPos+3]
            # print("currpos=" + str(currPos) + ", op=" + str(operation) + ", input1=" + str(inputPos1) + ", input2=" + str(inputPos2) + ", output=" + str(outputPos) + ", pos0=" + str(self.program[0]))

            if operation == IntcodeComputer.OP_ADD:
                result = self.program[inputPos1] + self.program[inputPos2]
                self.program[outputPos] = result
            elif operation == IntcodeComputer.OP_MULT:
                result = self.program[inputPos1] * self.program[inputPos2]
                self.program[outputPos] = result

            currPos += 4
            operation = self.program[currPos]

        return self.program

class NounVerbFinder:
    def __init__(self, program=[]):
        self.originalProgram = program

    def findNounAndVerbForOutput(self, targetOutput=0):
        noun = 0
        while noun <= 99:
            verb = 0
            while verb <= 99:
                program = self.originalProgram.copy()
                program[1] = noun
                program[2] = verb

                print("Trying " + str(noun) + "," + str(verb))
                output = IntcodeComputer(program).run_program()[0]
                print("Output=" + str(output))

                if output == targetOutput:
                    return (noun, verb)

                verb += 1
            noun += 1

        print("No solution found")



def load_program(filename=""):
    file = open(filename)
    programString = file.read()
    file.close()

    program = []
    strings = programString.split(",")
    for item in strings:
        program.append(int(item))

    return program



if __name__ == '__main__':
    print("Output: " + str(IntcodeComputer(load_program("../../resources/day2/program.txt")).run_program()))

    tuple = NounVerbFinder(load_program("../../resources/day2/program.txt")).findNounAndVerbForOutput(19690720)
    val = 100 * tuple[0] + tuple[1]
    print(val)