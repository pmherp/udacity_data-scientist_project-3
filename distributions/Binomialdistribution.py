# TODO: import necessary libraries
import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

# TODO: make a Binomial class that inherits from the Distribution class. Use the specifications below.
class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """
    # TODO: define the init function
    def __init__(self, prob=.5, size=50):
        self.p = prob
        self.n = size
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
     
    
    def calculate_mean(self):
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
        
        """
        mean_tmp = self.p * self.n
        self.mean = mean_tmp
        
        return self.mean
         

    #TODO: write a calculate_stdev() method accordin to the specifications below.
    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        stdev_tmp = math.sqrt(self.n * self.p * (1 - self.p))
        self.stdev = stdev_tmp
        
        return self.stdev

    
    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
        #update n attribute with data
        self.n = len(self.data)
        
        #update p attribute with data
        self.p = sum(self.data) / len(self.data)
        
        #update mean attribute with data
        self.mean = self.calculate_mean()
        
        #update the standard deviation attribute with data
        self.stdev = self.calculate_stdev()
        
        return self.p, self.n
        
    
    # TODO: write a method plot_bar() that outputs a bar chart of the data set according to the following specifications.
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        plt.bar(x = ['0', '1'], height = [(1 - self.p) * self.n, self.p * self.n])
        plt.title('Bar Chart for Data')
        plt.xlabel('data')
        plt.ylabel('count')
    
    
    #TODO: Calculate the probability density function of the binomial distribution
    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        return ((math.factorial(self.n)) / ((math.factorial(self.n - k)) * (math.factorial(k)))) * (self.p ** k) * ((1 - self.p) ** (self.n - k))
        

    # write a method to plot the probability density function of the binomial distribution
    def plot_histogram_pdf(self):
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        x = []
        y = []
        
        # calculate the x values to visualize
        for i in range(self.n + 1):
            x.append(i)
            y.append(self.pdf(i))

        # make the plots
        plt.bar(x, y)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')

        plt.show()

        return x, y
           
        
    # write a method to output the sum of two binomial distributions. Assume both distributions have the same p value.
    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        #create new binomial object
        new_binomial = Binomial()
        
        #calculate mean of new binomial
        new_binomial.calculate_mean()
        
        #calculate standard deviation of new binomial
        new_binomial.calculate_stdev()
        
        #calculate size of new binomial
        new_binomial.n = self.n + other.n
        
        #for easier implementation, probability will be assumed to be equal only
        new_binomial.p = self.p
        
        return new_binomial
                    
        
    # use the __repr__ magic method to output the characteristics of the binomial distribution object.
    def __repr__(self):
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """

        #override magic method __repr__
        return ('mean {}, standard deviation {}, p {}, n {}'.format(self.calculate_mean(), self.calculate_stdev(), self.p, self.n))
