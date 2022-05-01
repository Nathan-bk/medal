import glob
import tensorflow as tf
import matplotlib.pyplot as plt

# TAG_NAME = 

def get_section_results(file):
    """
        requires tensorflow==1.12.0
    """
    X = []

    tags = {}

    for e in tf.compat.v1.train.summary_iterator(file):
        for v in e.summary.value:
            # if v.tag == 'Train_EnvstepsSoFar':
            #     X.append(v.simple_value)
            tags.add(v.tag)
    
    print(tags)

    # return X

if __name__ == '__main__':
    import glob

    logdir = './runs/electra-03-03-16-42/events*'
    eventfile = glob.glob(logdir)[0]

    X = get_section_results(eventfile)

    # plt.plot(X)
    
    # plt.legend()
    # plt.xlabel("Epochs")
    # plt.ylabel("Eval_AverageReturn")
    # plt.title("Learning Curves Comparison for small batch sizes on HalfCheetah-v2 env with b50000_r0.02")
    # plt.grid()
    # plt.show()