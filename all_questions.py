# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "Mutually exclusive rules mean that no individual can satisfy more than one rule simultaneously. However, in this rule set, a person could satisfy multiple rules. For example, a person can be both a homeowner and have a low annual income, satisfying both Rule 1 and Rule 3"
    answers["(b) explain"] = "An exhaustive rule set would cover all possible combinations of attribute values, ensuring a classification for every conceivable case. In this set, there are combinations of attribute values that are not covered by any rule. For instance, there is no rule for a person who has a high annual income and is currently employed, or a person who is married but does not fit the description of Rules 6 and 7"
    answers["(c) explain"] = "Ordering might be needed if the system is designed to stop at the first rule that applies. Since the rules are not mutually exclusive, the order in which they are applied could affect the outcome. For instance, if a person is a homeowner and has a medium income and is currently employed, both Rule 1 and Rule 5 apply. If Rule 1 is checked first, the person will be classified as DB = Yes, but if Rule 5 is checked first, the classification would be DB = No"
    answers["(d) explain"] = "A default class is needed because the rule set is not exhaustive. There are possible scenarios where none of the provided rules apply, and without a default classification, such cases would be left unclassified. A default class would ensure that every individual is classified, even if none of the specific rules apply"

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "This means that each rule uniquely identifies a different class without overlap. For example, Rule 1 identifies Birds based on specific attributes that do not overlap with the attributes used in Rules 2, 3, or 4 for identifying Fishes, Mammals, or Reptiles, respectively"
    answers["(b) example"] = "An exhaustive set of rules would cover every possible attribute combination that a vertebrate in the data set could have. In the provided rules, there are no conditions set for amphibians, and there could be vertebrates that do not fit any of the rules provided"
    answers["(c) example"] = "Since the rules are mutually exclusive as indicated in the answer to the first question, no vertebrate could be classified under more than one rule, thus the order of rule application does not matter. Each vertebrate will be classified under the first rule that applies to it without any other rule conflicting"

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "The back-propagation algorithm indeed uses the gradients of weights at the K+1th layer to compute the gradients at the kth layer.This is because back-propagation works by first computing the output error and then propagating this error backward through the network to update the weights"
    answers["(b) explain"] = "This process occurs through a forward pass, where each layer's activations are calculated based on the activations of the preceding layer and the associated weights and biases"
    answers["(c) explain"] = " The vanishing gradient problem refers to the situation where gradients become very small, effectively preventing the weights from changing significantly. This problem can slow down training or cause it to converge prematurely"
    answers["(d) explain"] = "If an ANN model perfectly classifies all training instances at a given iteration, it means the loss function has reached a minimum for the training data. While the gradients of the loss with respect to the weights might be very small (since the model is performing well on the training data), they are not necessarily zero"

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = None

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 1
    answers["(b) K"] = 50

    # explain_string
    answers["(a) explain"] = "Since the classes are well separated, the nearest neighbor to a query point is very likely to be from the correct class. Using K = 1 minimizes the risk of including neighbors from the other class, which could occur with a larger K even in well-separated data due to random variation."
    answers["(b) explain"] = "As we can see the data points are not easily separable, we use larer K to reduce the noise which could be better as it would help in making a more generalized and noise-resistant classification."

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = None
    answers["(a) P(B=1|+)"] = None
    answers["(a) P(C=1|+)"] = None
    answers["(a) P(A=1|-)"] = None
    answers["(a) P(B=1|-)"] = None
    answers["(a) P(C=1|-)"] = None

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = None
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = None 
    answers["(b) P(R|+)"] = None
    answers["(b) P(R|-)"] = None

    # string, '+' or '-'
    answers["(b) class label"] = None

    # explain_string
    answers["(b) Explain your reasoning"] = None
  
    # float
    answers["(c) P(A=1)"] = None
    answers["(c) P(B=1)"] = None
    answers["(c) P(A=1,B=1)"] = None

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = None
  
    # type: float
    answers["(d) P(A=1)"] = None
    answers["(d) P(B=0)"] = None
    answers["(d) P(A=1,B=0)"] = None

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = None
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = None
    answers["(e) P(A=1|+)"] = None
    answers["(e) P(B=1|+)"] = None

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = None

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  None
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
