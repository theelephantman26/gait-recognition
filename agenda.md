# Project Journal

### September 8th, 2021
-  Currently the only idea that is in my mind is to re-implement this project using __PyTorch__ and use Jupyter Notebooks, so I have an easier time with visualization which happens to be one of the most frequent things that is involved when developing a data science model. I will be developing a neural network solution for this problem. I have many ideas that I want to cover:
    - Create fake data for seperate task of peak detection which will involve performing a fourier transform and using the top $n$ frequencies by the order of the amplitude to reproduce a somewhat similar signal for the purpose of peak detection to segment the signals which will be analyzed by the neural network to produce the idetifications of the subject based on previously known databas. This step will allow us bypass considering any noise removal techniques. Neural Network themeselves can work with noise to a very good degree, they are noise tolerant.
    - Research on noise removal from cyclical signals such as the ones we have recorded in our problem.
    - I am thinking about embedding the algorithm inside a CLI tool that can read in data and produce a model that identifies and produces results.

### Septermber 24th, 2021
-   It is however possible that the above approach is over engineered solution. You could receive the signal in its entirety and then segment it into fixed lengths, interpolate to a standard length and pass that to the network to recognize. An adavantage that this approach presents is that you have control over the amount of data you effectively have to train the neural network with given that you dont hard-segment a large signal i.e divide into contiguous parts of fixed length. Instead, you use a window approach to take read patches of the larger signal with a certain stride less than the length of the frame. These are overlapping signals and not contiguous parts.

